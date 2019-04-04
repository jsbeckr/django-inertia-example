import json
from django.core.exceptions import ImproperlyConfigured
from django.views.generic import View
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.generics import GenericAPIView

from django.views.generic import View
from django.conf import settings


def render_inertia(request, component, props, template=None):
    """
    Renders either an HttpRespone or JsonResponse of a component for 
    the use in an InertiaJS frontend integration.
    """

    inertia_template = None

    if template is not None:
        inertia_template = template

    if settings.INERTIA_TEMPLATE is not None:
        inertia_template = settings.INERTIA_TEMPLATE

    if inertia_template is None:
        raise ImproperlyConfigured(
            "No Inertia template found. Either set INERTIA_TEMPLATE"
            "in settings.py or pass template parameter."
            )

    

    pass

#class InertiaView(Base)
# TODO: refactor to base class + share via session

class InertiaDetailView(BaseDetailView):
    template_name = ""
    component_name = ""
    props = {}
    serializer_class = None

    def render_to_response(self, context):
        if self.serializer_class is None:
            raise ImproperlyConfigured(
                "%(cls)s is missing a ModelSerializer. Define "
                "%(cls)s.serializer_class." % {
                    'cls': self.__class__.__name__
                }
            )

        object_name = self.get_context_object_name(self.object)
        serialized_object = self.serializer_class(self.object).data

        if self.props is None:
            self.props = {object_name: serialized_object}
        else:
            self.props[object_name] = serialized_object

        # subsequent renders
        if 'x-inertia' in self.request.headers:
            response = JsonResponse({
                "component": self.component_name,
                "props": self.props,
                "url": self.request.path
            })

            response['X-Inertia'] = True
            response['Vary'] = 'Accept'
            return response

        # first render
        custom_context = {
            "component": self.component_name,
            "props": json.dumps(self.props)
        }

        return render(self.request, self.template_name, context=custom_context)


class InertiaListView(BaseListView):
    template_name = ""
    component_name = ""
    props = {}
    serializer_class = None

    def render_to_response(self, context):
        request = self.request

        if self.serializer_class is None:
            raise ImproperlyConfigured(
                "%(cls)s is missing a ModelSerializer. Define "
                "%(cls)s.serializer_class." % {
                    'cls': self.__class__.__name__
                }
            )

        object_name = self.get_context_object_name(self.object_list)
        serialized_object_list = self.serializer_class(
            self.object_list, many=True).data

        if self.props is None:
            self.props = {object_name: serialized_object_list}
        else:
            self.props[object_name] = serialized_object_list

        # subsequent renders
        if 'x-inertia' in request.headers:
            response = JsonResponse({
                "component": self.component_name,
                "props": self.props,
                "url": request.path
            })

            response['X-Inertia'] = True
            response['Vary'] = 'Accept'
            return response

        # first render
        custom_context = {
            "component": self.component_name,
            "props": json.dumps(self.props)
        }

        return render(request, self.template_name, context=custom_context)

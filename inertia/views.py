import json
from django.core.exceptions import ImproperlyConfigured
from django.views.generic.list import BaseListView
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import MultipleObjectMixin
from django.core import serializers
from django.shortcuts import render
from django.http import JsonResponse

from django.views.generic import View

class InertiaDetailView(BaseDetailView):
    template_name = ""
    component_name = ""
    props = {}
    serializer = None

    def render_to_response(self, context):
        vueComponent = f"{self.component_name}.vue"

        object_name = self.get_context_object_name(self.object)
        serialized_object = self.serializer(self.object).data

        if self.serializer is None:
            raise ImproperlyConfigured(
                    "%(cls)s is missing a ModelSerializer. Define "
                    "%(cls)s.serializer." % {
                        'cls': self.__class__.__name__
                    }
                )

        if self.props is None:
            self.props = {object_name: serialized_object}
        else:
            self.props[object_name] = serialized_object

        # subsequent renders
        if 'x-inertia' in self.request.headers:
            response = JsonResponse({
                "component": vueComponent,
                "props": self.props,
                "url": self.request.path
            })

            response['X-Inertia'] = True
            response['Vary'] = 'Accept'
            return response

        # first render
        custom_context = {
            "component": vueComponent,
            "props": json.dumps(self.props)
        }

        return render(self.request, self.template_name, context=custom_context)


class InertiaListView(BaseListView):
    template_name = ""
    component_name = ""
    props = {}
    serializer = None

    def render_to_response(self, context):
        vueComponent = f"{self.component_name}.vue"
        request = self.request

        if self.serializer is None:
            raise ImproperlyConfigured(
                    "%(cls)s is missing a ModelSerializer. Define "
                    "%(cls)s.serializer." % {
                        'cls': self.__class__.__name__
                    }
                )

        object_name = self.get_context_object_name(self.object_list)
        serialized_object_list = self.serializer(self.object_list, many=True).data

        if self.props is None:
            self.props = {object_name: serialized_object_list}
        else:
            self.props[object_name] = serialized_object_list

        # subsequent renders
        if 'x-inertia' in request.headers:
            response = JsonResponse({
                "component": vueComponent,
                "props": self.props,
                "url": request.path
            })

            response['X-Inertia'] = True
            response['Vary'] = 'Accept'
            return response

        # first render
        custom_context = {
            "component": vueComponent,
            "props": json.dumps(self.props)
        }

        return render(request, self.template_name, context=custom_context)


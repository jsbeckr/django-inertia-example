import json
from django.shortcuts import render
from django.http import JsonResponse

from .models import Contact
from .serializers import ContactSerializer

from inertia.views import InertiaListView, InertiaDetailView, render_inertia


def dummy(request):
    return render_inertia(request, 'Dummy')


class Index(InertiaListView):
    model = Contact
    serializer_class = ContactSerializer
    component_name = "Main"

class Second(InertiaDetailView):
    model = Contact
    serializer_class = ContactSerializer
    component_name = "Second"
    props = {"test": True}
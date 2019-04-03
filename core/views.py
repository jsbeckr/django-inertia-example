import json
from django.shortcuts import render
from django.http import JsonResponse

from .models import Contact
from .serializers import ContactSerializer

from inertia.views import InertiaListView, InertiaDetailView


class Index(InertiaListView):
    model = Contact
    serializer = ContactSerializer
    template_name = "index.html"
    component_name = "Main"
    props = None

class Second(InertiaDetailView):
    model = Contact
    serializer = ContactSerializer
    template_name = "index.html"
    component_name = "Second"
    props = {"test": True}
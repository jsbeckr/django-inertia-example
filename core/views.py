import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.http import JsonResponse

from .models import Contact
from .serializers import ContactSerializer

from inertia import InertiaListView, InertiaDetailView, render_inertia


def dummy(request):
    # for function use just use render_inertia function
    return render_inertia(request, 'Dummy')


class Index(InertiaListView):
    # Inertia supports List and DetailViews right now
    model = Contact
    serializer_class = ContactSerializer
    component_name = "Index"


class ContactView(InertiaDetailView):
    model = Contact
    serializer_class = ContactSerializer
    component_name = "Contact"
    props = {"test": True}  # you can inject any props you want

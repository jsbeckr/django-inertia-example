import json
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.http import JsonResponse

from .models import Contact
from .serializers import ContactSerializer

from inertia import InertiaListView, InertiaDetailView, render_inertia


def dummy(request):
    # for function use just use render_inertia function
    return render_inertia(request, 'Dummy')


def logout_user(request):
    logout(request)
    return redirect('index')


def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user = authenticate(username=data['username'], password=data['password'])
        if user is None:
            # TODO: Error message
            return render_inertia(request, 'Login')
        else:
            login(request, user)
            return redirect('index')
        
    return render_inertia(request, 'Login')


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

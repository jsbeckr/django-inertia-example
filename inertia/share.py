import typing
from django.http import HttpRequest

def share(request: HttpRequest, key, value):
    request.session.set(key, value)
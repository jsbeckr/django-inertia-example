from django.shortcuts import render
from django.http import JsonResponse
import json


def render_inertia(request, component, props):
    vueComponent = f"{component}.vue"

    # subsequent renders
    if 'x-inertia' in request.headers:
        response = JsonResponse({
            "component": vueComponent,
            "props": props,
            "url": request.path
        })

        response['X-Inertia'] = True
        response['Vary'] = 'Accept'
        return response

    # first render
    context = {
        "component": vueComponent,
        "props": json.dumps(props)
    }

    return render(request, "index.html", context=context)


def index(request):
    return render_inertia(request, "Main", None)


def second(request):
    return render_inertia(request, "Second", {"test": "THIS WORKS AS WELL"})

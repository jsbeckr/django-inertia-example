import time

from django.apps import AppConfig
from django.contrib.auth import get_user, get_user_model
from rest_framework import serializers

from inertia import share, asset_version


def current_user(request):
    class UserSerializer(serializers.ModelSerializer):

        class Meta:
            model = get_user_model()
            fields = ["username", "email"]

    return UserSerializer(get_user(request)).data


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        share('title', 'Django Inertia.js Example 🤘')
        share('user', current_user)

        # everytime the server restarts a new version will be delivered
        asset_version.set_version(time.time())

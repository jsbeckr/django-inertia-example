from django.apps import AppConfig
import inertia


class CoreConfig(AppConfig):
    name = 'core'

    def ready(self):
        inertia.share('name', 'Django InertiaJS Example 🤘')

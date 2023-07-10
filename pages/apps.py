from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'


class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField'
    name = 'Myapp'

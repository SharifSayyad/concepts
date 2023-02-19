from django.apps import AppConfig

print('inside apps.py')
class OnetooneConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'onetoone'

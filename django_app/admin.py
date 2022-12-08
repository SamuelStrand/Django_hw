from django.contrib import admin
from django_app import models as django_models


# Register your models here.

admin.site.register(django_models.IceCream)
admin.site.register(django_models.Human)
admin.site.register(django_models.Child_model)
admin.site.register(django_models.Kiosk)

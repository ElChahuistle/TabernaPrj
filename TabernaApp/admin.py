from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Cerverza)
admin.site.register(models.Cerveceria)
admin.site.register(models.TipoCerveza)
admin.site.register(models.Presentacion)
# admin.site.register(models.PresentacionCerveza)
from django.contrib import admin
from .models import Production, Paper, TypePrint, Colorfulness, Circulation


admin.site.register(Production)
admin.site.register(Paper)
admin.site.register(TypePrint)
admin.site.register(Colorfulness)
admin.site.register(Circulation)

# Register your models here.

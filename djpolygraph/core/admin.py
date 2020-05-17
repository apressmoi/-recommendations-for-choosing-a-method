from django.contrib import admin
from .models import Production, Paper, TypePrint, Colorfulness, Circulation,Profile


admin.site.register(Production)
admin.site.register(Paper)
admin.site.register(TypePrint)
admin.site.register(Colorfulness)
admin.site.register(Circulation)
admin.site.register(Profile)

# Register your models here.

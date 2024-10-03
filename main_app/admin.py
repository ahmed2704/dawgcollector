from django.contrib import admin
from .models import Dawg, Feeding, Toy

# Register your models here.
admin.site.register(Dawg)
admin.site.register(Feeding)
admin.site.register(Toy)
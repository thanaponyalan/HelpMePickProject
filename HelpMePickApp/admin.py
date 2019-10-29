from django.contrib import admin

# Register your models here.
from .models import Activity, Food
admin.site.register(Activity)
admin.site.register(Food)

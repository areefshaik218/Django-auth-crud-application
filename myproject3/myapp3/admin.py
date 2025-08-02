from django.contrib import admin
from .models import Mymodel
from .models import User

# Register your models here.
admin.site.register(Mymodel)
admin.site.register(User)
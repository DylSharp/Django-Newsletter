from django.contrib import admin

# Register your models here.
from .models import SignUp
from .forms import SignUpForm

class SignUpAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'timestamp', 'updated']
    form = SignUpForm
    class Meta:
        models = SignUp


admin.site.register(SignUp, SignUpAdmin)
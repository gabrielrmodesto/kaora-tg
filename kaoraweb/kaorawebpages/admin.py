from django.contrib import admin
from .models import Fisioterapeuta
from .models import Paciente
from .models import Login

admin.site.register(Fisioterapeuta)
admin.site.register(Paciente)
admin.site.register(Login)
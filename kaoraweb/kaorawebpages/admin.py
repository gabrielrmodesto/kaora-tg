from django.contrib import admin
from .models import Fisioterapeuta
from .models import Paciente
from .models import Login
from .models import Dados_Musculos

admin.site.register(Fisioterapeuta)
admin.site.register(Paciente)
admin.site.register(Login)
admin.site.register(Dados_Musculos)
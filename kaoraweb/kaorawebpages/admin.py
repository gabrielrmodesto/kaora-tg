from django.contrib import admin
from .models import Fisioterapeuta, Paciente, Login, Dados_Musculos, Anotacao_Paciente

admin.site.register(Fisioterapeuta)
admin.site.register(Paciente)
admin.site.register(Login)
admin.site.register(Dados_Musculos)
admin.site.register(Anotacao_Paciente)
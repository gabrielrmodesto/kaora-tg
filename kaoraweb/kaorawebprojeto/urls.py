from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from kaorawebpages.views import Cadastro_Fisioterapeuta, Cadastro_Paciente, logar, home, Consulta_Paciente, Perfil_Paciente, sair, Anotacao, Avaliacao, Remover_Paciente, Atualiza_Paciente

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', logar, name='login'),
    path('cadastro/', Cadastro_Fisioterapeuta, name='cadastro_fisioterapeuta'),
    path('home/', home, name='pagina_inicial'),
    path('cadastro_paciente/', Cadastro_Paciente, name='cadastro_paciente'),
    path('consulta_paciente/', Consulta_Paciente, name='consulta_paciente'),
    path('perfil_paciente/<int:pk>/', Perfil_Paciente, name='perfil_paciente'),
    path('logout/', sair, name='logout'),
    path('anotacao/<int:pk>/', Anotacao, name='anotacao'),
    path('avaliacao/', Avaliacao, name='avaliacao'),
    path('remover/<int:pk>/', Remover_Paciente, name='remove_paciente'),
    path('atualizar_paciente/<int:pk>', Atualiza_Paciente, name='atualiza_paciente'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

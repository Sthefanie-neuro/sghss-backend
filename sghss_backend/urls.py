from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UsuarioViewSet, PacienteViewSet, ProfissionalViewSet

# O Router cria as URLs automaticamente para nós
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)       # Cria /api/usuarios/
router.register(r'pacientes', PacienteViewSet)     # Cria /api/pacientes/
router.register(r'profissionais', ProfissionalViewSet) # Cria /api/profissionais/

urlpatterns = [
    # Painel Administrativo do Django (já vem pronto)
    path('admin/', admin.site.urls),
    
    # Nossas rotas da API
    path('api/', include(router.urls)),
    
    # Adiciona URLs de login da interface navegável do DRF (opcional, mas útil)
    path('api-auth/', include('rest_framework.urls')),
]
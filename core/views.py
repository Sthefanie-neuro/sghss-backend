from rest_framework import viewsets, permissions
from .models import Usuario, Paciente, ProfissionalSaude
from .serializers import UsuarioSerializer, PacienteSerializer, ProfissionalSerializer

# 1. View para Gerenciar Usuários (Autenticação)
class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    
    # Permite que qualquer pessoa se cadastre (Sign-up), mas apenas Admin vê a lista de todos
    def get_permissions(self):
        if self.action == 'create':
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]

# 2. View para Gerenciar Pacientes (CRUD Completo)
class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    # Apenas usuários logados podem ver ou criar pacientes (Segurança/LGPD)
    permission_classes = [permissions.IsAuthenticated]

# 3. View para Gerenciar Profissionais
class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalSaude.objects.all()
    serializer_class = ProfissionalSerializer
    permission_classes = [permissions.IsAuthenticated]
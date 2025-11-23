from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Modelo de Usuário Customizado (Autenticação Central)
class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        PACIENTE = 'PACIENTE', 'Paciente'
        PROFISSIONAL = 'PROFISSIONAL', 'Profissional de Saúde'
        ADMIN = 'ADMIN', 'Administrador'

    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.PACIENTE
    )
    
    # Campos obrigatórios para o Django não reclamar
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )

# 2. Perfil de Paciente (Ligado ao Usuário)
class Paciente(models.Model):
    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        primary_key=True,
        related_name='paciente_perfil'
    )
    cpf = models.CharField(max_length=14, unique=True)
    cartao_sus = models.CharField(max_length=20, blank=True, null=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.cpf}"

# 3. Perfil de Profissional de Saúde (Ligado ao Usuário)
class ProfissionalSaude(models.Model):
    usuario = models.OneToOneField(
        Usuario, 
        on_delete=models.CASCADE, 
        primary_key=True,
        related_name='profissional_perfil'
    )
    registro_profissional = models.CharField(max_length=20, unique=True, help_text="CRM, COREN, etc.")
    especialidade = models.CharField(max_length=50)

    def __str__(self):
        return f"Dr(a). {self.usuario.first_name} - {self.especialidade}"
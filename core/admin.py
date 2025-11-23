from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Paciente, ProfissionalSaude

# Registra o Modelo de Usuário usando o visual padrão do Django
admin.site.register(Usuario, UserAdmin)

# Registra os nossos modelos do SGHSS
admin.site.register(Paciente)
admin.site.register(ProfissionalSaude)
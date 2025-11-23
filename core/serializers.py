from rest_framework import serializers
from .models import Usuario, Paciente, ProfissionalSaude

# 1. Tradutor de Usuários (Para Login e Cadastro)
class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # A senha nunca é devolvida na leitura, apenas escrita

    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'password', 'tipo_usuario']

    # Esta função garante que a senha seja criptografada ao criar o usuário
    def create(self, validated_data):
        user = Usuario.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            tipo_usuario=validated_data.get('tipo_usuario', 'PACIENTE')
        )
        return user

# 2. Tradutor de Pacientes
class PacienteSerializer(serializers.ModelSerializer):
    # Inclui os dados do usuário (nome, email) dentro do objeto paciente para facilitar a leitura
    nome_usuario = serializers.CharField(source='usuario.username', read_only=True)
    email_usuario = serializers.CharField(source='usuario.email', read_only=True)

    class Meta:
        model = Paciente
        fields = ['usuario', 'nome_usuario', 'email_usuario', 'cpf', 'cartao_sus', 'data_nascimento']

# 3. Tradutor de Profissionais
class ProfissionalSerializer(serializers.ModelSerializer):
    nome_usuario = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = ProfissionalSaude
        fields = ['usuario', 'nome_usuario', 'registro_profissional', 'especialidade']
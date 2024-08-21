from django.db import models

# Create your models here.

class Estudante(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True, max_length=30)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    celular = models.CharField(max_length=14)

    def __str__(self) -> str:
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100, blank=False)
    nivel = models.CharField(max_length = 1, choices = NIVEL, blank=False, null=False, default = 'B')

    def __str__(self) -> str:
        return self.codigo
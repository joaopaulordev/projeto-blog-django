from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField(max_length=300, null=True, blank=True)
    foto = models.ImageField(null=False, blank=False, default='user-default.png')
    cargo = models.CharField(max_length=200, null=True, blank=True)


    class Meta:
        verbose_name = "Funcionário"
        verbose_name_plural = "Funcionários"

    def __str__(self):
        return f'{self.nome} | {self.cargo}'

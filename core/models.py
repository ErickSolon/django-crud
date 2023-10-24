from django.db import models


class InformacoesSensiveis(models.Model):
    id = models.BigAutoField(primary_key=True)
    cpf = models.CharField(max_length=25)
    identidade = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.cpf


class Pessoas(models.Model):
    id = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.IntegerField(null=True)
    InformacoesSensiveis = models.OneToOneField(
        InformacoesSensiveis,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self) -> str:
        return self.nome

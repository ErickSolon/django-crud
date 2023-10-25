from django.db import models


class InformacoesSensiveis(models.Model):
    cpf = models.CharField(max_length=25)
    identidade = models.CharField(max_length=25)

    def __str__(self) -> str:
        return self.cpf

class Pessoas(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    telefone = models.IntegerField(null=True)
    InformacoesSensiveis = models.ForeignKey(
        InformacoesSensiveis,
        on_delete=models.CASCADE,
        related_name='pessoa',
        null=True
    )

    def __str__(self):
        return self.nome


    def __str__(self):
        return self.nome

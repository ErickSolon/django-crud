from rest_framework import serializers
from .models import Pessoas, InformacoesSensiveis


class InformacoesSensiveisSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesSensiveis
        fields = ['id', 'cpf', 'identidade']


class PessoasSerializer(serializers.ModelSerializer):
    InformacoesSensiveis = InformacoesSensiveisSerializer()

    class Meta:
        model = Pessoas
        fields = ['id', 'nome', 'sobrenome',
                  'telefone', 'InformacoesSensiveis']

    def create(self, validated_data):
        informacoes_sensiveis_data = validated_data.pop('InformacoesSensiveis')
        informacoes_sensiveis_instance = InformacoesSensiveis.objects.create(
            **informacoes_sensiveis_data)
        pessoa_instance = Pessoas.objects.create(
            InformacoesSensiveis=informacoes_sensiveis_instance, **validated_data)
        return pessoa_instance

    def update(self, instance, validated_data):
        informacoes_sensiveis_data = validated_data.pop('InformacoesSensiveis')
        informacoes_sensiveis_instance = instance.InformacoesSensiveis

        instance.nome = validated_data.get('nome', instance.nome)
        instance.sobrenome = validated_data.get(
            'sobrenome', instance.sobrenome)
        instance.telefone = validated_data.get(
            'telefone', instance.telefone)
        instance.save()

        informacoes_sensiveis_instance.cpf = informacoes_sensiveis_data.get(
            'cpf', informacoes_sensiveis_instance.cpf)
        informacoes_sensiveis_instance.identidade = informacoes_sensiveis_data.get(
            'identidade', informacoes_sensiveis_instance.identidade)

        return instance


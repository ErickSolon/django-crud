from django.shortcuts import render
from .models import Pessoas
from .serializers import PessoasSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        informacoes_sensiveis_instance = instance.InformacoesSensiveis
        if informacoes_sensiveis_instance:
            informacoes_sensiveis_instance.delete()

        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

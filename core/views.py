from django.shortcuts import render
from .models import Pessoas
from .serializers import PessoasSerializer
from rest_framework import viewsets


class PessoasViewSet(viewsets.ModelViewSet):
    queryset = Pessoas.objects.all()
    serializer_class = PessoasSerializer

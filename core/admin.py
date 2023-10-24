from django.contrib import admin
from .models import Pessoas, InformacoesSensiveis

admin.site.register(Pessoas)
admin.site.register(InformacoesSensiveis)
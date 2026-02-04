#!/usr/bin/env python
"""Script para criar evento de exemplo no banco de dados"""

import os
import sys
import django

# Setup Django
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from pages.models import Evento
from django.utils import timezone
from datetime import timedelta

def criar_evento():
    # Data futura (40 dias a partir de hoje)
    from datetime import date
    data_evento = date.today() + timedelta(days=40)
    
    # Verificar se já existe
    if Evento.objects.filter(titulo="Hackathon IPM 2026").exists():
        print("⚠️  Evento 'Hackathon IPM 2026' já existe!")
        evento = Evento.objects.get(titulo="Hackathon IPM 2026")
    else:
        # Criar evento
        evento = Evento.objects.create(
            titulo="Hackathon IPM 2026",
            descricao="Grande competição de programação e inovação tecnológica. Participe e mostre suas habilidades em desenvolvimento de software, inteligência artificial e soluções criativas para problemas reais. Prêmios incríveis para os vencedores!",
            data=data_evento,
            vagas=50
        )
        print("✅ Evento criado com sucesso!")
    
    print(f"\n📋 Detalhes do Evento:")
    print(f"   Título: {evento.titulo}")
    print(f"   ID: {evento.id}")
    print(f"   Data: {evento.data.strftime('%d/%m/%Y')}")
    print(f"   Vagas: {evento.vagas}")
    print(f"\n🔗 URL: http://127.0.0.1:8000/evento/{evento.id}/")

if __name__ == "__main__":
    criar_evento()

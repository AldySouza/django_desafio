from rest_framework import generics, permissions
from .models import Characters
from .serializers import CharactersSerializer

class CharacterList(generics.ListCreateAPIView):
    queryset = Characters.objects.all()
    #autenticação
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CharactersSerializer

class CharacterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Characters.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CharactersSerializer

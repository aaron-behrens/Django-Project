from rest_framework import generics

from .models import Movie
from .serializers import MovieSerializer

class MovieList(generics.ListCreateAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset
    
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
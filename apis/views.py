from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,DestroyAPIView
from .serialaizes import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status  


class ActorListAPIVIEW(ListAPIView):
    queryset =Actor.objects.filter(is_deleted = False).order_by("-id")
    serializer_class = Actorserial
    
    @action(detail=True,methods = "POST")
    def restore(self,request,pk=None):
        actor = Actor.objects.filter(id=pk).first()
        if actor and actor.is_deleted:
            actor.restore()
            return Response("object restored", status=status.HTTP_200_OK) 
        
    @action(detail=True, methods=['delete'])
    def hard_delete(self, request, pk=None):
        try:
            actor = Actor.objects.get(pk=pk)
            actor.delete()  
            return Response({"message": "Actor deleted permanently."}, status=status.HTTP_204_NO_CONTENT)
        except Actor.DoesNotExist:
            return Response({"error": "Actor not found."}, status=status.HTTP_404_NOT_FOUND)
    
    
    
class ActorCreateAPIVIEW(CreateAPIView):
    serializer_class = Actorserial
    
    
class ActorRetrieveAPIView(RetrieveAPIView):
    queryset = Actor.objects.all()
    serializer_class = Actorserial
    
class ActorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = Actorserial
    
    
class ActorDestroyAPIView(DestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = Actor.objects.all()
    
    
# Director
class DirectorListAPIVIEW(ListAPIView):
    queryset =Director.objects.all().order_by("-id")
    serializer_class = DirectorrSerial
    
class DirectorCreateAPIVIEW(CreateAPIView):
    serializer_class = DirectorrSerial
    
    
class DirectorRetrieveAPIView(RetrieveAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorrSerial
    
class DirectorRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorrSerial
    
    
class DirectorDestroyAPIView(DestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = Director.objects.all()
    
    
# Genres
class GenresListAPIVIEW(ListAPIView):
    queryset = Genres.objects.all().order_by("-id")
    serializer_class = GenresSerial
    
class GenresCreateAPIVIEW(CreateAPIView):
    serializer_class = GenresSerial
    
    
class GenresRetrieveAPIView(RetrieveAPIView):
    queryset =  Genres.objects.all()
    serializer_class = GenresSerial
    
class GenresRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =  Genres.objects.all()
    serializer_class = GenresSerial
    
    
class GenresDestroyAPIView(DestroyAPIView):
    queryset =  Genres.objects.all()
    serializer_class =  Genres.objects.all()
    
    
    
# Movie

class MovieListAPIVIEW(ListAPIView):
    queryset =  Movie.objects.all().order_by("-id")
    serializer_class = MovieSerial
    
class MovieCreateAPIVIEW(CreateAPIView):
    serializer_class = MovieSerial
    
    
class MovieRetrieveAPIView(RetrieveAPIView):
    queryset =   Movie.objects.all()
    serializer_class = MovieSerial
    
class MovieRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =   Movie.objects.all()
    serializer_class = MovieSerial
    
    
class MovieDestroyAPIView(DestroyAPIView):
    queryset =   Movie.objects.all()
    serializer_class =   Movie.objects.all()
    
    
# Reviewer


class ReviewerListAPIVIEW(ListAPIView):
    queryset =  Reviewer.objects.all().order_by("-id")
    serializer_class = ReviewerSerial
    
class ReviewerCreateAPIVIEW(CreateAPIView):
    serializer_class = ReviewerSerial
    
    
class ReviewerRetrieveAPIView(RetrieveAPIView):
    queryset =   Reviewer.objects.all()
    serializer_class = ReviewerSerial
    
class ReviewerRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =   Reviewer.objects.all()
    serializer_class = ReviewerSerial
    
    
class ReviewerDestroyAPIView(DestroyAPIView):
    queryset =   Reviewer.objects.all()
    serializer_class =   Reviewer.objects.all()
    
    
    
# Movie_cast
class Movie_castListAPIVIEW(ListAPIView):
    queryset =  Movie_cast.objects.all().order_by("-id")
    serializer_class = Movie_castSerial
    
class Movie_castCreateAPIVIEW(CreateAPIView):
    serializer_class = Movie_castSerial
    
    
class Movie_castRetrieveAPIView(RetrieveAPIView):
    queryset =   Movie_cast.objects.all()
    serializer_class = Movie_castSerial
    
class Movie_castRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =   Movie_cast.objects.all()
    serializer_class = Movie_castSerial
    
    
class Movie_castDestroyAPIView(DestroyAPIView):
    queryset =   Movie_cast.objects.all()
    serializer_class =   Movie_cast.objects.all()


# Movie_genres

class Movie_genresListAPIVIEW(ListAPIView):
    queryset =  Movie_genres.objects.all().order_by("-id")
    serializer_class = Movie_genresSerial
    
class Movie_genresCreateAPIVIEW(CreateAPIView):
    serializer_class = Movie_genresSerial
    
    
class Movie_genresRetrieveAPIView(RetrieveAPIView):
    queryset =   Movie_genres.objects.all()
    serializer_class = Movie_genresSerial
    
class Movie_genresRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =   Movie_genres.objects.all()
    serializer_class = Movie_genresSerial
    
    
class Movie_genresDestroyAPIView(DestroyAPIView):
    queryset =   Movie_genres.objects.all()
    serializer_class =   Movie_genres.objects.all()
    
    
    

    
    
# Rating
class RatingListAPIVIEW(ListAPIView):
    queryset =  Rating.objects.all().order_by("-id")
    serializer_class = RatingSerial
    
class RatingCreateAPIVIEW(CreateAPIView):
    serializer_class = RatingSerial
    
    
class RatingRetrieveAPIView(RetrieveAPIView):
    queryset =   Rating.objects.all()
    serializer_class = RatingSerial
    
class RatingRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =   Rating.objects.all()
    serializer_class = RatingSerial
    
    
class RatingDestroyAPIView(DestroyAPIView):
    queryset =   Rating.objects.all()
    serializer_class =   Rating.objects.all()



# Movie_direction

class Movie_directionListAPIVIEW(ListAPIView):
    queryset =  Movie_direction.objects.all().order_by("-id")
    serializer_class = Movie_directionSerial
    
class Movie_directionCreateAPIVIEW(CreateAPIView):
    serializer_class = Movie_directionSerial
    
    
class Movie_directionRetrieveAPIView(RetrieveAPIView):
    queryset =   Movie_direction.objects.all()
    serializer_class = Movie_directionSerial
    
class Movie_directionRetrieveUpdateAPIView(RetrieveUpdateAPIView):
    queryset =   Movie_direction.objects.all()
    serializer_class = Movie_directionSerial
    
    
class Movie_directionDestroyAPIView(DestroyAPIView):
    queryset =   Movie_direction.objects.all()
    serializer_class =   Movie_direction.objects.all()
    
    
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view



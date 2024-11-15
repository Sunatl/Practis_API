from .views import *
from django.urls import path

urlpatterns = [
    path("l_actor",ActorListAPIVIEW.as_view(),name="l_actor"),
    path("c_actor",ActorCreateAPIVIEW.as_view(),name="c_actor"),
    path("d_actor/<int:pk>",ActorDestroyAPIView.as_view(),name="d_actor"),
    path("r_actor/<int:pk>",ActorRetrieveAPIView.as_view(),name="r_actor"),
    path("u_actor/<int:pk>",ActorRetrieveUpdateAPIView.as_view(),name="u_actor"),
    
    path("l_Director",DirectorListAPIVIEW.as_view(),name="l_Director"),
    path("c_Director",DirectorCreateAPIVIEW.as_view(),name="c_Director"),
    path("d_Director/<int:pk>",DirectorDestroyAPIView.as_view(),name="d_Director"),
    path("r_Director/<int:pk>",DirectorRetrieveAPIView.as_view(),name="r_Director"),
    path("u_Director/<int:pk>",DirectorRetrieveUpdateAPIView.as_view(),name="u_Director"),
    
    
    path("l_Genres",GenresListAPIVIEW.as_view(),name="l_Genres"),
    path("c_Genres",GenresCreateAPIVIEW.as_view(),name="c_Genres"),
    path("d_Genres/<int:pk>",GenresDestroyAPIView.as_view(),name="d_Genres"),
    path("r_Genres/<int:pk>",GenresRetrieveAPIView.as_view(),name="r_Genres"),
    path("u_Genres/<int:pk>",GenresRetrieveUpdateAPIView.as_view(),name="u_Genres"),
    
    
    path("l_Movie",MovieListAPIVIEW.as_view(),name="l_Movie"),
    path("c_Movie",MovieCreateAPIVIEW.as_view(),name="c_Movie"),
    path("d_Movie/<int:pk>",MovieDestroyAPIView.as_view(),name="d_Movie"),
    path("r_Movie/<int:pk>",MovieRetrieveAPIView.as_view(),name="r_Movie"),
    path("u_Movie/<int:pk>",MovieRetrieveUpdateAPIView.as_view(),name="u_Movie"),
    
    
    path("l_Reviewer",ReviewerListAPIVIEW.as_view(),name="l_Reviewer"),
    path("c_Reviewer",ReviewerCreateAPIVIEW.as_view(),name="c_Reviewer"),
    path("d_Reviewer/<int:pk>",ReviewerDestroyAPIView.as_view(),name="d_Reviewer"),
    path("r_Reviewer/<int:pk>",ReviewerRetrieveAPIView.as_view(),name="r_Reviewer"),
    path("u_Reviewer/<int:pk>",ReviewerRetrieveUpdateAPIView.as_view(),name="u_Reviewer"),
    
    
    
    path("l_Movie_cast",Movie_castListAPIVIEW.as_view(),name="l_Movie_cast"),
    path("c_Movie_cast",Movie_castCreateAPIVIEW.as_view(),name="c_Movie_cast"),
    path("d_Movie_cast/<int:pk>",Movie_castDestroyAPIView.as_view(),name="d_Movie_cast"),
    path("r_Movie_cast/<int:pk>",Movie_castRetrieveAPIView.as_view(),name="r_Movie_cast"),
    path("u_Movie_cast/<int:pk>",Movie_castRetrieveUpdateAPIView.as_view(),name="u_Movie_cast"),
    
    
    path("l_Movie_genres",Movie_genresListAPIVIEW.as_view(),name="l_Movie_genres"),
    path("c_Movie_genres",Movie_genresCreateAPIVIEW.as_view(),name="c_Movie_genres"),
    path("d_Movie_genres/<int:pk>",Movie_genresDestroyAPIView.as_view(),name="d_Movie_genres"),
    path("r_Movie_genres/<int:pk>",Movie_genresRetrieveAPIView.as_view(),name="r_Movie_genres"),
    path("u_Movie_genres/<int:pk>",Movie_genresRetrieveUpdateAPIView.as_view(),name="u_Movie_genres"),
    
    
    path("l_Rating",RatingListAPIVIEW.as_view(),name="l_Rating"),
    path("c_Rating",RatingCreateAPIVIEW.as_view(),name="c_Rating"),
    path("d_Rating/<int:pk>",RatingDestroyAPIView.as_view(),name="d_Rating"),
    path("r_Rating/<int:pk>",RatingRetrieveAPIView.as_view(),name="r_Rating"),
    path("u_Rating/<int:pk>",RatingRetrieveUpdateAPIView.as_view(),name="u_Rating"),
    
    path("l_Movie_direction",Movie_directionListAPIVIEW.as_view(),name="l_Movie_direction"),
    path("c_Movie_direction",Movie_directionCreateAPIVIEW.as_view(),name="c_Movie_direction"),
    path("d_Movie_direction/<int:pk>",Movie_directionDestroyAPIView.as_view(),name="d_Movie_direction"),
    path("r_Movie_direction/<int:pk>",Movie_directionRetrieveAPIView.as_view(),name="r_Movie_direction"),
    path("u_Movie_direction/<int:pk>",Movie_directionRetrieveUpdateAPIView.as_view(),name="u_Movie_direction"),
    
    
    
    
]

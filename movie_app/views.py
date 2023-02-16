from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializer import DirectorSerializer, MovieSerializer, ReviewSerializer

#режиссеры
@api_view(['GET'])
def directors_list_api_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def directors_detail_api_view(request, id):
    try:
        directors = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = DirectorSerializer(directors, many=False)
    return Response(data=serializer.data)

# фильмы
@api_view(['GET'])
def movies_list_api_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def movies_detail_api_view(request, id):
    try:
        movies = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = MovieSerializer(movies, many=False)
    return Response(data=serializer.data)

# Отзывы
@api_view(['GET'])
def reviews_list_api_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def reviews_detail_api_view(request, id):
    try:
        reviews = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = ReviewSerializer(reviews, many=False)
    return Response(data=serializer.data)
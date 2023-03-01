from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import MovieSerializer, DirectorSerializer, ReviewSerializer, MovieReviewSerializer, \
    DirectorValidateSerializer, MovieValidateSerializer, ReviewValidateSerializer
from .models import Movie, Director, Review


@api_view(['GET'])
def movie_reviews_view(request):
    movie = Movie.objects.all()
    serializer = MovieReviewSerializer(movie, many=True)
    return Response(data=serializer.data)


@api_view(['GET', 'POST'])
def director_list_api_view(request):
    if request.method == 'GET':
        '''list of directors'''
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)
        return Response(data=serializer.data)

    elif request.method == 'POST':
        '''creation of directors'''
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        return Response(data={'message': 'Data received',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_api_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'detail': 'Director_not_found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data={'message': 'Data received',
                              'director': DirectorSerializer(director).data},
                        status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])
def movie_list_api_view(request):
    if request.method == 'GET':
        '''List of movies'''
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(data=serializer.data)


    elif request.method == 'POST':
        '''Creation of movies'''
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data=serializer.errors,
                            status=status.HTTP_406_NOT_ACCEPTABLE)
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        # director = Director.objects.create(name=request.data.get('name'))
        return Response(data={'message': 'Data received',
                              'movie': MovieSerializer(movie).data},
                              status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def movie_detail_api_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'detail': 'movie_not_found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MovieSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = MovieValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie.title = request.data.get('title')
        movie.description = request.data.get('description')
        movie.duration = request.data.get('duration')
        movie.director_id = request.data.get('director_id')
        movie.save()
        return Response(data={'message': 'Data received',
                              'movie': MovieSerializer(movie).data},
                        status=status.HTTP_200_OK)



@api_view(['GET', 'POST'])
def review_list_api_view(request):
    if request.method == 'GET':
        '''List of reviews'''
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(data=serializer.data)
    elif request.method == 'POST':
        '''Creation of reviews'''
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        text = request.data.get('text')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text, stars=stars)
        return Response(data={'message': 'Data received',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_api_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'detail': 'Review_not_found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ReviewSerializer(review, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ReviewValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review.text = request.data.get('text')
        review.stars = request.data.get('stars')
        review.movie = request.data.get('movie')
        review.save()
        return Response(data={'message': 'Data received',
                              'review': ReviewSerializer(review).data},
                        status=status.HTTP_200_OK)





from rest_framework import serializers
from .models import Director, Movie, Review
from rest_framework.exceptions import ValidationError


class MovieReviewSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    stars = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = "title reviews rating stars".split()


    def get_stars(self, movie):
        return [i.stars for i in movie.movie_reviews.all()]


    def get_reviews(self, movie):
        return [i.text for i in movie.movie_reviews.all()]


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'name movies_count'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars '.split()


class MovieSerializer(serializers.ModelSerializer):
    director = DirectorSerializer()
    movie_reviews = ReviewSerializer(many=True)
    filtered_reviews = ReviewSerializer(many=True)
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'duration', 'director_name',
                 'filtered_reviews', 'director', 'movie_reviews', 'rating']

class DirectorValidateSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=20, min_length=5,)

    def validate_name(self, name):
        if len(name) < 2:
            raise ValidationError('Too short')
        elif len(name) > 25:
            raise ValidationError('Too long')

class MovieValidateSerializer(serializers.Serializer):
    title = serializers.CharField(required=True, max_length=20, min_length=2)
    description = serializers.CharField(required=True, max_length=200)
    duration = serializers.FloatField(required=False, max_value=5)
    director_id = serializers.IntegerField(required=False)


    def validate_director_id(self, director_id):
        try:
            Director.objects.get(id=director_id)
        except Director.DoesNotExist:
            raise ValidationError('not exists!')
        return director_id

class ReviewValidateSerializer(serializers.Serializer):
    text = serializers.CharField(required=True, max_length=200)
    stars = serializers.IntegerField(required=True)


    def validate_stars(self, stars):
        if stars > 5:
            raise ValidationError('maximum value=5')
        elif stars < 1:
            raise ValidationError('minimum value=1')
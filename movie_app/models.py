from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    @property
    def movies_count(self):
        count = self.movies_quantity.all().count()
        return count






class Movie(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    duration = models.FloatField(null=False)
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True, related_name='movies_quantity')

    def __str__(self):
        return self.title

    def filtered_reviews(self):
        return self.movie_reviews.filter(stars__gt=3)


    def director_name(self):
        try:
            return self.director.name
        except:
            return ''

    @property
    def rating(self):
        count = self.movie_reviews.all().count()
        sum_stars = 0
        for i in self.movie_reviews.all():
            sum_stars += i.stars
        if count != 0:
            return sum_stars // count


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, null=True, related_name='movie_reviews')
    text = models.TextField(null=True, blank=True)
    stars = models.IntegerField(choices=(
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ), default=5)
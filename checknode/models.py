# there would be 2 types of node :
# 1)Actor
# 2)movie


from django.db import models

# Create your models here.

# class Actor(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

#     class Meta:
#         ordering = ('name',)

# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     actors = models.ManyToManyField(Actor)
#     year = models.IntegerField()

#     def __str__(self):
#         return self.title

#     class Meta:
#         ordering = ('title',)

class Genre(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Production_company(models.Model):
    id=models.IntegerField(primary_key=True)
    path_logo = models.ImageField()
    name= models.CharField(max_length=500)
    origin_country= models.CharField(max_length=100)

class Production_countries(models.Model):
    iso_3166_1 = models.CharField(max_length=100)
    name = models.CharField(max_length=200)

class Spoken_languages(models.Model):
    english_name = models.CharField(max_length=200)
    iso_639_1 = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Mockmovie(models.Model):
    adult = models.BooleanField()
    backdrop_path = models.CharField(max_length=500)
    belongs_to_collection = models.CharField(max_length=500)
    budget = models.IntegerField()
    genre= models.ManyToManyField(Genre)
    homepage=models.CharField(max_length=500)
    id=models.IntegerField(primary_key=True)
    imdb_id = models.CharField(max_length=500)
    original_language = models.CharField(max_length=1000)
    original_title = models.CharField(max_length=500)
    overview = models.CharField(max_length=500)
    popularity = models.FloatField()
    poster_path = models.CharField(max_length=500)
    production_companies=models.ManyToManyField(Production_company)
    production_countries = models.ManyToManyField(Production_countries)
    release_date = models.CharField(max_length=100)
    revenue = models.IntegerField()
    runtime = models.IntegerField() 
    spoken_languages = models.ManyToManyField(Spoken_languages)
    status = models.CharField(max_length=500)
    tagline = models.CharField(max_length=1000)
    title = models.CharField(max_length=500)
    video = models.BooleanField()
    vote_average =models.FloatField()
    vote_count = models.IntegerField()
    is_processed = models.BooleanField()
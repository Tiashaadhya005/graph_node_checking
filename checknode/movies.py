import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import Actor, Genre, Mockmovie, Movie, Production_company, Production_countries, Spoken_languages

# Create a GraphQL type for the actor model
class ActorType(DjangoObjectType):
    class Meta:
        model = Actor

# Create a GraphQL type for the movie model
class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

# class Query1(ObjectType):
#     # movie properties return one value of ActorType and MovieType respectively, 
#     # and both require an ID that's an integer.

#     #The actors and movies properties return a list of their respective types
    
#     actor = graphene.Field(ActorType, id=graphene.Int())
#     movie = graphene.Field(MovieType, id=graphene.Int())
#     actors = graphene.List(ActorType)
#     movies= graphene.List(MovieType)

#     def resolve_actor(self, info, **kwargs):
#         '''Functionality to get actor name with particular id'''
#         id = kwargs.get('id')
#         if id is not None:
#             return Actor.objects.get(pk=id)
#         return None

#     def resolve_movie(self, info, **kwargs):
#         '''Functionality to get movie name with particular id'''
#         id = kwargs.get('id')
#         if id is not None:
#             return Movie.objects.get(pk=id)
#         return None

#     def resolve_actors(self, info, **kwargs):
#         '''Functionality to get all actors '''
#         return Actor.objects.all()

#     def resolve_movies(self, info, **kwargs):
#         '''Functionality to get all actors '''
#         return Movie.objects.all()

    # def resolve_node_name(self,info,**kwargs):
    #     if kwargs.get('type')=='actor':
    #         return Actor.objects.get(pk=id)

class GenreType(DjangoObjectType):
    class Meta:
        model = Genre

class MockMovieType(DjangoObjectType):
    class Meta:
        model = Mockmovie

class Production_compType(DjangoObjectType):
    class Meta:
        model = Production_company

class Production_countryType(DjangoObjectType):
    class Meta:
        model = Production_countries

class SpokenLanguageType(DjangoObjectType):
    class Meta:
        model = Spoken_languages

class Query(ObjectType):
    mock_movies= graphene.Field(MockMovieType, id=graphene.Int())

    def resolve_mock_movie(self, info, **kwargs):
        '''Functionality to get movie name with particular id'''
        id = kwargs.get('id')
        if id is not None:
            return Movie.objects.get(pk=id)
        return None


schema = graphene.Schema(query=Query)


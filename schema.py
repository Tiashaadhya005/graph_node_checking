import graphene
import graphnode.checknode.movies

class Query(graphnode.checknode.movies.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass

# class Mutation(django_graphql_movies.movies.schema.Mutation, graphene.ObjectType):
#     # This class will inherit from multiple Queries
#     # as we begin to add more apps to our project
#     pass

schema = graphene.Schema(query=Query)
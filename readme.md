## purpose: To create graph node using graphql in django

---------------------------
Point to be Noted:
1)  Graphene-Django provides some additional abstractions that make it easy to add GraphQL  functionality to your Django project.

2)  Query: class which is similar to GET method in REST API
    Mutation : class which is similar to POST, PUT and DELETE methods
    Subscriptions: class similar to pub-sub model

-----------------------------

GraphQL represents data in the form of Graph wherein each node represent a data model. GraphQL Schema represents this!

# Designing a Movie Schema
(inside models.py)
```type Actor {
  id: ID!
  name: String!
}
```

```type Movie {
  id: ID!
  title: String!
  actors: [Actor]
  year: Int!
}
```
Note: The exclamation mark signifies that the field is required.

# Creating Queries
(onside movies.py)
A query specifies what data can be retrieved and what's required to get to it:

```
  type Query {
  actor(id: ID!): Actor
  movie(id: ID!): Movie
  actors: [Actor]
  movies: [Movie]
}
```

-----------------------------------------
As with the GraphQL schema, the Actor model has a name whereas the Movie model has a title, a many-to-many relationship with the actors and a year. The IDs are automatically generated for us by Django.

-----------------------------------------

After we build our API, we'll want to be able to perform queries to test if it works. Let's load some data into our database, save the following JSON as data.json in project's root directory.

then run the following command:
```
python manage.py loaddata movies.json
```

-------------------------------------------

The four methods we created in the Query class inside mvies.py file are called resolvers. Resolvers connect the queries in the schema to actual actions done by the database. As is standard in Django, we interact with our database via models.

Consider the 'resolve_actor' function. We retrieve the ID from the query parameters and return the actor from our database with that ID as its primary key. The 'resolve_actors' function simply gets all the actors in the database and returns them as a list.

-------------------------------------------------

## Testing the api:
url: http://127.0.0.1:8000/graphql/

```
query getActors {
  actors {
    id
    name
  }
}
```
result:
```
{
  "data": {
    "actors": [
      {
        "id": "1",
        "name": "Michael B. Jordan"
      },
      {
        "id": "2",
        "name": "Sylvester Stallone"
      }
    ]
  }
}
```

```
query getMovie {
  movie(id: 1) {
    title
    actors {
      id
      name
    }
  }
}

```

result(don't want to show id and year for the movie)

```
{
  "data": {
    "movie": {
      "title": "Creed",
      "actors": [
        {
          "id": "1",
          "name": "Michael B. Jordan"
        },
        {
          "id": "2",
          "name": "Sylvester Stallone"
        }
      ]
    }
  }
}
```

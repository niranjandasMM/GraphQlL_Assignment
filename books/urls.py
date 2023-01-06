from django.urls import path, include
from graphene_django.views import GraphQLView
from books.schema import schema

urlpatterns = [
    path("graphql", GraphQLView.as_view(graphiql=True, schema= schema)),
]

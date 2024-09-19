from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# models = resoures in API


class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()  # return a query (lazy object)
        resource_name = 'movies'  # determine the endpoint
        exclude = ['date_created']

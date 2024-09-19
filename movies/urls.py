from django.urls import path
from . import views

# url configuration: it contains one or more path objects that map url endpoints to view functions
# any url starts with movies/
app_name = 'movies'

urlpatterns = [
    # good practice to prefix with name of app =movies
    path('', views.index, name='index'),
    path('<int:movie_id>', views.detail, name='detail')
]

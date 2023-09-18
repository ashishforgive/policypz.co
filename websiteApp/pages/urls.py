from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('registration', views.registration, name='registration'),
    path('login', views.userLogin, name='user_login'),



    path('about-policy', views.aboutPolicy, name='about_policy'),
    path('privacy', views.privacy, name='privacy'),
    path('how-to-vote', views.howToVote, name='how_to_vote'),
    path('term', views.term, name='term'),
    path('browse-all-elections', views.allElections, name='all_elections'),
    path('your-favourites', views.yourFavourites, name='your_favourites'),
    path('school', views.school, name='school'),   
    path('policy', views.policy, name='policy'),   
]
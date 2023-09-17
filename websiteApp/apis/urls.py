from django.urls import path
from . import views

urlpatterns = [
    path('party-create', views.PartyDataViewSet.as_view({'post': 'partyCreate'})),
    path('condidate-create', views.CondidateDataViewSet.as_view({'post': 'condidateCreate'})),
]
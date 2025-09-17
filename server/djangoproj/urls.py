from django.urls import path
from . import views

urlpatterns = [
    # Routes pour l'authentification
    path('login_user', views.login_user, name='login_user'),
    path('logout_request', views.logout_request, name='logout_request'),
    path('registration', views.registration, name='registration'),
    
    # Routes pour les concessionnaires
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),
    path('get_dealer/<int:dealer_id>', views.get_dealer_details, name='get_dealer_details'),
    
    # Routes pour les avis
    path('get_reviews/<int:dealer_id>', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),
]
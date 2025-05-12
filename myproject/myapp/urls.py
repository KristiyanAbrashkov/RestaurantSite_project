from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginView, name = 'login'),
    path('logout/', views.logoutUser, name = 'logout'),
    path('register/', views.registerUser, name = 'register'),
    path('', views.home, name = 'home'),
    path('reviews/', views.reviews, name = 'reviews'),
    path('create-review/', views.createReview, name = 'create-review'),
    path('update-review/<str:pk>/', views.updateReview, name = 'update-review'),
    path('delete-review/<str:pk>/', views.deleteReview, name = 'delete-review')
]
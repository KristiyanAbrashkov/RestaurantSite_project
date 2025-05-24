from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('reviews/', views.getReviews),
    path('reviews/<str:pk>', views.getReview),
    path('profile/', views.getUserProfile),
    path('edit-profile/', views.updateUserProfile),
]
from rest_framework.serializers import ModelSerializer
from myapp.models import Review
from django.contrib.auth.models import User

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
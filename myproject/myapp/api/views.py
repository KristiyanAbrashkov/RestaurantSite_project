from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from myapp.models import Review
from django.contrib.auth.models import User
from .serializers import ReviewSerializer, UserSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api/',
        'GET /api/reviews',
        'GET /api/reviews/:id',
        'GET /api/profile',
        'PUT /api/edit-profile'
    ]
    return Response(routes)

@api_view(['GET'])
def getReviews(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getReview(request, pk):
    review = Review.objects.get(id=pk)
    serializer = ReviewSerializer(review, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createReview(request):
    serializer = ReviewSerializer(data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['PUT'])
def updateReview(request, pk):
    review = Review.objects.get(id=pk)
    serializer = ReviewSerializer(instance=review, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteReview(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return Response('Review deleted successfully')

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUserProfile(request):
    user = request.user
    serializer = UserSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
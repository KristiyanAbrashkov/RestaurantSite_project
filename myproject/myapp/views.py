from django.shortcuts import render
from .models import Review

# Create your views here.

#review = [
#    {'review': 'GOOD'},
#    {'review': 'MID'},
#    {'review': 'BAD'},
#]
def reviews(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'myapp/reviews.html', context)

def home(request):
    return render(request, 'myapp/home.html')

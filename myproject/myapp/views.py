from django.shortcuts import render

# Create your views here.

review = [
    {'review': 'GOOD'},
    {'review': 'MID'},
    {'review': 'BAD'},
]
def reviews(request):
    context = {'review': review}
    return render(request, 'myapp/reviews.html', context)

def home(request):
    return render(request, 'myapp/home.html')

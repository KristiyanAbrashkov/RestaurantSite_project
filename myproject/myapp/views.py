from django.shortcuts import render

# Create your views here.

review = [
    {'id':1, 'name': 'GOOD'},
    {'id':2, 'name': 'MID'},
    {'id':3, 'name': 'BAD'},
]
def reviews(request):
    context = {'review': review}
    return render(request, 'myapp/review.html', context)

def home(request):
    return render(request, 'myapp/home.html')

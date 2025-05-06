from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm

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

def createReview(request):
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('reviews')

    context = {'form':form}
    return render(request, 'myapp/review_form.html', context)

def updateReview(request, pk):
    review = Review.objects.get(id = pk)
    form = ReviewForm(instance = review)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid:
            form.save()
            return redirect('reviews')
    context = {'form':form}
    return render(request, 'myapp/review_form.html', context)

def deleteReview(request, pk):
    review = Review.objects.get(id = pk)
    if request.method == 'POST':
        review.delete()
        return redirect('reviews')
    return render(request, 'myapp/delete.html', {'obj': review})
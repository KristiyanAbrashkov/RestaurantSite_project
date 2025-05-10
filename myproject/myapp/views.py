from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Review
from .forms import ReviewForm

# Create your views here.

def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or Password does not exist')
    context = {}
    return render(request, 'myapp/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

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
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Review
from .forms import ReviewForm

# Create your views here.

def loginView(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
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
    context = {'page':page}
    return render(request, 'myapp/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An Error occurred during registration!')
    return render(request, 'myapp/login_register.html', {'form':form})

def reviews(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'myapp/reviews.html', context)

def home(request):
    return render(request, 'myapp/home.html')

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    reviews = user.review_set.all()
    context = {'user':user, 'reviews':reviews}
    return render(request, 'myapp/profile.html', context)

@login_required(login_url = 'login')
def createReview(request):
    form = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('reviews')

    context = {'form':form}
    return render(request, 'myapp/review_form.html', context)

@login_required(login_url = 'login')
def updateReview(request, pk):
    review = Review.objects.get(id = pk)
    form = ReviewForm(instance = review)

    if request.user != review.author:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid:
            form.save()
            return redirect('reviews')
    context = {'form':form}
    return render(request, 'myapp/review_form.html', context)

@login_required(login_url = 'login')
def deleteReview(request, pk):
    review = Review.objects.get(id = pk)

    if request.user != review.author:
        return HttpResponse('You are not allowed here!')

    if request.method == 'POST':
        review.delete()
        return redirect('reviews')
    return render(request, 'myapp/delete.html', {'obj': review})
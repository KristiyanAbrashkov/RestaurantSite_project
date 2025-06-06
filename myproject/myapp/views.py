from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from .models import Review
from .forms import ReviewForm, UserForm, CustomUserCreationForm

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
    return render(request, 'myapp/login_register.html', context, status=200)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An Error occurred during registration!')
    context = {'form':form}
    return render(request, 'myapp/login_register.html', context, status=200)

def reviews(request):
    review = Review.objects.all()
    context = {'review': review}
    return render(request, 'myapp/reviews.html', context, status=200)

def home(request):
    return render(request, 'myapp/home.html', status=200)

def userProfile(request, pk):
    try:
        user = User.objects.get(id=pk)
    except User.DoesNotExist:
        return HttpResponse('User not found.', status=404)
    reviews = user.review_set.all()
    context = {'user':user, 'reviews':reviews}
    return render(request, 'myapp/profile.html', context, status=200)

@login_required(login_url = 'login')
def createReview(request):
    form = ReviewForm()

    if request.method == 'POST':
        Review.objects.create(
        author = request.user,
        main_review = request.POST.get('main_review'),
        description = request.POST.get('description'),
        )
        return redirect('reviews')
    
    context = {'form':form}
    return render(request, 'myapp/review_form.html', context, status=200)

@login_required(login_url = 'login')
def updateReview(request, pk):
    try:
        review = Review.objects.get(id = pk)
    except Review.DoesNotExist:
        return HttpResponse('Review not found.', status=404)

    if request.user != review.author:
        return HttpResponse('You are not allowed here!', status=403)

    form = ReviewForm(instance = review)

    if request.method == 'POST':
        form = ReviewForm(request.POST, instance = review)
        if form.is_valid:
            form.save()
            return redirect('reviews')
    context = {'form':form}
    return render(request, 'myapp/review_form.html', context, status=200)

@login_required(login_url = 'login')
def deleteReview(request, pk):
    try:
        review = Review.objects.get(id = pk)
    except Review.DoesNotExist:
        return HttpResponse('Review not found.', status=404)

    if request.user != review.author:
        return HttpResponse('You are not allowed here!', status=403)

    if request.method == 'POST':
        review.delete()
        return redirect('reviews')
    return render(request, 'myapp/delete.html', {'obj': review}, status=200)

@login_required(login_url = 'login')
def updateProfile(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST,instance=user)
        if form.is_valid:
            form.save()
            return redirect('user-profile', pk=user.id)
    return render(request, 'myapp/edit_profile.html', {'form':form}, status=200)

def menu(request):
    return render(request, 'myapp/menu.html', status=200)
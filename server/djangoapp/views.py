# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from datetime import datetime

import logging
import json
from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provide credential can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to login current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    # Get the user object based on session id in request
    print("Log out the user `{}`".format(request.user.username))
    # Logout the user
    logout(request)
    # Redirect user back to course list view
    return JsonResponse({"userName": ""})

# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data['userName']
        password = data['password']
        first_name = data['firstName']
        last_name = data['lastName']
        email = data['email']
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Already Registered"})
        
        # Create new user
        try:
            user = User.objects.create_user(
                username=username,
                password=password,
                first_name=first_name,
                last_name=last_name,
                email=email
            )
            # Login the user after registration
            login(request, user)
            return JsonResponse({"userName": username, "status": "Authenticated"})
        except Exception as e:
            return JsonResponse({"error": str(e)})
    
    return JsonResponse({"error": "Invalid request method"})

# Update the `get_dealerships` view to render the index page with
# a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_reviews` view to render the reviews of a dealer
def get_dealer_reviews(request, dealer_id):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `get_dealer_details` view to render the dealer details
def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)

# Create a `add_review` view to submit a review
def add_review(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)
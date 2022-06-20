from django.shortcuts import render
from rest_framework import generics
import json # need to import this so you can get the json data out of the dictionary from user login page
from .models import UserAccount
from .serializers import UserAccountSerializer

from django.http import JsonResponse # needed to import to send valid response to front end
from django.contrib.auth.hashers import make_password, check_password # create and check passwords


# Create your views here.
class UserAccountList(generics.ListCreateAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer


class UserAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all().order_by('id')
    serializer_class = UserAccountSerializer

### THIS IS THE FUNCTION THAT PERFORMS AUTH
def check_login(request):
        #IF A GET REQUEST IS MADE, RETURN AN EMPTY {}
    if request.method=='GET':
        return JsonResponse({})

        #CHECK IF A PUT REQUEST IS BEING MADE
    if request.method=='PUT':
        jsonRequest = json.loads(request.body) #make the request JSON format
        username = jsonRequest['username'] #get the username from the request
        password = jsonRequest['password'] #get the password from the request
        if UserAccount.objects.get(username=username): #see if username exists in db
            # print("Username: " + username + " = ok")
            user = UserAccount.objects.get(username=username)  #find user object with matching username
            print(password + " ?=? " + user.password)
            check_password(password, user.password):
            # if password == user.password:
                # needed to temporarily change this to check against plain text since our app isn't storing hashed passwords
                # we are working on the hashed password bug
                # print("Password Match")
                return JsonResponse({'id': user.id, 'username': user.username, 'staff':user.staff}) #if passwords match, return a user dict
            else: #passwords don't match so return empty dict
                # print("Password Does Not Match: " + password)
                return JsonResponse({})
        else: #if username doesn't exist in db, return empty dict
            # print("Username " + username + " is not a matching username")
            return JsonResponse({})

# Import required Module to run our server...
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from .forms import RegisterForm
from Home.models import To_do_List_model , Contacts
from django.views.generic.list import ListView


# SuperUser -> hello , passqord-> a

# Create your views here.

# Request for Home page 
def home(request):
    return render(request, 'home.html')

# Request for login Page if user were enter correct password and user id than login other wise return to again login page
def loginuser(request):
    if request.method =='POST':
        user = request.POST.get('user_n') # Taking user-id from web page
        password = request.POST.get('pass') # Taking password from web page
        # Checking login Credintals
        user = authenticate(username=user, password=password) # if user is authenticated than user login else user = None
        # print(user, password)
        if user is not None: # Checking User is not None
             # A  backend authenticated the credentials
             login(request, user) # Login to application
             return redirect("/add_note") # Goes to loged in web page
        else:
             # No backend authenticated the credentials
             return render(request, 'login.html') # Return to login
    return render(request, 'login.html')


# Request to create user

def create_user(request):
    if request.method == 'GET':
        form = RegisterForm() # A registration Form is creating.
        return render(request, 'create_user.html', { 'form': form}) 
    if request.method == 'POST':
        form = RegisterForm(request.POST) # A registration Form is creating.
        if form.is_valid(): # if form is valid.
            user = form.save(commit=True) 
            user.username = user.username.lower()
            user.save() # Form save
            login(request, user)
            return redirect('/login')  # Return to login
        else:
            return render(request, 'create_user.html', {'form': form})  # Return to User creation Form

#Log-out User
def logoutuser(request):
    logout(request) #pre-define Function
    return redirect('/home') # return to home page

# Our main application

def app(request):
    if request.method =='POST': 
        title= request.POST.get('title') # Taking title from web page
        note= request.POST.get('notes') # Taking task from web page
        # Check=request.POST.get('check')
        file = To_do_List_model(title=title,notes=note) # Update to our To-do model
        file.save() # File save
    return render(request, 'app.html') # Return to application page

# Show task and add task also...
def add_note(request):
    todo_lists = To_do_List_model.objects.all() # Take all object from our model.
    return render(request, 'add_note.html', {'file': todo_lists}) # Request to show our data.


# Thanks note web page...
def thanks(request):
    return render(request, 'Thanks.html') # REquesting to web page for thanking you to enter your contact...

# Enter Your Contact Information..
def contact(request):
    if request.method =='POST':
        # Taking all required data...
        FN= request.POST.get('First_name')
        LN= request.POST.get('Last_name')
        EI= request.POST.get('Email')
        A1= request.POST.get('Address_1')
        A2= request.POST.get('Address_2')
        C= request.POST.get('City')
        S= request.POST.get('State')
        Z= request.POST.get('Zip')
        contact =  Contacts(First_Name=FN,Last_Name=LN,Email_Name=EI,Address_1=A1,City=C,State=S,Zip=Z)
        # print(contact)
        contact.save() # Save Contact
        if request.user.is_anonymous: # If user is not logged in than go to hame page 
            return redirect('/home') 
        else: # otherwise go to thanks note...
            return redirect('/thanks')
    return render(request,'contact.html')
    

# Creating object from our model class
class list(ListView):
    model = To_do_List_model
    context_object_name = 'tasks'


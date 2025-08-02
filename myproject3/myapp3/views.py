from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Mymodel, User


def contact(request):
    return render(request, 'myapp3/contact.html')

# Create your views here.

def insert_data(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')  
        description=request.POST.get('description')
    
        mymodel = Mymodel(name=name, email=email, description=description)
        mymodel.save()
        
    
        return redirect('show_page')
    
    
def show_page(request):
    all_data= Mymodel.objects.all()
    return render(request, 'myapp3/show.html', {'key1': all_data})


def edit_data(request,id):
    data= Mymodel.objects.get(id=id)
    return render(request, 'myapp3/edit.html', {'key2': data})

    
                                            
def update_data(request, id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        description = request.POST.get('description')
        
        mymodel = Mymodel.objects.get(id=id)
        mymodel.name = name
        mymodel.email = email
        mymodel.description = description
        mymodel.save()
        
        return redirect('show_page')
    
    return HttpResponse("Invalid request method.")

def delete_data(request, id):
    if request.method == 'POST':
        mymodel = Mymodel.objects.get(id=id)
        mymodel.delete()
        return redirect('show_page')
    return HttpResponse("Invalid request method.")


def register(request):
    return render(request, 'myapp3/register.html')


def register_user(request):
    if request.method=="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        description = request.POST.get('description')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        
        # so , geeting the data from the form and store on the database
    
        user=User.objects.filter(email=email)
        if user:
            return render(request, 'myapp3/register.html', {'error': 'Email already exists'})
        else:
            if password == cpassword:
                user = User(username=username, email=email, description=description, password=password)
                user.save()
                return render(request, 'myapp3/login.html')
            else:
                return HttpResponse("Passwords do not match")
            
            
    return render(request, 'myapp3/register.html', {'error': 'Invalid request method'})


def login(request):
    return render(request, 'myapp3/login.html')

def login_user(request):
    if request.method == "POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        
        user=User.objects.get(email=email)
        # checking if the user exists or not
        if user:
             if user.password==password:
                 request.session['username'] = user.username 
                 request.session['email'] = user.email
                 request.session['description'] = user.description
                 return render(request, 'myapp3/home.html')
             
             else:
                 return render(request, 'myapp3/login.html', {'error': 'Invalid password'})
             
        else:
            return render(request, 'myapp3/login.html', {'error': 'Email does not exist'})
        
        
        
        
def logout_user(request):
    if 'username' in request.session:
        del request.session['username']
    if 'email' in request.session:
        del request.session['email']
    if 'description' in request.session:
        del request.session['description']
    
    return redirect('login') 

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def register(request):

    if request.method == 'POST':

        #    Get Values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            #Check username
            if User.objects.filter(username=username).exists():
                messages.error(request,"This username is allrady taken")
                return redirect("register")

            # Check Email 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,"This email is allrady registerad")
                    return redirect("register")
                else:
                    #  Lets Go
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    user.save()
                    messages.success(request,"You are now Registered.you can login")
                    return redirect("login")
        else:
            messages.error(request,"Password do not match")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html') 


def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
       
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now Login")
            return redirect('dashboard')
        else:
            messages.error(request,'username of password is invalid')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method=="POST":
        auth.logout(request)
        messages.success(request,"You now Logout")
        return redirect('login')


def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact_date').filter(user_id = request.user.id)
    context = {
        'contacts':user_contacts
    }
    return render(request, 'accounts/dashboard.html',context)

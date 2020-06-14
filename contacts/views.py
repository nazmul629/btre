from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .models import Contact


def contact(request):
    if request.method == "POST":
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        # realtor_email = request.POST['realtor_email']

         
        if request.user.is_authenticated:

            user_id  = request.user.id

            has_connected = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)

            if has_connected:
                messages.error(request,"You are alrady mande  an inqueiry for this listing ")
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,phone=phone,message=message,user_id=user_id)
        contact.save()

        # SEND MAIL
        # send_mail(
        #     'Property Listinf Inquiry',
        #     "there hasbeen an inquiry for",listing,"Sign in the more informeation ",
        #     'nazmulhossain.qnh@gmail.com',
        #     ['programming9143@gmail.com','borohaldia.cig@gmail.com'],
        #     fail_silently=False
        # )


        messages.success(request,'Your request havebeen submeted')
        
        return redirect('/listings/'+listing_id)
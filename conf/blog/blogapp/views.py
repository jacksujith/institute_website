from django.shortcuts import render, redirect
from .models import ConsultationRequest
from django.contrib import messages

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        service = request.POST.get('service')
        message = request.POST.get('message')

        # Validate and save data
        if name and phone and email and service:
            ConsultationRequest.objects.create(
                name=name,
                phone=phone,
                email=email,
                service=service,
                message=message,
            )
            messages.success(request, 'Your request has been submitted successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Please fill in all required fields.')

    return render(request, 'contact.html')


def index(request):
          return render(request,'index.html')

def about(request):
          return render(request,'about.html')


# def contact(request):
#           return render(request,'contact.html')
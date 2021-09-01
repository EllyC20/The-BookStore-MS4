from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from . forms import SubscriberForm
from django.contrib import messages

# Create your views here.


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def returns(request):
    """ A view to return the returns page """
    return render(request, 'home/returns.html')


def faq(request):
    """ A view to return the FAQ page """
    return render(request, 'home/faq.html')


def contact(request):
    """ A view to return the contact page and form submission """
    form = SubscriberForm()
    if request.method == "POST":
        message_email = request.POST['message-email']
        message_name = request.POST['message-name']
        message = request.POST['message']

        # Send an email
        send_mail(
           'message from ' + message_name,  # subject line
           message,  # message
           message_email,  # from email
           ['ms4.thebookstore@gmail.com'],  # in real world app site owner email here
        )

        return render(request, 'home/contact.html', {'message_name': message_name, 'form': form})
    else:
        return render(request, 'home/contact.html', {'form': form})


def subscribe_form(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Subscribed.')
        return redirect(reverse("contact"))


def subscriber_email(request):
    """ A view to allow superusers to send an email to their subscriber list """
    context = {

    }
    return render(request, 'home/subscriber_email.html', context)
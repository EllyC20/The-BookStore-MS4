from django.shortcuts import render, redirect, reverse
from django.core.mail import send_mail
from . forms import SubscriberForm, EmailForm
from . models import Subscribers
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django_pandas.io import read_frame

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
           ['ms4.thebookstore@gmail.com'],
        )

        return render(request, 'home/contact.html',
                      {'message_name': message_name, 'form': form})
    else:
        return render(request, 'home/contact.html', {'form': form})


def subscribe_form(request):
    if request.method == "POST":
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Subscribed.')
        return redirect(reverse("contact"))


@login_required
def subscriber_email(request):
    """ A view to allow superusers to send an email to their subscriber list """
    emails = Subscribers.objects.all()
    dataframe = read_frame(emails, fieldnames=['email'])
    mail_list = dataframe['email'].values.tolist()
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid:
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            send_mail(
                title,
                message,
                '',
                mail_list,
                fail_silently=False,
            )
            messages.success(request,
                             'You Have Sent Your Newsletter \
                              To Your Subscribers.')
            return redirect(reverse("subscriber_email"))
    else:
        form = EmailForm()
    context = {
        'form': form,
    }
    return render(request, 'home/subscriber_email.html', context)

from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, SignUpForm


def home(request):
    title = 'User: %s' % request.user

    if request.method == 'POST':
        print request.POST

    form = SignUpForm(request.POST or None)
    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        # form.save()
        instance = form.save(commit=False)
        full_name = form.cleaned_data.get('full_name')

        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        instance.save()
        context = {
            'title': 'Thank you'
        }
    return render(request, "home.html", context)


def contact(request):
    title = "Contact Us"
    form = ContactForm(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        message = form.cleaned_data.get('message')
        full_name = form.cleaned_data.get('full_name')

        subject = 'Email from TryDjango18 Site'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email]
        contact_message = 'From: %s\n' \
                          'Email: %s\n\n' \
                          'Message: %s' %(full_name, email, message)
        send_mail(subject, contact_message, from_email, to_email, fail_silently=False)

    context = {
        'title': title,
        'form': form,
    }
    return  render(request, 'forms.html', context)
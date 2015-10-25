from django.shortcuts import render
from .forms import SignUpForm

# Create your views here.

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
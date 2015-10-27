__author__ = 'Dylan'

from django.shortcuts import render


def about(request):
    return render(request, "about.html", {})
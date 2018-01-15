"""Views for the Translations app
blah blah...
"""
from django.shortcuts import render
from translations.forms import TranslationForm

def home_page(request):
    return render(request, 'home.html', {'form': TranslationForm()})

def result(request, text):
    return render(request, 'result.html')

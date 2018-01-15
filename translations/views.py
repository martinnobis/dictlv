"""Views for the Translations app
blah blah...
"""
from django.urls import reverse
from django.shortcuts import render, redirect
from translations.forms import SearchForm

def home_page(request):
    return render(request, 'home.html', {'form': SearchForm()})

def result(request, text):
    """Displays the result
    """
    return render(request, 'result.html', {'text': text, 'form': SearchForm()})

def search(request):
    """Handles the form for searching the database.
    """
    if request.method == "POST":
        form = SearchForm(request.POST)
        text = form.data['text']
        return redirect(reverse('view_result', kwargs={'text': text.title()}))
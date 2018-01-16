"""Views for the Translations app
blah blah...
"""
from django.shortcuts import render, redirect
from translations.forms import SearchForm

def home_page(request):
    return render(request, 'home.html', {'form': SearchForm()})

def search(request):
    """Handles the form for searching the database.
    """
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            text = form.data['text']
            return render(request, 'result.html', {'text': text.title(), 'form': form})

from django.shortcuts import render, redirect
from translations.forms import SearchForm

def home_page(request):
    """Returns the homepage
    """
    return render(request, 'home.html', {'form': SearchForm()})

def search(request):
    """Handles the search form which attempts to retrieve translations from the
    database.
    """
    if request.method == "GET":
        form = SearchForm(request.GET)
        if form.is_valid():
            text = form.data['text']
            return render(request, 'result.html', {'text': text, 'form': form})

"""Views for the Translations app
blah blah...
"""
from django.shortcuts import render, redirect
from translations.forms import SearchForm

def home_page(request):
    return render(request, 'home.html', {'form': SearchForm()})

def result(request, text):
    """Displays the result
    """
    return render(request, 'result.html', {'text': text})

def search(request):
    """Handles the form for searching the database.
    """
    form = SearchForm(request.POST)
    text = form.data['text']
    print(text)
    if form.is_valid():
        print("is valid")
        return redirect('result.html', {'text': text})
    else:
        print("is not valid")
        return render(request, 'home.html', {'form': form})

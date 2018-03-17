"""Views for the translations app."""

from itertools import repeat
from django.shortcuts import render, redirect
from django.urls import reverse
from translations.forms import SearchForm
from translations.models import English, Latvian
from translations.utils import (get_translations, get_similar_latvian_words,
                                translation_exists)


def home_page(request):
    """Return the homepage."""
    return render(request, 'home.html', {'form': SearchForm()})


# TODO: This view has a lot of if statements
def search(request):
    """Handle requests from the search form."""
    # Try exact translation
    # If successful, return result.html
    form = SearchForm(data=request.GET)
    if form.is_valid():
        term = form.data['text']
        term = term.strip()
    else:
        # Handle invalid form 
        pass
        #return render(request, 'noresult.html', {'search_term': term, 'form': SearchForm()})

    lv_translations = get_translations(English, Latvian, term)
    en_translations = get_translations(Latvian, English, term)
    trans = lv_translations + en_translations
    if trans:
        return render(request, 'result.html', {
            'search_term': term,
            'translations': trans,
            'form': SearchForm()
        })

    # Try translation w/o special characters
    # If successful, return didyoumean.html
    candidates = get_similar_latvian_words(term)
    if candidates:
        if any(
                map(translation_exists, repeat(Latvian),
                    [candidate for candidate in candidates])):
            return render(request, 'didyoumean.html', {
                'search_term': term,
                'candidates': candidates,
                'form': SearchForm()
            })

    # Else, return noresult.html
    return render(request, 'noresult.html', {
        'search_term': term,
        'form': SearchForm()
    })


def show_translation(request, language, term):
    """Retrieve and show the exact translation."""
    pass


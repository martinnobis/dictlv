from django.shortcuts import render, redirect
from django.urls import reverse
from translations.forms import SearchForm
from translations.models import English, Latvian
from translations.utils import get_translations, special_chars, get_similar_latvian_words

def home_page(request):
    """Returns the homepage
    """
    return render(request, 'home.html', {'form': SearchForm()})

# TODO: This view has a lot of if statements
def show_translation(request, term):

    # Try exact translation
    # If successful, return result.html
    lv_translations = get_translations(English, Latvian, term)
    en_translations = get_translations(Latvian, English, term)
    trans = []
    if lv_translations:
        trans = trans + lv_translations
    if en_translations:
        trans = trans + en_translations
    if trans:
        return render(request, 'result.html',
            {'search_term': term, 'translations': trans, 'form': SearchForm()})

    # Try translation w/o special characters
    # If successful, return didyoumean.html
    candidates = get_similar_latvian_words(term)
    if candidates:
        return render(request, 'didyoumean.html',
            {'search_term': term, 'candidates': candidates, 'form': SearchForm()})

    # Else, return noresult.html
    else:
        return render(request, 'noresult.html', {'search_term': term, 'form': SearchForm()})

def search(request):
    """Handles the search form which attempts to retrieve translations from the
    database.
    """
    form = SearchForm(request.GET)
    if form.is_valid():
        # TODO: also trim trailing whitespace, punctuation etc.
        user_in = form.data['text'].lower()
        return redirect(reverse('show_translation', kwargs={'term': user_in}))

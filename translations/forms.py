"""Forms for the translation app."""

from django import forms


class SearchForm(forms.Form):
    """Main search form of the website."""

    text = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter a word to translate'}))

    #class Meta:
    #    fields = ('text',)

from django import forms


class SearchForm(forms.Form):

    text = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter a word to translate'}))

    class Meta:
        fields = ('text',)

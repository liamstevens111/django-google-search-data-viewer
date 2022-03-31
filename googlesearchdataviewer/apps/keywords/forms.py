from django import forms


class UploadCsvKeywordsForm(forms.Form):
    file = forms.FileField(allow_empty_file=False, widget=forms.FileInput(attrs={'accept':'text/csv'}))

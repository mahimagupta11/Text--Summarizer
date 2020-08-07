from django import forms
class TextForm(forms.Form):
    num_sentences = forms.IntegerField(label="Number of Output Sentences",
	widget=forms.NumberInput(attrs={'class': 'text-muted form-control bg-light', 'style': 'width: 18ch','placeholder': 0}))
    content = forms.CharField(label="Text to Summarize",
	widget=forms.Textarea(attrs={'class': 'text-muted form-control bg-light', 'placeholder':'Type text to summarize...'}))
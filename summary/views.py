from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TextForm
from .summary import Textsum

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            text = Textsum().summary(form.cleaned_data['content'], form.cleaned_data['num_sentences'])
            new_form = TextForm()
            return render(request, 'summary/index.html', dict(form=new_form, summary=text))

    return render(request, 'summary/index.html', dict(form=TextForm(), summary=""))




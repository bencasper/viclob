from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from formdemo.models import DemoForm


def demo(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = DemoForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/testform/thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = DemoForm()

    return render(request, 'formdemo/demo_form.html', {'form': form})


def thanks(request):
    return render(request, 'formdemo/thanks.html')

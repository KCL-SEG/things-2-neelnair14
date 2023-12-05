from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            # Process valid form data, for example, save to the database
            form.save()
    else:
        form = ThingForm()

    return render(request, 'home.html', {'form': form})

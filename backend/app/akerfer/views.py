from django.shortcuts import render, redirect
from .forms import SushiCardForm
from .models import SushiCard

def create_sushi_card(request):
    if request.method == 'POST':
        form = SushiCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('sushi_card_list')
    else:
        form = SushiCardForm()

    cards = SushiCard.objects.all()
    return render(request, 'sushi_card_list.html', {'form': form, 'cards': cards})

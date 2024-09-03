from django.shortcuts import render, redirect, get_object_or_404
from .models import SushiCard
from .forms import SushiCardForm

def create_sushi_card(request):
    if request.method == 'POST':
        form = SushiCardForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('create_sushi_card')
    else:
        form = SushiCardForm()

    cards = SushiCard.objects.all()
    return render(request, 'sushi_card_list.html', {'form': form, 'cards': cards})

def delete_sushi_card(request, card_id):
    card = get_object_or_404(SushiCard, id=card_id)
    if request.method == 'POST':
        card.delete()
        return redirect('create_sushi_card')
    return render(request, 'confirm_delete.html', {'card': card})

def update_sushi_card(request, card_id):
    sushi_card = get_object_or_404(SushiCard, id=card_id)
    
    if request.method == 'POST':
        form = SushiCardForm(request.POST, request.FILES, instance=sushi_card)
        if form.is_valid():
            form.save()
            return redirect('create_sushi_card')
    else:
        form = SushiCardForm(instance=sushi_card)
    
    return render(request, 'update_sushi_card.html', {'form': form, 'sushi_card': sushi_card})


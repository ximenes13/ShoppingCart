from django.shortcuts import render
from .scraper import get_price_continente
from .forms import ShoppingListForm



def home(request):
    if request.method == 'POST':
        form = ShoppingListForm(request.POST)
        if form.is_valid():
            raw_items = form.cleaned_data['items']
            items = [i.strip() for i in raw_items.split('\n') if i.strip()]
            resultados = [(item, get_price_continente(item)) for item in items]
            return render(request, 'shopping_app/result.html', {'resultados': resultados})
    else:
        form = ShoppingListForm()
    return render(request, 'shopping_app/home.html', {'form': form})

from django import forms

class ShoppingListForm(forms.Form):
    items = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 6, "placeholder": "Digite um item por linha"}),
        label="Sua lista de compras"
    )

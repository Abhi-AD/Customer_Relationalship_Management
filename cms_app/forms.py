from django import forms
from cms_app.models import Contact, CashTransaction, Inventory, InventoryBalance


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]


class CashTransactionForm(forms.ModelForm):
    class Meta:
        model = CashTransaction
        fields = ["user", "amount", "transaction_type", "date", "description"]


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ["name", "quantity", "unit_price","date"]


class InventoryBalanceForm(forms.ModelForm):
    class Meta:
        model = InventoryBalance
        fields = ["inventory", "balance_date", "quantity_on_hand"]

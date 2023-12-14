from django import forms
from cms_app.models import Contact, CashTransaction, Inventory, InventoryBalance,AddMember


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class CashTransactionForm(forms.ModelForm):
    class Meta:
        model = CashTransaction
        fields = "__all__"


class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = "__all__"


class InventoryBalanceForm(forms.ModelForm):
    class Meta:
        model = InventoryBalance
        fields = "__all__"


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = AddMember
        fields = "__all__"

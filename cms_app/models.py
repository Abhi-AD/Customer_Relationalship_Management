from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Plan_Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    images = models.ImageField(upload_to="Price_subscription/%Y/%m/%d", blank=False)

    def __str__(self):
        return self.name


class Service_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sub_Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AddMember(models.Model):
    STATUS_CHOICES = [
        ("basic", "Basic"),
        ("gold", "Gold"),
    ]
    STATUS_PAYMENT = [
        ("online", "Online"),
        ("case", "Case"),
    ]
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255, blank=True, null=True)
    street_address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state_province = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    email = models.EmailField()
    membership_types = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="basic"
    )
    billing_address = models.CharField(max_length=20, choices=STATUS_PAYMENT)
    date_of_signature = models.DateTimeField(default=timezone.now)
    emergency_contact = models.CharField(max_length=10)
    service_category = models.ManyToManyField(Service_Category)
    sub_category = models.ManyToManyField(Sub_Category)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DisplayProfile(models.Model):
    profile = models.OneToOneField(AddMember, on_delete=models.CASCADE)

    def __str__(self):
        return f"DisplayProfile for {self.profile}"


class User_Subscription(models.Model):
    name = models.OneToOneField(DisplayProfile, on_delete=models.CASCADE)
    plan = models.OneToOneField(Plan_Subscription, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Attendance(models.Model):
    user = models.ForeignKey(DisplayProfile, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.date}"


class CashTransaction(models.Model):
    transaction_type_choices = [
        ("CASH_IN", "Cash In"),
        ("CASH_OUT", "Cash Out"),
    ]
    user = models.ForeignKey(DisplayProfile, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=8, choices=transaction_type_choices)
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"


class Inventory(models.Model):
    name = models.ForeignKey(DisplayProfile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} - {self.quantity} units"


class InventoryBalance(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    balance_date = models.DateField(default=timezone.now)
    quantity_on_hand = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.inventory} - {self.balance_date} - {self.quantity_on_hand} units"

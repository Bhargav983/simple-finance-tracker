from django.db import models

class Expenditure(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Utilities', 'Utilities'),
        ('Housing', 'Housing'),
        ('Subscriptions', 'Subscriptions'),
        ('Health care', 'Health care'),
        ('Donations', 'Donations'),
        ('Entertainment', 'Entertainment'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Food')
    type = models.CharField(max_length=100, help_text="Enter the type of expenditure (e.g., grocery, taxi, etc.)")
    date = models.DateField(help_text="Enter the date of the expenditure")
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Enter the amount of expenditure")

    def __str__(self):
        return f"{self.category} - {self.type} - {self.amount}"


class User(models.Model):
    ROLE_CHOICES = [
        ('Admin', 'Admin'),
        ('Viewer', 'Viewer')
    ]
    
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    password = models.CharField(max_length=128)  # To store hashed passwords
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.email} - {self.role}"

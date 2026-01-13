from django.db import models

class Debt(models.Model):
    """
    OOP: Debt entity encapsulating financial data.
    DBMS: Structured for relational integrity.
    """
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2) # APR
    min_payment = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - ${self.balance}"
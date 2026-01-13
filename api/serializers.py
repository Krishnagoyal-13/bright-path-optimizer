from rest_framework import serializers

class DebtSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    balance = serializers.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = serializers.DecimalField(max_digits=5, decimal_places=2)
    min_payment = serializers.DecimalField(max_digits=10, decimal_places=2)

class CalculateRequestSerializer(serializers.Serializer):
    debts = DebtSerializer(many=True)
    extra_monthly_budget = serializers.DecimalField(max_digits=10, decimal_places=2)
    strategy = serializers.ChoiceField(choices=['avalanche', 'snowball'])
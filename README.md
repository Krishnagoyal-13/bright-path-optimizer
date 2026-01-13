# Bright-Path: Debt Repayment Optimizer

### 🧠 Project Vision
A specialized engine designed to simulate debt paydown strategies (Avalanche vs. Snowball). Built for the SDE Intern role at Bright Money to demonstrate:
1. **First Principles:** Custom interest compounding logic.
2. **LLD:** Use of the Strategy Pattern for algorithm selection.
3. **Fintech Focus:** Using `Decimal` for currency precision.

### 🏗 High-Level Design
- **API Layer:** Django Rest Framework for handling JSON requests.
- **Service Layer:** `RepaymentOptimizer` class encapsulates the business logic.
- **Data Layer:** Designed for PostgreSQL (ACID compliant).

### 🚀 How to use
POST to `/api/optimize/` with:
```json
{
  "debts": [{"name": "Card A", "balance": 5000, "interest_rate": 18, "min_payment": 150}],
  "extra_monthly_budget": 500,
  "strategy": "avalanche"
}
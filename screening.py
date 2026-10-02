# KYC Screening Simulator
# Educational project using fictional client data.

clients = [
    {"name": "Ana Silva", "country": "Portugal", "transaction_amount": 5000, "account_age_days": 400, "salary": 2500},
    {"name": "John Doe", "country": "Panama", "transaction_amount": 15000, "account_age_days": 10, "salary": 4000},
    {"name": "Maria Costa", "country": "Brazil", "transaction_amount": 8000, "account_age_days": 200, "salary": 3000},
    {"name": "Igor Petrov", "country": "Russia", "transaction_amount": 20000, "account_age_days": 5, "salary": 6000},
    {"name": "Li Wei", "country": "China", "transaction_amount": 3000, "account_age_days": 100, "salary": 2500},
    {"name": "Ali Reza", "country": "Iran", "transaction_amount": 12000, "account_age_days": 15, "salary": 5000},
    {"name": "Sofia Martins","country": "Portugal", "transaction_amount": 900, "account_age_days": 60, "salary": 2500,},
    {"name": "Carlos Mendes", "country": "Spain", "transaction_amount": 7500, "account_age_days": 20, "salary": 5000, },
    {"name": "Leila Hassan", "country": "Iran", "transaction_amount": 1200, "account_age_days": 120, "salary": 1800, },
]

high_risk_countries = ["Panama", "Russia", "North Korea", "Iran"]
transaction_limit = 10000
minimum_account_age = 30

def screen_client(client):
    flags = []

        # Rule 1: Transaction amount exceeds limit
    if client["transaction_amount"] > transaction_limit:
        flags.append("Transaction above limit")

        # Rule 2: High-risk country
    if client["country"] in high_risk_countries:
        flags.append("High-risk country")

        # Rule 3: Account too recent
    if client["account_age_days"] < minimum_account_age:
        flags.append("Account too recent")

        # Rule 4: Transaction exceeds 3x monthly salary
    if "salary" in client and client["transaction_amount"] > client["salary"] * 3:
        flags.append("Transaction above 3x monthly salary")

    return flags

for client in clients:
    flags = screen_client(client)
    if flags:
        print(f"⚠️ {client['name']} - ATTENTION:")
        for flag in flags:
            print(f"   - {flag}")
    else:
        print(f"✅ {client['name']} - No flags")
    print()
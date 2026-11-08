from decimal import Decimal
from collections import defaultdict

invoices = [
    {"no": "INV-001", "vendor": "Acme", "amount": Decimal("1000.00"), "status": "paid"},
    {"no": "INV-002", "vendor": "Globex", "amount": Decimal("250.50"), "status": "pending"},
    {"no": "INV-003", "vendor": "Acme", "amount": Decimal("730.25"), "status": "pending"},
    {"no": "INV-004", "vendor": "Initech", "amount": Decimal("99.99"), "status": "rejected"},
    {"no": "INV-005", "vendor": "Globex", "amount": Decimal("1200.00"), "status": "pending"},
]

pending_nos = [inv["no"] for inv in invoices if inv["status"] == 'pending']
print(pending_nos)

dict_comp = {inv["no"] : inv["amount"] for inv in invoices if inv["amount"] > 500}
print(dict_comp)

vendor_set = {inv["vendor"] for inv in invoices}
print(len(vendor_set))

sum_amount = sum((inv["amount"] for inv in invoices if inv["status"] == 'pending'), start=Decimal("0"))
print(sum_amount)

dict_vendor = defaultdict(Decimal)
for inv in invoices:
    dict_vendor[inv["vendor"]] += inv["amount"]

print(dict(dict_vendor))
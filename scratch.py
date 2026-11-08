from pathlib import Path
from invoice_processor.load import load_invoices
import json

data = load_invoices(Path("data/invoices.json"))
assert isinstance(data, list)
assert len(data) == 22

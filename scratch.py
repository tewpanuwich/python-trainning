from pathlib import Path
from invoice_processor.io import load_invoices
import json

data = load_invoices(Path("data/invoices.json"))
assert isinstance(data, list)
assert len(data) == 22

try:
    data = load_invoices(Path("data/str.json"))
except ValueError as e:
    assert "Cannot parse" in str(e)


try:
    data = load_invoices(Path("data/notfound.json"))
except OSError as e:
    assert "Not found" in str(e)


try:
    data = load_invoices(Path("data/invalidjson.json"))
except OSError as e:
    assert "Cannot load" in str(e)


try:
    data = load_invoices(Path("data/empty.json"))
except OSError as e:
    assert "Cannot load" in str(e)
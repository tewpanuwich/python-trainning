from pathlib import Path
from invoice_processor.load import load_invoices
import json

def test1():
    try:
        data = load_invoices(Path("data/str.json"))
    except ValueError as e:
        assert "Cannot parse" in str(e)
    else:
        raise AssertionError("expected ValueError was not raised")


def test2():
    try:
        data = load_invoices(Path("data/notfound.json"))
    except OSError as e:
        assert "Not found" in str(e)
    else:
        raise AssertionError("expected OSError was not raised")


def test3():
    try:
        data = load_invoices(Path("data/invalidjson.json"))
    except ValueError as e:
        assert "Cannot load" in str(e)
    else:
        raise AssertionError("expected ValueError was not raised")


def test4():
    try:
        data = load_invoices(Path("data/empty.json"))
    except ValueError as e:
        assert "Cannot load" in str(e)
    else:
        raise AssertionError("expected ValueError was not raised")

def test5():
    try:
        data = load_invoices(Path("data/thai.json"))
    except ValueError as e:
        assert "Cannot load" in str(e)
    else:
        raise AssertionError("expected ValueError was not raised")
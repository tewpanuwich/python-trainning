from pathlib import Path
import json

def load_invoices(path: Path) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as e:
        raise OSError(f"Not found '{path}': {e}")
    except json.JSONDecodeError as e:
        raise ValueError(f"Cannot load '{path}': {e}")
    except ValueError as e:
        raise ValueError(f"Cannot load '{path}': {e}")
    
    if not isinstance(data, list): 
        raise ValueError(f"Cannot parse '{type(data)}' to JSON.")
    return data
    




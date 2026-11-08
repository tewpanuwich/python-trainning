from pathlib import Path
import json

def load_invoices(path: Path) -> list[dict]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as e:
        raise OSError(f"Not found '{path}': {e}") from e
    except json.JSONDecodeError as e:
        raise OSError(f"Cannot load '{path}': {e}") from e
    
    if not isinstance(data, list): 
        raise ValueError(f"Cannot parse '{type(data)}' to JSON.")
    return data
    




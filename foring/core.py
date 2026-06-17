import csv
import json
import pickle
import plistlib
import xml.etree.ElementTree as ET
from pathlib import Path

# --- HANDLERS ---
def _read_csv(filepath):
    with open(filepath, 'r', encoding='utf-8', newline='') as f:
        dialect = csv.Sniffer().sniff(f.read(1024) or ',')
        f.seek(0)
        return list(csv.reader(f, dialect))

def _write_csv(data, filepath):
    with open(filepath, 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        if data and isinstance(data, list) and isinstance(data[0], list):
            writer.writerows(data)
        else:
            writer.writerow(data)

def _read_ini(filepath):
    import configparser
    config = configparser.ConfigParser()
    config.read(filepath, encoding='utf-8')
    return {section: dict(config[section]) for section in config.sections()}

def _write_ini(data, filepath):
    import configparser
    config = configparser.ConfigParser()
    for section, keys in data.items():
        config[section] = keys
    with open(filepath, 'w', encoding='utf-8') as f:
        config.write(f)

def _read_yaml(filepath):
    import yaml
    with open(filepath, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def _write_yaml(data, filepath):
    import yaml
    with open(filepath, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f, default_flow_style=False)

def _read_xml(filepath):
    tree = ET.parse(filepath)
    return tree.getroot()

def _write_xml(data, filepath):
    if isinstance(data, ET.Element):
        tree = ET.ElementTree(data)
        tree.write(filepath, encoding='utf-8', xml_declaration=True)
    else:
        Path(filepath).write_text(str(data), encoding='utf-8')



HANDLERS = {
    '.json': (lambda p: json.loads(Path(p).read_text(encoding='utf-8')), 
              lambda d, p: Path(p).write_text(json.dumps(d, indent=4), encoding='utf-8')),
    
    '.pkl': (lambda p: pickle.loads(Path(p).read_bytes()), 
             lambda d, p: Path(p).write_bytes(pickle.dumps(d))),
    '.pickle': (lambda p: pickle.loads(Path(p).read_bytes()), 
                lambda d, p: Path(p).write_bytes(pickle.dumps(d))),
    
    '.csv': (_read_csv, _write_csv),
    
    '.ini': (_read_ini, _write_ini),
    '.plist': (lambda p: plistlib.loads(Path(p).read_bytes()), 
               lambda d, p: Path(p).write_bytes(plistlib.dumps(d))),
    '.yml': (_read_yaml, _write_yaml),
    '.yaml': (_read_yaml, _write_yaml),
    
    '.html': (lambda p: Path(p).read_text(encoding='utf-8'), 
              lambda d, p: Path(p).write_text(str(d), encoding='utf-8')),
    '.xml': (_read_xml, _write_xml),
    
    '.txt': (lambda p: Path(p).read_text(encoding='utf-8'), 
             lambda d, p: Path(p).write_text(str(d), encoding='utf-8')),
    '.md': (lambda p: Path(p).read_text(encoding='utf-8'), 
            lambda d, p: Path(p).write_text(str(d), encoding='utf-8')),
    '.log': (lambda p: Path(p).read_text(encoding='utf-8'), 
             lambda d, p: Path(p).write_text(str(d), encoding='utf-8')),
}


# --- MAIN API TO HANDLE READ AND WRITE ACTIVITIES ---

def read(filepath: str):
    ext = Path(filepath).suffix.lower()
    if ext in HANDLERS:
        return HANDLERS[ext][0](filepath)
    try:
        return Path(filepath).read_text(encoding='utf-8')
    except UnicodeDecodeError:
        return Path(filepath).read_bytes()


def write(data, filepath: str):
    ext = Path(filepath).suffix.lower()
    if ext in HANDLERS:
        HANDLERS[ext][1](data, filepath)
        return
        
    if isinstance(data, bytes):
        Path(filepath).write_bytes(data)
    elif isinstance(data, str):
        Path(filepath).write_text(data, encoding='utf-8')
    else:
        Path(filepath).write_text(str(data), encoding='utf-8')
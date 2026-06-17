![foring_logo](https://raw.githubusercontent.com/shayansaha85/foring/refs/heads/master/logo.png)
<p>
<img src = 'https://img.shields.io/badge/python-3.14.5-blue'>
<img src = 'https://img.shields.io/badge/foring-0.1.0-green'>
<img src = 'https://img.shields.io/badge/license-MIT-red'>


</p>

---
<br>
`foring` is a lightweight, intuitive Python utility designed to take the friction out of file I/O operations. Inspired by the simplicity of `pandas` data loading routines, `foring` lets you read and write virtually any file format using just two clean, highly smart top-level functions: `read()` and `write()`. 

No more managing context managers (`with open...`), manually choosing between text or binary modes (`'r'`, `'wb'`), parsing formats, or handling complex serialization formats like `pickle` or `plist` manually. `foring` auto-detects the extension and takes care of the heavy lifting.



## 🚀 Installation

You can install `foring` directly from PyPI using `pip`:

```bash
pip install foring
```

## Dependencies

foring relies entirely on Python's built-in standard library, with the single exception of PyYAML (which is automatically fetched and configured during the pip install process to parse YAML profiles cleanly).

## 🛠️ Quick Start & Core Usage

The entire power of the library resides in a highly focused import structure:

```python
import foring.core as fc
```
---
### 1. JSON Files

JSON is perfect for structured, human-readable data serialization.

**Writing JSON:**
```python
import foring.core as fc

user_data = {"name": "Shayan Saha", "role": "Developer", "verified": True}
fc.write(user_data, "profile.json")
```

**File content (`profile.json`):**
```json
{
    "name": "Shayan Saha",
    "role": "Developer",
    "verified": true
}
```

**Reading JSON:**
```python
import foring.core as fc

data = fc.read("profile.json")
print(data["name"])  # Output: Shayan Saha
```
---
### 2. CSV Files

CSV files are ideal for tabular data and spreadsheets. Automatically detects delimiters.

**Writing CSV:**
```python
import foring.core as fc

matrix = [["ID", "Item"], ["101", "Laptop"], ["102", "Monitor"]]
fc.write(matrix, "inventory.csv")
```

**File content (`inventory.csv`):**
```csv
ID,Item
101,Laptop
102,Monitor
```

**Reading CSV:**
```python
import foring.core as fc

rows = fc.read("inventory.csv")
print(rows[1])  # Output: ['101', 'Laptop']
```
---
### 3. YAML Files

YAML is perfect for configuration files and human-readable hierarchical data. Supports both `.yaml` and `.yml` extensions.

**Writing YAML:**
```python
import foring.core as fc

yaml_config = {
    "server": {
        "host": "localhost",
        "ports": [8000, 8080]
    },
    "database": {
        "enabled": True
    }
}
fc.write(yaml_config, "config.yaml")
```

**File content (`config.yaml`):**
```yaml
database:
  enabled: true
server:
  host: localhost
  ports:
  - 8000
  - 8080
```

**Reading YAML:**
```python
import foring.core as fc

config = fc.read("config.yaml")
print(config["server"]["ports"])  # Output: [8000, 8080]
```
---
### 4. INI Files

INI files are commonly used for configuration with sections and key-value pairs.

**Writing INI:**
```python
import foring.core as fc

ini_data = {
    "DATABASE": {"Host": "localhost", "User": "root", "Password": "secret"},
    "LOGGING": {"Level": "DEBUG", "File": "app.log"}
}
fc.write(ini_data, "settings.ini")
```

**File content (`settings.ini`):**
```ini
[DATABASE]
host = localhost
user = root
password = secret

[LOGGING]
level = DEBUG
file = app.log
```

**Reading INI:**
```python
import foring.core as fc

settings = fc.read("settings.ini")
print(settings["DATABASE"]["User"])  # Output: root
```
---
### 5. XML Files

XML is ideal for hierarchical, structured data with attributes and nested elements.

**Writing XML:**
```python
import xml.etree.ElementTree as ET
import foring.core as fc

# Build standard XML tree structural elements
root = ET.Element("project")
child = ET.SubElement(root, "name")
child.text = "foring"
child.set("version", "1.0")

# Writes as an XML element hierarchy tree
fc.write(root, "meta.xml")
```

**File content (`meta.xml`):**
```xml
<?xml version='1.0' encoding='utf-8'?>
<project><name version="1.0">foring</name></project>
```

**Reading XML:**
```python
import foring.core as fc

parsed_root = fc.read("meta.xml")
print(parsed_root.find("name").text)  # Output: foring
print(parsed_root.find("name").get("version"))  # Output: 1.0
```
---
### 6. Text Files (TXT)

Plain text files for logs, notes, and unformatted content.

**Writing Text:**
```python
import foring.core as fc

content = "This is a plain text file.\nLine 2 of content."
fc.write(content, "notes.txt")
```

**File content (`notes.txt`):**
```text
This is a plain text file.
Line 2 of content.
```

**Reading Text:**
```python
import foring.core as fc

text = fc.read("notes.txt")
print(text)  # Output: This is a plain text file. Line 2 of content.
```
---
### 7. Markdown Files (MD)

Markdown files for documentation and formatted text content.

**Writing Markdown:**
```python
import foring.core as fc

markdown_content = """# My Project

This is a **bold** statement.

- Item 1
- Item 2
"""
fc.write(markdown_content, "README.md")
```

**File content (`README.md`):**
```markdown
# My Project

This is a **bold** statement.

- Item 1
- Item 2
```

**Reading Markdown:**
```python
import foring.core as fc

content = fc.read("README.md")
print(content)
```
---
### 8. Log Files (LOG)

Log files for application events and diagnostics.

**Writing Logs:**
```python
import foring.core as fc

log_message = "2026-06-17 10:45:32: Operation completed successfully.\n2026-06-17 10:46:00: Process finished."
fc.write(log_message, "app.log")
```

**File content (`app.log`):**
```log
2026-06-17 10:45:32: Operation completed successfully.
2026-06-17 10:46:00: Process finished.
```

**Reading Logs:**
```python
import foring.core as fc

logs = fc.read("app.log")
print(logs)
```
---
### 9. Pickle Files (PKL & PICKLE)

Python pickle format for serializing complex Python objects, including tuples, lists, and custom objects.

**Writing Pickle:**
```python
import foring.core as fc

# Store a tuple with mixed data types
state_packet = (1, "active", [10, 20, 30], {"key": "value"})
fc.write(state_packet, "state.pkl")
```

**File content (`state.pkl`):**
```
(Binary pickled Python object - not human-readable)
Size: ~50 bytes (varies by content)
```

**Reading Pickle:**
```python
import foring.core as fc

loaded_packet = fc.read("state.pkl")
print(loaded_packet[1])  # Output: active
print(loaded_packet[2])  # Output: [10, 20, 30]
```
---
### 10. PList Files (PLIST)

Property list files commonly used on macOS for storing structured data.

**Writing PList:**
```python
import foring.core as fc

plist_data = {
    "Name": "MyApp",
    "Version": "1.0",
    "Enabled": True,
    "Settings": {"Theme": "dark", "AutoSave": True}
}
fc.write(plist_data, "app.plist")
```

**File content (`app.plist`):**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Name</key>
    <string>MyApp</string>
    <key>Version</key>
    <string>1.0</string>
    <key>Enabled</key>
    <true/>
    <key>Settings</key>
    <dict>
        <key>Theme</key>
        <string>dark</string>
        <key>AutoSave</key>
        <true/>
    </dict>
</dict>
</plist>
```

**Reading PList:**
```python
import foring.core as fc

plist_content = fc.read("app.plist")
print(plist_content["Settings"]["Theme"])  # Output: dark
```
---
### 11. HTML Files (HTML)

HTML markup for web content and structured markup.

**Writing HTML:**
```python
import foring.core as fc

html_content = """<html>
    <body>
        <h1>Welcome to foring</h1>
        <p>A lightweight file I/O utility.</p>
    </body>
</html>"""
fc.write(html_content, "index.html")
```

**File content (`index.html`):**
```html
<html>
    <body>
        <h1>Welcome to foring</h1>
        <p>A lightweight file I/O utility.</p>
    </body>
</html>
```

**Reading HTML:**
```python
import foring.core as fc

html = fc.read("index.html")
print(html)
```
---
### 12. Binary & Media Files (PNG, PDF, ZIP, etc.)

For unsupported extensions, foring automatically handles binary files. It tries text decoding first, then falls back to raw bytes for binary formats.

**Writing Binary:**
```python
import foring.core as fc

# Read binary image
raw_image = open("original.png", "rb").read()

# Write as backup
fc.write(raw_image, "backup.png")
```

**Reading Binary:**
```python
import foring.core as fc

# Read any binary file
raw_data = fc.read("image.png")
print(f"File size: {len(raw_data)} bytes")

# Works seamlessly with images, PDFs, ZIP archives, etc.
```


## 📄 License
This project is open-source software licensed under the terms of the MIT License. Feel free to use, modify, and distribute it as needed!

## Attributions
Logo : <a href="https://www.flaticon.com/free-icons/dragonfly" title="dragonfly icons">Dragonfly icons created by Khadija Arif - Flaticon</a>
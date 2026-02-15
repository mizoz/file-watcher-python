# File Watcher Python

[![PyPI Version](https://img.shields.io/pypi/v/file-watcher-python?style=flat-square)](https://pypi.org/project/file-watcher-python/)
[![PyPI Downloads](https://img.shields.io/pypi/dm/file-watcher-python?style=flat-square)](https://pypi.org/project/file-watcher-python/)
[![License](https://img.shields.io/pypi/l/file-watcher-python?style=flat-square)](LICENSE)
[![Python Version](https://img.shields.io/pypi/pyversions/file-watcher-python?style=flat-square)](https://pypi.org/project/file-watcher-python/)
[![GitHub Stars](https://img.shields.io/github/stars/mizoz/file-watcher-python?style=flat-square)](https://github.com/mizoz/file-watcher-python)

> A Python CLI tool for watching file system changes in real-time.

## Features

- Watch files for changes
- Watch directories for modifications
- Detect file creation, modification, deletion
- Run commands on file changes
- Recursive directory watching
- Python API for integration

## Installation

### From PyPI

```bash
pip install file-watcher-python
```

### From Source

```bash
git clone https://github.com/mizoz/file-watcher-python.git
cd file-watcher-python
pip install -e .
```

## Usage

### Command Line

```bash
# Watch a file
file-watcher myfile.txt

# Watch a directory
file-watcher myfolder/

# Run command on change
file-watcher myfolder/ --command "npm run build"
```

### Python API

```python
from file_watcher import FileWatcher

def on_change(path):
    print(f"File changed: {path}")

watcher = FileWatcher("myfolder/", callback=on_change)
watcher.start()
```

## CLI Options

| Option | Description |
|--------|-------------|
| `-c, --command` | Run command on file change |
| `-r, --recursive` | Watch directories recursively |

## Requirements

- Python 3.7+

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**mizoz**
- GitHub: [@mizoz](https://github.com/mizoz)

---

⭐ If you find this project useful, please consider giving it a star on GitHub!

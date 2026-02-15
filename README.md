# File Watcher Python

A Python library for watching file system changes in real-time.

## Features

- Watch single files for changes
- Watch directories for file modifications
- Detect file creation, modification, and deletion
- Debouncing to prevent duplicate events
- Recursive directory watching
- File pattern filtering

## Installation

```bash
pip install file-watcher-python
```

Or clone and install:

```bash
git clone https://github.com/mizoz/file-watcher-python.git
cd file-watcher-python
pip install -e .
```

## Usage

### Command Line

```bash
# Watch a file
file-watcher watch myfile.txt

# Watch a directory
file-watcher watch ./src

# Watch with recursive option
file-watcher watch --recursive ./src

# Watch specific file types
file-watcher watch --pattern "*.py" ./src
```

### Python API

```python
from file_watcher import FileWatcher

def on_change(event):
    print(f"File changed: {event.path}")
    print(f"Event type: {event.type}")

watcher = FileWatcher('./src')
watcher.watch(on_change)
```

## Event Types

- `created` - A new file was created
- `modified` - A file was modified
- `deleted` - A file was deleted
- `moved` - A file was moved/renamed

## License

MIT License

## Author

mizoz

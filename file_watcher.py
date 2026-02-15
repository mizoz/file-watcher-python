#!/usr/bin/env python3
"""Watch files for changes and run commands."""
import sys, time, subprocess, os
from pathlib import Path

if __name__ == "__main__":
    if len(sys.argv) < 3: print("Usage: file_watcher.py <path> <command>"); sys.exit(1)
    path, cmd = sys.argv[1], ' '.join(sys.argv[2:])
    if not os.path.exists(path): print(f"Error: {path} not found"); sys.exit(1)
    print(f"Watching {path}... Press Ctrl+C")
    mtime = {f: os.path.getmtime(f) for f in Path(path).rglob('*') if f.is_file()}
    while True:
        time.sleep(1)
        for f in Path(path).rglob('*'):
            if f.is_file():
                mt = os.path.getmtime(f)
                if f not in mtime or mt > mtime[f]:
                    mtime[f] = mt
                    print(f"Changed: {f}")
                    subprocess.run(cmd, shell=True)

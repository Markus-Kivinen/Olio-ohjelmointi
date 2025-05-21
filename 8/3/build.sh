#!/bin/bash

# python3 -m venv .venv

# Check if .venv has Scripts or bin directory
if [ -d ".venv/Scripts" ]; then
    # Windows
    source .venv/Scripts/activate
elif [ -d ".venv/bin" ]; then
    # Linux or MacOS
    source .venv/bin/activate
fi

# pip install pyinstaller==6.6.0
pyinstaller --noconfirm --onefile copy.py
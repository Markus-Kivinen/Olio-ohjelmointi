#/bin/bash
python -m venv .venv
if [ -d ".venv/Scripts" ]; then
    source .venv/Scripts/activate
elif [ -d ".venv/bin" ]; then
    source .venv/bin/activate
fi
python --version
which python
pip install kirje
pip freeze > requirements.txt

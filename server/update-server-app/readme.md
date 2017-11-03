# Python APK Update Server
## Dev Environment

virtualenv --no-site-packages -p `which python` .venv
source .venv/bin/activate
pip install -r requirements.txt

## Testing
Run service: python update-server.py

sh ./test.sh

import os

DATA_DIR = os.getenv("DATA_DIR") or os.path.abspath(os.path.join(os.path.dirname(__file__), 'data'))
print(DATA_DIR)
# config.py
import os

# Get the absolute path of the project root directory
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# Define paths relative to the root directory
DATA_DIR = os.path.join(ROOT_DIR, 'data', 'raw')
SDR_DATABASE_PATH = os.path.join(DATA_DIR, 'SDR-2022-database.xlsx')
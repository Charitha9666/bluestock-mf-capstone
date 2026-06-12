"""
Master Pipeline Script

Runs all project modules
in sequence.
"""

import os

os.system("python scripts/data_ingestion.py")
os.system("python scripts/data_cleaning.py")
os.system("python scripts/load_to_sqlite.py")
os.system("python scripts/live_nav_fetch.py")
os.system("python scripts/recommender.py")
# logger_config.py

import logging
import os


# -----------------------------
# Create reports folder if missing
# -----------------------------
REPORTS_FOLDER = "reports"

if not os.path.exists(REPORTS_FOLDER):
    os.makedirs(REPORTS_FOLDER)


# -----------------------------
# Create Logger
# -----------------------------
logger = logging.getLogger("BankLogger")

logger.setLevel(logging.DEBUG)


# Prevent duplicate logs
logger.propagate = False


# -----------------------------
# Formatter
# -----------------------------
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%d-%m-%Y %H:%M:%S"
)


# -----------------------------
# Bank Log Handler
# -----------------------------
bank_handler = logging.FileHandler(
    os.path.join(REPORTS_FOLDER, "bank.log")
)

bank_handler.setLevel(logging.INFO)

bank_handler.setFormatter(formatter)


# -----------------------------
# Error Log Handler
# -----------------------------
error_handler = logging.FileHandler(
    os.path.join(REPORTS_FOLDER, "error.log")
)

error_handler.setLevel(logging.ERROR)

error_handler.setFormatter(formatter)


# -----------------------------
# Console Handler
# -----------------------------
console_handler = logging.StreamHandler()

console_handler.setLevel(logging.INFO)

console_handler.setFormatter(formatter)


# -----------------------------
# Avoid Duplicate Handlers
# -----------------------------
if not logger.handlers:
    logger.addHandler(bank_handler)
    logger.addHandler(error_handler)
    logger.addHandler(console_handler)
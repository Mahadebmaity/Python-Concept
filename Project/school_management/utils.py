"""
Utility helpers: reg generation, backup trigger, validation
"""
import random, string, shutil, os, datetime

DB_FILE = "school.db"
BACKUP_DIR = "backups"

def generate_reg_no_safe(name: str) -> str:
    # first two letters of name (alpha)
    letters = ''.join([c for c in name if c.isalpha()])[:2].upper()
    if len(letters) < 2:
        letters = (letters + "XX")[:2]
    digits = ''.join(random.choices(string.digits, k=5))
    return letters + digits

def ensure_backup():
    # called before major mutations
    if not os.path.exists(BACKUP_DIR):
        os.makedirs(BACKUP_DIR)
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst = os.path.join(BACKUP_DIR, f"school_{ts}.db")
    try:
        shutil.copy2(DB_FILE, dst)
    except Exception:
        pass  # non-fatal

def create_db_backup():
    # used by database module after writes
    ensure_backup()

# simple wrapper for backups (used by database)
from utils import ensure_backup
def create_db_backup():
    ensure_backup()

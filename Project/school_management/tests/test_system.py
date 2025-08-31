import os
import tempfile
import pytest
from database import init_db, set_subjects, add_student, get_student_by_reg, delete_student

def test_add_and_delete_student():
    # Create temp file for test DB
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        db_path = tmp.name

    try:
        # initialize DB for testing
        init_db(db_path)
        set_subjects(['Math', 'English'], db_path)
        
        reg = add_student("8th", "Test Student", "01", db_path=db_path)
        assert reg is not None and len(reg) == 7

        s = get_student_by_reg(reg, db_path=db_path)
        assert s is not None
        assert s['name'] == "Test Student"

        ok = delete_student(reg, db_path=db_path)
        assert ok is True

        s2 = get_student_by_reg(reg, db_path=db_path)
        assert s2 is None
    finally:
        os.remove(db_path)

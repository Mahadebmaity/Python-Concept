"""
All DB operations using sqlite3
"""
import sqlite3
import os
import json
from utils import generate_reg_no_safe
from typing import List, Dict, Optional
from backup import create_db_backup

DB_FILE = "school.db"

def get_conn():
    return sqlite3.connect(DB_FILE)

def init_db():
    first_time = not os.path.exists(DB_FILE)
    conn = get_conn()
    cur = conn.cursor()
    # admin table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS admin (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )""")
    # subjects table
    cur.execute("CREATE TABLE IF NOT EXISTS subjects (id INTEGER PRIMARY KEY, name TEXT UNIQUE)")
    # students table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        class TEXT,
        name TEXT,
        roll TEXT,
        reg_no TEXT UNIQUE
    )""")
    # marks table
    cur.execute("""
    CREATE TABLE IF NOT EXISTS marks (
        id INTEGER PRIMARY KEY,
        student_id INTEGER,
        subject_id INTEGER,
        marks INTEGER,
        FOREIGN KEY(student_id) REFERENCES students(id),
        FOREIGN KEY(subject_id) REFERENCES subjects(id)
    )""")
    conn.commit()
    # default admin
    cur.execute("SELECT COUNT(*) FROM admin")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO admin (username, password) VALUES (?,?)", ("admin","admin123"))
    conn.commit()
    conn.close()

def authenticate_admin(username: str, password: str) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT password FROM admin WHERE username=?", (username,))
    row = cur.fetchone()
    conn.close()
    return bool(row and row[0] == password)

def change_admin_password(username: str, old: str, new: str):
    if not authenticate_admin(username, old):
        raise Exception("Invalid current credentials")
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("UPDATE admin SET password=? WHERE username=?", (new, username))
    conn.commit()
    conn.close()

# SUBJECTS
def set_subjects(subjects: List[str]):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM subjects")
    for s in subjects:
        cur.execute("INSERT INTO subjects (name) VALUES (?)", (s,))
    conn.commit()
    conn.close()

def get_subjects() -> List[str]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT name FROM subjects ORDER BY id")
    rows = [r[0] for r in cur.fetchall()]
    conn.close()
    return rows

# STUDENT CRUD
def add_student(cls: str, name: str, roll: str) -> str:
    if not get_subjects():
        raise Exception("Subjects not set. Please set subjects before adding students.")
    # validate duplicates
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM students WHERE class=? AND roll=?", (cls, roll))
    if cur.fetchone():
        conn.close()
        raise Exception("Duplicate roll in class.")
    reg_no = generate_reg_no_safe(name)
    # ensure unique reg_no
    cur.execute("SELECT 1 FROM students WHERE reg_no=?", (reg_no,))
    while cur.fetchone():
        reg_no = generate_reg_no_safe(name)
        cur.execute("SELECT 1 FROM students WHERE reg_no=?", (reg_no,))
    cur.execute("INSERT INTO students (class, name, roll, reg_no) VALUES (?,?,?,?)", (cls, name, roll, reg_no))
    student_id = cur.lastrowid
    # initialize marks to 0
    cur.execute("SELECT id FROM subjects")
    subjects = cur.fetchall()
    for sid, in subjects:
        cur.execute("INSERT INTO marks (student_id, subject_id, marks) VALUES (?,?,?)", (student_id, sid, 0))
    conn.commit()
    conn.close()
    create_db_backup()
    return reg_no

def update_student(reg_no: str) -> bool:
    # interactive update handled in main; here we fetch and update minimal
    # But for simplicity we'll do interactive updates here (pull current data, ask)
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, class, name, roll FROM students WHERE reg_no=?", (reg_no,))
    row = cur.fetchone()
    if not row:
        conn.close()
        return False
    sid, cls, name, roll = row
    # We'll collect updates from user via input in main.update_student_interactive => call helpers instead
    # For compatibility, we'll return current data so main can use actual update helpers.
    conn.close()
    return True

def delete_student(reg_no: str) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM students WHERE reg_no=?", (reg_no,))
    r = cur.fetchone()
    if not r:
        conn.close()
        return False
    sid = r[0]
    cur.execute("DELETE FROM marks WHERE student_id=?", (sid,))
    cur.execute("DELETE FROM students WHERE id=?", (sid,))
    conn.commit()
    conn.close()
    create_db_backup()
    return True

def list_class_students(cls: str) -> List[Dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, roll, reg_no FROM students WHERE class=? ORDER BY name", (cls,))
    rows = cur.fetchall()
    subjects = get_subjects()
    result = []
    for sid, name, roll, reg in rows:
        cur.execute("SELECT subjects.name, marks.marks FROM marks JOIN subjects ON marks.subject_id=subjects.id WHERE marks.student_id=?", (sid,))
        mrows = cur.fetchall()
        marks = {m[0]: m[1] for m in mrows}
        total = sum(marks.values())
        max_marks = len(subjects) * 100
        percentage = (total / max_marks * 100) if max_marks else 0.0
        grade = _grade_for_pct(percentage)
        status = _status_for_pct(percentage)
        result.append({'id': sid, 'name': name, 'roll': roll, 'reg_no': reg, 'marks': marks, 'total': total, 'percentage': percentage, 'grade': grade, 'status': status})
    # assign ranks
    result.sort(key=lambda x: x['total'], reverse=True)
    for i, s in enumerate(result, start=1):
        s['rank'] = i
    conn.close()
    return result

def list_all_students() -> List[Dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, class, name, roll, reg_no FROM students ORDER BY class,name")
    rows = cur.fetchall()
    out = []
    for sid, cls, name, roll, reg in rows:
        cur.execute("SELECT subjects.name, marks.marks FROM marks JOIN subjects ON marks.subject_id=subjects.id WHERE marks.student_id=?", (sid,))
        mrows = cur.fetchall()
        marks = {m[0]: m[1] for m in mrows}
        total = sum(marks.values())
        max_marks = len(marks)*100
        percentage = (total / max_marks * 100) if max_marks else 0.0
        out.append({'class': cls, 'name': name, 'roll': roll, 'reg_no': reg, 'marks': marks, 'total': total, 'percentage': percentage})
    conn.close()
    return out

def get_student_by_reg(reg_no: str) -> Optional[Dict]:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, class, name, roll FROM students WHERE reg_no=?", (reg_no,))
    r = cur.fetchone()
    if not r:
        conn.close()
        return None
    sid, cls, name, roll = r
    cur.execute("SELECT subjects.name, marks.marks FROM marks JOIN subjects ON marks.subject_id=subjects.id WHERE marks.student_id=?", (sid,))
    mrows = cur.fetchall()
    marks = {m[0]: m[1] for m in mrows}
    total = sum(marks.values())
    max_marks = len(marks)*100
    percentage = (total / max_marks * 100) if max_marks else 0.0
    grade = _grade_for_pct(percentage)
    status = _status_for_pct(percentage)
    conn.close()
    return {'id': sid, 'class': cls, 'name': name, 'roll': roll, 'reg_no': reg_no, 'marks': marks, 'total': total, 'percentage': percentage, 'grade': grade, 'status': status}

def update_student_marks_and_info(reg_no: str, new_name=None, new_roll=None, new_marks: Dict[str,int]=None) -> bool:
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM students WHERE reg_no=?", (reg_no,))
    r = cur.fetchone()
    if not r:
        conn.close()
        return False
    sid = r[0]
    if new_name:
        cur.execute("UPDATE students SET name=? WHERE id=?", (new_name, sid))
    if new_roll:
        # check duplicate roll
        cur.execute("SELECT id FROM students WHERE class=(SELECT class FROM students WHERE id=?) AND roll=? AND id<>?", (sid, new_roll, sid))
        if cur.fetchone():
            conn.close()
            raise Exception("Duplicate roll in same class.")
        cur.execute("UPDATE students SET roll=? WHERE id=?", (new_roll, sid))
    if new_marks:
        # map subject names to ids
        cur.execute("SELECT id, name FROM subjects")
        map_sub = {r[1]: r[0] for r in cur.fetchall()}
        for sub, m in new_marks.items():
            if sub not in map_sub:
                continue
            cur.execute("UPDATE marks SET marks=? WHERE student_id=? AND subject_id=?", (m, sid, map_sub[sub]))
    conn.commit()
    conn.close()
    create_db_backup()
    return True

def import_students_from_csv(path: str) -> int:
    import csv
    if not os.path.exists(path):
        raise Exception("File not found")
    subjects = get_subjects()
    count = 0
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            cls = row.get('class') or row.get('class_name') or row.get('className')
            name = row.get('name')
            roll = row.get('roll')
            if not (cls and name and roll):
                continue
            try:
                reg = add_student(cls, name, roll)
            except Exception:
                continue
            # fill marks if columns match subject names
            conn = get_conn()
            cur = conn.cursor()
            cur.execute("SELECT id FROM students WHERE reg_no=?", (reg,))
            sid = cur.fetchone()[0]
            cur.execute("SELECT id, name FROM subjects")
            subs = cur.fetchall()
            for sid_s, sname in subs:
                try:
                    m = int(row.get(sname, 0))
                except:
                    m = 0
                cur.execute("UPDATE marks SET marks=? WHERE student_id=? AND subject_id=?", (m, sid, sid_s))
            conn.commit()
            conn.close()
            count += 1
    return count

# SEARCH & STATS
def search_students(q: str):
    q_like = f"%{q}%"
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT class, name, roll, reg_no, id FROM students WHERE name LIKE ? OR roll LIKE ? OR reg_no LIKE ?", (q_like, q_like, q_like))
    rows = cur.fetchall()
    out = []
    for cls, name, roll, reg, sid in rows:
        cur.execute("SELECT subjects.name, marks.marks FROM marks JOIN subjects ON marks.subject_id=subjects.id WHERE marks.student_id=?", (sid,))
        mrows = cur.fetchall()
        marks = {m[0]: m[1] for m in mrows}
        total = sum(marks.values())
        max_marks = len(marks)*100
        percentage = (total / max_marks * 100) if max_marks else 0.0
        out.append({'class': cls, 'name': name, 'roll': roll, 'reg_no': reg, 'percentage': percentage})
    conn.close()
    return out

def subject_statistics(cls: str):
    students = list_class_students(cls)
    if not students:
        return {}
    subjects = get_subjects()
    stats = {}
    for sub in subjects:
        vals = [s['marks'].get(sub,0) for s in students]
        if not vals:
            continue
        mx = max(vals)
        mn = min(vals)
        avg = sum(vals)/len(vals)
        topper = None
        for s in students:
            if s['marks'].get(sub,0) == mx:
                topper = s['name']
                break
        stats[sub] = {'max': mx, 'min': mn, 'avg': round(avg,2), 'topper_name': topper}
    return stats

def top_n_toppers(cls: str, n:int=3):
    students = list_class_students(cls)
    students.sort(key=lambda x: x['total'], reverse=True)
    return students[:n]

# helpers
def _grade_for_pct(p):
    if p >= 90: return "A+"
    if p >= 80: return "A"
    if p >= 70: return "B"
    if p >= 60: return "C"
    if p >= 50: return "D"
    return "F"

def _status_for_pct(p):
    return "Pass" if p >= 33 else "Fail"

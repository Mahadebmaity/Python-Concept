"""
Exports class reports to CSV, Excel and PDF
"""
import sqlite3, os
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors

DB_FILE = "school.db"

def _class_df(cls: str):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, name, roll, reg_no FROM students WHERE class=?", (cls,))
    rows = cur.fetchall()
    if not rows:
        conn.close()
        return None
    cur.execute("SELECT name FROM subjects ORDER BY id")
    subs = [r[0] for r in cur.fetchall()]
    data = []
    for sid, name, roll, reg in rows:
        cur.execute("SELECT subjects.name, marks.marks FROM marks JOIN subjects ON marks.subject_id=subjects.id WHERE marks.student_id=?", (sid,))
        mrows = cur.fetchall()
        marks = {m[0]: m[1] for m in mrows}
        total = sum(marks.values())
        perc = (total / (len(subs)*100) * 100) if subs else 0.0
        row = {"Reg No": reg, "Name": name, "Roll": roll}
        row.update(marks)
        row["Total"] = total
        row["Percentage"] = round(perc,2)
        data.append(row)
    conn.close()
    df = pd.DataFrame(data)
    return df

def export_class_csv(cls: str, out_dir="reports"):
    df = _class_df(cls)
    if df is None:
        raise Exception("No data")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{cls}_report.csv")
    df.to_csv(path, index=False)
    return path

def export_class_excel(cls: str, out_dir="reports"):
    df = _class_df(cls)
    if df is None:
        raise Exception("No data")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{cls}_report.xlsx")
    df.to_excel(path, index=False)
    return path

def export_class_pdf(cls: str, out_dir="reports"):
    df = _class_df(cls)
    if df is None:
        raise Exception("No data")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, f"{cls}_report.pdf")
    doc = SimpleDocTemplate(path)
    data = [list(df.columns)] + df.values.tolist()
    table = Table(data)
    style = TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.grey),
        ('GRID', (0,0), (-1,-1), 0.5, colors.black),
    ])
    table.setStyle(style)
    doc.build([table])
    return path

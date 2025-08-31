# import glob

# # Get all .txt files in current folder
# txt_files = glob.glob("*.py")
# py_files = glob.glob("*.txt")
# print(f"{txt_files}\n {py_files}")

# import glob

# # Find all .py files in 'scripts/' folder
# py_files = glob.glob("scripts/*.py")
# print(py_files)


import tempfile

# Create a temporary file
with tempfile.TemporaryFile(mode='w+t') as temp:
    temp.write("Hello Temporary File!")
    temp.seek(0)
    print(temp.read())


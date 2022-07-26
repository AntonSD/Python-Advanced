from io import open
file_path = './file_reader.py'

try:
    open(file_path, 'r')
    print("File found")

except FileNotFoundError:
    print("File not found")

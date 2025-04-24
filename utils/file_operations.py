# filepath: object-detection-project/src/utils/file_operations.py
import os

def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return ""

def write_file(file_path, data):
    with open(file_path, 'a') as file:
        file.write(data)

def clear_file(file_path):
    with open(file_path, 'w') as file:
        file.write("")
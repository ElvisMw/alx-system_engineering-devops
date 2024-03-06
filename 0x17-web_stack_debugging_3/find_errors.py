# Python script to search for errors in strace_output.txt

file_path = "strace_output.txt"

try:
    with open(file_path, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            if 'error' in line.lower():
                print(f"Line {line_number}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: File {file_path} not found.")
except Exception as e:
    print(f"An error occurred: {e}")

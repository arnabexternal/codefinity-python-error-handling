def read_file_contents(filename):
    # Your code here
    file = None
    contents = None
    try:
        file = open(filename, 'r')
        contents = file.read()
    except Exception:
        print("An error occurred while reading the file.")
        contents = None
    finally:
        if file is not None:
            file.close()
        print("File has been closed.")

    return contents

# Example usage for testing:
with open('example.txt', 'w') as f:
    f.write('Hello, world!')
# Example usage for your testing:
print(read_file_contents('example.txt'))     # Should print "Hello, world!"
print(read_file_contents('nonexistent.txt')) # Should print the error message and return None

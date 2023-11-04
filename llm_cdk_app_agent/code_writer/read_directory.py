import os

def read_file_or_directory_contents(path: str):
    try:
        if os.path.isfile(path):
            # If the path is a file, read and return its content
            with open(path, 'r') as file:
                content = file.read()
            return content
        elif os.path.isdir(path):
            # If the path is a directory, list and return its contents
            files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
            files = (" ").join(files)
            return files
        else:
            return f"Path '{path}' is neither a file nor a directory."
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
# if __name__ == "__main__":
#     file_or_dir_path = "temp_code_dest/fml/kys/blah.py"  # Replace with the actual path
#     result = read_file_or_directory_contents(file_or_dir_path)
#     print(result)

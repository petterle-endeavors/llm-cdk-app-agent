import subprocess
import os


class FileRunner:
    def run_file(self, filepath):
        if os.path.isfile(filepath):
            try:
                # Run the specified file using the default associated program
                subprocess.run(["python", filepath])
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            raise ValueError("Not a valid file to run")


# Example usage:
if __name__ == "__main__":
    runner = FileRunner()
    file_to_run = "temp_code_dest/fml/kys/blah.py"  # Replace with the actual file path
    runner.run_file(file_to_run)

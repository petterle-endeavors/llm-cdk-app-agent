import re
import os


class CodeWriter:
    BASE_PATH = "temp_code_dest/"

    def create(self, content: str, filepath: str) -> None:
        """
        This is the create method that will write passed code to a new file and write the the file to the provided path relative the BASE_PATH

        parameters
        - content: code string to be written to a file
        - filepath: relative pathstring to place specify a location for code to be written

        Returns:
            void
        """
        # content will likely be markdown formatted, need to remove any extra characters that might pollute our python file
        content = self.remove_markdown(content)

        # file path should start with / - trim whitespace and append backslash if it doesn't exist
        if filepath.strip()[0] == "/":
            filepath = filepath[1::]

        filepath = os.path.join(self.BASE_PATH, filepath)
        if self.is_valid_linux_filepath(filepath):
            self.create_file(filepath, content)
        else:
            raise ValueError("file path is not valid please enter a valid linux filepath")

        # raise ValueError('This is not a valid linux filepath: reference this example to "/home/user/documents/example.py"')

    def delete_file(self, filepath: str, startLine: int, endLine: int, deleteAll) -> None:
        fullPath = self.BASE_PATH + filepath
        print(fullPath)

        if deleteAll:
            os.remove(fullPath)
        else:
            with open(fullPath, "r") as fMatt:
                lines = fMatt.readlines()
            with open(fullPath, "w") as fMattAgain:
                for number, line in enumerate(lines):
                    if number not in range(startLine, endLine + 1):
                        print(line)
                        fMattAgain.write(line)

    def remove_markdown(self, text):
        """
        Remove Markdown syntax from the input text.

        This function removes common Markdown elements such as headers, bold and italic text, code blocks, inline code,
        and lists from the provided text.

        Parameters:
        - text (str): The input text containing Markdown syntax.

        Returns:
            str: The cleaned text with Markdown syntax removed.
        """
        # Remove headers (## Header)
        text = re.sub(r"^\s*#.*$", "", text, flags=re.MULTILINE)

        # Remove bold and italic (**bold** or *italic*)
        text = re.sub(r"(\*\*|__)(.*?)\1", r"\2", text)
        text = re.sub(r"(\*|_)(.*?)\1", r"\2", text)

        # Remove code blocks (```python ... ```)
        text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

        # Remove inline code (`code`)
        text = re.sub(r"`([^`]+)`", "", text)

        # Remove lists
        text = re.sub(r"^\s*[-*+]\s+.*$", "", text, flags=re.MULTILINE)

        return text

    def is_valid_linux_filepath(self, filepath):
        """
        Validate a Linux file path.

        This function checks if the given filepath adheres to the rules of a Linux file path.

        Parameters:
        - filepath (str): The file path to be validated.

        Returns:
        bool: True if the filepath is valid, False otherwise.
        """
        # Regular expression for a valid Linux file path
        # Assumes basic Linux path structure and does not cover all edge cases
        linux_filepath_pattern = r"^[a-zA-Z0-9_\-./]+\.py$"

        # Check if the filepath matches the pattern
        if re.match(linux_filepath_pattern, filepath):
            return True
        else:
            return False

    def create_file(self, filepath, content=""):
        """
        Create a file at the specified filepath, including directories if necessary.

        Parameters:
        - filepath (str): The filepath for the new file.
        - content (str): Optional content to write to the file.

        Returns:
        None
        """
        # Ensure the directory structure exists
        directory = os.path.dirname(filepath)
        print(directory)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Create the file and write content if provided
        with open(filepath, "w") as file:
            if content:
                file.write(content)

    def update(self, file_path: str, line_number: int, text_to_insert: str) -> None:
        """
        Insert text at a specific line in a file.

        Parameters:
        - file_path (str): The path to the file.
        - line_number (int): The line number at which to insert the text.
        - text_to_insert (str): The text to insert into the file.

        Returns:
        None
        """
        print(135, file_path)
        full_path = self.BASE_PATH + file_path
        print(137, full_path)
        if self.is_valid_linux_filepath(full_path):
            # Read the existing content
            with open(full_path, "r") as file:
                lines = file.readlines()

            # Insert the new text at the specified line
            lines.insert(line_number - 1, text_to_insert)

            # Write the modified content back to the file
            with open(full_path, "w") as file:
                file.writelines("\n".join(lines))
        else:
            raise ValueError("filepath not valid please enter a valid linux filepath")


# obj = CodeWriter()

# obj.create(content="print('hello, world!')", filepath="/fml/kys/blah.py")
# obj.delete_file("fmatt.txt", 2, 4, True)
# obj.update("/fml/kys/blah.py", 1, 'print("solo sux")')


# todo
# validation
# wraping new code around old code?
# checking file paths
# ensuring files paths are .py?

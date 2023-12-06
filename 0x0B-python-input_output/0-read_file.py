#!/usr/bin/python3
def read_file(filename=""):
    """
    Reads and prints the content of a file line by line.

    Args:
        filename (str): The name of the file to be read. Defaults to an empty string.
        
    Returns:
        None

    Raises:
        FileNotFoundError: If the specified file is not found.
        IOError: If an error occurs while reading the file.

    Example:
        >>> read_file("example.txt")
        This is line 1
        This is line 2
        This is line 3
    """
    try:
        with open(filename, mode="r", encoding="utf-8") as myFile:
            for line in myFile:
                print(line, end="")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file '{filename}' was not found.")
    except IOError as e:
        raise IOError(f"Error reading the file '{filename}': {str(e)}")

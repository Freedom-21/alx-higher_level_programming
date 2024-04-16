#!/usr/bin/python3
"""A function that reads a text file"""

def read_file(filename=""):
    """ 
    Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, "r", encoding="utf=8") as f:
        print(f.read(), end="")

if __name__ == "__main__":
	read_file("my_file_0.txt")

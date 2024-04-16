#!/usr/bin/python3
"""
A Module that wirtes into a file
"""
def write_file(filename="", text=""):
    """
     Writes a text into a file

     Args:
         filename (str): The name of the file 
         text (str): a text to be written to the filename
   
    """
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)

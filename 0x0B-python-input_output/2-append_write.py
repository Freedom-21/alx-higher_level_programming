#!/usr/bin/python3
"""
A Module that wirtes into a file
"""
def append_write(filename="", text=""):
    """
     Writes a text into a file or append if exist

     Args:
         filename (str): The name of the file 
         text (str): a text to be written to the filename
   
    """
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)

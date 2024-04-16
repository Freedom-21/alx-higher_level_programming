#!/usr/bin/python3

def write_file(filename="", text=""):
    """
     Writes a text into a file

     Args:
         filename (str): The name of the file 
         text (str): a text to be written to the filename
   
    """
    with open(filename, "w", encoding="UTF8") as f:
        print(f.write(text))

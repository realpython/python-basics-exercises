# 12.5 - Reading and Writing Files
# Solutions to Exercises


# Exercise 1
from pathlib import Path

starships = ["Discovery\n", "Enterprise\n", "Defiant\n", "Voyager"]

file_path = Path.home() / "starships.txt"
with file_path.open(mode="w", encoding="utf-8") as file:
    file.writelines(starships)


# Exercise 2
with file_path.open(mode="r", encoding="utf-8") as file:
    for starship in file.readlines():
        print(starship, end="")


# Exercise 3
with file_path.open(mode="r", encoding="utf-8") as file:
    for starship in file.readlines():
        if starship.startswith("D"):
            print(starship, end="")
            
            

# Using os module
import os 
try: 
    # If the file does not exist, then it would throw an IOError 
    filename = 'my_file.txt'
    f = open(filename, 'rU') 
    text = f.read() 
    f.close() 
  
# Control jumps directly to here if any of the above lines throws IOError.     
except IOError: 
  
    # print(os.error) will <class 'OSError'> 
    print('Problem reading: ' + filename) 
      
# In any case, the code then continues with the line after the try/except 

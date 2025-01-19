import math
from datetime import datetime
import os

number=49
print(math.sqrt(number))

print(datetime.now())

files_and_dirs = os.listdir()
files = [f for f in files_and_dirs if os.path.isfile(f)]
print("Files in the current directory:")
for file in files:
    print(file)
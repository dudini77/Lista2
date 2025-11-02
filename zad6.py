import os

def find(path, filename):
  
    result = []
    
    for dirpath, dirnames, filenames in os.walk(path):
        if filename in filenames:
            result.append(os.path.join(dirpath, filename))
    
    return result
files = find("test_folder", "test.txt")
for f in files:
    print(f)
    #O(n)
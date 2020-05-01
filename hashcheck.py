"""
hashcheck.py

Generates and verifies MD5 hashes for files in the directory the script is placed in.

Keegan Crankshaw
April 2020
"""
import hashlib
import os

# Place your "expected" list here
# The method "get_checksums" will produce this list for all files in the current directory
expected = [
["example.exe", "<example.exe md5"],
["file2.rar", "<file2.rar md5>"],
]

def md5(fname):
    """
    Get the MD5 hashes for a file. If the file is large, process accordingly
    Taken from https://stackoverflow.com/a/3431838
    """
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
    
def get_checksums():
    """
    Get the checksum for all files in the current directory
    """
    print ("Expected = [")
    with os.scandir(".") as it:
        for entry in it:
            if entry.is_file():
                print("[\"{}\", \"{}\"],".format(entry.name, md5(entry.name)))
    print("]")
                
def verify_checksums():
    """
    Scan the current directory for files in the "expected" list and see if the hashes match
    """
    for f in expected: 
        if os.path.exists(f[0]):
            print("{} - Correct hash".format(f[0])) if md5(f[0]) == f[1] else print("{} Badly downloaded".format(f[0]))
        else:
            print("{} - File does not exist.".format(f[0]))

if __name__ == "__main__":
    # Adjust the line below to call the method you need
    get_checksums()
    
            

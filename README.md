# MD5-Checker
A script to generate and validate MD5 hashes for files

## Overview
MD5 checksums can be provided to ensure large files are downloaded correctly.   
The method `get_checksums` will print out a list in the expected format that the script requires.   
The method `verify_checksums` will iterate over the "expected" list, look for those files, and verify the checksum.

## Usage
1. To get the checksums of files, place this script in the root directory, and change the line under `if __name__ == "__main__":` to call `get_checksums()`
2. Copy the output of the script in as the `expected` list
3. change the line under `if __name__ == "__main__":` to call `verify_checksums()`
4. Run the script to ensure output is correct.
5. Done!

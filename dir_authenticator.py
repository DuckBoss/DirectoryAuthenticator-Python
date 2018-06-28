import hashlib
import sys
import os

if len(sys.argv) != 3:
    print("ERROR: This script requires 3 total system arguments.")
    print("FORMAT: python <this_script.py> <src_dir> <dst_dir>")
    sys.exit(1)

src_dir = sys.argv[1]
dst_dir = sys.argv[2]

if not os.path.isdir(src_dir):
    print("ERROR: src_dir missing!")
    print("Please make sure both directories exist!")
    sys.exit(1)
if not os.path.isdir(dst_dir):
    print("ERROR: dst_dir missing!")
    print("Please make sure both directories exist!")
    sys.exit(1)

src_dir_hash_list = []
dst_dir_hash_list = []

BUFFER_SIZE = 65536  # 64kb chunks

for root, dirs, files in os.walk(src_dir, topdown=True):
    for name in files:
        fileName = os.path.join(root, name)
        md5 = hashlib.md5()

        with open(str(fileName), 'rb') as f:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            md5.update(data)
        src_dir_hash_list.append(md5.hexdigest())

for root, dirs, files in os.walk(dst_dir, topdown=True):
    for name in files:
        fileName = os.path.join(root, name)
        md5 = hashlib.md5()

        with open(str(fileName), 'rb') as f:
            data = f.read(BUFFER_SIZE)
            if not data:
                break
            md5.update(data)
        dst_dir_hash_list.append(md5.hexdigest())

if src_dir_hash_list == dst_dir_hash_list:
    print("The provided directories are IDENTICAL")
else:
    print("The provided directories are DIFFERENT")

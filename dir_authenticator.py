import hashlib
import sys
import os

BUFFER_SIZE = 65536  # 64kb chunks

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


def file_auth(file_name):
    md5 = hashlib.md5()
    with open(file_name, 'rb') as src:
        while True:
            data_src = src.read(BUFFER_SIZE)
            if not data_src:
                break
            md5.update(data_src)
    return md5.hexdigest()


def dir_auth(dir_name):
    hash_list = []
    for root, dirs, files in os.walk(dir_name, topdown=True):
        for name in files:
            file_name = os.path.join(root, name)
            hash_list.append(file_auth(file_name))
    return hash_list


src_dir_hash_list = dir_auth(src_dir)
dst_dir_hash_list = dir_auth(dst_dir)


if src_dir_hash_list == dst_dir_hash_list:
    print("The Src Directory and Dst Directory is IDENTICAL.")
else:
    print("The Src Directory and Dst Directory is DIFFERENT.")

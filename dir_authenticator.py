import sys
import os
import auth_api

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


src_dir_hash_list = auth_api.dir_auth(src_dir, BUFFER_SIZE)
dst_dir_hash_list = auth_api.dir_auth(dst_dir, BUFFER_SIZE)


if src_dir_hash_list == dst_dir_hash_list:
    print("The Src Directory and Dst Directory is IDENTICAL.")
else:
    print("The Src Directory and Dst Directory is DIFFERENT.")

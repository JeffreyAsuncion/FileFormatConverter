import os
import shutil

print("Cleaning up Target Folder : /data/retail_db_json/")
shutil.rmtree('/home/jepoy/Documents/Projects/github/FileFormatConverter/data/retail_db_json/')
print("Target Folder - cleared...")
os.makedirs('/home/jepoy/Documents/Projects/github/FileFormatConverter/data/retail_db_json/')
print("Target Folder Ready.")
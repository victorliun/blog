#!/usr/bin/python

import os
import datetime
import sys
import stat
import shutil

output_d = ""
input_d = ""

def mv_files(dir):
    """ list all files in this dir, go to every subfolders, and move the 
    file to related new folder which according to the created timee."""
    print "mv_files"
    counter = 0
    print dir
    for (path, folders, files) in os.walk(dir):
        print path, folders, files
        if  not len(files):
            print "no file folder: %s" %path
            continue
        
        print files, "before"
        files = [file for file in files if not file.startswith(".") ]
        print files, "after trim"
        for file in files:
            f_path = os.path.join(path, file)
            fs = os.stat(f_path)
            c_time = datetime.datetime.fromtimestamp(fs[stat.ST_CTIME])
            year = str(c_time.year)
            month = c_time.month
            if month < 10:
                month = "0" + str(month)
            else:
                month = str(month)
            day = c_time.day
            if day < 10:
                day = "0" + str(day)
            else:
                day = str(day)
            output_dir = '%s%s/%s/%s' %(output_d, year, month, day)
            if not os.path.exists(output_dir):
                print "%s does not exist" %output_dir
                os.makedirs(output_dir)
            if os.path.exists(output_dir+'/'+file):
                file = file.split(".")[0]+"_d"+file.split(".")[1]
                print file
                shutil.move(f_path,output_dir+"/"+file)
            else:
                print "copy file from %s to %s, date:%s" %(f_path, output_dir, c_time)
                shutil.move(f_path,output_dir)
            counter = counter + 1

    print "%s files copied" % counter

if __name__ == "__main__":
    args = str(sys.argv)
    
    print args
    output_d = sys.argv[2]
    input_d = sys.argv[1]
    print sys.argv
    mv_files(input_d)

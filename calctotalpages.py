import sys
import os

folder = "C:\\Users\\poa\\Documents\\InsectaMundi"

file_list = os.listdir(folder)

out_filename = "C:\\Users\\poa\\Documents\\InsectaMundi\\IM_Pages_2009-2020.txt"

countTotalPages = 0

for f in file_list:

    countPages = 0

    if "InsectaMundi" in f:
        with open((folder + "\\" + f), encoding='utf-8') as in_file, open(out_filename, 'a') as out_file:
            #print(f)
            """
            print(f.find("."))
            print(f.find("_"))
            print(f[(f.find("_") + 1):f.find(".")])
            """
            for line in in_file:
                if "(1-" in line:
                    substring = line[line.find(")") + 1:]
                    countPages += int(substring[substring.find("-") + 1:][:-2])

            out_file.write(f[(f.find("_") + 1):f.find(".")] + ": " + str(countPages) + "\n")
            countTotalPages += countPages

with open(out_filename, 'a') as out_file:
    out_file.write("Total pages: " + str(countTotalPages))
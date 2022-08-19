"""
Use in Google Collab
"""
import re
all =open("all.txt","w")
! du -h /content/drive/My\ Drive/Twice\ Data/* >all.txt
all.close()
GB = open("GB.txt", "w")
for line in open("all.txt", "r"):
    if re.search("G\t", line):
        GB.write(line)
        print(line)
GB.close()

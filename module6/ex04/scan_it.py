import sys
import re


if len(sys.argv) != 3:
    exit("none")

matches = re.findall(sys.argv[1], sys.argv[2])
print(len(matches))
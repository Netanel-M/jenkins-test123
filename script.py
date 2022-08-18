#!/usr/bin/python3

import sys
argument = sys.argv[1]
with open("artifact.txt", "w") as file_handler:
  for i in range(int(argument)):
    file_handler.writelines([str(i)])

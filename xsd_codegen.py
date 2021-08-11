# -*- coding: utf-8 -*-
import os
import re
import sys

def get_schemas(path_value):   
    file = open(path_value)
    txt = file.read();
    matches = re.findall('schemaLocation="(?P<schemaLocation>(\w|[\.\/]?)+)"', txt)
    path_value_head, _ = os.path.split(path_value)
    for match in matches:
        schemaLocation = match[0]
        schemaLocation_head, _ = os.path.split(schemaLocation)
        if schemaLocation_head == '':
            schemaLocation = os.path.join(path_value_head,schemaLocation)
        schemaLocation_path= os.path.realpath(schemaLocation)
        print(schemaLocation_path)
        get_schemas(schemaLocation_path)
        codeparams.append(os.path.relpath(schemaLocation_path))
        

run_dir, run_file = os.path.split(sys.argv[1])

        
os.chdir(run_dir)

codeparams = [run_file]

get_schemas(os.path.realpath(run_file))

for v in sys.argv[2:]:
    codeparams.append(v)

codeparams.reverse()

codeline = 'xsd /c '
codeparams2 = []
for str in codeparams:
    if str not in codeparams2:
        codeparams2.append(str)
        codeline += str
        codeline += ' '

print ("Running: " + codeline)

stream = os.popen(codeline)
output = stream.read()


print (output)

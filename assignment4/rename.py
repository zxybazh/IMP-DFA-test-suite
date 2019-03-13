import os
import subprocess

rootdir = "."

def run_ourcode(imppath, oursolpath):
	subprocess.call(["scala imp-dfa.jar {} --flow_sensitive > {}".format(imppath, oursolpath)], shell=True)
	assert os.path.exists(oursolpath)
	with open(oursolpath, 'r') as f:
		return f.read()


for rootdir, _, files in os.walk(rootdir):
	for file in files:
		if file.endswith('.solution') and "-notfs." in file:
                    name = file
                    mode = name.split('-')[3].split(".")[0]
                    new_name = name.split("-")[0] + "-" + name.split("-")[1] + "-" + mode + "-"+  name.split("-")[2] + "." + "solution"
                    os.rename(file,new_name)
                    print new_name

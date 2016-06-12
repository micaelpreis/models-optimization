# coverage.py

# Micael Reis  		2010143871 
# Samuel Nunes  	2011158011
# Joao Cerveira  	2010130654 

import subprocess
import sys
import os

def reset():
	f = open("outputs/coverage/coverage_" + sys.argv[1] + ".txt", "w")
	f.close()

def save():
	f = open("output.dat", "r")
	path = f.readlines()
	f.close()

	f = open("outputs/coverage/coverage_" + sys.argv[1] + ".txt", "a")
	path = "".join(path)
	f.write(path)
	f.close()

def insert_percentage(percentage):
	f = open("coverage.mod", "r")
	paths = f.readlines()
	f.close()

	index = paths.index("# Percentage\n")
	percentage = "param p := " + str(percentage) + ";\n"	
	paths.insert(index+n, percentage)

	f = open("coverage.mod", "w")
	paths = "".join(paths)
	f.write(paths)
	f.close()

def restore(backup):
	f = open("coverage.mod", "w")
	backup = "".join(backup)
	f.write(backup)
	f.close()

# ---------------------------------------------------------------------------------------------------
n = 1

# Checks arguments
if(len(sys.argv)!=3):
    print "One argument is required, see report on how to use the scripts"
    exit(0)

# Backups coverage.mod
f = open("coverage.mod", "r")
backup = f.readlines()
f.close()

# Erase output
reset()

# Insert percentage in coverage.mod
percentage = float(sys.argv[2])/100
print percentage
insert_percentage(percentage)

# Get results
subprocess.call(["glpsol","-m","coverage.mod","-d","datafiles/coverage_"+sys.argv[1]+".dat","-y","output.dat"])

# Checks if there is another path available
if(os.stat("output.dat").st_size == 0):
	print "\n\nNo results available!"

else:
	# Save results
	save()

# Restores coverage.mod
restore(backup)

print "\nCompleted!"

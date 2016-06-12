# cycles.py

# Micael Reis  		2010143871 
# Samuel Nunes  	2011158011
# Joao Cerveira  	2010130654 

import subprocess
import sys
import os

def reset():
	f = open("outputs/cycles/cycles_" + sys.argv[1] + ".txt", "w")
	f.close()

def save_path(n):
	f = open("output.dat", "r")
	path = f.readlines()
	f.close()

	f = open("outputs/cycles/cycles_" + sys.argv[1] + ".txt", "a")
	path = "".join(path)
	f.write("--- Cycle ---\n")
	f.write(path)
	f.close()

def generate_constraint(n):
	f = open("output.dat", "r")
	path = f.readlines()
	f.close()
	size = len(path)

	constraint = "s.t. constraint" + str(n) + ": "

	for index in range(size):
		aux = path[index].split(" ");
		if(index==0):
			constraint = constraint + "x[" + aux[0][1:] + "," + aux[1][:-1] + "]"
		else:
			constraint = constraint + " + x[" + aux[0][1:] + "," + aux[1][:-1] + "]"

	constraint = constraint + " <= " + str(size-1) + ";\n" 
	return constraint
	
def insert_constraint(n):
	f = open("cycles.mod", "r")
	paths = f.readlines()
	f.close()

	index = paths.index("# Other constraints\n")
	constraint = generate_constraint(n)
	paths.insert(index+n, constraint)

	f = open("cycles.mod", "w")
	paths = "".join(paths)
	f.write(paths)
	f.close()

def restore(backup):
	f = open("cycles.mod", "w")
	backup = "".join(backup)
	f.write(backup)
	f.close()

# ---------------------------------------------------------------------------------------------------
n = 1

# Checks arguments
if(len(sys.argv)!=2):
    print "One argument is required, see report on how to use the scripts"
    exit(0)

# Backups paths.mod
f = open("cycles.mod", "r")
backup = f.readlines()
f.close()

# Erase output
reset()

# Obtain paths
while True:
	# Get path
	subprocess.call(["glpsol","-m","cycles.mod","-d","datafiles/"+sys.argv[1]+".dat","-y","output.dat"])

	# Checks if there is another path available
	if(os.stat("output.dat").st_size == 0):
		print "\n\nNo more cycles available!"
		break;

	# Save path in file
	save_path(n)

	# Insert constraint in paths.mod
	insert_constraint(n)
	n = n+1
		

# Restores paths.mod
restore(backup)

print "Cycles finded: " + str(n-1)
print "Completed!"

# join.py

# Micael Reis  		2010143871 
# Samuel Nunes  	2011158011
# Joao Cerveira  	2010130654 

import sys
import os

def reset():
	f = open("outputs/paths_cycles/paths_cycles_" + sys.argv[1] + ".txt", "w")
	f.close()

def copy_paths():
	f = open("outputs/paths/paths_" + sys.argv[1] + ".txt", "r")
	paths = f.readlines()
	f.close()

	n = paths.count("--- Path ---\n");

	f = open("outputs/paths_cycles/paths_cycles_" + sys.argv[1] + ".txt", "a")
	paths = "".join(paths)
	f.write(paths)
	f.close()

	return n

def get_paths():
	f = open("outputs/paths_cycles/paths_cycles_" + sys.argv[1] + ".txt", "r")
	paths = f.readlines()
	f.close()

	return paths

def save(path):
	f = open("outputs/paths_cycles/paths_cycles_" + sys.argv[1] + ".txt", "a")
	f.write(path)
	f.close()	

def delete_dots():
	f = open("outputs/paths_cycles/paths_cycles_" + sys.argv[1] + ".txt", "r")
	paths = f.readlines()
	f.close()

	f = open("outputs/paths_cycles/paths_cycles_" + sys.argv[1] + ".txt", "w")
	paths = "".join(paths)
	paths = paths.replace(".", "")
	f.write(paths)
	f.close()

def lists_overlap(a, b):
	for index in a:
		if index in b:
			return True
	return False

# ---------------------------------------------------------------------------------------------------

n = 0

# Checks arguments
if(len(sys.argv)!=2):
    print "One argument is required, see report on how to use the scripts"
    exit(0)

# Erase output
reset()

# Get paths
f = open("outputs/paths/paths_" + sys.argv[1] + ".txt", "r")
paths = f.readlines()
f.close()

# Get cycles
f = open("outputs/cycles/cycles_" + sys.argv[1] + ".txt", "r")
cycles = f.readlines()
f.close()
aux = "".join(cycles)
cycles = aux.split("--- Cycle ---\n")
cycles.remove("")
cycleslen = len(cycles)

# Checks if there is cycles
check = True;
if(os.stat("outputs/cycles/cycles_" + sys.argv[1] + ".txt").st_size == 0):
	check = False;

n = copy_paths()

# There is cycles to join
if (check==True):
	# Go through each cycle
	for index in range(cycleslen):
		# All paths
		paths = get_paths()
		paths = "".join(paths)
		paths = paths.split("--- Path ---\n")
		paths.remove("")
		pathslen = len(paths);

		# Cycles
		aux = cycles[index].split(" ");
		aux = "".join(cycles[index])
		aux = aux.replace("\n", " ")
		aux = aux.split(" ")
		aux.remove("")

		# Go through each path
		for index2 in range(pathslen):
			# Select One path
			aux2 = "".join(paths[index2])
			aux2 = aux2.replace("\n", " ")
			aux2 = aux2.split(" ")
			aux2.remove("")

			# Cycle is valid in this path
			if(lists_overlap(aux,aux2) == True):
				# Add path
				save("--- Path ---\n")
				save(paths[index2])

				# Checks for repeated edges
				a = "".join(paths[index2])
				a = a.split("\n")
				b = "".join(cycles[index])
				b = b.split("\n")
				for x in range(len(b)):
					if(a.count(b[x])!=1):
						save(b[x])
						save("\n")
				n = n+1

# Delete dots
delete_dots()

print "Number of paths: " + str(n)
print "Completed!"

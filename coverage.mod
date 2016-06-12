/* coverage.mod */

# Micael Reis  		2010143871 
# Samuel Nunes  	2011158011
# Joao Cerveira  	2010130654 

/* --------------------------------------------------------------------------------------------------------- */ 
/* Variables */

param nPaths, integer, > 0;		# Number of paths
param n, integer, > 0;			# Number of nodes / edges
set Paths := 1..nPaths; 		# Set of paths
set N := 1..n;					# Set of nodes / edges / edge-pair
param Matrix{Paths, N};			# Matrix with paths 
param Weight{Paths};			# Weight of each path

# Percentage

# x[i] = 1 means that path i is selected
var x{Paths}, binary;

# y[i] = 1 means that node is inside of some path selected at the moment
var y{N}, binary;

/* --------------------------------------------------------------------------------------------------------- */
/* Constraints */

s.t. r{j in N}: (sum{i in Paths} (Matrix[i,j] * x[i])) >= y[j];
s.t. constraint: sum{j in N} y[j] >= n*p;

/* --------------------------------------------------------------------------------------------------------- */
/* Calculates coverage */

minimize Z: sum{i in Paths} Weight[i] * x[i];

/* --------------------------------------------------------------------------------------------------------- */
/* Obtains solution and returns it */ 

solve;          

printf {i in Paths} "%i\n", x[i];
printf "Total Weight: %i\n", sum{i in Paths} Weight[i] * x[i];

end;

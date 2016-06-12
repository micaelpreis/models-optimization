/* cycles.mod */

# Micael Reis  		2010143871 
# Samuel Nunes  	2011158011
# Joao Cerveira  	2010130654 

/* --------------------------------------------------------------------------------------------------------- */ 
/* Variables */

param n, integer, > 0;                  # Number of nodes in the graph
param s, in {0..n};                     # Source node
param t, in {0..n};                     # Terminal node
set E, within {i in 0..n, j in 0..n};   # Set the edges of the graph
param c{(i,j) in E};                    # Distance of each edge (default is 1)

# x[i,j] = 1 means that edge (i,j) belong to shortest path
# x[i,j] = 0 means that edge (i,j) does not belong to shortest path
var x{(i,j) in E}, binary;

/* --------------------------------------------------------------------------------------------------------- */
/* Constraints */

s.t. r{i in 0..n}: sum{(j,i) in E} x[j,i] = sum{(i,j) in E} x[i,j]; 
s.t. constraint: sum{(i,j) in E} x[i,j] >= 1;

# Other constraints

/* --------------------------------------------------------------------------------------------------------- */
/* Calculate shortest path */

minimize Z: sum{(i,j) in E} c[i,j] * x[i,j];

/* --------------------------------------------------------------------------------------------------------- */
/* Obtains solution and returns it */ 

solve;   
       
printf {(i,j) in E: x[i,j] >= 1} ".%i %i\n", i, j;    

end;

# models-optimization
### Path-Set Selection in Control-Flow Testing

This project was developed as a school project for the System Modelling and Analysis course. 

It consists on producing integer linear programming (ILP) models that allow to enumerate paths in a control flow graph and to find exact solutions to the optimal (weighted) path-set selection problem using a standard ILP solver.

Control-flow testing is a technique used to test the implementation of a program.

#### The Problem

The control-flow graph (CFG) is a directed graph (or digraph) where nodes represent code segments to be executed sequentially without branching (or basic blocks), and edges represent transfer of control flow from one code segment to another due to a branch instruction at the end of a code segment

A particular execution of the program, given some sort of input (a test case), may then be represented as a path from the source node to the terminal node of the CFG, where nodes and edges may or may not be visited multiple times.

Although determining all paths in the graph from the source node to the terminal node may be possible, all-path testing may be too costly in practice, and a smaller set of paths is usually sought to provide the desired coverage.

So, how can we find a smallest set of paths satisfying a required coverage criterion?

**Note:** Common coverage criteria include node coverage (all nodes should be executed at least once), edge coverage (all edges should be traversed at least once), and consecutive edge-pair coverage (all pairs of consecutive edges in the graph should be covered). Such criteria may be relaxed to allow a given (small) percentage of nodes, edges or edge pairs to be left uncovered, at the expense of lower testing quality

#### Implementation

All ILP models developed were implemented in the GNU MathProg modelling language, and results were obtained using the glpk solver. Pre-processing, post-processing, and visualisation of input and output data was done in Python.

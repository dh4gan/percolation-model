2D Percolation Model (square lattice)
=====================================

This is a collection of Python scripts to generate a simple 2D percolation model

(following Landis 1999, "The Fermi Paradox: An Approach Based on Percolation Theory", JBIS, 51, 163-166
http://www.geoffreylandis.com/percolation.htp)

The code institutes a grid, with a sampling of initial colony points.  The points will colonise their neighbours with probability P
Below a critical probability Pc, the points will fail to occupy the entire box, and regions of space will be left empty.
Well above Pc, the majority of the box is colonised.  Around the critical probability, arbitrary large regions can either be colonised or left empty.

Depends on numpy and matplotlib (pcolor) to generate graphics

(Developed on numpy 1.8.0, and matplotlib 1.3.0)

`PercolationModel2D.py` contains the PercolationModel2D object which holds the automaton
and the rules by which it evolves

`PercolationModelPatterns.py` contains a set of basic patterns to add to the grid initially

`run_model.py` is a run script to generate percolation models


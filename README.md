# final-repo
Scripts for Steric Clash upon Docking

Upon molecular docking of a receptor with a ligand, steric clash between these two molecules should be cared for. Because steric clash can increase the energy and affect the structure of the molecules. That's why, I wrote a Python script which can show the residues in which the ligand and receptor have a distance smaller than 2 Å, and the contact counts in this residue. 

Upon molecular docking, the software gives many clusters and the first cluster has the best docking score. We usually have to choose one cluster for our future studies. The clusters with steric clash might affect our results. That's why, our cluster should be free of steric clash. This scripts might be useful for this purpose. 

In this repo, there are two scripts, one for PyMOL written in Python language, which can combine the receptor and ligand in the cluster into one object, and the other for the calculation of steric clash via Python. 

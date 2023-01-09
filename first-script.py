from pymol import cmd
from pymol import stored

cmd.loadall("*.pdb")                   

cmd.alter("lig*" + " and chain B", "chain='I'")     

cmd.create("obj0_00","lig.000.00.pdb or rec.pdb") 
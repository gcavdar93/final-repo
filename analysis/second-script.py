#!/usr/bin/env python
# coding: utf-8

# In[1]:


import vmd
import pandas as pd
import numpy as np


# In[2]:


mol = vmd.molecule.load('pdb' , 'obj01.pdb')


# In[3]:


mol


# In[4]:


n_frames = vmd.molecule.numframes(mol)
n_frames


# In[5]:


ligand = vmd.atomsel('(chain I) and (noh)')
receptor = vmd.atomsel('(chain A B C D E F G H) and (noh)')


# In[6]:


clash = []

for frame in range(0,n_frames):
    vmd.molecule.set_frame(mol,frame)
    if frame == 0:
        first = ligand.resid[0]
        last = ligand.resid[-1]

for i in range(first,last+1):
    residue = vmd.atomsel('(chain I and resid \'' + str(i) + '\')')
    contact_residue = len(residue.contacts(selection=receptor,cutoff=2)[0])
    clash.append([frame,i,contact_residue])


# In[7]:


df_clash = pd.DataFrame(clash, columns = ['frame', 'residue', 'contact_residue'])


# In[8]:


df_clash


# In[9]:


df = df_clash[df_clash["contact_residue"] > 0]
df


# In[10]:


df.to_csv('df.csv', index=False)


# In[ ]:





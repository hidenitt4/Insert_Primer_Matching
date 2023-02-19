#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import pandas as pd


# In[2]:


class Sequence(): 

    def __init__(self,seq): 
        self.seq = seq
        self.dseq = {}

        self.seq_to_dict()
    
    def __len__(self): 
        flat_seq = re.sub(r'\([^)]*\)', '#', self.seq)
            
        return len(flat_seq)
        
    def __str__(self): 
        
        return self.seq

    
    
    def seq_to_dict(self):
        if '(' not in self.seq:    
            for a,b in enumerate(self.seq):
                self.dseq[a] = b
            return
        
        else:
            flat_seq = re.sub(r'\([^)]*\)', '#', self.seq)
            d1 = {}
            count = 0
                
            for x,y in enumerate(flat_seq): 
                self.dseq[x] = y 
            for match in re.finditer(r'\([^)]*\)',self.seq): 
                d1[match.start()-count]= re.sub('[(/)]',"",match.group())
                count += len(match.group())-1
                
            self.dseq = self.dseq|d1
            
    def dict_compare(self, primer):
        count = 0
        
        for x,y in enumerate(self.dseq.values()): 
            if len(y) == 1:
                if y in primer.dseq[x]:  
                    count +=1
                else:
                    continue    
            elif len(y) > 1: 
                sub_count = 0 
                
                for z in [*y]: 
                    if z in primer.dseq[x]:
                        count +=1 
                        break      
                else: 
                    continue 
                                               
        return count
        
    
   


# In[ ]:





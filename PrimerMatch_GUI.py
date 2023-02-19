#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re 
from Sequence1 import Sequence 
from Primer_Match import PrimerMatching
import customtkinter as ctk
import tkinter as tk
from R_Sequence import Sequence
import csv, subprocess


# In[ ]:


class PrimerMatching():
    
    def __init__(self):
        self.clusters = []
        self.motifs = [] 
        self.comp = 0 
        self.match = 'Sequence Class'
        self.match_results = []
        
        # Execute 
        self.process_entries()
        self.insert_primer_match()
        
        self.to_xlsx()
        
    def process_entries(self): 
        self.clusters = [Sequence(cseq) for cseq in entry_1.get().split()] 
        self.motifs = [Sequence(mseq) for mseq in entry_2.get().split()] 
        
        return 
        
    def check_len(self): 
        checkC = set([len(cseq) for cseq in self.clusters])
        checkM = set([len(mseq) for mseq in self.motifs])
        
        if len(checkC) and len(checkM) != 1: 
            raise Exception('Please input consistent residue lengths.')
            
        else: 
            return
        
    def insert_primer_match(self): 

        for cseq in self.clusters: 
            for mseq in self.motifs:
                if cseq.dict_compare(mseq) <= self.comp:
                    continue
                else:
                    self.comp = cseq.dict_compare(mseq)
                    self.match = mseq
            self.comp = 0 
            self.match_results.append(self.match.seq)
            
        return
    
    def to_xlsx(self):
        inserts = [cseq.seq for cseq in self.clusters]
        df1 = pd.DataFrame({'Insert Sequence': inserts, 'Theoretical Matching Primer': self.match_results})
        
        df1.to_excel('Output.xlsx')
        subprocess.call(['open', 'Output.xlsx'])
        
        return


# In[ ]:


# GUI 
                       
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.geometry('500x350')                       
                       
                       
    
frame = ctk.CTkFrame(master = root)
frame.pack(pady=20,padx=60,fill='both',expand=True)
    
label = ctk.CTkLabel(master=frame, text='Primer Matching',font=('Georgia',24))
label.pack(pady=12,padx=10) 
    
    
 # Interactions

entry_1 = ctk.CTkEntry(master=frame,placeholder_text='Insert Sequences')
entry_1.pack(pady=12,padx=10)

entry_2 = ctk.CTkEntry(master=frame,placeholder_text='Primer Motifs')
entry_2.pack(pady=12,padx=10)
    
button = ctk.CTkButton(master=frame, text='Match',command=PrimerMatching)
button.pack(pady=12,padx=10)
                       

root.mainloop()


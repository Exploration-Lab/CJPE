#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os
import re
import spacy
import random
import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
import nltk.data
import time
import sys
import progressbar
import random
import shutil
import progressbar
import json

tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

input_paths_of_files = "gdrive/My Drive/data/" # give path to the directory where all the case files are contained
files = os.listdir(input_paths_of_files)

corpus = []
label = []
filen = []

ctAAcce = [] #"appeal accepted."
ctADisp = [] #"appeal disposed."
ctAAllo = [] #"appeal allowed."
ctADism = [] #"appeal dismissed."
ctAReje = [] #"appeal rejected."
ctPAcce = [] #"appeal accepted."
ctPDisp = [] #"appeal disposed."
ctPAllo = [] #"appeal allowed."
ctPDism = [] #"appeal dismissed."
ctPReje = [] #"appeal rejected."
ctAsAcce = [] #"appeal accepted."
ctAsDisp = [] #"appeal disposed."
ctAsAllo = [] #"appeal allowed."
ctAsDism = [] #"appeal dismissed."
ctAsReje = [] #"appeal rejected."
ctPsAcce = [] #"appeal accepted."
ctPsDisp = [] #"appeal disposed."
ctPsAllo = [] #"appeal allowed."
ctPsDism = [] #"appeal dismissed."
ctPsReje = [] #"appeal rejected."


for i in progressbar.progressbar(range(len(files))):# loop through all cases
    
    file_path = os.path.join(input_paths_of_files, files[i])
    f = open(files[i], "r", encoding="latin1")
    text = f.read()
    text = text.lower()
    textf = text[len(text)-100:]# will check if a particular text is present or not in last 100 characters for label finding
    
    if(re.search("appeal accepted\.",textf)!=None):# check if "appeal accepted" is there or not
        text = text[:len(text)-len(textf)+ re.search("appeal accepted\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAAcce.append(file_path)
        continue
    if(re.search("appeal rejected\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeal rejected\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAReje.append(file_path)
        continue
    if(re.search("appeal disposed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeal disposed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctADisp.append(file_path)
        continue
    if(re.search("appeal dismissed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeal dismissed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctADism.append(file_path)
        continue
    if(re.search("appeal allowed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeal allowed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAAllo.append(file_path)
        continue
    if(re.search("petition accepted\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petition accepted\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPAcce.append(file_path)
        continue
    if(re.search("petition rejected\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petition rejected\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPReje.append(file_path)
        continue
    if(re.search("petition disposed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petition disposed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPDisp.append(file_path)
        continue
    if(re.search("petition dismissed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petition dismissed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPDism.append(file_path)
        continue
    if(re.search("petition allowed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petition allowed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPAllo.append(file_path)
        continue
    if(re.search("appeals accepted\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeals accepted\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAsAcce.append(file_path)
        continue
    if(re.search("appeals rejected\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeals rejected\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAsReje.append(file_path)
        continue
    if(re.search("appeals disposed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeals disposed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAsDisp.append(file_path)
        continue
    if(re.search("appeals dismissed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeals dismissed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAsDism.append(file_path)
        continue
    if(re.search("appeals allowed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("appeals allowed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctAsAllo.append(file_path)
        continue
    if(re.search("petitions accepted\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petitions accepted\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPsAcce.append(file_path)
        continue
    if(re.search("petitions rejected\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petitions rejected\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPsReje.append(file_path)
        continue
    if(re.search("petitions disposed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petitions disposed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPsDisp.append(file_path)
        continue
    if(re.search("petitions dismissed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petitions dismissed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(0)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPsDism.append(file_path)
        continue
    if(re.search("petitions allowed\.",textf)!=None):
        text = text[:len(text)-len(textf)+ re.search("petitions allowed\.",textf).span()[0]]
        sents = tokenizer.tokenize(text)
        sents = sents[:len(sents)-4]
        text = (" ").join(sents)
        
        corpus.append(text)
        label.append(1)
        filen.append(file_path[file_path.rfind("/")+1:] + ".txt")
        ctPsAllo.append(file_path)
    

Acc_files = ctAAcce + ctAAllo + ctPAllo + ctPAcce
Rej_files = ctAReje + ctADism + ctADisp + ctPReje + ctPDism + ctPDisp

Acc_files = [f[f.rfind("/")+1:]+ ".txt" for f in Acc_files]
Rej_files = [f[f.rfind("/")+1:]+ ".txt" for f in Rej_files]

f = open("/home/vijit/miniset_files/anno_acc_list.txt", "w+")# writing all the accepted list files in a directory, give the path according to you
for fi in Acc_files:
    f.write(fi + "\n")
    
f.close()

f = open("/home/vijit/miniset_files/anno_rej_list.txt", "w+") # writing all the rejected list files in a directory, give the path according to you
for fi in Acc_files:
for fi in Rej_files:
    f.write(fi + "\n")
f.close()


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

nltk.download('punkt')
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

path_dataset_dir = "SCI/full_data/" # give the path of directory where the dataset is saved
files = os.listdir(path_dataset_dir) # all the files in the dataset


num_files_till_now = 0 # counter to count how many files have been preprocessed at a certain instance


for i in progressbar.progressbar(range(len(files))):
    file_path = os.path.join(path_dataset_dir, files[i])
    f = open(file_path, "r")
    text = f.read()
    text = re.sub(r"\xa0"," ",text)
    text = text.split("\n") # splitting using new line character
    text = [re.sub(r'[^a-zA-Z0-9.,)\-(/?\t ]','',sentence) for sentence in text] # removing everything other than these a-zA-Z0-9.,)\-(/?\t
    text = [re.sub(r'(?<=[^0-9])/(?=[^0-9])',' ',sentence) for sentence in text]
    text = [re.sub("\t+"," ",sentence) for sentence in text] # converting multiple tabs and spaces ito a single tab or space
    text = [re.sub(" +"," ",sentence) for sentence in text]
    text = [re.sub("\.\.+","",sentence) for sentence in text]# these were the commmon noises in out data, depends on data
    text = [re.sub("\A ?","",sentence) for sentence in text]
    text = [sentence for sentence in text if(len(sentence) != 1 and not re.fullmatch("(\d|\d\d|\d\d\d)",sentence))]
    text = [re.sub('\A\(?(\d|\d\d\d|\d\d|[a-zA-Z])(\.|\))\s?(?=[A-Z])','\n',sentence) for sentence in text]#dividing into para wrt to points
    text = [re.sub("\A\(([ivx]+)\)\s?(?=[a-zA-Z0-9])",'\n',sentence) for sentence in text] #dividing into para wrt to roman points
    text = re.sub(r"[()[\]\"$']"," ",text) # removing ()[\]\"$' these characters
    text = re.sub(r" no."," number",text) # converting no., nos., co., ltd.  to number, numbers, company and limited
    text = re.sub(r" nos."," numbers",text)
    text = re.sub(r" co."," company",text)
    text = re.sub(r" ltd."," limited",text)
    text2 = []
    for index in range(len(text)):#for removing multiple new-lines
        if(index>0 and text[index]=='' and text[index-1]==''):
            continue
        if(index<len(text)-1 and text[index+1]!='' and text[index+1][0]=='\n' and text[index]==''):
            continue
        text2.append(text[index])
    text = text2
    for i in range(len(text)): # ignoring the text before JUDGMENT,ORDER......
       if(re.search("\A(ORDER|JUDGMENT|J U D G M E N T|O R D E R)",text[i])):
           break
    if(i == len(text)-1):
       continue
    if(re.search("\A(ORDER|JUDGMENT|J U D G M E N T|O R D E R)",text[i+1])):
       i = i+1
    text = text[i+1:]
    text = "\n".join(text)
    lines = text.split("\n")
    text_new = " ".join(lines) # joining all the lines into a single text
    text_new = re.sub(" +"," ",text_new)
    num_tokens = len(word_tokenize(text_new))
    num_files_till_now+=1
    if(num_files_till_now%1000 == 0):
        print("Number of files that have been preprocessed: {0}".format(num_files_till_now))
    if(num_tokens < 100): # if number of tokens in file after preprocessing is less than 100 skipping the file
        continue
    
    fff = open("SCI/Preprocessed_files/" + files[i] + ".txt" ,"w+") #finally writing the preprocessed file in utput directory
    fff.write(text_new)
    fff.close()

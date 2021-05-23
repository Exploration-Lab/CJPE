#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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

input_paths_of_files = "gdrive/My Drive/data/" # give path to the directory where all the case files are contained
files = os.listdir(input_paths_of_files)

data = {}
data['data']={}

def label_for_file(sentence_set): # an implementation to find the label of each case, assumption that every case has words like accepted,rejected etc. at the end of the case
  label = -1
  sentnum = -1
  for i in range(len(sentence_set)):# loop through all sentences in which we will check for the words like asscepted, rejected etc.
          sentence = sentence_set[i]
          sentence = sentence.lower()
          A_accepted = ("accepted" in sentence) or ("accept" in sentence) or ("accepting" in sentence)# for accepeted cases we check words like accepted, approved, permitted and their variations
          A_allowed = ("allowed" in sentence) or ("allow" in sentence) or ("allowing" in sentence)
          A_permitted = ("permitted" in sentence) or ("permit" in sentence) or ("permitting" in sentence)
          A = A_accepted or A_allowed or A_permitted
          R_rejected = ("rejected" in sentence) or ("reject" in sentence) or ("rejecting" in sentence)# for rejected cases we check words like rejected, disposed, dismissed and their variations
          R_disposed = ("disposed" in sentence) or ("dispose" in sentence) or ("disposing" in sentence)
          R_dismissed = ("dismissed" in sentence) or ("dismiss" in sentence) or ("dismissing" in sentence)
          R = R_rejected or R_dismissed or R_disposed
          Appeal = ("appeal" in sentence) or ("appeals" in sentence)# we check if any sentence has accepted type and appeal together in a sentence and similarly for rejected type
          App = Appeal
          Not = ("not" in sentence) or ("no" in sentence)
          if(App and A and R and Not):
              break
          if(App and A and R):
              break
          if(App and A):
              label = 1
              sentnum = i
              break
          if(App and R):
              label = 0
              sentnum = i
              break
          if(App and A and Not):
              break
          if(App and R and Not):
              break    

  return label, sentnum

for i in progressbar.progressbar(range(len(dirs))):
    file_path = dirs[i]
    f = open(file_path, "r")
    text = f.read()
    
    sentences = tokenizer.tokenize(text)
    sentence_set = sentences[max(0,len(sentences)-100):]# we consider last 100 sentences where we check for label
    sentence_set.reverse()# reverse the set of sentences
    
    label, sentnum = label_for_file(sentence_set)

    if(label==-1):# if no label is found skip case
      continue

    cut_sentences = sentences[:len(sentences)-sentnum-1]# after lable is found, cut the end part of text where label was found
    new_sentence_set = sentences[max(0,len(cut_sentences)-10):]
    new_sentence_set.reverse()

    new_label, new_sentnum = label_for_file(new_sentence_set)

    if(new_label!=label):
      new_text = (" ").join(cut_sentences)
      final_text = new_text

      if(label==1):# label 1 for accepted
        p_file = open(like_orig_path + "Accepted/" + file_path[26:] + ".txt" ,"w")
        p_file.write(final_text) # write the final text in a file
        tokens = word_tokenize(final_text)
        num_tokens = len(tokens)
        data['data'][file_path[26:]] = {}
        data['data'][file_path[26:]]['name'] = file_path[26:] # the name key contains the name of file
        data['data'][file_path[26:]]['tokens'] = num_tokens# the tokens key contains number of tokens of file
        data['data'][file_path[26:]]['sentences'] = len(cut_sentences)# the sentences key contains the length of all sentences after removing the part which helped in label finding 
        data['data'][file_path[26:]]['label'] = 'Accepted'# the label key contains the label of case
        data['data'][file_path[26:]]['proof_sentence'] = sentence_set[sentnum] # the proof_sentence key contains the sentennce which helped in label finding
        p_file.close()
        lines = final_text.split("\n")
        text_new = " ".join(lines)
        text_new = re.sub(" +"," ",text_new)
        CT_file = open(summ_feed + "Accepted/" + file_path[26:] + ".txt" ,"w")
        CT_file.write(text_new)
        CT_file.close()

      elif(label==0):# label 0 for rejected
        p_file = open(like_orig_path + "Rejected/" + file_path[26:] + ".txt" ,"w")
        p_file.write(final_text)
        tokens = word_tokenize(final_text)
        num_tokens = len(tokens)
        data['data'][file_path[26:]] = {}
        data['data'][file_path[26:]]['name'] = file_path[26:]
        data['data'][file_path[26:]]['tokens'] = num_tokens
        data['data'][file_path[26:]]['sentences'] = len(cut_sentences)
        data['data'][file_path[26:]]['label'] = 'Rejected'
        data['data'][file_path[26:]]['proof_sentence'] = sentence_set[sentnum] 
        p_file.close()
        lines = final_text.split("\n")
        text_new = " ".join(lines)
        text_new = re.sub(" +"," ",text_new)
        CT_file = open(summ_feed + "Rejected/" + file_path[26:] + ".txt" ,"w")
        CT_file.write(text_new)
        CT_file.close()

    else:
      new_cut_sentences = cut_sentences[:len(cut_sentences)-new_sentnum-1]
      new_text = (" ").join(new_cut_sentences)
      final_text = new_text

      if(label==1):
        p_file = open(like_orig_path + "Accepted/" + file_path[26:] + ".txt" ,"w")
        p_file.write(final_text)
        tokens = word_tokenize(final_text)
        num_tokens = len(tokens)
        data['data'][file_path[26:]] = {}
        data['data'][file_path[26:]]['name'] = file_path[26:]
        data['data'][file_path[26:]]['tokens'] = num_tokens
        data['data'][file_path[26:]]['sentences'] = len(new_cut_sentences)
        data['data'][file_path[26:]]['label'] = 'Accepted'
        data['data'][file_path[26:]]['proof_sentence'] = sentence_set[sentnum] 
        p_file.close()
        lines = final_text.split("\n")
        text_new = " ".join(lines)
        text_new = re.sub(" +"," ",text_new)
        CT_file = open(summ_feed + "Accepted/" + file_path[26:] + ".txt" ,"w")
        CT_file.write(text_new)
        CT_file.close()

      elif(label==0):
        p_file = open(like_orig_path + "Rejected/" + file_path[26:] + ".txt" ,"w")
        p_file.write(final_text)
        tokens = word_tokenize(final_text)
        num_tokens = len(tokens)
        data['data'][file_path[26:]] = {}
        data['data'][file_path[26:]]['name'] = file_path[26:]
        data['data'][file_path[26:]]['tokens'] = num_tokens
        data['data'][file_path[26:]]['sentences'] = len(new_cut_sentences)
        data['data'][file_path[26:]]['label'] = 'Rejected'
        data['data'][file_path[26:]]['proof_sentence'] = sentence_set[sentnum] 
        p_file.close()
        lines = final_text.split("\n")
        text_new = " ".join(lines)
        text_new = re.sub(" +"," ",text_new)
        CT_file = open(summ_feed + "Rejected/" + file_path[26:] + ".txt" ,"w")
        CT_file.write(text_new)
        CT_file.close()

json_file = open(js_path + "splitter.json", "w")# now save the 'data' dictonary  in a json file
json.dump(file_info, json_file)


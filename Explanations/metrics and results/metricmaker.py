#!/usr/bin/env python
# coding: utf-8

# In[72]:


import json
g_json = open("gold_explanations_ranked.json", "r")
gold_exp = json.load(g_json)
o_json = open("occ_explanations.json", "r")
occ_exp = json.load(o_json)


# In[73]:


files = list(occ_exp.keys())


# In[76]:


import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from rouge import Rouge 
import nltk.translate
from nltk.translate import meteor_score
import progressbar
import numpy as np

# In[77]:


def get_BLEU_score(ref_text, machine_text):
    tok_ref_text = word_tokenize(ref_text)
    tok_machine_text = word_tokenize(machine_text)
    sc = nltk.translate.bleu_score.sentence_bleu([tok_ref_text], tok_machine_text, weights = (0.5,0.5))
    return sc

def jaccard_similarity(query, document):
    query = word_tokenize(query)
    document = word_tokenize(document)
    intersection = set(query).intersection(set(document))
    union = set(query).union(set(document))
    if(len(union)==0):
        return 0
    return len(intersection)/len(union)

def overlap_coefficient_min(query, document):
    query = word_tokenize(query)
    document = word_tokenize(document)
    intersection = set(query).intersection(set(document))
    den = min(len(set(query)),len(set(document)))
    if(den==0):
        return 0
    return len(intersection)/den

def overlap_coefficient_max(query, document):
    query = word_tokenize(query)
    document = word_tokenize(document)
    intersection = set(query).intersection(set(document))
    den = max(len(set(query)),len(set(document)))
    if(den==0):
        return 0
    return len(intersection)/den


# In[86]:


def occ_result_maker(file_to_write, Rank_initial, Rank_final, occ_exp, gold_exp):
    rouge1 = []
    rouge2 = []
    rougel = []
    jaccard = []
    bleu = []
    meteor = []
    overlap_min = []
    overlap_max = []
    
    for u in range(5):
        user = "User " + str(u+1)
        r1 = []
        r2 = []
        rl = []
        jacc = []
        bl = []
        met = []
        omin = []
        omax = []
        
        for i in progressbar.progressbar(range(len(files))):
            f = files[i]
            ref_text = ""
            for rank in range(Rank_initial, Rank_final+1, 1):
                if(gold_exp[f][user]["exp"]["Rank" + str(rank)]!=""):
                    ref_text += gold_exp[f][user]["exp"]["Rank" + str(rank)] + " "
                
            machine_text = occ_exp[f]
            machine_text = machine_text.lower()
            ref_text = ref_text.lower()
            
            if(ref_text == ""):
                continue
            rouge = Rouge()
            score = rouge.get_scores(machine_text, ref_text)
            r1.append(score[0]['rouge-1']['f'])
            r2.append(score[0]['rouge-2']['f'])
            rl.append(score[0]['rouge-l']['f'])
            jacc.append(jaccard_similarity(ref_text, machine_text))
            omin.append(overlap_coefficient_min(ref_text, machine_text))
            omax.append(overlap_coefficient_max(ref_text, machine_text))
            bl.append(get_BLEU_score(ref_text, machine_text))
            met.append(nltk.translate.meteor_score.meteor_score([ref_text], machine_text))
            
        rouge1.append(np.mean(r1))
        rouge2.append(np.mean(r2))
        rougel.append(np.mean(rl))
        jaccard.append(np.mean(jacc))
        overlap_min.append(np.mean(omin))
        overlap_max.append(np.mean(omax))
        bleu.append(np.mean(bl))
        meteor.append(np.mean(met))
        
    file_to_write.write("ROUGE-1 : {:}".format(rouge1) + "\n\n")
    file_to_write.write("ROUGE-2 : {:}".format(rouge2) + "\n\n")
    file_to_write.write("ROUGE-L : {:}".format(rougel)+ "\n\n")
    file_to_write.write("Jaccard : {:}".format(jaccard)+ "\n\n")
    file_to_write.write("Overmin : {:}".format(overlap_min)+ "\n\n")
    file_to_write.write("Overmax : {:}".format(overlap_max)+ "\n\n")
    file_to_write.write("BLEU    : {:}".format(bleu)+ "\n\n")
    file_to_write.write("METEOR  : {:}".format(meteor)+ "\n\n") 
            



experiments = [(1,10), (1,1), (2,2), (3,3,), (4,4), (5,5), (6,6), (7,7), (8,8), (9,9), (10,10), (1,5), (5,10)]
for exp in experiments:
    print(exp)
    f = open("result_files/Rank_" + str(exp[0]) + "_to_" + str(exp[1]) + ".txt", "w")
    occ_result_maker(f, exp[0], exp[1], occ_exp, gold_exp)




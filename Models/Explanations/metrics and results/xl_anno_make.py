#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
g_json = open("gold_explanations.json", "r")
gold_exp = json.load(g_json)


# In[2]:


#!export PYTHONPATH=$PYTHONPATH:/opt/anaconda3/lib/python3.7/site-packages


# In[3]:


import nltk
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from rouge import Rouge 
import nltk.translate
from nltk.translate import meteor_score
import xlsxwriter
import progressbar


# In[3]:


files = list(gold_exp.keys())


# In[4]:


def get_BLEU_score(ref_text, machine_text):
    tok_ref_text = word_tokenize(ref_text)
    tok_machine_text = word_tokenize(machine_text)
    sc = nltk.translate.bleu_score.sentence_bleu([tok_ref_text], tok_machine_text)
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


# In[5]:


book = xlsxwriter.Workbook("anno_explanations_scores" + ".xlsx") #creating new xlsx file 
cell_format = book.add_format()
cell_format.set_text_wrap()
cell_format.set_align("top")


# In[6]:


def write_dummy_labels(sheet, row, column):
    sheet.write(row, column, "User 1", cell_format)
    sheet.write(row, column+1, "User 2", cell_format)
    sheet.write(row, column+2, "User 3", cell_format)
    sheet.write(row, column+3, "User 4", cell_format)
    sheet.write(row, column+4, "User 5", cell_format)
    sheet.write(row, column+5, "Jaccard", cell_format)
    sheet.write(row, column+6, "OverlapMin", cell_format)
    sheet.write(row, column+7, "OverlapMax", cell_format)
    sheet.write(row, column+8, "ROUGE-1", cell_format)
    sheet.write(row, column+9, "ROUGE-2", cell_format)
    sheet.write(row, column+10, "ROUGE-L", cell_format)
    sheet.write(row, column+11, "BLEU", cell_format)
    sheet.write(row, column+12, "METEOR", cell_format)
    row=1
    column=0
    sheet.write(row, column, "Explanation", cell_format) #write rank labels on column 0
    sheet.write(row+1, column, "Decision", cell_format) #11th row has the label decision
    


def metric_score(metric, machine_text, ref_text):
    if(metric == "ROUGE-1"):
        rouge = Rouge()
        score = rouge.get_scores(machine_text, ref_text)
        return score[0]['rouge-1']['f']
    elif(metric == "ROUGE-2"):
        rouge = Rouge()
        score = rouge.get_scores(machine_text, ref_text)
        return score[0]['rouge-2']['f']
    elif(metric == "ROUGE-L"):
        rouge = Rouge()
        score = rouge.get_scores(machine_text, ref_text)
        return score[0]['rouge-l']['f']
    elif(metric == "Jaccard"):
        return jaccard_similarity(ref_text, machine_text)
    elif(metric == "Overmin"):
        return overlap_coefficient_min(ref_text, machine_text)
    elif(metric == "Overmax"):
        return overlap_coefficient_max(ref_text, machine_text)
    elif(metric == "BLEU"):
        return get_BLEU_score(ref_text, machine_text)
    elif(metric == "METEOR"):
        return nltk.translate.meteor_score.meteor_score([ref_text], machine_text)
    else:
        print("Not a correct metric was given.")
        return 0


# In[7]:


def writing_sheet_for_users(file_name, gold_exp, book):
    sheet = book.add_worksheet() #add a sheet
    sheet.set_column(0,0,15)
    sheet.set_column(1,5,70)
    sheet.set_column(6,13,40)
    row, column = 0,0
    sheet.write(row, column, file_name, cell_format)
    column+=1
    write_dummy_labels(sheet, row, column)
    row,column=1,1
    
    for u in range(5):
        explanation = gold_exp[file_name]["User " + str(u+1)]["exp"]
        verdict = gold_exp[file_name]["User " + str(u+1)]["verdict"]
        sheet.write(row,column,explanation, cell_format)
        sheet.write(row+1,column,verdict,cell_format)
        column+=1
    
    metrics = ["Jaccard", "Overmin", "Overmax", "ROUGE-1", "ROUGE-2", "ROUGE-L", "BLEU", "METEOR"]
    
    row=1
    column=6
    for i,metric in enumerate(metrics):
        metric_string = ""
        for u1 in range(1,6,1):
            inistring = "User " + str(u1) + "vs User "
            for u2 in range(1,6,1):
                if(u1==u2):
                    continue
                score = metric_score(metric, gold_exp[file_name]["User " + str(u1)]["exp"], gold_exp[file_name]["User " + str(u2)]["exp"])
                rounded_score = round(score,4)
                finstring = inistring + str(u2) + " = " + str(rounded_score)
                metric_string += finstring + "\n\n"
                
        sheet.write(row, column, metric_string, cell_format)
        column+=1


# In[8]:


for i in progressbar.progressbar(range(len(files))):
    writing_sheet_for_users(files[i], gold_exp, book)

# In[107]:


book.close()


# In[ ]:




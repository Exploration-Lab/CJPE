As mentioned in the paper we have used two types of embeddings with classical models: **Sent2Vec** and **Doc2Vec**. Both of these models were trained on the train set of **ILDC<sub>multi</sub>**. We are not releasing the trained models of these but we are releasing the mapped vectors from sentences (in case of sent2vec) and documents (in case of doc2vec) as we believe these are more convenient to use. If you want to train your own models you can use the train set of **ILDC<sub>multi</sub>** to train the embeddings. We used the following codebase for reference:
* For sent2vec. [(here)](https://ilmoirfan.com/how-to-train-sent2vec-model/)
* For doc2vec. [(here)](https://radimrehurek.com/gensim/models/doc2vec.html)

### Sent2Vec embeddings of ILDC<sub>multi</sub>: ### 

**Config**: mincount = 5, Vocab size = 750000, n-gram = 2, dimension size = 200. You can find the numpy files [here](https://drive.google.com/drive/folders/1d9TTu06NQzVL9WqZY3qNjKGt3w9PSUh3?usp=sharing)

### Doc2Vec embeddings of ILDC<sub>multi</sub>: ###

We are releasing two numpy files from two different versions of doc2vec

**Config**: dimension size = 500. You can find the numpy files [here](https://drive.google.com/drive/folders/1G0-8-j1br6aPa3E97HxXguvsfBiG2xUX?usp=sharing)

**Config**: dimension size = 1000. You can find the numpy files [here](https://drive.google.com/drive/folders/17qQe9t4BwD1VIjd2DGwpimC7rNlBioGH?usp=sharing)

## For reproducing results: ##
* Sent2Vec: You will need the numpy files for sent2vec mentioned above. You can then run the following command:
```
python classical_models_sent2vec_avgd.py path_to/train_set_npy_file path_to/test_set_npy_file path/to/dev_set_npy_file
```
* Doc2Vec: You will need the numpy files for Doc2Vec mentioned above (Use any one configuration). You can then run the following command:
```
python classical_models_doc2vec.py path_to/train_set_npy_file path_to_train_set_labels_file path_to/test_set_npy_file path_to/test_set_labels_file path_to/dev_set_npy_file path/to/dev_set_labels_file
```

For either of the embedding type the output will be 3 files in the working directory. **SVM_results.txt, RF_results.txt, LR_results.txt** for each of the hyperparameter setting. **Be careful while using 1000 dimension size Doc2Vec model with SVM. It can take up a lot of time to generate results.**

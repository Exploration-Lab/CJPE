## Link of the Dataset ##
The **CatchPhrase** dataset can be found [here](https://drive.google.com/drive/folders/1xY0b5WgFSgcMFcMM1BGicBSvof-7iGeP?usp=sharing).

### Description of CatchPhrase Dataset ###

* Firstly, we extract the noun phrases using the paper [Automatic Catchphrase Identification from Legal Court Case Documents, by A Mandal, K Ghosh, A Pal, S Ghosh at CIKM, 2017](https://dl.acm.org/doi/10.1145/3132847.3133102) and Github repo of [NNP-extractor](https://github.com/amarnamarpan/NNP-extractor-a-highly-customisable-noun-phrase-extraction-module). 

* After we get the noun phrases we passes for the score that phrase, sentence or word using the above mentioned paper and Github repo of [PSLEGAL - An unsupervised way of legal catchphrase extraction](https://github.com/amarnamarpan/PSLEGAL-An-unsupervised-way-of-legal-catchphrase-extraction).

* Using the scored phrases for each documents first we sort the phrases according to the score.

* We extract the sentences using the top scored phrases corresponding to that documents.

* Using the NLTK sentence tokenizer we get 200 sentences covered 90% of the data in catch-phrase dataset, so we extracted only top 200 sentences form the corresponding documents.

### Embeddings ###

We have used two types of embeddings with classical models: **Sent2Vec** and **Doc2Vec**. Both of these models were trained on the train set of **CatchPhrase** dataset. We are not releasing the trained models of these but we are releasing the mapped vectors from sentences (in case of sent2vec) and documents (in case of doc2vec) as we believe these are more convenient to use. If you want to train your own models you can use the train set of **CatchPhrase** dataset to train the embeddings. We used the following codebase for reference:
* For sent2vec. [(here)](https://ilmoirfan.com/how-to-train-sent2vec-model/)
* For doc2vec. [(here)](https://radimrehurek.com/gensim/models/doc2vec.html)

#### Sent2Vec embeddings of CatchPhrase dataset: ####

**Config**: mincount = 5, Vocab size = 750000, n-gram = 2, dimension size = 200. You can find the numpy files [here](https://drive.google.com/drive/folders/1vPE5GZdIVsLNVZFCR5DJBuaucUFi4IZQ?usp=sharing)

#### Doc2Vec embeddings of CatchPhrase dataset: ####

**Config**: dimension size = 500. You can find the numpy files [here](https://drive.google.com/drive/folders/1vPE5GZdIVsLNVZFCR5DJBuaucUFi4IZQ?usp=sharing)

#### For reproducing results: ####
* Sent2Vec: You will need the numpy files for sent2vec mentioned above. You can then run the following command:
```
python classical_models_sent2vec_avgd.py path_to/train_set_npy_file path_to/test_set_npy_file path/to/dev_set_npy_file
```
* Doc2Vec: You will need the numpy files for Doc2Vec mentioned above (Use any one configuration). You can then run the following command:
```
python classical_models_doc2vec.py path_to/train_set_npy_file path_to_train_set_labels_file path_to/test_set_npy_file path_to/test_set_labels_file path_to/dev_set_npy_file path/to/dev_set_labels_file
```

### Models ###
We run two sequential models on the catch-phrase dataset:
* BiGRU 
  * Sent2Vec embeddings of CatchPhrase dataset
  * Doc2Vec embeddings of CatchPhrase dataset
* BiGRu with attention
  * Sent2Vec embeddings of CatchPhrase dataset
  * Doc2Vec embeddings of CatchPhrase dataset

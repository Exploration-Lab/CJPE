## Sequential Models


### BIGRU

We used BIGRU with four types of inputs:
 - **Sent2Vec Embedding**(Embedding Dim: 200). For Doc2Vec embeddings numpy file please refer to *CJPE/Classical Models/README.md*
 - **GloVe embeddings**( last 512 tokens of case tokenized with nltk tokenizer, Embedding Dim = 180). GloVe Model: [link](https://drive.google.com/drive/folders/1vNcOo4e8-qEhWQosJCND6g6_lTsZdOua) 
 - **Doc2Vec Embeddings**(applied for every 500 token chunk length, tokenized with nltk tokenizer, Embedding Dim: 1000). For Sent2Vec embeddings numpy file please refer to *CJPE/Classical Models/README.md*
 - **Transformers Chunk Embeddings**(eg. BERT, XLNet, RoBERTa.) with every chunk Embedding Dim: 768(except concatenated one). For more details please refer to *CJPE/transformers/* folder.
>  **Note1**: For all the above we used both *ILDC<sub>single</sub>*   and *ILDC<sub>multi</sub>* dataset. 

> **Note2**: For 4<sup>th</sup> point, the entire model with Transformers are called Hierarchical Model.

### BIGRU with Attention

The inputs are similar to BIGRU just we are using an **Attention Layer** on top of the BIGRU so as to assign weigths to each chunk depending on their importance in label prediction.

### HAN

We use both the datasets *ILDC<sub>multi</sub>* and *ILDC<sub>single</sub>* datasets. 

**Input**: For input we use the GloVe Embeddings( Embedding Dim: 180) to train the model. We take the last 40 sentences(atmost) with 50 tokens(atmost) for each sentence, used the NLTK tokenizer to tokenize the data.
GloVe model: [link](https://drive.google.com/drive/folders/1vNcOo4e8-qEhWQosJCND6g6_lTsZdOua) 

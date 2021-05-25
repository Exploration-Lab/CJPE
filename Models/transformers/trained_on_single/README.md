### Fine-tuned transformers on ILDC<sub>single</sub>

We used the SequenceClassification models' codebase from Chris Mccormick's tutorials [here](https://mccormickml.com/)

The fine-tuning of these transformers was done on ILDC<sub>single</sub> in the following steps:
* Load the ILDC<sub>single</sub> data.
* For each document divide it into chunks of 512 tokens each with an overlap of 100 tokens with neighbouring chunk.
* Give each chunk the same label as the whole document.
* Now fine-tune the transformer model taking each chunk as a separate input in training.

You can find our fine-tuned models from here: (all saved models were trained using the above strategy)

Model      |  link |
-----------|-------|
BERT       | [here](https://drive.google.com/drive/folders/1TD2FQix8_gIOXiV2rTgbCU7lfrplH1HM?usp=sharing)|
RoBERTa    | [here](https://drive.google.com/drive/folders/1-u66E41nlGowY4RFAVCBR9iMkDL8zB80?usp=sharing)  |
XLNet      | [here](https://drive.google.com/drive/folders/1d8p1StTObDzQoc_X2hEs7nGITfxa6L9I?usp=sharing)  |

**Note**: If you want to know more about the training hyperparameters we used, please look at section A of appendix in the paper.

### For Hierarchical models using ILDC<sub>single</sub>

Please remember that we fine-tuned the transformer on ILDC<sub>single</sub> using the above strategy. However, for the training of BiGRU or other models on [CLS] embedding features we used the fine-tuned model to *get the [CLS] embeddings of each chunk of every document in ILDC<sub>multi</sub>*

For easy reproducibilty, we also make available the [CLS] token embeddings. You can easily reproduce the hierarchical model results (transformer trained on ILDC<sub>single</sub>) using these embeddings and training a BiGRU model on these as in the directory of Sequential_Models. We have made available the code for both attention included and without attention models of Bidirectional GRUs.

You can access the saved [CLS] embeddings from here:

Model      | link |
-----------|-------|
BERT       | [here](https://drive.google.com/drive/folders/1g4di6WHAnKPoUl8gQ8YcQUOILBmmy1q7?usp=sharing)|
RoBERTa    | [here](https://drive.google.com/drive/folders/1NF5AGgztp29comv4HMABcRwowP4Kf0v5?usp=sharing)  |
XLNet      | [here](https://drive.google.com/drive/folders/1aYH_dbe7YIiqZ6ULR_OVvXBlbKa_PyA5?usp=sharing)  |

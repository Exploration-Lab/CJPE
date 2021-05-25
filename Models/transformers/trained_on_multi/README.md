### Fine-tuned transformers on ILDC<sub>multi</sub>

We used the SequenceClassification models' codebase from Chris Mccormick's tutorials [here](https://mccormickml.com/)

In the paper we mentioned that for BERT we tried out multiple combinations of input tokens. The notebook provided here for BERT has only the last 512 tokens implementaion. We encourage the reader to change the code (only a slight change is needed in the function input_id_maker) as it is really straightforward. The other transformer models were fine-tuned using the last 512 tokens only.

You can find our fine-tuned models from here: (all saved models were trained on last 512 tokens only)

Model      | Performance (Accuracy) | link |
-----------|------------------------|------|
DistilBERT |  64.21%                |  [here](https://drive.google.com/drive/folders/1-bdRjxo0l6rItR5jsGWnYE0p7iZanB_E)    |
BERT       |  67.24%                |  [here](https://drive.google.com/drive/folders/17nddWo9e4Z-rljF83jIq1aEb3w71DouZ?usp=sharing)|
RoBERTa    |  71.26%                |  [here](https://drive.google.com/drive/folders/10CuJ9p2MNcRAwM87bNXisS07_smi97qX?usp=sharing)  |
XLNet      |  70.01%                |  [here](https://drive.google.com/drive/folders/1Pn3uaPz6PNFaBo9IrtuJpC2PNpDMDXhS?usp=sharing)  |

**Note1**: These transformers are also used in the Voting Ensemble method as well.

**Note2**: If you want to know more about the training hyperparameters we used, please look at section A of appendix in the paper.

### For Hierarchical models using ILDC<sub>multi</sub>

For easy reproducibilty, we also make available the [CLS] token embeddings. You can easily reproduce the hierarchical model results (transformer trained on ILDC<sub>multi</sub> using these embeddings and training a BiGRU model on these as in the directory of Sequential_Models. We have made available the code for both attention included and without attention models of Bidirectional GRUs.

You can access the saved [CLS] embeddings from here (except DistilBERT)

Model      | link |
-----------|-------|
BERT       | [here](https://drive.google.com/drive/folders/1bYrsn8JEu_C2ExWBQnqUPmApCn-is8IL?usp=sharing)|
RoBERTa    | [here](https://drive.google.com/drive/folders/1b_9j1XoXpdvGEOnwahvIcSDz5SzVLvJ9?usp=sharing)  |
XLNet      | [here](https://drive.google.com/drive/folders/1TXQctks4_8mPuBUrHC7mvDxhjs4Lxab2?usp=sharing)  |




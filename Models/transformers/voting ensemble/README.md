## Voting Ensemble ##

We used only RoBERTa and XLNet for voting ensemble techniques as they had the best results in individual transformers results. Steps for getting the results in Voting Ensemble method:
* Load the fine-tuned model (we used the transformers that were trained on ILDC<sub>multi</sub> last 512 tokens only).
* Divide each document into chunks of 512 tokens each with an overlap of 100 tokens with the neighbouring chunks.
* Use the fine-tuned model to get the label of each chunk.
* The label for the whole document was determined by majority out of each chunk label of the document.

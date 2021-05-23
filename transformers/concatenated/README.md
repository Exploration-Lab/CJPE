### For "Hierarchical Concatenated model trained on ILDC<sub>single</sub>" ###

We used the XLNet model trained on the ILDC<sub>single</sub> train set. For more information about the fine-tuning of this transformer you can check out the readme file in the path: CJPE/transformers/trained_on_single.

Using the fine-tuned model we extracted out the [CLS] embeddings of the last 4 hidden layers and concatenated them into a single 768 x 4 dimension embedding.
The file **concat_XLNet_embeddings_maker.ipynb** demonstrates the task of doing the same by loading the pretrained model and then saving the concatenated embeddings of last 4 hidden states.
For ease in reproducibility we have saved the numpy files on google drive [here](https://drive.google.com/drive/folders/1tGDa8Jm4r3C5Cs_BuAvn-S3dH66e4cP7?usp=sharing).

**Note:** Train set has been split into 3 files 1GB each due to their huge size.

You can use the file **XLNet_full_concat_results.ipynb** file to reproduce the results. You will need the ILDC dataset files and the saved numpy files given above.




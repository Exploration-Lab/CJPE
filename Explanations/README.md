# File Descriptions #

**File name**| **Description**
-------------|----------------
**occ_explanations_hierarchical.ipynb:**| This file was used for the BiGRU half occlusion (refer to paper). We trained the BiGRU model without attention and used the defined occlusion method to give wieghts to each chunk in every document of **ILDC<sub>expert</sub>**.
**XLNet_noatt_2layer_occlusion:**| This file was used for XLNet half occlusion (refer to paper). We used the occlusion weights generated from the above file to rank and extract sentences from each chunk having a positive chunk score.
**metrics and results**| The results of machine explanations and annotated explanations' json files are stored in this folder. This also has scripts for each metric and results.

To make reproducibility easier, we have also released occlusion weights of each document after the BiGRU step [here](https://drive.google.com/drive/folders/1g4di6WHAnKPoUl8gQ8YcQUOILBmmy1q7?usp=sharing). You can plot these yourself if desired.



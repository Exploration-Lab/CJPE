### Description of the Dataset ###
The **ILDC_expert** have two repositories, source and annotation. The source repository contains the preprocessed documents (56 in total), which was given to the 5 different annotators. The annotation repository also contains the 56 document folders but here each folder has 5 annotated json files corresponding to every user.

Use the `ILDC_EXPERT_Convert_To_CSV` file to convert the json files for each user and each case to csv files. The csv file contain 2 columns a `TEXT` and a `LABEL` column. `TEXT` is a section of the case and `LABEL` is it's rank. 

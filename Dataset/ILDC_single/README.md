## Link of the Dataset ##
The **ILDC_single** dataset (7593) including train (5082), development (994) and test (1517) can be found [here]().

### Description of the Dataset ###

The link contains the CSV file of **ILDC_single** dataset, which has four columns ['text', 'label', 'split', 'name']. 
Where,
* 'text' contains the preprocessed data
* 'label' contains either '0' or '1'
  * '0' represents all petitions have been rejected
  * '1' represents all petitions have been accepted
* 'split' maintains that the file belongs either train set, validation set or test set
* 'name' shows that the name of file.

### Example of Train set ###

text                                              | label | split | name
------------------------------------------------- | ----- | ----- | ----
F. NARIMAN, J. Leave granted. In 2008, the Pu...	| 1     |	train |	2019_890.txt
S. THAKUR, J. Leave granted. These appeals ar...	| 0	    |train  |	2014_170.txt
Markandey Katju, J. Leave granted. Heard lear...	| 1	    |train	| 2010_721.txt

*The Validation/Development and Test sets are same as **ILDC_multi**.*

### Example of Validation/Development set ###

text                                              | label | split | name
------------------------------------------------- | ----- | ----- | ----
civil appellate jurisdiction civil appeal numb...	| 0	    | dev	  | 1989_75.txt
original jurisdiction writ petitions number. 8...	| 0	    | dev	  | 1985_233.txt
\nsarkar j. \n\nwe think this appeal must be a...	| 1	    | dev	  | 1963_285.txt


### Example of Test set ###

text                                              | label | split | name
------------------------------------------------- | ----- | ----- | ----
civil appellate jurisdiction civil appeal numb...	| 1	    | test	 | 1986_397.txt
criminal appellate jurisdiction special leave ...	| 0	    | test	 | 1977_183.txt
criminal appellate jurisdiction criminal appea...	| 0	    | test	 | 1993_98.txt


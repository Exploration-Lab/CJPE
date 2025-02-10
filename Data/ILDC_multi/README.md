## Link of the Dataset ##
The **ILDC_multi** dataset (34816) including train (32305), development (994) and test (1517). 

### Description of the Dataset ###

The link contains the CSV file of **ILDC_multi** dataset, which has four columns ['text', 'label', 'split', 'name']. 
Where,
* 'text' contains the preprocessed data
* 'label' contains either '0' or '1'
  * '0' represents all petitions have been rejected
  * '1' represents atleast one petition has been accepted
* 'split' maintains that the file belongs either train set, validation set or test set
* 'name' shows that the name of file.

### Example of Train set ###

text                                              | label | split | name
------------------------------------------------- | ----- | ----- | ----
Uday Umesh Lalit, J. These appeals arise out ...  | 0     | train | 2020_1.txt
Indira Banerjee, J. These appeals are against...	| 0	    | train	| 2020_2.txt
M. Khanwilkar, J. Delay companydoned. Leave g...	| 1     |	train	| 2020_12.txt

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
criminal appellate jurisdiction criminal appea...	| 0	    | test	  | 1993_98.txt


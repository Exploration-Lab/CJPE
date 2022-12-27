# CJPE (Court Judgment Prediction and Explanation)
Court Judgment Prediction and Explanation (Paper: <https://aclanthology.org/2021.acl-long.313/>)

The repository contains the full codebase of experiments and results of the ACL-IJCNLP 2021 paper "ILDC for CJPE: Indian Legal Documents Corpus for Court Judgment Prediction and Explanation". 

You can get ILDC dataset in the Dataset folder.

Our contributions can be summarized as below:
* We introduce a new task – Court Judgment Prediction and Explanation (CJPE) with the following sub-tasks: Court Judgment Prediction and Explanation of the Prediction.
* We create a new corpus (Indian Legal Documents Corpus (ILDC) annotated with court decisions and corresponding explanations.
* We develop a battery of methods to solve the task. We perform an extensive experimentation with state of the art machine learning algorithms for the judgement prediction task. We develop a new method for explaining machine predictions since none of the existing methods could be readily applied in our setting. We evaluate our explainability results with annotations by legal experts, showing significant differences between point of view of algorithms and experts. We also perform a detailed case study to understand the annotations by lawyers (for more details please check the paper)

## License

[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)


The ILDC dataset and CJPE software follows [CC-BY-NC](CC-BY-NC) license. Thus, users can share and adapt our dataset if they give credit to us and do not use our dataset for any commercial purposes.

## Citation

```
@inproceedings{malik-etal-2021-ildc,
    title = "{ILDC} for {CJPE}: {I}ndian Legal Documents Corpus for Court Judgment Prediction and Explanation",
    author = "Malik, Vijit  and
      Sanjay, Rishabh  and
      Nigam, Shubham Kumar  and
      Ghosh, Kripabandhu  and
      Guha, Shouvik Kumar  and
      Bhattacharya, Arnab  and
      Modi, Ashutosh",
    booktitle = "Proceedings of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing (Volume 1: Long Papers)",
    month = aug,
    year = "2021",
    address = "Online",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2021.acl-long.313",
    doi = "10.18653/v1/2021.acl-long.313",
    pages = "4046--4062",
    abstract = "An automated system that could assist a judge in predicting the outcome of a case would help expedite the judicial process. For such a system to be practically useful, predictions by the system should be explainable. To promote research in developing such a system, we introduce ILDC (Indian Legal Documents Corpus). ILDC is a large corpus of 35k Indian Supreme Court cases annotated with original court decisions. A portion of the corpus (a separate test set) is annotated with gold standard explanations by legal experts. Based on ILDC, we propose the task of Court Judgment Prediction and Explanation (CJPE). The task requires an automated system to predict an explainable outcome of a case. We experiment with a battery of baseline models for case predictions and propose a hierarchical occlusion based model for explainability. Our best prediction model has an accuracy of 78{\%} versus 94{\%} for human legal experts, pointing towards the complexity of the prediction task. The analysis of explanations by the proposed algorithm reveals a significant difference in the point of view of the algorithm and legal experts for explaining the judgments, pointing towards scope for future research.",
}
```

## Contact

In case of any queries, please contact <ashutoshm.iitk@gmail.com>, <vijitvm21@gmail.com>

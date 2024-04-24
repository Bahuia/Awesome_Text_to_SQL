# Text-to-SQL Literature 
This repository is maintained by [Yongrui Chen](). Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). 
The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

You can directly use our bibtex.bib in overleaf with this [link]().

This page categorizes the literature by the **LLM Technique**

## Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/scenario/README.md#hyperlink)
- [![](https://img.shields.io/badge/Hard_Prompt-2-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/scenario/README.md#hard-prompt)
- [![](https://img.shields.io/badge/Supervised_Fine_tuning-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/scenario/README.md#supervised-fine-tuning)
- [![](https://img.shields.io/badge/Data_Augmentation-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/scenario/README.md#data-augmentation)
- [![](https://img.shields.io/badge/Incremental_Pre_training-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/scenario/README.md#incremental-pre-training)
## Hyperlink 
- [[Overview]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/README.md) -- [Homepage](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/README.md)
-  -- [Summary](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/./)
-  -- [Model Architecture](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/architecture)
-  -- [Conference](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/conference)
-  -- [Dataset](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/dataset)
-  -- [SQL Generation Framework](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/framework)
-  -- [Intermedia Representation](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/intermedia)
-  -- [Journal](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/journal)
-  -- [Large Language Model](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/llm)
-  -- [Metric](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/metric)
-  -- [Paper Type](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/paper_type)
-  -- [ Learning Paradigm](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/paradigm)
-  -- [Preprint](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/preprint)
-  -- [Application Scenario](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/scenario)
-  -- [Task](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/task)
-  -- [LLM Technique](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/text2sql/technique)

## Hard Prompt

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2403.09732)<a href="https://scholar.google.com.hk/scholar?q=PET-SQL:+A+Prompt-enhanced+Two-stage+Text-to-SQL+Framework+with+Cross-consistency"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**PET-SQL: A Prompt-enhanced Two-stage Text-to-SQL Framework with
Cross-consistency**](https://doi.org/10.48550/arXiv.2403.09732) , <br> by *Zhishuai Li and
Xiang Wang and
Jingjing Zhao and
Sun Yang and
Guoqing Du and
Xiaoru Hu and
Bin Zhang and
Yuxiao Ye and
Ziyue Li and
Rui Zhao and
Hangyu Mao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L9-L44) <br>```PET-SQL, Two-stage pure prompt method, retrieve domain-agnostic examples, voting for curation
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-09732```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L47-L91) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Supervised Fine-tuning

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L47-L91) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Data Augmentation

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L47-L91) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Incremental Pre-training

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L47-L91) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
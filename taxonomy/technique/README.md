# Text-to-SQL Literature 
This repository is maintained by [Yongrui Chen](). Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). 
The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

You can directly use our bibtex.bib in overleaf with this [link]().

This page categorizes the literature by the **LLM Technique**.

## Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#hyperlink)
- [![](https://img.shields.io/badge/Program_of_Thought-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#program-of-thought)
- [![](https://img.shields.io/badge/Hard_Prompt-7-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#hard-prompt)
- [![](https://img.shields.io/badge/Supervised_Fine_tuning-5-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#supervised-fine-tuning)
- [![](https://img.shields.io/badge/Data_Augmentation-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#data-augmentation)
- [![](https://img.shields.io/badge/Incremental_Pre_training-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#incremental-pre-training)
- [![](https://img.shields.io/badge/Retrieval_augmented_Generation-2-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique/README.md#retrieval-augmented-generation)
## Hyperlink 
- [[Overview]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/README.md)
-  -- [Summary](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/./)
-  -- [Model Architecture](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture)
-  -- [Author](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/author)
-  -- [Dataset](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/dataset)
-  -- [SQL Generation Framework](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/framework)
-  -- [Intermedia Representation](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/intermedia)
-  -- [Large Language Model](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/llm)
-  -- [Metric](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/metric)
-  -- [Paper Type](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/paper_type)
-  -- [ Learning Paradigm](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/paradigm)
-  -- [Application Scenario](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/scenario)
-  -- [Task](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/task)
-  -- [LLM Technique](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/technique)
-  -- [Published Venue](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/venue)
-  -- [Published Year](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/year)

## Program of Thought

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.14851)<a href="https://scholar.google.com.hk/scholar?q=SQL-CRAFT:+Text-to-SQL+through+Interactive+Refinement+and+Enhanced+Reasoning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SQL-CRAFT: Text-to-SQL through Interactive Refinement and Enhanced
Reasoning**](https://doi.org/10.48550/arXiv.2402.14851) , <br> by *Hanchen Xia and
Feng Jiang and
Naihao Deng and
Cunxiang Wang and
Guojiang Zhao and
Rada Mihalcea and
Yue Zhang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L238-L272) <br>```1: simultaneously generate python and sql; 2: first generate python and then genearte SQL. The loop terminates when the program detects that the model has generated the same SQL again.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-14851```
## Hard Prompt

- [![](https://img.shields.io/badge/COLING-2024-blue)](https://aclanthology.org/2024.lrec-main.539)<a href="https://scholar.google.com.hk/scholar?q=Enhancing+Text-to-SQL+Capabilities+of+Large+Language+Models+through+Tailored+Promptings"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Enhancing Text-to-SQL Capabilities of Large Language Models through
Tailored Promptings**](https://aclanthology.org/2024.lrec-main.539) , <br> by *Zhao Tan and
Xiping Liu and
Qing Shu and
Xi Li and
Changxuan Wan and
Dexi Liu and
Qizhi Wan and
Guoqiong Liao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L8-L49) <br>```three prompts: 1) Prompting for Schema Linking. 2) Prompting for SQL Generation. 3) Combining Promptings. Finally, result selection prompt based on self-consistency.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```TanLSLWLWL24```
- <a href="https://scholar.google.com.hk/scholar?q=SQL-to-Schema+Enhances+Schema+Linking+in+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **SQL-to-Schema Enhances Schema Linking in Text-to-SQL**, <br> by *Yang, Sun, Su, Qiong, Li, Zhishuai, Li, Ziyue, Mao, Hangyu, Liu, Chenxi and Zhao, Rui* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L52-L69) <br>```three stage: 1) generate an initial SQL query by utilizing the complete database schema. 2) extract tables and columns from the initial SQL query to create a concise schema. 3) generate the final sql.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```yang2024sql```
- [![](https://img.shields.io/badge/VLDB-2024-blue)](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf)<a href="https://scholar.google.com.hk/scholar?q=Text-to-SQL+Empowered+by+Large+Language+Models:+A+Benchmark+Evaluation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation**](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf) , <br> by *Dawei Gao and
Haibin Wang and
Yaliang Li and
Xiuyu Sun and
Yichen Qian and
Bolin Ding and
Jingren Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L73-L119) <br>```Evaluate Prompt Engnieering, In-context learning and SFT
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```pvldb-GaoWLSQDZ24```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.14851)<a href="https://scholar.google.com.hk/scholar?q=SQL-CRAFT:+Text-to-SQL+through+Interactive+Refinement+and+Enhanced+Reasoning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SQL-CRAFT: Text-to-SQL through Interactive Refinement and Enhanced
Reasoning**](https://doi.org/10.48550/arXiv.2402.14851) , <br> by *Hanchen Xia and
Feng Jiang and
Naihao Deng and
Cunxiang Wang and
Guojiang Zhao and
Rada Mihalcea and
Yue Zhang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L238-L272) <br>```1: simultaneously generate python and sql; 2: first generate python and then genearte SQL. The loop terminates when the program detects that the model has generated the same SQL again.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-14851```
- <a href="https://scholar.google.com.hk/scholar?q=Dubo-SQL:+Diverse+Retrieval-Augmented+Generation+and+Fine+Tuning+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **Dubo-SQL: Diverse Retrieval-Augmented Generation and Fine Tuning for Text-to-SQL**, <br> by *Thorpe, Dayton G, Duberstein, Andrew J and Kinsey, Ian A* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L275-L294) <br>```v1: SFT + gpt3.5, v2: RAG from training set, ICL + GPT-4. 1: 'We find the LLM learns more from the few-shot examples if we include the questions as user messages and the answers as assistant messages in the conversation history.' 2: 'the output in JSON format improves execution accuracy.'
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```thorpe2024dubo```
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
Hangyu Mao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L327-L363) <br>```PET-SQL, Two-stage pure prompt method, retrieve domain-agnostic examples, voting for curation
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
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L366-L411) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Supervised Fine-tuning

- [![](https://img.shields.io/badge/VLDB-2024-blue)](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf)<a href="https://scholar.google.com.hk/scholar?q=Text-to-SQL+Empowered+by+Large+Language+Models:+A+Benchmark+Evaluation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation**](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf) , <br> by *Dawei Gao and
Haibin Wang and
Yaliang Li and
Xiuyu Sun and
Yichen Qian and
Bolin Ding and
Jingren Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L73-L119) <br>```Evaluate Prompt Engnieering, In-context learning and SFT
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```pvldb-GaoWLSQDZ24```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.01117)<a href="https://scholar.google.com.hk/scholar?q=DTS-SQL:+Decomposed+Text-to-SQL+with+Small+Large+Language+Models"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**DTS-SQL: Decomposed Text-to-SQL with Small Large Language Models**](https://doi.org/10.48550/arXiv.2402.01117) , <br> by *Mohammadreza Pourreza and
Davood Rafiei* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L123-L158) <br>```Two-stage SFT, 1) Schema Linking, 2) SQL Generation.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-2402-01117```
- <a href="https://scholar.google.com.hk/scholar?q=SFT+for+Improved+Text-to-SQL+Translation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **SFT for Improved Text-to-SQL Translation**, <br> by *Ojha, Puneet Kumar, Gautam, Abhishek, Agrahari, Ankit and Singh, Parikshit* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L162-L181) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```ojha2024sft```
- <a href="https://scholar.google.com.hk/scholar?q=Dubo-SQL:+Diverse+Retrieval-Augmented+Generation+and+Fine+Tuning+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **Dubo-SQL: Diverse Retrieval-Augmented Generation and Fine Tuning for Text-to-SQL**, <br> by *Thorpe, Dayton G, Duberstein, Andrew J and Kinsey, Ian A* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L275-L294) <br>```v1: SFT + gpt3.5, v2: RAG from training set, ICL + GPT-4. 1: 'We find the LLM learns more from the few-shot examples if we include the questions as user messages and the answers as assistant messages in the conversation history.' 2: 'the output in JSON format improves execution accuracy.'
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```thorpe2024dubo```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L366-L411) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
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
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L366-L411) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
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
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L366-L411) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Retrieval-augmented Generation

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.14851)<a href="https://scholar.google.com.hk/scholar?q=SQL-CRAFT:+Text-to-SQL+through+Interactive+Refinement+and+Enhanced+Reasoning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SQL-CRAFT: Text-to-SQL through Interactive Refinement and Enhanced
Reasoning**](https://doi.org/10.48550/arXiv.2402.14851) , <br> by *Hanchen Xia and
Feng Jiang and
Naihao Deng and
Cunxiang Wang and
Guojiang Zhao and
Rada Mihalcea and
Yue Zhang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L238-L272) <br>```1: simultaneously generate python and sql; 2: first generate python and then genearte SQL. The loop terminates when the program detects that the model has generated the same SQL again.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-14851```
- <a href="https://scholar.google.com.hk/scholar?q=Dubo-SQL:+Diverse+Retrieval-Augmented+Generation+and+Fine+Tuning+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **Dubo-SQL: Diverse Retrieval-Augmented Generation and Fine Tuning for Text-to-SQL**, <br> by *Thorpe, Dayton G, Duberstein, Andrew J and Kinsey, Ian A* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L275-L294) <br>```v1: SFT + gpt3.5, v2: RAG from training set, ICL + GPT-4. 1: 'We find the LLM learns more from the few-shot examples if we include the questions as user messages and the answers as assistant messages in the conversation history.' 2: 'the output in JSON format improves execution accuracy.'
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```thorpe2024dubo```
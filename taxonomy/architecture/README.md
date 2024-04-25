# Text-to-SQL Literature 
This repository is maintained by [Yongrui Chen](). Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). 
The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

You can directly use our bibtex.bib in overleaf with this [link]().

This page categorizes the literature by the **Dataset**

## Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#hyperlink)
- [![](https://img.shields.io/badge/BIRD-2-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#bird)
- [![](https://img.shields.io/badge/BigTable_0.2k-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#bigtable-0.2k)
- [![](https://img.shields.io/badge/Dr.Spider-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#dr.spider)
- [![](https://img.shields.io/badge/Spider-7-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#spider)
- [![](https://img.shields.io/badge/Spider_DK-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#spider-dk)
- [![](https://img.shields.io/badge/Spider_Realistic-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#spider-realistic)
- [![](https://img.shields.io/badge/Spider_Syn-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#spider-syn)
- [![](https://img.shields.io/badge/WikiSQL-5-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#wikisql)
## Hyperlink 
- [[Overview]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/README.md) -- [Homepage](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/README.md)
-  -- [Summary](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./)
-  -- [Model Architecture](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/architecture)
-  -- [Conference](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/conference)
-  -- [Dataset](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/dataset)
-  -- [SQL Generation Framework](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/framework)
-  -- [Intermedia Representation](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/intermedia)
-  -- [Journal](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/journal)
-  -- [Large Language Model](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/llm)
-  -- [Metric](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/metric)
-  -- [Paper Type](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/paper_type)
-  -- [ Learning Paradigm](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/paradigm)
-  -- [Preprint](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/preprint)
-  -- [Application Scenario](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scenario)
-  -- [Task](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/task)
-  -- [LLM Technique](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/technique)

## BIRD

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L96-L140) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
- [![](https://img.shields.io/badge/NeurIPS_2023-2023-blue)](http://papers.nips.cc/paper\_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html)<a href="https://scholar.google.com.hk/scholar?q=DIN-SQL:+Decomposed+In-Context+Learning+of+Text-to-SQL+with+Self-Correction"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction**](http://papers.nips.cc/paper\_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html) , <br> by *Mohammadreza Pourreza and
Davood Rafiei* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L144-L176) <br>```First construct a pipeline to split text-to-SQL into multiple subtasks, then leverage in-context learning to handle each subtask. Classify the example into three forms: simple, nested complex and non-nested complex.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-nips-PourrezaR23```
## BigTable-0.2k

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2403.02951)<a href="https://scholar.google.com.hk/scholar?q=Benchmarking+the+Text-to-SQL+Capability+of+Large+Language+Models:+A+Comprehensive+Evaluation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Benchmarking the Text-to-SQL Capability of Large Language Models:
A Comprehensive Evaluation**](https://doi.org/10.48550/arXiv.2403.02951) , <br> by *Bin Zhang and
Yuxiao Ye and
Guoqing Du and
Xiaoru Hu and
Zhishuai Li and
Sun Yang and
Chi Harold Liu and
Rui Zhao and
Ziyue Li and
Hangyu Mao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L179-L228) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-02951```
## Dr.Spider

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L96-L140) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Spider

- <a href="https://scholar.google.com.hk/scholar?q=Dubo-SQL:+Diverse+Retrieval-Augmented+Generation+and+Fine+Tuning+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **Dubo-SQL: Diverse Retrieval-Augmented Generation and Fine Tuning for Text-to-SQL**, <br> by *Thorpe, Dayton G, Duberstein, Andrew J and Kinsey, Ian A* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L8-L26) <br>```v1: SFT + gpt3.5, v2: RAG from training set, ICL + GPT-4. 1: 'We find the LLM learns more from the few-shot examples if we include the questions as user messages and the answers as assistant messages in the conversation history.' 2: 'the output in JSON format improves execution accuracy.'
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```thorpe2024dubo```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2403.09706)<a href="https://scholar.google.com.hk/scholar?q=Schema-Aware+Multi-Task+Learning+for+Complex+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Schema-Aware Multi-Task Learning for Complex Text-to-SQL**](https://doi.org/10.48550/arXiv.2403.09706) , <br> by *Yangjun Wu and
Han Wang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L29-L56) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-09706```
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
Hangyu Mao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L58-L93) <br>```PET-SQL, Two-stage pure prompt method, retrieve domain-agnostic examples, voting for curation
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
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L96-L140) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
- [![](https://img.shields.io/badge/NeurIPS_2023-2023-blue)](http://papers.nips.cc/paper\_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html)<a href="https://scholar.google.com.hk/scholar?q=DIN-SQL:+Decomposed+In-Context+Learning+of+Text-to-SQL+with+Self-Correction"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction**](http://papers.nips.cc/paper\_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html) , <br> by *Mohammadreza Pourreza and
Davood Rafiei* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L144-L176) <br>```First construct a pipeline to split text-to-SQL into multiple subtasks, then leverage in-context learning to handle each subtask. Classify the example into three forms: simple, nested complex and non-nested complex.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-nips-PourrezaR23```
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.29)<a href="https://scholar.google.com.hk/scholar?q=SmBoP:+Semi-autoregressive+Bottom-up+Semantic+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SmBoP: Semi-autoregressive Bottom-up Semantic Parsing**](https://doi.org/10.18653/v1/2021.naacl-main.29) , <br> by *Ohad Rubin and
Jonathan Berant* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L844-L876) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-naacl-RubinB21```
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://www.aclweb.org/anthology/2020.acl-main.677/)<a href="https://scholar.google.com.hk/scholar?q=RAT-SQL:+Relation-Aware+Schema+Encoding+and+Linking+for+Text-to-SQL+Parsers"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers**](https://www.aclweb.org/anthology/2020.acl-main.677/) , <br> by *Bailin Wang and
Richard Shin and
Xiaodong Liu and
Oleksandr Polozov and
Matthew Richardson* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L230-L250) <br>```Joint Encoding of Question and Schema
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```WangSLPR20```
## Spider-DK

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L96-L140) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Spider-Realistic

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L96-L140) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## Spider-Syn

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.16347)<a href="https://scholar.google.com.hk/scholar?q=CodeS:+Towards+Building+Open-source+Language+Models+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CodeS: Towards Building Open-source Language Models for Text-to-SQL**](https://doi.org/10.48550/arXiv.2402.16347) , <br> by *Haoyang Li and
Jing Zhang and
Hanbing Liu and
Ju Fan and
Xiaokang Zhang and
Jun Zhu and
Renjie Wei and
Hongyan Pan and
Cuiping Li and
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L96-L140) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
## WikiSQL

- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://aaai.org/ojs/index.php/AAAI/article/view/6246)<a href="https://scholar.google.com.hk/scholar?q=Zero-Shot+Text-to-SQL+Learning+with+Auxiliary+Task"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Zero-Shot Text-to-SQL Learning with Auxiliary Task**](https://aaai.org/ojs/index.php/AAAI/article/view/6246) , <br> by *Shuaichen Chang and
Pengfei Liu and
Yun Tang and
Jing Huang and
Xiaodong He and
Bowen Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L375-L404) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```ChangLT0HZ20```
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1902.01069)<a href="https://scholar.google.com.hk/scholar?q=A+Comprehensive+Exploration+on+WikiSQL+with+Table-Aware+Word+Contextualization"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**A Comprehensive Exploration on WikiSQL with Table-Aware Word Contextualization**](http://arxiv.org/abs/1902.01069) , <br> by *Wonseok Hwang and
Jinyeung Yim and
Seunghyun Park and
Minjoon Seo* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L317-L343) <br>```Propose Sketch framework to generate SQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-1902-01069```
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1908.08113)<a href="https://scholar.google.com.hk/scholar?q=X-SQL:+reinforce+schema+representation+with+context"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**X-SQL: reinforce schema representation with context**](http://arxiv.org/abs/1908.08113) , <br> by *Pengcheng He and
Yi Mao and
Kaushik Chakrabarti and
Weizhu Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L346-L373) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-1908-08113```
- [![](https://img.shields.io/badge/NAACL-2018-blue)](https://doi.org/10.18653/v1/n18-2115)<a href="https://scholar.google.com.hk/scholar?q=Natural+Language+to+Structured+Query+Generation+via+Meta-Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Natural Language to Structured Query Generation via Meta-Learning**](https://doi.org/10.18653/v1/n18-2115) , <br> by *Po{-}Sen Huang and
Chenglong Wang and
Rishabh Singh and
Wen{-}tau Yih and
Xiaodong He* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L283-L314) <br>```The first application of meta-learning to text-to-SQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```HuangWSYH18```
- [![](https://img.shields.io/badge/CoRR-2017-blue)](http://arxiv.org/abs/1709.00103)<a href="https://scholar.google.com.hk/scholar?q=Seq2SQL:+Generating+Structured+Queries+from+Natural+Language+using+Reinforcement+Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Seq2SQL: Generating Structured Queries from Natural Language using
Reinforcement Learning**](http://arxiv.org/abs/1709.00103) , <br> by *Victor Zhong and
Caiming Xiong and
Richard Socher* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L253-L280) <br>```Propose WikiSQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-1709-00103```
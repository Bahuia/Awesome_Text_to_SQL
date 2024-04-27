# Text-to-SQL Literature 
This repository is maintained by [Yongrui Chen](). Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). 
The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

You can directly use our bibtex.bib in overleaf with this [link]().

This page categorizes the literature by the **Model Architecture**.

## Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#hyperlink)
- [![](https://img.shields.io/badge/Transformer-6-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#transformer)
- [![](https://img.shields.io/badge/LSTM-3-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/architecture/README.md#lstm)
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

## Transformer

- [![](https://img.shields.io/badge/VLDB-2024-blue)](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf)<a href="https://scholar.google.com.hk/scholar?q=Text-to-SQL+Empowered+by+Large+Language+Models:+A+Benchmark+Evaluation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation**](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf) , <br> by *Dawei Gao and
Haibin Wang and
Yaliang Li and
Xiuyu Sun and
Yichen Qian and
Bolin Ding and
Jingren Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L8-L54) <br>```Evaluate Prompt Engnieering, In-context learning and SFT
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```pvldb-GaoWLSQDZ24```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.01117)<a href="https://scholar.google.com.hk/scholar?q=DTS-SQL:+Decomposed+Text-to-SQL+with+Small+Large+Language+Models"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**DTS-SQL: Decomposed Text-to-SQL with Small Large Language Models**](https://doi.org/10.48550/arXiv.2402.01117) , <br> by *Mohammadreza Pourreza and
Davood Rafiei* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L58-L93) <br>```Two-stage SFT, 1) Schema Linking, 2) SQL Generation.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-2402-01117```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.14851)<a href="https://scholar.google.com.hk/scholar?q=SQL-CRAFT:+Text-to-SQL+through+Interactive+Refinement+and+Enhanced+Reasoning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SQL-CRAFT: Text-to-SQL through Interactive Refinement and Enhanced
Reasoning**](https://doi.org/10.48550/arXiv.2402.14851) , <br> by *Hanchen Xia and
Feng Jiang and
Naihao Deng and
Cunxiang Wang and
Guojiang Zhao and
Rada Mihalcea and
Yue Zhang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L173-L207) <br>```1: simultaneously generate python and sql; 2: first generate python and then genearte SQL. The loop terminates when the program detects that the model has generated the same SQL again.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-14851```
- <a href="https://scholar.google.com.hk/scholar?q=Dubo-SQL:+Diverse+Retrieval-Augmented+Generation+and+Fine+Tuning+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **Dubo-SQL: Diverse Retrieval-Augmented Generation and Fine Tuning for Text-to-SQL**, <br> by *Thorpe, Dayton G, Duberstein, Andrew J and Kinsey, Ian A* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L210-L229) <br>```v1: SFT + gpt3.5, v2: RAG from training set, ICL + GPT-4. 1: 'We find the LLM learns more from the few-shot examples if we include the questions as user messages and the answers as assistant messages in the conversation history.' 2: 'the output in JSON format improves execution accuracy.'
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```thorpe2024dubo```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2403.09706)<a href="https://scholar.google.com.hk/scholar?q=Schema-Aware+Multi-Task+Learning+for+Complex+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Schema-Aware Multi-Task Learning for Complex Text-to-SQL**](https://doi.org/10.48550/arXiv.2403.09706) , <br> by *Yangjun Wu and
Han Wang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L232-L260) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-09706```
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1908.08113)<a href="https://scholar.google.com.hk/scholar?q=X-SQL:+reinforce+schema+representation+with+context"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**X-SQL: reinforce schema representation with context**](http://arxiv.org/abs/1908.08113) , <br> by *Pengcheng He and
Yi Mao and
Kaushik Chakrabarti and
Weizhu Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L554-L581) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-1908-08113```
## LSTM

- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://aaai.org/ojs/index.php/AAAI/article/view/6246)<a href="https://scholar.google.com.hk/scholar?q=Zero-Shot+Text-to-SQL+Learning+with+Auxiliary+Task"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Zero-Shot Text-to-SQL Learning with Auxiliary Task**](https://aaai.org/ojs/index.php/AAAI/article/view/6246) , <br> by *Shuaichen Chang and
Pengfei Liu and
Yun Tang and
Jing Huang and
Xiaodong He and
Bowen Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L583-L612) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```ChangLT0HZ20```
- [![](https://img.shields.io/badge/NAACL-2018-blue)](https://doi.org/10.18653/v1/n18-2115)<a href="https://scholar.google.com.hk/scholar?q=Natural+Language+to+Structured+Query+Generation+via+Meta-Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Natural Language to Structured Query Generation via Meta-Learning**](https://doi.org/10.18653/v1/n18-2115) , <br> by *Po{-}Sen Huang and
Chenglong Wang and
Rishabh Singh and
Wen{-}tau Yih and
Xiaodong He* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L491-L522) <br>```The first application of meta-learning to text-to-SQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```HuangWSYH18```
- [![](https://img.shields.io/badge/CoRR-2017-blue)](http://arxiv.org/abs/1709.00103)<a href="https://scholar.google.com.hk/scholar?q=Seq2SQL:+Generating+Structured+Queries+from+Natural+Language+using+Reinforcement+Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Seq2SQL: Generating Structured Queries from Natural Language using
Reinforcement Learning**](http://arxiv.org/abs/1709.00103) , <br> by *Victor Zhong and
Caiming Xiong and
Richard Socher* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L461-L488) <br>```Propose WikiSQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-1709-00103```
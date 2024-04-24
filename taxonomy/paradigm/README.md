# Text-to-SQL Literature 
This repository is maintained by [Yongrui Chen](). Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). 
The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

You can directly use our bibtex.bib in overleaf with this [link]().

This page categorizes the literature by the **Model Architecture**

## Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/paradigm/README.md#hyperlink)
- [![](https://img.shields.io/badge/LSTM-3-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/paradigm/README.md#lstm)
- [![](https://img.shields.io/badge/Transformer-1-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/taxonomy/paradigm/README.md#transformer)
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

## LSTM

- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://aaai.org/ojs/index.php/AAAI/article/view/6246)<a href="https://scholar.google.com.hk/scholar?q=Zero-Shot+Text-to-SQL+Learning+with+Auxiliary+Task"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Zero-Shot Text-to-SQL Learning with Auxiliary Task**](https://aaai.org/ojs/index.php/AAAI/article/view/6246) , <br> by *Shuaichen Chang and
Pengfei Liu and
Yun Tang and
Jing Huang and
Xiaodong He and
Bowen Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L229-L258) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```ChangLT0HZ20```
- [![](https://img.shields.io/badge/NAACL-2018-blue)](https://doi.org/10.18653/v1/n18-2115)<a href="https://scholar.google.com.hk/scholar?q=Natural+Language+to+Structured+Query+Generation+via+Meta-Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Natural Language to Structured Query Generation via Meta-Learning**](https://doi.org/10.18653/v1/n18-2115) , <br> by *Po{-}Sen Huang and
Chenglong Wang and
Rishabh Singh and
Wen{-}tau Yih and
Xiaodong He* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L137-L168) <br>```The first application of meta-learning to text-to-SQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```HuangWSYH18```
- [![](https://img.shields.io/badge/CoRR-2017-blue)](http://arxiv.org/abs/1709.00103)<a href="https://scholar.google.com.hk/scholar?q=Seq2SQL:+Generating+Structured+Queries+from+Natural+Language+using+Reinforcement+Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Seq2SQL: Generating Structured Queries from Natural Language using
Reinforcement Learning**](http://arxiv.org/abs/1709.00103) , <br> by *Victor Zhong and
Caiming Xiong and
Richard Socher* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L107-L134) <br>```Propose WikiSQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-1709-00103```
## Transformer

- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1908.08113)<a href="https://scholar.google.com.hk/scholar?q=X-SQL:+reinforce+schema+representation+with+context"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**X-SQL: reinforce schema representation with context**](http://arxiv.org/abs/1908.08113) , <br> by *Pengcheng He and
Yi Mao and
Kaushik Chakrabarti and
Weizhu Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./bibtex.bib#L200-L227) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals/corr/abs-1908-08113```
# Text-to-SQL Literature 
This repository is maintained by [Yongrui Chen](). Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). 
The automation script of this repo is powered by [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).

You can directly use our bibtex.bib in overleaf with this [link]().

This page categorizes the literature by the **Paper Type**.

## Outline 
- [![](https://img.shields.io/badge/Hyperlink-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./../README.md#hyperlink)
- [![](https://img.shields.io/badge/Benchmark-3-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./../README.md#benchmark)
- [![](https://img.shields.io/badge/Method-39-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./../README.md#method)
- [![](https://img.shields.io/badge/Evaluation-3-blue)](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/./../README.md#evaluation)
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

## Benchmark

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2403.15879)<a href="https://scholar.google.com.hk/scholar?q=TrustSQL:+A+Reliability+Benchmark+for+Text-to-SQL+Models+with+Diverse+Unanswerable+Questions"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**TrustSQL: A Reliability Benchmark for Text-to-SQL Models with Diverse
Unanswerable Questions**](https://doi.org/10.48550/arXiv.2403.15879) , <br> by *Gyubok Lee and
Woosog Chay and
Seonhee Cho and
Edward Choi* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L298-L328) <br>```Trust-SQL requires models to provide one of two outputs: 1) an SQL prediction or 2) abstention from making an SQL prediction, either due to potential errors in the generated SQL or when faced with unanswerable questions.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-15879```
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
Hangyu Mao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L566-L616) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-02951```
- [![](https://img.shields.io/badge/CoRR-2017-blue)](http://arxiv.org/abs/1709.00103)<a href="https://scholar.google.com.hk/scholar?q=Seq2SQL:+Generating+Structured+Queries+from+Natural+Language+using+Reinforcement+Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Seq2SQL: Generating Structured Queries from Natural Language using
Reinforcement Learning**](http://arxiv.org/abs/1709.00103) , <br> by *Victor Zhong and
Caiming Xiong and
Richard Socher* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L641-L668) <br>```Propose WikiSQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-1709-00103```
## Method

- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2405.15307)<a href="https://scholar.google.com.hk/scholar?q=Before+Generation,+Align+it!+A+Novel+and+Effective+Strategy+for+Mitigating+Hallucinations+in+Text-to-SQL+Generation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Before Generation, Align it! A Novel and Effective Strategy for
Mitigating Hallucinations in Text-to-SQL Generation**](https://doi.org/10.48550/arXiv.2405.15307) , <br> by *Ge Qu and
Jinyang Li and
Bowen Li and
Bowen Qin and
Nan Huo and
Chenhao Ma and
Reynold Cheng* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L8-L46) <br>```two stages: 1)schema linking: first generating a dummy SQL query and then extracting related schema entities from it as the final output. 2)logical synthesis: based on the extracted entities, replace the traditional panda API functions with SQL keyword-like symbolic functions, then generate accurate SQL queries.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-2405-15307```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2405.02712)<a href="https://scholar.google.com.hk/scholar?q=CoE-SQL:+In-Context+Learning+for+Multi-Turn+Text-to-SQL+with+Chain-of-Editions"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**CoE-SQL: In-Context Learning for Multi-Turn Text-to-SQL with Chain-of-Editions**](https://doi.org/10.48550/arXiv.2405.02712) , <br> by *Hanchong Zhang and
Ruisheng Cao and
Hongshen Xu and
Lu Chen and
Kai Yu* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L50-L82) <br>```If a question has a high structural similarity to the previous questions, the current SQL query can be generated by updating the previous ones through a few editions.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-2405-02712```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.11517)<a href="https://scholar.google.com.hk/scholar?q=Knowledge-to-SQL:+Enhancing+SQL+Generation+with+Data+Expert+LLM"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Knowledge-to-SQL: Enhancing SQL Generation with Data Expert LLM**](https://doi.org/10.48550/arXiv.2402.11517) , <br> by *Zijin Hong and
Zheng Yuan and
Hao Chen and
Qinggang Zhang and
Feiran Huang and
Xiao Huang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L86-L119) <br>```propose a knowledge-to-text framework (SFT + RLHF), to generate the text knowledge by performing sft on llms. The gold knowledge is annotated by humans (from evidence of BIRD). Then, use RL with DB/SQL feedbace to further train the expert llm.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-2402-11517```
- [![](https://img.shields.io/badge/COLING-2024-blue)](https://aclanthology.org/2024.lrec-main.539)<a href="https://scholar.google.com.hk/scholar?q=Enhancing+Text-to-SQL+Capabilities+of+Large+Language+Models+through+Tailored+Promptings"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Enhancing Text-to-SQL Capabilities of Large Language Models through
Tailored Promptings**](https://aclanthology.org/2024.lrec-main.539) , <br> by *Zhao Tan and
Xiping Liu and
Qing Shu and
Xi Li and
Changxuan Wan and
Dexi Liu and
Qizhi Wan and
Guoqiong Liao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L123-L164) <br>```three prompts: 1) Prompting for Schema Linking. 2) Prompting for SQL Generation. 3) Combining Promptings. Finally, result selection prompt based on self-consistency.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```TanLSLWLWL24```
- <a href="https://scholar.google.com.hk/scholar?q=SQL-to-Schema+Enhances+Schema+Linking+in+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **SQL-to-Schema Enhances Schema Linking in Text-to-SQL**, <br> by *Yang, Sun, Su, Qiong, Li, Zhishuai, Li, Ziyue, Mao, Hangyu, Liu, Chenxi and Zhao, Rui* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L167-L184) <br>```three stage: 1) generate an initial SQL query by utilizing the complete database schema. 2) extract tables and columns from the initial SQL query to create a concise schema. 3) generate the final sql.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```yang2024sql```
- [![](https://img.shields.io/badge/VLDB-2024-blue)](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf)<a href="https://scholar.google.com.hk/scholar?q=Text-to-SQL+Empowered+by+Large+Language+Models:+A+Benchmark+Evaluation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation**](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf) , <br> by *Dawei Gao and
Haibin Wang and
Yaliang Li and
Xiuyu Sun and
Yichen Qian and
Bolin Ding and
Jingren Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L188-L234) <br>```Evaluate Prompt Engnieering, In-context learning and SFT
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```pvldb-GaoWLSQDZ24```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.01117)<a href="https://scholar.google.com.hk/scholar?q=DTS-SQL:+Decomposed+Text-to-SQL+with+Small+Large+Language+Models"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**DTS-SQL: Decomposed Text-to-SQL with Small Large Language Models**](https://doi.org/10.48550/arXiv.2402.01117) , <br> by *Mohammadreza Pourreza and
Davood Rafiei* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L238-L273) <br>```Two-stage SFT, 1) Schema Linking, 2) SQL Generation.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-2402-01117```
- <a href="https://scholar.google.com.hk/scholar?q=SFT+for+Improved+Text-to-SQL+Translation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **SFT for Improved Text-to-SQL Translation**, <br> by *Ojha, Puneet Kumar, Gautam, Abhishek, Agrahari, Ankit and Singh, Parikshit* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L277-L296) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```ojha2024sft```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2402.14851)<a href="https://scholar.google.com.hk/scholar?q=SQL-CRAFT:+Text-to-SQL+through+Interactive+Refinement+and+Enhanced+Reasoning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SQL-CRAFT: Text-to-SQL through Interactive Refinement and Enhanced
Reasoning**](https://doi.org/10.48550/arXiv.2402.14851) , <br> by *Hanchen Xia and
Feng Jiang and
Naihao Deng and
Cunxiang Wang and
Guojiang Zhao and
Rada Mihalcea and
Yue Zhang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L353-L387) <br>```1: simultaneously generate python and sql; 2: first generate python and then genearte SQL. The loop terminates when the program detects that the model has generated the same SQL again.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-14851```
- <a href="https://scholar.google.com.hk/scholar?q=Dubo-SQL:+Diverse+Retrieval-Augmented+Generation+and+Fine+Tuning+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> **Dubo-SQL: Diverse Retrieval-Augmented Generation and Fine Tuning for Text-to-SQL**, <br> by *Thorpe, Dayton G, Duberstein, Andrew J and Kinsey, Ian A* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L390-L409) <br>```v1: SFT + gpt3.5, v2: RAG from training set, ICL + GPT-4. 1: 'We find the LLM learns more from the few-shot examples if we include the questions as user messages and the answers as assistant messages in the conversation history.' 2: 'the output in JSON format improves execution accuracy.'
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```thorpe2024dubo```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://doi.org/10.48550/arXiv.2403.09706)<a href="https://scholar.google.com.hk/scholar?q=Schema-Aware+Multi-Task+Learning+for+Complex+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Schema-Aware Multi-Task Learning for Complex Text-to-SQL**](https://doi.org/10.48550/arXiv.2403.09706) , <br> by *Yangjun Wu and
Han Wang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L412-L440) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2403-09706```
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
Hangyu Mao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L442-L478) <br>```PET-SQL, Two-stage pure prompt method, retrieve domain-agnostic examples, voting for curation
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
Hong Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L481-L526) <br>```Propose CodeS, a LLM for text-to-SQL. 1. Use two direction data augmentation: SQL->Text, Text->SQL; 2. Construct prompts of database metadata with a coarse filtering and matching; 3. Further Pretraining
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2402-16347```
- [![](https://img.shields.io/badge/NeurIPS_2023-2023-blue)](http://papers.nips.cc/paper\_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html)<a href="https://scholar.google.com.hk/scholar?q=DIN-SQL:+Decomposed+In-Context+Learning+of+Text-to-SQL+with+Self-Correction"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction**](http://papers.nips.cc/paper\_files/paper/2023/hash/72223cc66f63ca1aa59edaec1b3670e6-Abstract-Conference.html) , <br> by *Mohammadreza Pourreza and
Davood Rafiei* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L530-L563) <br>```First construct a pipeline to split text-to-SQL into multiple subtasks, then leverage in-context learning to handle each subtask. Classify the example into three forms: simple, nested complex and non-nested complex.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-nips-PourrezaR23```
- [![](https://img.shields.io/badge/ICLR-2021-blue)](https://openreview.net/forum?id=kyaIeYj4zZ)<a href="https://scholar.google.com.hk/scholar?q=GraPPa:+Grammar-Augmented+Pre-Training+for+Table+Semantic+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**GraPPa: Grammar-Augmented Pre-Training for Table Semantic Parsing**](https://openreview.net/forum?id=kyaIeYj4zZ) , <br> by *Tao Yu and
Chien{-}Sheng Wu and
Xi Victoria Lin and
Bailin Wang and
Yi Chern Tan and
Xinyi Yang and
Dragomir R. Radev and
Richard Socher and
Caiming Xiong* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L819-L840) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-iclr-0009WLWTYRSX21```
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2103.04399)<a href="https://scholar.google.com.hk/scholar?q=Improving+Text-to-SQL+with+Schema+Dependency+Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Improving Text-to-SQL with Schema Dependency Learning**](https://arxiv.org/abs/2103.04399) , <br> by *Binyuan Hui and
Xiang Shi and
Ruiying Geng and
Binhua Li and
Yongbin Li and
Jian Sun and
Xiaodan Zhu* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L864-L885) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2103-04399```
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.105)<a href="https://scholar.google.com.hk/scholar?q=Structure-Grounded+Pretraining+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Structure-Grounded Pretraining for Text-to-SQL**](https://doi.org/10.18653/v1/2021.naacl-main.105) , <br> by *Xiang Deng and
Ahmed Hassan Awadallah and
Christopher Meek and
Oleksandr Polozov and
Huan Sun and
Matthew Richardson* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L887-L916) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-naacl-DengAMPSR21```
- [![](https://img.shields.io/badge/AAAI-2021-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/16519)<a href="https://scholar.google.com.hk/scholar?q=Leveraging+Table+Content+for+Zero-shot+Text-to-SQL+with+Meta-Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Leveraging Table Content for Zero-shot Text-to-SQL with Meta-Learning**](https://ojs.aaai.org/index.php/AAAI/article/view/16519) , <br> by *Yongrui Chen and
Xinnan Guo and
Chaojie Wang and
Jian Qiu and
Guilin Qi and
Meng Wang and
Huiying Li* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L968-L989) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-aaai-ChenG0QQWL21```
- [![](https://img.shields.io/badge/CoRR-2021-blue)](https://arxiv.org/abs/2101.09901)<a href="https://scholar.google.com.hk/scholar?q=GP:+Context-free+Grammar+Pre-training+for+Text-to-SQL+Parsers"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**GP: Context-free Grammar Pre-training for Text-to-SQL Parsers**](https://arxiv.org/abs/2101.09901) , <br> by *Liang Zhao and
Hexin Cao and
Yunsong Zhao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1134-L1151) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2101-09901```
- [![](https://img.shields.io/badge/AAAI-2021-blue)](https://ojs.aaai.org/index.php/AAAI/article/view/17627)<a href="https://scholar.google.com.hk/scholar?q=Learning+Contextual+Representations+for+Semantic+Parsing+with+Generation-Augmented+Pre-Training"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Learning Contextual Representations for Semantic Parsing with Generation-Augmented
Pre-Training**](https://ojs.aaai.org/index.php/AAAI/article/view/17627) , <br> by *Peng Shi and
Patrick Ng and
Zhiguo Wang and
Henghui Zhu and
Alexander Hanbo Li and
Jun Wang and
C{\'{\i}}cero Nogueira dos Santos and
Bing Xiang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1153-L1175) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-aaai-ShiNWZLWSX21```
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.198)<a href="https://scholar.google.com.hk/scholar?q=LGESQL:+Line+Graph+Enhanced+Text-to-SQL+Model+with+Mixed+Local+and+Non-Local+Relations"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**LGESQL: Line Graph Enhanced Text-to-SQL Model with Mixed Local and
Non-Local Relations**](https://doi.org/10.18653/v1/2021.acl-long.198) , <br> by *Ruisheng Cao and
Lu Chen and
Zhi Chen and
Yanbin Zhao and
Su Zhu and
Kai Yu* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1177-L1202) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-CaoC0ZZ020```
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.33)<a href="https://scholar.google.com.hk/scholar?q=Meta-Learning+for+Domain+Generalization+in+Semantic+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Meta-Learning for Domain Generalization in Semantic Parsing**](https://doi.org/10.18653/v1/2021.naacl-main.33) , <br> by *Bailin Wang and
Mirella Lapata and
Ivan Titov* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1204-L1230) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-naacl-WangLT21```
- [![](https://img.shields.io/badge/ACL-2021-blue)](https://doi.org/10.18653/v1/2021.acl-long.163)<a href="https://scholar.google.com.hk/scholar?q=Optimizing+Deeper+Transformer+on+Small+Datasets"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Optimizing Deeper Transformer on Small Datasets**](https://doi.org/10.18653/v1/2021.acl-long.163) , <br> by *Peng Xu and
Dhruv Kumar and
Wei Yang and
Wenjie Zi and
Keyi Tang and
Chenyang Huang and
Jackie Chi Kit Cheung and
Simon J. D. Prince and
Yanshuai Cao* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1232-L1259) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-Xu0YZT0CPC20```
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.441)<a href="https://scholar.google.com.hk/scholar?q=ShadowGNN:+Graph+Projection+Neural+Network+for+Text-to-SQL+Parser"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**ShadowGNN: Graph Projection Neural Network for Text-to-SQL Parser**](https://doi.org/10.18653/v1/2021.naacl-main.441) , <br> by *Zhi Chen and
Lu Chen and
Yanbin Zhao and
Ruisheng Cao and
Zihan Xu and
Su Zhu and
Kai Yu* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1261-L1291) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-naacl-ChenCZCXZY21```
- [![](https://img.shields.io/badge/NAACL-2021-blue)](https://doi.org/10.18653/v1/2021.naacl-main.29)<a href="https://scholar.google.com.hk/scholar?q=SmBoP:+Semi-autoregressive+Bottom-up+Semantic+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SmBoP: Semi-autoregressive Bottom-up Semantic Parsing**](https://doi.org/10.18653/v1/2021.naacl-main.29) , <br> by *Ohad Rubin and
Jonathan Berant* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1293-L1325) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-naacl-RubinB21```
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://www.aclweb.org/anthology/2020.acl-main.677/)<a href="https://scholar.google.com.hk/scholar?q=RAT-SQL:+Relation-Aware+Schema+Encoding+and+Linking+for+Text-to-SQL+Parsers"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**RAT-SQL: Relation-Aware Schema Encoding and Linking for Text-to-SQL Parsers**](https://www.aclweb.org/anthology/2020.acl-main.677/) , <br> by *Bailin Wang and
Richard Shin and
Xiaodong Liu and
Oleksandr Polozov and
Matthew Richardson* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L618-L638) <br>```Joint Encoding of Question and Schema
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```WangSLPR20```
- [![](https://img.shields.io/badge/AAAI-2020-blue)](https://aaai.org/ojs/index.php/AAAI/article/view/6246)<a href="https://scholar.google.com.hk/scholar?q=Zero-Shot+Text-to-SQL+Learning+with+Auxiliary+Task"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Zero-Shot Text-to-SQL Learning with Auxiliary Task**](https://aaai.org/ojs/index.php/AAAI/article/view/6246) , <br> by *Shuaichen Chang and
Pengfei Liu and
Yun Tang and
Jing Huang and
Xiaodong He and
Bowen Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L763-L792) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```ChangLT0HZ20```
- [![](https://img.shields.io/badge/EMNLP_findings-2020-blue)](https://doi.org/10.18653/v1/2020.findings-emnlp.438)<a href="https://scholar.google.com.hk/scholar?q=Bridging+Textual+and+Tabular+Data+for+Cross-Domain+Text-to-SQL+Semantic+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Bridging Textual and Tabular Data for Cross-Domain Text-to-SQL Semantic
Parsing**](https://doi.org/10.18653/v1/2020.findings-emnlp.438) , <br> by *Xi Victoria Lin and
Richard Socher and
Caiming Xiong* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L794-L817) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-emnlp-LinSX20```
- [![](https://img.shields.io/badge/CoRR-2020-blue)](https://arxiv.org/abs/2008.04759)<a href="https://scholar.google.com.hk/scholar?q=Hybrid+Ranking+Network+for+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Hybrid Ranking Network for Text-to-SQL**](https://arxiv.org/abs/2008.04759) , <br> by *Qin Lyu and
Kaushik Chakrabarti and
Shobhit Hathi and
Souvik Kundu and
Jianwen Zhang and
Zheng Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L842-L862) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-2008-04759```
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.745)<a href="https://scholar.google.com.hk/scholar?q=TaBERT:+Pretraining+for+Joint+Understanding+of+Textual+and+Tabular+Data"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**TaBERT: Pretraining for Joint Understanding of Textual and Tabular
Data**](https://doi.org/10.18653/v1/2020.acl-main.745) , <br> by *Pengcheng Yin and
Graham Neubig and
Wen{-}tau Yih and
Sebastian Riedel* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L918-L941) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-YinNYR20```
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.398)<a href="https://scholar.google.com.hk/scholar?q=TaPas:+Weakly+Supervised+Table+Parsing+via+Pre-training"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**TaPas: Weakly Supervised Table Parsing via Pre-training**](https://doi.org/10.18653/v1/2020.acl-main.398) , <br> by *Jonathan Herzig and
Pawel Krzysztof Nowak and
Thomas M{\"{u}}ller and
Francesco Piccinno and
Julian Martin Eisenschlos* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L943-L966) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-HerzigNMPE20```
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1902.01069)<a href="https://scholar.google.com.hk/scholar?q=A+Comprehensive+Exploration+on+WikiSQL+with+Table-Aware+Word+Contextualization"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**A Comprehensive Exploration on WikiSQL with Table-Aware Word Contextualization**](http://arxiv.org/abs/1902.01069) , <br> by *Wonseok Hwang and
Jinyeung Yim and
Seunghyun Park and
Minjoon Seo* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L705-L731) <br>```Propose Sketch framework to generate SQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```abs-1902-01069```
- [![](https://img.shields.io/badge/CoRR-2019-blue)](http://arxiv.org/abs/1908.08113)<a href="https://scholar.google.com.hk/scholar?q=X-SQL:+reinforce+schema+representation+with+context"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**X-SQL: reinforce schema representation with context**](http://arxiv.org/abs/1908.08113) , <br> by *Pengcheng He and
Yi Mao and
Kaushik Chakrabarti and
Weizhu Chen* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L734-L761) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-1908-08113```
- [![](https://img.shields.io/badge/ACL-2019-blue)](https://doi.org/10.18653/v1/p19-1448)<a href="https://scholar.google.com.hk/scholar?q=Representing+Schema+Structure+with+Graph+Neural+Networks+for+Text-to-SQL+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Representing Schema Structure with Graph Neural Networks for Text-to-SQL
Parsing**](https://doi.org/10.18653/v1/p19-1448) , <br> by *Ben Bogin and
Jonathan Berant and
Matt Gardner* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1059-L1080) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-BoginBG19```
- [![](https://img.shields.io/badge/ACL-2019-blue)](https://doi.org/10.18653/v1/p19-1444)<a href="https://scholar.google.com.hk/scholar?q=Towards+Complex+Text-to-SQL+in+Cross-Domain+Database+with+Intermediate+Representation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Towards Complex Text-to-SQL in Cross-Domain Database with Intermediate
Representation**](https://doi.org/10.18653/v1/p19-1444) , <br> by *Jiaqi Guo and
Zecheng Zhan and
Yan Gao and
Yan Xiao and
Jian{-}Guang Lou and
Ting Liu and
Dongmei Zhang* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1082-L1107) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-GuoZGXLLZ19```
- [![](https://img.shields.io/badge/NAACL-2018-blue)](https://doi.org/10.18653/v1/n18-2115)<a href="https://scholar.google.com.hk/scholar?q=Natural+Language+to+Structured+Query+Generation+via+Meta-Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Natural Language to Structured Query Generation via Meta-Learning**](https://doi.org/10.18653/v1/n18-2115) , <br> by *Po{-}Sen Huang and
Chenglong Wang and
Rishabh Singh and
Wen{-}tau Yih and
Xiaodong He* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L671-L702) <br>```The first application of meta-learning to text-to-SQL
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```HuangWSYH18```
- [![](https://img.shields.io/badge/CoRR-2018-blue)](http://arxiv.org/abs/1810.05237)<a href="https://scholar.google.com.hk/scholar?q=SyntaxSQLNet:+Syntax+Tree+Networks+for+Complex+and+Cross-DomainText-to-SQL+Task"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SyntaxSQLNet: Syntax Tree Networks for Complex and Cross-DomainText-to-SQL
Task**](http://arxiv.org/abs/1810.05237) , <br> by *Tao Yu and
Michihiro Yasunaga and
Kai Yang and
Rui Zhang and
Dongxu Wang and
Zifan Li and
Dragomir R. Radev* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1011-L1033) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-1810-05237```
- [![](https://img.shields.io/badge/NAACL-2018-blue)](https://doi.org/10.18653/v1/n18-2093)<a href="https://scholar.google.com.hk/scholar?q=TypeSQL:+Knowledge-Based+Type-Aware+Neural+Text-to-SQL+Generation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**TypeSQL: Knowledge-Based Type-Aware Neural Text-to-SQL Generation**](https://doi.org/10.18653/v1/n18-2093) , <br> by *Tao Yu and
Zifan Li and
Zilin Zhang and
Rui Zhang and
Dragomir R. Radev* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1035-L1057) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-naacl-YuLZZR18```
- [![](https://img.shields.io/badge/CoRR-2017-blue)](http://arxiv.org/abs/1711.04436)<a href="https://scholar.google.com.hk/scholar?q=SQLNet:+Generating+Structured+Queries+From+Natural+Language+Without+Reinforcement+Learning"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**SQLNet: Generating Structured Queries From Natural Language Without
Reinforcement Learning**](http://arxiv.org/abs/1711.04436) , <br> by *Xiaojun Xu and
Chang Liu and
Dawn Song* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L991-L1009) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```journals-corr-abs-1711-04436```
## Evaluation

- [![](https://img.shields.io/badge/VLDB-2024-blue)](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf)<a href="https://scholar.google.com.hk/scholar?q=Text-to-SQL+Empowered+by+Large+Language+Models:+A+Benchmark+Evaluation"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation**](https://www.vldb.org/pvldb/vol17/p1132-gao.pdf) , <br> by *Dawei Gao and
Haibin Wang and
Yaliang Li and
Xiuyu Sun and
Yichen Qian and
Bolin Ding and
Jingren Zhou* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L188-L234) <br>```Evaluate Prompt Engnieering, In-context learning and SFT
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```pvldb-GaoWLSQDZ24```
- [![](https://img.shields.io/badge/CoRR-2024-blue)](https://arxiv.org/abs/2404.02389)<a href="https://scholar.google.com.hk/scholar?q=On+Linearizing+Structured+Data+in+Encoder-Decoder+Language+Models:+Insights+from+Text-to-SQL"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**On Linearizing Structured Data in Encoder-Decoder Language Models: Insights from Text-to-SQL**](https://arxiv.org/abs/2404.02389) , <br> by *Shao, Yutong and Nakashole, Ndapa* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L331-L349) <br>```Coruption Study, encodings of structure nodes are predominantly 'ego-centric'.
```</details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```shao2024linearizing```
- [![](https://img.shields.io/badge/ACL-2020-blue)](https://doi.org/10.18653/v1/2020.acl-main.742)<a href="https://scholar.google.com.hk/scholar?q=Exploring+Unexplored+Generalization+Challenges+for+Cross-Database+Semantic+Parsing"><img src="https://img.shields.io/badge/-blue.svg?&logo=google-scholar&logoColor=white" height="18" align="bottom"></a> [**Exploring Unexplored Generalization Challenges for Cross-Database
Semantic Parsing**](https://doi.org/10.18653/v1/2020.acl-main.742) , <br> by *Alane Suhr and
Ming{-}Wei Chang and
Peter Shaw and
Kenton Lee* [[bib]](https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/../bibtex.bib#L1109-L1132) <br></details><details><summary><img src=https://github.com/bahuia/Awesome_Text_to_SQL/blob/master/scripts/svg/copy_icon.png height="20" align="bottom"></summary><pre>```conf-acl-SuhrCSL20```
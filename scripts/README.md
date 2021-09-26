# Auto-Bibfile
Auto-Bibfile is an automatic toolkit for README.md generation based on bibtex file.

## Quick Start
- Install: 
```pip install bibtexparser```
  
- Update the configuration in [scripts/config.py](https://github.com/wutong8023/Auto-Bibfile/blob/master/scripts/config.py).

- Add a new paper: 
paste a bib entry to [bibtex.bib](https://github.com/wutong8023/Auto-Bibfile/blob/master/bibtex.bib).

- Run: 
```python scripts/run.py```  (click [HERE](https://github.com/wutong8023/Auto-Bibfile/tree/master/your_topic4all) to see a demo.
)

- Categorize:
Add ```keywords``` to each entry and write down your note within ```@String()```. For example,

```latex
@inproceedings{WuLLHQZX21,
    author = {Tongtong Wu and
        Xuekai Li and
        Yuan{-}Fang Li and
        Gholamreza Haffari and
        Guilin Qi and
        Yujin Zhu and
        Guoqiang Xu},
    title = {Curriculum-Meta Learning for Order-Robust Continual Relation Extraction},
    booktitle = {Proceedings of AAAI},
    pages = {10363--10369},
    year = {2021},
    url = {https://ojs.aaai.org/index.php/AAAI/article/view/17241},
    keywords = {
        New Method,
        NLP,
        Supervised Learning,
        Relation Extraction,
        Rehearsal, Meta-learning,
        w/ External Knowledge,
        Class Incremental,
        Catastrophic Forgetting, Order Sensitivity,
        RNNs,
        Fewrel, SimpleQuestion, Tacred,
        Accuracy
    },
}
@String(WuLLHQZX21="Add a brief note behind the bib entry")
```

## Instruction
1. Update [bibtex.bib](https://github.com/wutong8023/Auto-Bibfile/blob/master/bibtex.bib): Auto-Bibfile will parse the keywords and meta-info of each entry.
2. The keywords **MUST** be predefined in [scripts/config.py # fined_taxonomy](https://github.com/wutong8023/Auto-Bibfile/tree/master/scripts/config.py#L20-L73), but feel free to update what you need.
3. Update [scripts/config.py](https://github.com/wutong8023/Auto-Bibfile/blob/master/scripts/config.py) for customization.

## How to Contribute
Please feel free to use and share [Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git). It would be great 
if you can mention it in your repository by adding:
> The automation script of this repo is powered by \[Auto-Bibfile\](https://github.com/wutong8023/Auto-Bibfile.git).

## Acknowledgement
This repository is developed and maintained by [Tongtong Wu](https://wutong8023.site). The automation script of this repo is partially adapted from [Automatic_Awesome_Bibliography](https://github.com/TLESORT/Automatic_Awesome_Bibliography).

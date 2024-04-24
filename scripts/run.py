from utils import generate_md_file
import bibtexparser
from config import *

file_name = 'bibtex.bib'
with open(file_name) as bibtex_file:
    bibtex_str = bibtex_file.read()
bib_db = bibtexparser.loads(bibtex_str, parser=bibtexparser.bparser.BibTexParser(ignore_nonstandard_types=False))


def check_repetition(DB=bib_db):
    bib_dict = {}
    for entry in DB.entries:
        title = entry["title"]
        title = str(title).strip()
        title = title.replace("{", "").replace("}", "")
        if title in bib_dict.keys():
            bib_dict[title] = bib_dict[title] + 1
        else:
            bib_dict[title] = 1
    repet_bib = [i for i in bib_dict.keys() if bib_dict[i] > 1]
    
    if len(repet_bib) != 0:
        print("Attention! Repetition detected in the bibtex file! Please check the following entries:")
        print("---------------------------")
    for i, title in enumerate(repet_bib):
        print(i + 1, title)


def plot_titles(titles):
    return '\n' + "## " + titles[0] + '\n'


def get_outline(list_classif, count_list, filename, dicrib, add_hyperlink=False):

    if filename.startswith("" + your_research_topic + "4nlp"):
        # str_outline = external_link
        str_outline = "# " + your_research_topic_full_name + " Literature in NLP \n"
    elif filename.startswith("" + your_research_topic + "4cv"):
        # str_outline = external_link
        str_outline = "# " + your_research_topic_full_name + " Literature in CV \n"
    else:
        # str_outline = external_link
        str_outline = "# " + your_research_topic_full_name + " Literature \n"

    str_outline += "This repository is maintained by [{author_info}]({personal_link}). " \
                   "Please don't hesitate to send me an email to collaborate or fix some entries (wutong8023 AT gmail.com). \n" \
                   "The automation script of this repo is powered by " \
                   "[Auto-Bibfile](https://github.com/wutong8023/Auto-Bibfile.git).\n\n" \
                   "You can directly use our bibtex.bib in overleaf with this " \
                   "[link]({bib_link_overleaf}).\n\n" \
                   "".format(author_info=author_info, personal_link=personal_link, bib_link_overleaf=bib_link_overleaf)
 
    str_outline += dicrib + "\n\n"
    
    str_outline += "## Outline \n"
    
    if add_hyperlink:
        hyperlink = f"![](https://img.shields.io/badge/Hyperlink-{color})"
        link = base_link + filename + '#hyperlink'
        str_outline += "- [" + hyperlink + "](" + link + ')\n'
    
    for i, item in enumerate(list_classif):
        paper_number = "![](https://img.shields.io/badge/{}-{}-{})".format(
            item[0].replace(" ", "_").replace("-", "_"), str(count_list[i]), color)
        link = base_link + "" + filename + "#" + item[0].replace(" ", "-").lower()
        paper_number = "[{}]({})".format(paper_number, link)
        
        str_outline += "- " + paper_number + '\n'
    
    return str_outline

def get_hyperlink(hyperlinks, mapping_name):
    str_hyperlink = "## Hyperlink \n"
    hyperlinks = sorted(hyperlinks)
    
    # Note: please check the branch name carefully!
    str_hyperlink += f"- [[Overview]]({base_link}README.md) -- [Homepage]({base_link}README.md)\n"
    for i, item in enumerate(hyperlinks):
        item = item.split('/')[-1] if item != "./" else item
        str_hyperlink += "- "
        str_hyperlink += f" -- [{mapping_name[item]}]({base_link + your_research_topic}/{item})\n"

    return str_hyperlink

def plot_content(index, keys, dir_path, disc, list_type, plot_titles=plot_titles, mapping_name=None):
    generate_md_file(DB=bib_db, list_classif=list_type, key=keys, plot_title_fct=plot_titles,
                     filename="README.md", add_comments=True, dir_path=dir_path[index], filter_key="keywords",
                     filter_content=[], mapping_name=mapping_name,
                     discrib=disc, add_hyperlink=True, hyperlinks=dir_path,
                     get_outline=get_outline, get_hyperlink=get_hyperlink)

# check repetition
check_repetition()

taxonomy_key = list(fined_taxonomy.keys())

mapping_name = {
    "./": "Summary",
    "conference": "Conference",
    "journal": "Journal",
    "preprint": "Preprint",
    "paper_type": "Paper Type",
    "venue": "Published Venue",
    "time": "Published Time",
    "scenario": "Application Scenario",
    "paradigm": " Learning Paradigm",
    "task": "Task",
    "framework": "SQL Generation Framework",
    "setting": "Setting",
    "technique": "LLM Technique",
    "architecture": "Model Architecture",
    "dataset": "Dataset",
    "metric": "Metric",
    "author": "Author",
    "llm": "Large Language Model",
    "intermedia": "Intermedia Representation"
}
dir_path = ["./"] + ["taxonomy/" + x for x in taxonomy_key]


# 0 Home / Paper Type
list_type = [[x] for x in fined_taxonomy["paper_type"]]
indexs = [0, -1]
disc = f"This page categorizes the literature by the **{mapping_name['paper_type']}**."
for index in indexs:
    plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
                  mapping_name=mapping_name)

# 2 time
list_type = [[str(x)] for x in range(1980, 2030)][::-1]
index = 2
disc = "This page categorizes the literature by the **Last Post**"
plot_content(index=index, keys=["year"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 3 Task
list_type = [[x] for x in fined_taxonomy["task"]]
index = 3
disc = f"This page categorizes the literature by the **{mapping_name['task']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 4 Learning Paradigm
list_type = [[x] for x in fined_taxonomy["paradigm"]]
index = 4
disc = f"This page categorizes the literature by the **{mapping_name['paradigm']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 5 Model Framework
list_type = [[x] for x in fined_taxonomy["framework"]]
index = 5
disc = f"This page categorizes the literature by the **{mapping_name['framework']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 6 Application Scenario
list_type = [[x] for x in fined_taxonomy["scenario"]]
index = 6
disc = f"This page categorizes the literature by the **{mapping_name['scenario']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 7 Model Architecture
list_type = [[x] for x in fined_taxonomy["architecture"]]
list_type.sort()
index = 7
disc = f"This page categorizes the literature by the **{mapping_name['architecture']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 8 llm
list_type = [[x] for x in fined_taxonomy["llm"]]
list_type.sort()
index = 8
disc = f"This page categorizes the literature by the **{mapping_name['llm']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 9 LLM Technique
list_type = [[x] for x in fined_taxonomy["technique"]]
index = 9
disc = f"This page categorizes the literature by the **{mapping_name['technique']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 10 dataset
list_type = [[bm] for bm in fined_taxonomy["dataset"]]
list_type.sort()
index = 10
disc = f"This page categorizes the literature by the **{mapping_name['dataset']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 11 Metric
list_type = [[bm] for bm in fined_taxonomy["metric"]]
list_type.sort()
index = 11
disc = f"This page categorizes the literature by the **{mapping_name['metric']}**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)

# 12 Author
index = 12
disc = "This page categorizes the literature by the **Author**"
plot_content(index=index, keys=["author"], dir_path=dir_path, disc=disc, list_type=None,
             mapping_name=mapping_name)

# 13 Venue
list_type = [[x] for x in fined_taxonomy["conference"]]
list_type += fined_taxonomy["journal"]
list_type.append(fined_taxonomy["preprint"])
indexs = [13]
disc = "This page categorizes the literature by the **Published Venue**"
for index in indexs:
    plot_content(index=index, keys=["booktitle", "journal"], dir_path=dir_path, disc=disc, list_type=list_type,
                  mapping_name=mapping_name)

# Intermedia Representation
list_type = [[x] for x in fined_taxonomy["intermedia"]]
list_type.sort()
index = 14
disc = "This page categorizes the literature by the **Intermedia Representation**"
plot_content(index=index, keys=["keywords"], dir_path=dir_path, disc=disc, list_type=list_type,
             mapping_name=mapping_name)


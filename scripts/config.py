"""
Configuration

Author: Tong
Time: 24-06-2021
"""
user_id = "bahuia"  # github id
author_info = "Yongrui Chen"  # used in introduction
personal_link = ""  # used in introduction
repo_name = "Awesome_Text_to_SQL"  # repository name
branch_name = "master"  # branch name
your_research_topic = "text2sql"  # used for dictionary name
your_research_topic_full_name = "Text-to-SQL"  # used for title
bib_link_overleaf = ""  # used for overleaf
color = "blue"

base_link = f"https://github.com/{user_id}/{repo_name}/blob/{branch_name}/"

# user customized taxonomy
fined_taxonomy = {
    "Conference": ["ACL", "EMNLP", "ACL findings", "EMNLP findings", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS", "AISTATS", "AAAI",
                   "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV"],
    
    "Journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."]],
    
    "Preprint": ["arXiv", "CoRR"],
    
    # 1: resource type
    "Contribution": ["New Dataset", "Survey", "Important", "New Settings or Metrics", "New Application",
             "Empirical Study", "Theory", "New Backbone Model", "New Method", "Thesis", "Library", "Workshop",
             "Other Type"],
    # 2: Area
    "Area": ["CV", "NLP", "Multi-Modal", "Robotics"],
    
    # 3: Supervision
    "Supervision": ["Supervised Learning",
                    "Semi-Supervised Learning",
                    "UnSupervised Learning",
                    "Reinforcement Learning",
                    "Other Learning Paradigm"],
    
    # 4: Application
    "Application": ["Text-to-SQL", "TableQA"],
    
    # 5: Approach
    "Approach": ["Seq2Seq", "Encoder-Submodule", "Meta-learning", "Continual-learning", "Other Approach"],
    
    # 6: Whether need memory
    "Memory": ["w/ External Knowledge", "w/o External Knowledge"],
    
    # 7: Setting
    "Setting": ["Single-Table", "Multi-Table", "Interaction"],
    
    # 8: Research Question
    "RQs": {"Few-shot", "Zero-shot", "Combinatorial Generalization", "Others RQs"},
    
    # 9: Backbone
    "Backbone": ["BERTs", "Transformers", "Adapter", "RNNs", "CNNs", "GNNs", "Attentions", "Capsule Net",
                 "Probabilistic Graphical Model", "VAEs", "Other Structure"],
    
    # 10: Dataset
    "Dataset": ["WikiSQL", "WikiTableQuestions",
                "Spider",
                "ATIS",
                "Other Dataset"
                ],
    
    # 11: Metrics
    "Metrics": ["Accuracy", "F1", "LF", "EX"],
}

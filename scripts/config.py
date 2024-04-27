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
    "conference": [
        "ACL", "EMNLP", "NAACL", "COLING", "EACL", "CoNLL", "ICML", "ICLR", "NeurIPS",
        "AISTATS", "AAAI", "IJCAI", "WWW", "MM", "CVPR", "ICCV", "ECCV", "WACV", "VLDB",
        "OpenAI", "ISoLA", "ACL Findings", "AutoML", "EMNLP Findings", "CIKM", "SIGIR",
        "ECIR", "IA3", "EDBT", "Euro-Par", "ICDCS", "AIIoT", "ICPADS", "OSDI", "ISSTA",
        "openreview", "FSE", "ICSE", "MSR", "WASA", "ICSME", "ASE", "ICER", "ECML",
        "CHI", "EvoMUSART", "KDD"
    ],

    "journal": [
        ["TACL", "Transactions of the Association for Computational Linguistics", "Trans. Assoc. Comput. Linguistics"],
        ["TKDE", "IEEE Transactions on Knowledge and Data Engineering", "{IEEE} Trans. Knowl. Data Eng."],
        ["TNNLS", "IEEE Transactions on Neural Networks and Learning Systems",
         "{IEEE} Trans. Neural Networks Learn. Syst."],
        ["IPM", "Information Processing and Managemen", "Inf. Process. Manag."],
        ["KBS", "Knowledge-BasedSystems", "Knowl. Based Syst."],
        ["FCST", "Journal of Frontiers of Computer Science & Technology"],
        ['JAIR', ' Journal of Artificial Intelligence Research'],
        ['JKSUCIS', ' Journal of King Saud University - Computer and Information Sciences'],
        ['T-PAMI', 'IEEE Transactions on Pattern Analysis and Machine Intelligence'],
        ['NeuroComputing', 'NeuroComputing'],
        ['FLPI', 'Federated Learning: Privacy and Incentive'],
        ['JIS', 'Journal of Information Science'],
        ['TNSE', 'Trans. Netw. Sci. Eng.', 'IEEE Transactions on Network Science and Engineering'],
        ['KIS', 'Knowl. Inf. Syst.', 'Knowledge and Information Systems'],
        ['TIST', 'Trans. Intell. Syst. Technol.'],
        ['JSTSP', 'J. Sel. Top. Signal Process.'],
        ['Applied Sciences', 'Applied Sciences'],
        ['TOIS', 'ACM Transactions on Information Systems'],
        ['JMLR', 'J. Mach. Learn. Res.'],
        ['IJRR', 'Int. J. Robotics Res.'],
        ['IJISAE','International Journal of Intelligent Systems and Applications in Engineering']
    ],
    
    "preprint": ["arXiv", "CoRR"],

    "paper_type": ["Benchmark", "Method", "Evaluation", "Survey"],

    "task": [
        "Text-to-SQL",
        "TableQA",
        "SQL-to-Text",
        "SQL Debugging",
        "SQL Optimization",
        "Schema Linking",
        "Triple Extraction",
        "Node Name Reconstruction",
        "Link Prediction",
        "Structured Data Representation"
    ],
    
    "framework": [
        "Seq2Seq",
        "Sketch",
        "Pipeline",
        "Schema-aware Encoding",
        "Bottom-up Decoding",
        "Top-down Decoding"
    ],

    "paradigm": [
        "Supervised Learning",
        "Semi-Supervised Learning",
        "UnSupervised Learning",
        "Reinforcement Learning",
        "Meta Learning",
        "Multi-task Learning",
        "Continual Learning",
        "Low-resource Learning",
        "Few-shot Learning",
        "Zero-shot Learning",
        "In-context Learning"
    ],

    "intermedia": [
        "SemQL",
        "NatSQL",
    ],

    "scenario": [
        "Single-table",
        "Multi-table",
        "Interaction"
    ],

    "architecture": [
        "Transformer",
        "LSTM",
        "CNN",
        "GNN"
    ],
    
    "dataset": [
        "WikiSQL",
        "WikiTableQuestions",
        "Spider",
        "ATIS",
        "BIRD",
        "BigTable-0.2k",
        "Bank-Financials",
        "Aminer-Simplified",
        "Spider-DK",
        "Spider-Syn",
        "Spider-Realistic",
        "Dr.Spider",
        "Advising",
        "EHRQSL"
    ],

    "metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1",
        "EM",
        "EX",
        "VES",
        "AUC",
        "TS",
        "RES",
        "Rouge-1",
        "Rouge-2",
        "Rouge-L",
        "BertScore",
        "ChatGPT Evaluator",
        "InternLM2 Evaluator",
        "Reliability Score"
    ],

    "technique": [
        "Chain of Thought",
        "Program of Thought",
        "Hard Prompt",
        "P-Tuning",
        "Prompt Tuning",
        "Lora",
        "Supervised Fine-tuning",
        "Data Augmentation",
        "Incremental Pre-training",
        "Retrieval-augmented Generation"
    ],

    "llm": [
        "BERT",
        "RoBERTa",
        "Grappa",
        "TaBERT",
        "TAPAS",
        "GPT-1",
        "GPT-2",
        "GPT-3",
        "T5",
        "GPT-4",
        "GPT-3.5",
        "LLaMa2-Chat-70B",
        "InternLM-70B",
        "InternLM2-20B",
        "Codellama-34B",
        "SQLCoder-34B",
        "StarCoder",
        "CodeS",
        "LLaMa2-7B",
        "CodeLLaMa",
        "Mistral-7B",
        "DeepSeek-7B"
    ],

}

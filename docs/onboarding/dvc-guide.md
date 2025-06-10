📦 DVC Tracking Tutorial + git (Internal Guide)

This guide teaches you how to use **Git** and **DVC** from scratch to track code, data, models, and experiments in a clean, 
reproducible way.

We assume **no prior experience** with either tool.


Highly recommended to read this 
[source](https://www.datacamp.com/tutorial/data-version-control-dvc?utm_source=google&utm_medium=paid_search&utm_campaignid=19589720821&utm_adgroupid=157098104615&utm_device=c&utm_keyword=&utm_matchtype=&utm_network=g&utm_adpostion=&utm_creative=684592139969&utm_targetid=dsa-2264919292029&utm_loc_interest_ms=&utm_loc_physical_ms=9217465&utm_content=ps-other~emea-en~dsa~tofu~tutorial-data-engineering&accountid=9624585688&utm_campaign=230119_1-ps-other~dsa~tofu_2-b2c_3-emea_4-prc_5-na_6-na_7-le_8-pdsh-go_9-nb-e_10-na_11-na&gad_source=1&gad_campaignid=19589720821&gbraid=0AAAAADQ9WsG0cz8Ol0SiDXPWr1o61cgRb&gclid=CjwKCAjwo4rCBhAbEiwAxhJlCblK6Rvvi6O24CqA0MwAofdVm17sMLPDF_Y_kBpfIz-Gp6iB3bG6phoCi6cQAvD_BwE) 
for end to end understanding of dvc.

---

## 🧰 What Gets Tracked Where?

| Type                 | Use Tool | Why?                                      |
| -------------------- | -------- | ----------------------------------------- |
| Source code          | Git      | Version control for all scripts/configs   |
| Docs (Markdown)      | Git      | Easy collaboration + versioning           |
| Small config files   | Git      | Human-readable, diffable                  |
| Data files           | DVC      | Git isn't optimized for large files       |

> 🔒 **Never add raw datasets or model files directly to Git. Always track them with DVC.**

---

## 🔧 1. Project Setup From Scratch

### a) Initialize Git repo

```bash
mkdir my-ml-project && cd my-ml-project
git init
```

Create a basic folder structure:

```bash
mkdir -p data/raw models notebooks scripts docs
```

### b) Create `.gitignore`

```bash
echo "__pycache__/\n*.pyc\n.env\n.vscode/\ndata/*" > .gitignore
git add .gitignore
```

### c) Commit base structure

```bash
git add .
git commit -m "Initialize repo structure"
```

---

## 📦 2. Set Up DVC

### a) Install and initialize DVC

```bash
pip install dvc
dvc init
```

This creates a `.dvc` directory and updates `.gitignore`.

### b) Commit DVC setup to Git

```bash
git add .dvc .gitignore 
git commit -m "Initialize DVC"
```

### c) Configure remote storage (internal)

```bash
dvc remote add myremote ssh aiml@...
```

> 🧠 Ask your admin for the correct internal SSH path and credentials.

---

## 🗂️ 3. Tracking Data with DVC

### a) Add raw data

```bash
mv ~/Downloads/train.csv data/raw/
dvc add data/raw/train.csv
```

### b) Commit data reference

```bash
git add data/raw/train.csv.dvc .gitignore
git commit -m "Track train.csv with DVC"
```

### c) Push to remote

```bash
dvc push
```

---

## 🤝 4. Collaborating with Git + DVC

### Pull team member’s changes:

```bash
git pull origin main
dvc pull  # fetch corresponding datasets or models
```

---

## 🧠 5. Tracking Models and Artifacts 
## (EXPERIMENTAL!!! NOT REQUIRED)

### a) Add model files after training

```bash
python train.py  # outputs to models/model.pkl

dvc add models/model.pkl
git add models/model.pkl.dvc
git commit -m "Track model with DVC"
dvc push
```

### b) Track evaluation results, logs, plots

```bash
dvc add outputs/metrics.json

git add outputs/metrics.json.dvc
git commit -m "Log metrics for experiment v2"
dvc push
```

---

## 🛠 Common Git & DVC Commands

| Task                       | Command                              |
| -------------------------- | ------------------------------------ |
| Initialize Git & DVC       | `git init`, `dvc init`               |
| Track new file             | `dvc add file.csv`                   |
| Commit file metadata       | `git add file.csv.dvc && git commit` |
| Push large files to remote | `dvc push`                           |
| Pull files from teammates  | `git pull` + `dvc pull`              |

---

## 🔐 Final Checklist

✅ Data is tracked with DVC ( model files)
✅ Git repo contains only `.dvc` references
✅ All changes pushed to GitHub
✅ `dvc push` run after every experiment
✅ Metadata (`.dvc`) are versioned in Git

---



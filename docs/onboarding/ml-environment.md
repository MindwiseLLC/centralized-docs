# 🖥️ ML Environment Setup Tutorial

To contribute to any ML project, you must set up your environment with access to our internal services.

❗You can [download this script](../scripts/setup_ml_tools.py.zip) and run it in your directory.
```sh
python setup_ml_tools.py
```
It will automatically setup the basic environment for ML workflow. 
The script creates local setup of mkdocs so you can test your documentation. It also downloads MLFlow and DVC.


## 📢 Please communicate with your administrator. 
#### To use all the tools you will need 

* [ ] Access to our organisational Github
* [ ] VPN credentials for acces to the server
* [ ] MLFlow credentials for access to the unified MLFlow website
* [ ] Server credentials for DVC usage

---

##  🔗 Connect to GitHub, Create your branch, Start working

```bash
git clone ghttps://github.com/MindwiseLLC/Your-Project-Name.git
cd project
git checkout -b feature/your-branch
```


##  📊 Use MLflow for Unified Experiment Tracking

Receive VPN credentials from you administrator. 

Receive MLFlow credentials from you administrator. 

> MLflow is already running on our server: `http://mlflow.daniam.am`

Set tracking URI:

```python
import mlflow
mlflow.set_tracking_uri("http://mlflow.daniam.am")
mlflow.set_experiment("product-matching")
```

Find detailed Mlflow tutorial and workflow [here](./mlflow-guide.md).

## 📦 Use DVC with Internal Remote

DVC is pre-configured on the server. 

You will use following address to as your remote.


```bash
ssh://aiml@192.168.150.222:/mnt/sdd/git_data/dvc_storage
```

Find detailed DVC tutorial and workflow [here](./dvc-guide.md).

## 🧾 Edit and Build Documentation Locally

```bash
pip install mkdocs
mkdocs new my-project 
cd my-project
```

Edit `docs/` markdown files, then:

```bash
mkdocs serve  # preview at http://127.0.0.1:8000
```

Find our how to add your local documentation to our Unified Documentation system [here](./mkdocs-guide.md)


---

## 🧪 Your First Experiment Checklist

* [ ] Create a new Git branch: `experiment/lstm-v1` or new github repository
* [ ] Run your experiment, track wiht internal MLflow 
* [ ] Add data via DVC
* [ ] Commit everything to GitHub with references to MLflow run ID
* [ ] Create/update related documentation (manuals or technical)
* [ ] Add your local docs to Unified Documentation Hub

---

📌 **Remember:** No result exists until it is reproducible via:

* A Git commit
* MLflow run ID
* DVC-tracked dataset 
* Documentation


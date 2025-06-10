# 📚 How to Contribute Your Documentation to the Unified Documentation Hub

This tutorial explains how to add your project’s documentation to our **unified MkDocs documentation hub** using the 
**multirepo plugin**. Follow these steps carefully to avoid build errors.

---

## 🧭 Step 1: Prepare Your Repository

Your GitHub repository should:

* Contain a `docs/` folder with `.md` (Markdown) files
* Have a working `mkdocs.yml` (OPTIONAL)

Example structure:

```bash
my-repo/
├── docs/
│   ├── business.md
│   ├── technical.md
│   └── user-guide.md
├── README.md
└── mkdocs.yml  # optional
```

> ✅ Your `docs/` folder is what will be imported into the documentation hub.

---

## 🧩 Step 2: Add Your Repo to the Hub (Multirepo Plugin)

In the main hub’s `mkdocs.yml`, locate the plugin section:

```yaml
plugins:
  - multirepo:
      keep_docs_dir: true
      temp_dir: projects
      nav_repos:
```

Then, add your repo:

```yaml
        - name: your-section-name
          import_url: https://github.com/<your-org>/<your-repo>?branch=main&edit_uri=/blob/main/
          imports: [/docs/*]
```

* `name`: a unique key for your section (used later in nav)
* `import_url`: be sure to append `?branch=...&edit_uri=...`
* `imports`: what to include from the repo (usually `/docs/*`)

---

## 🗺️ Step 3: Add Your Docs to the Navigation

In the `nav:` section of `mkdocs.yml`, reference your section and imported files:

```yaml
nav:
  - Business Documentation:
      - My Project:
          - Overview: your-section-name/docs/business.md
          - Technical Guide: your-section-name/docs/technical.md
```

* Match `your-section-name` to what you defined above
* Use relative paths to the files in the `docs/` folder

---
## 📘 Step 4: Add Jupyter Notebooks

You can include `.ipynb` files directly — **the plugin is already activated** in the central hub.

Just make sure to:

* Load the notebook file from github
* Reference it correctly in the `nav:` section

```yaml
      - Data Analysis: your-section-name/docs/eda_notebook.ipynb
```

> 📌 Notebooks will be automatically rendered in the website.

---

## 🧠 Step 5: Use mkdocstrings for Code Documentation

If your technical documentation is auto-generated from code comments:

1. Install mkdocstrings:

```bash
pip install mkdocstrings[python]
```

2. In `mkdocs.yml`:

```yaml
plugins:
  - mkdocstrings:
      handlers:
        python:
          paths: [src]
```
Always add the path, or the plugin wwill not work.
In unified docs paths are relative to the project root **after** multirepo copies files


3. In your Markdown:

```markdown
::: mypackage.module.MyClass
```

> This will automatically pull docstrings from your code into the docs.

If you're using mkdocstrings, don't forget to import your `src/` folder too in the multirepo `imports:` list:

```yaml
imports: [/docs/*, /src/*]
```

---

## 🧪 Step 6: Test Documentation Locally

Before pushing changes:

1. Clone the central documentation hub repository:

```bash
git clone https://github.com/MindwiseLLC/centralized-docs.git
cd centralized-docs
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Serve locally:

```bash
mkdocs serve
```

Then open `http://127.0.0.1:8000` in your browser.

Check that:

* All files render without error
* Jupyter notebooks load correctly
* Navigation links work

---

## 🚀 Step 7: Push Your Changes & Submit a PR

After testing locally:

1. Create a new branch:

```bash
git checkout -b add-my-project-docs
```

2. Add your changes (to `mkdocs.yml`, etc.)

```bash
git add mkdocs.yml
# add any related assets if needed

git commit -m "Add documentation for my-project"
git push origin add-my-project-docs
```

3. Open a Pull Request from your branch to `main` in the centralized documentation GitHub repo.

> ✅ Once approved, your docs will be live on the documentation hub.



---

## ✅ Final Checklist

* [ ] Repo contains `docs/` folder with content
* [ ] Added to `nav_repos` in `mkdocs.yml`
* [ ] Added to `nav:` section with correct paths
* [ ] Optional: Jupyter notebooks render properly
* [ ] Optional: mkdocstrings renders code documentation

---

Let your team lead know once your section is integrated! 🚀



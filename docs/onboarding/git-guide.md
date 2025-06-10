# 🧩 Git Workflow Guide (Internal ML Team)

This guide explains how we use **Git** as our primary code versioning and collaboration tool. Every team member must follow this 
structure to ensure clean, traceable, and production-ready development.

---

## 🔒 Core Principle

> **If it’s not in GitHub, it doesn’t exist.** Code must never be shared over email, chat, or zip files.

✅ Everything must be committed and pushed to GitHub.
❌ No local-only scripts.

---

## 🏢 GitHub Organization Setup

All documentation repositories **must** reside under our **GitHub organization**.

* Your repo must be located under `https://github.com/MindwiseLLC/`.
* Do not create standalone or personal forks/repos.

We use **GitHub Teams** to manage access to repositories.

> ✅ Please ask your lead/admin to add you to the correct GitHub team if you do not have access.

---


## 🌱 Branching Strategy

| Branch             | Purpose                                     |
| ------------------ | ------------------------------------------- |
| `main`             | Active development (tested, but not final)  |
| `production`       | **Production-ready**, DevOps-compliant code |
| `feature/<name>`   | New isolated features                       |
| `experiment/<tag>` | Experiments and model iterations            |
| `fix/<bug>`        | Fixes to bugs or issues                     |

> 🛑 Do not commit directly to `main` or `production` unless authorized.

---

## 🔀 Workflow Rules

### 1. Start with a new branch for each task

```bash
git checkout -b feature/add-normalization
```

### 2. Commit frequently, with meaningful messages

```bash
git add .
git commit -m "Add text normalization step to preprocessing pipeline"
```

### 3. Push your branch to GitHub

```bash
git push origin feature/add-normalization
```

### 4. Open a Pull Request into `main`

* Assign at least one reviewer
* Link related issues
* Describe what changed and why

### 5. Merge to `main` only after review

```bash
git checkout main
git pull
git merge feature/add-normalization
```

---

## 🚀 Deploying to Production

### ✅ Merge to `production` **only if**:

* Code has been reviewed and approved
* Code runs on staging/dev environments
* Outputs match expected format and metrics
* It satisfies our **DevOps production criteria** (runtime, structure, reproducibility)

> 👋 **If it's your first time working on `production`, talk to your lead before merging.**

### Deployment flow:

```bash
git checkout production
git pull origin main  # merge latest stable code
# test again
# merge and tag
```

---

## 🏷️ Tagging Releases

Use tags to mark key experiment versions or stable releases.

```bash
git tag -a v1.0.0 -m "First production-ready release"
git push origin --tags
```

Use format: `vX.Y.Z` or `exp-<date>-<name>` (e.g., `exp-2025-06-10-xgb-grid`)

---

## 💬 Commit Message Guidelines

* ✅ Clear, lowercase, present-tense: `add`, `fix`, `refactor`
* ❌ Avoid: `update`, `more edits`, `temp`

Examples:

```bash
git commit -m "add config loader for multilingual support"
git commit -m "fix NaN issue in metrics evaluation"
```

---

## ✅ Git Best Practices

* Pull regularly from `main` to stay up to date
* Never rewrite shared history (`git push --force` is discouraged)
* Keep commits small and focused
* Never commit `.env`, credentials, or raw datasets

---



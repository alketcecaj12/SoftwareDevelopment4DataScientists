# 🛠️ Software Development for Data Scientists

> *Writing notebooks is easy. Writing good software is a skill. This repo bridges the gap.*

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=flat-square&logo=jupyter&logoColor=white)
![Topics](https://img.shields.io/badge/Topics-Packaging%20%7C%20Modularity%20%7C%20Docs%20%7C%20Pandas-6366f1?style=flat-square)
![Level](https://img.shields.io/badge/Level-Intermediate-f59e0b?style=flat-square)

---

## 🎯 What Is This?

A practical, notebook-driven guide to the **software engineering concepts that data scientists most often skip** — and most often need.

Most data science education focuses on algorithms, models, and statistics. This repo focuses on the craft that makes that work maintainable, reusable, and shareable: writing modular code, building Python packages, documenting functions properly, and using pandas effectively.

Each notebook is a self-contained lesson with working code examples. The companion packages (`mypackages`, `text_analyzer`, `textanalysis`) demonstrate the concepts in action on real text data.

---

## 📁 Repository Structure

```
SoftwareDevelopment4DataScientists/
│
├── 📓 Notebooks (lessons)
│   ├── ModularCode.ipynb          # Structuring code into reusable modules
│   ├── BuildPackage.ipynb         # Creating and installing Python packages
│   ├── FunctionDocumentation.ipynb # Docstrings, type hints, and auto-docs
│   └── ApplyFunctionInPandas.ipynb # apply(), map(), vectorization patterns
│
├── 📦 Packages (applied examples)
│   ├── mypackages/                # General-purpose package skeleton
│   ├── text_analyzer/             # Installable text analysis package
│   └── textanalysis/              # Text analysis module (flat structure)
│
├── 📄 Data files
│   ├── alice.txt                  # Alice in Wonderland — NLP/text use cases
│   └── hotel-reviews.txt          # Hotel reviews — sentiment/analysis use cases
│
└── 🐍 Scripts
    ├── my_script.py               # Standalone script example
    ├── new_script.py              # Script refactoring example
    └── yes.py                     # Minimal script demo
```

---

## 📚 Notebook Guide

### 1. `ModularCode.ipynb` — Writing Code That Can Be Reused

**The problem:** Data scientists often write long, monolithic notebooks where logic is tangled with execution. When something needs to change — or be reused — it's painful.

**What you'll learn:**
- How to identify and extract reusable logic into functions and modules
- The difference between a script, a module, and a package
- How to import your own code cleanly
- Structuring a project so it scales

**Key concepts:** separation of concerns, `__init__.py`, relative imports, module organisation

---

### 2. `BuildPackage.ipynb` — Creating Your Own Python Package

**The problem:** Copy-pasting utility functions across projects. Sharing code via Slack or email. "Works on my machine."

**What you'll learn:**
- The anatomy of a Python package (`setup.py` / `pyproject.toml`, `__init__.py`, entry points)
- How to install a local package in editable mode (`pip install -e .`)
- Versioning and dependency declaration
- Publishing-ready package structure

**Key concepts:** `setuptools`, `pyproject.toml`, editable installs, package discovery

**Companion folders:** `mypackages/`, `text_analyzer/`, `textanalysis/`

---

### 3. `FunctionDocumentation.ipynb` — Documenting Code Like a Professional

**The problem:** A function called `process_data` that no one (including you, six months later) understands.

**What you'll learn:**
- Writing NumPy-style, Google-style, and reStructuredText docstrings
- Using type hints (`->`, `Optional`, `List`, etc.) for clarity and IDE support
- Auto-generating documentation with `help()` and tools like `pydoc`
- Best practices for parameter descriptions, return values, and examples in docstrings

**Key concepts:** docstrings, `__doc__`, type annotations, PEP 257, `help()`

---

### 4. `ApplyFunctionInPandas.ipynb` — Pandas Beyond the Basics

**The problem:** Slow, hard-to-read pandas code full of loops. Not knowing when to use `apply()` vs `map()` vs vectorized operations.

**What you'll learn:**
- `Series.apply()` and `DataFrame.apply()` — when and how to use them
- `Series.map()` for element-wise transformations
- `DataFrame.applymap()` / `map()` for cell-level operations
- Vectorization: when to avoid `apply()` entirely for performance
- Lambda functions vs named functions in pandas pipelines

**Key concepts:** `apply`, `map`, `transform`, `groupby` + aggregation, vectorization, performance tradeoffs

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Jupyter Lab or Jupyter Notebook

```bash
git clone https://github.com/alketcecaj12/SoftwareDevelopment4DataScientists.git
cd SoftwareDevelopment4DataScientists
```

### Install dependencies

```bash
pip install jupyter pandas numpy
```

### Run the notebooks

```bash
jupyter lab
```

Open any `.ipynb` file and run cells top-to-bottom. Each notebook is self-contained.

### Install the example packages locally

```bash
# Install text_analyzer in editable mode
cd text_analyzer
pip install -e .

# Or install mypackages
cd ../mypackages
pip install -e .
```

---

## 🎓 Who Is This For?

| Profile | How this helps |
|---------|---------------|
| **Data scientists moving toward engineering** | Practical patterns for writing production-ready code |
| **Analysts who live in notebooks** | Learn when and how to step outside the notebook |
| **Students learning Python for data science** | Structured lessons on SE fundamentals often missing from data curricula |
| **Anyone who's copy-pasted utility functions across 3+ projects** | Time to build a package |

---

## 🧩 Learning Path

If you're working through this repo from scratch, suggested order:

```
FunctionDocumentation → ModularCode → BuildPackage → ApplyFunctionInPandas
```

Start with documentation because good habits there make everything else easier. Then structure your code, package it, and finally apply pandas patterns with the right mental model.

---

## 🔗 Related Topics

If you find this useful, you might also be interested in:

- **Testing** — `pytest` for data science code
- **Type checking** — `mypy` for enforcing type hints at scale  
- **Code style** — `black`, `ruff`, `flake8`
- **CI/CD for notebooks** — `nbmake`, `papermill`

---

## 📬 Author

**Alket Cecaj** — Data Scientist & Quantitative Analyst  
[GitHub](https://github.com/alketcecaj12) · Copenhagen, Denmark

---

*Because the best model in the world is useless if the code around it can't be maintained.*

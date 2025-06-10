import os
import platform
import shutil
import subprocess
from pathlib import Path
import textwrap


# Editable: list of required pip packages for your docs site (except multirepo plugin)
REQUIRED_PACKAGES = [
    "mkdocs",
    "mkdocs-material",
    "mkdocs-encryptcontent-plugin",
    "mkdocs-jupyter",
    "mkdocs-exporter",
    "mkdocstrings",
    "mkdocstrings[python]",
    "dvc",           # Uncomment if needed
    "mlflow"        # Uncomment if needed
]

# Editable: sample mkdocs.yml (update plugins/extensions as needed)
MKDOCS_YML = textwrap.dedent("""
    site_name: "Test Local Documentation"
    site_url: ""
    theme:
      name: material
      features:
        features:
          - navigation.tabs
          - navigation.top
          - navigation.instant
          - navigation.instant.progress
          - navigation.footer
          - search.suggest
          - search.highlight
          - content.code.annotate
          - content.tabs.link
          - content.action.edit  
          - content.code.copy
      palette:
        - media: "(prefers-color-scheme: light)"
          scheme: default
          toggle:
            icon: material/brightness-7
            name: Switch to dark mode
          primary: blue grey
        - media: "(prefers-color-scheme: dark)"
          scheme: slate
          toggle:
            icon: material/brightness-4
            name: Switch to light mode
          primary: grey
      font:
        text: Roboto
        code: Roboto Mono

    plugins:
      - search
      - mkdocstrings:
          handlers:
            python:
              paths:
                - docs/

      - mkdocs-jupyter

    markdown_extensions:
      - attr_list
      - md_in_html
      - admonition
      - pymdownx.details
      - pymdownx.caret
      - pymdownx.mark
      - pymdownx.tilde
      - pymdownx.keys
      - pymdownx.highlight
      - codehilite
      - pymdownx.superfences:
          custom_fences:
            - name: mermaid
              class: mermaid
              format: !!python/name:pymdownx.superfences.fence_code_format
      - pymdownx.tabbed:
          alternate_style: true
      - pymdownx.tasklist:
          custom_checkbox: true
          clickable_checkbox: true

    nav:
      - Home: index.md
""")

def find_python_executable():
    for candidate in ["python3", "python"]:
        try:
            subprocess.run([candidate, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return candidate
        except Exception:
            continue
    raise RuntimeError("Neither 'python3' nor 'python' is available.")



def run(cmd):
  print(f"Running: {cmd}")
  result = subprocess.run(cmd, shell=True)
  if result.returncode != 0:
      print(f"Command failed: {cmd}")
      exit(1)


def main():
  IS_WINDOWS = platform.system() == "Windows"
  py_executable = find_python_executable()
  print(f'python executable is {py_executable}')
  
  base_dir = Path.cwd()
  venv_dir =  Path("venv")
  pip_path = venv_dir / ("Scripts" if IS_WINDOWS else "bin") / ("pip.exe" if IS_WINDOWS else "pip")
  
  docs_dir = base_dir / "docs"
  req_file = base_dir / "requirements.txt"
  mkdocs_yml = base_dir / "mkdocs.yml"
  index_md = docs_dir / "index.md"
  readme_md = base_dir / "README.md"



  # 1. Create virtualenv
  print("Creating Python virtual environment...")
  run(f"{py_executable} -m venv venv")


  # 3. Write and install requirements
  print("Writing requirements.txt...")
  req_file.write_text("\n".join(REQUIRED_PACKAGES))

  print("Installing requirements...")
  run(f"{pip_path} install -r requirements.txt")

  # 4. Create docs folder & sample index.md
  print("Creating docs folder and sample index.md...")
  docs_dir.mkdir(exist_ok=True)
  index_md.write_text("# Welcome!\n\nThis is a test documentation site.\n")

  # 5. Write mkdocs.yml
  print("Writing mkdocs.yml...")
  mkdocs_yml.write_text(MKDOCS_YML.strip())

 
  print("\nSetup complete! To begin write the command:")
 
  print("  source venv/bin/activate on linux/unix systems or \n Scripts/bin/activate on windows")
  print("  mkdocs serve")
  print("Then open http://localhost:8000 in your browser.")

if __name__ == "__main__":
 main()

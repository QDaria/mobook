---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Intro Team Effekt

```python
import plotly.io as pio
import plotly.express as px
import plotly.offline as py
```


## Quickly add YAML metadata for MyST Notebooks

If you have a markdown file and you'd like to quickly add YAML metadata to it, so that Jupyter Book will treat it as a MyST Markdown Notebook, run the following command:

```{code-cell}
jupyter-book myst init path/to/markdownfile.md
```

---
substitutions:
  key1: "I'm a **substitution**"
  key2: |
    ```{note}
    {{ key1 }}
    ```
  fishy: |
    ```{image} img/mo2.png
    :alt: fishy
    :width: 200px
    ```
---

[the Jupyter Book documentation](https://jupyterbook.org) 

```{tableofcontents}
```

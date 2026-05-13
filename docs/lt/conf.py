project = "Katalogas"
copyright = "2026, Katalogas Team"
author = "Katalogas Team"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_rtd_theme",
    "myst_parser",
    "sphinxcontrib.mermaid",
]

templates_path = ["_templates"]

language = "lt"

locale_dirs = ["locale/"]
gettext_compact = False


def setup(app):
    if app.config.language:
        app.tags.add(app.config.language)


exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", ".venv"]

html_theme = "sphinx_rtd_theme"

html_theme_options = {
    "collapse_navigation": False,
}

html_static_path = ["static"]

master_doc = "index"

autodoc_typehints = "description"

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
]

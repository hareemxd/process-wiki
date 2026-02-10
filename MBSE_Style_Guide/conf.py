project = "MBSE Style Guide"

extensions = [
    "myst_parser",
]

numfig = True
numfig_format = {
    "figure": "Figure %s",
}


myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "tasklist",
    "substitution",
    "attrs_inline",
]

myst_heading_anchors = 3
master_doc = "index"

latex_engine = "xelatex"
latex_elements = {
    "papersize": "letterpaper",
    "pointsize": "10pt",
}

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
myst_yml = ROOT / "myst.yml"
out_index = ROOT / "index.md"

data = yaml.safe_load(myst_yml.read_text(encoding="utf-8"))
toc = data["project"]["toc"]

def emit_toctree(items, caption=None, maxdepth=2):
    lines = []
    lines.append("```{toctree}")
    lines.append(f":maxdepth: {maxdepth}")
    if caption:
        lines.append(f":caption: {caption}")
    lines.append("")
    for it in items:
        # Sphinx wants docnames without ".md"
        f = it["file"]
        if f.lower().endswith(".md"):
            f = f[:-3]
        lines.append(f)
    lines.append("```")
    return "\n".join(lines)

# Find the root index file (first toc entry usually file: index.md)
# We'll overwrite index.md to include a generated toctree that matches myst.yml.
root_title = data["project"].get("title", "Document")

# Pull out the "Work_Instructions" group from myst.yml
work = next((x for x in toc if isinstance(x, dict) and x.get("title") == "Work_Instructions"), None)
work_children = (work or {}).get("children", [])

content = []
content.append(f"# {root_title}")
content.append("")
if work_children:
    content.append(emit_toctree(work_children, caption="Work_Instructions", maxdepth=2))
    content.append("")
else:
    content.append("> No Work_Instructions entries found in myst.yml")
    content.append("")

out_index.write_text("\n".join(content), encoding="utf-8")
print(f"Wrote {out_index}")

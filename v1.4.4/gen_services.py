# docs/gen_services.py
from __future__ import annotations
import pathlib
import mkdocs_gen_files as gen

# Paths relative to this file (docs/mkdocs.yaml lives in docs/)
ROOT = pathlib.Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
PKG = SRC / "scc_utility" / "services"

# Optional: build a nav structure for mkdocs-literate-nav
# nav = gen.Nav()

# Write a simple landing page for Services
# with gen.open("reference/services/index.md", "w") as fd:
#     fd.write("# Services\n\n")
#     fd.write("Auto-generated from `scc_utility.services` modules.\n")

# Generate one page per service module
for path in sorted(PKG.rglob("*.py")):
    if path.name == "__init__.py":
        continue

    # e.g. "scc_utility.services.device_upgrade"
    module_path = (
        "scc_utility.services."
        + path.relative_to(PKG).with_suffix("").as_posix().replace("/", ".")
    )

    # Output path under docs/reference/services/...
    doc_rel = pathlib.Path("reference", "services", path.relative_to(PKG)).with_suffix(".md")
    # doc_abs = pathlib.Path(gen.dest_dir) / doc_rel
    # doc_abs.parent.mkdir(parents=True, exist_ok=True)

    # Human title (Device Upgrade -> Device Upgrade)
    title = path.stem.replace("_", " ").title()

    with gen.open(doc_rel, "w") as fd:
        fd.write(f"# {title}\n\n")
        fd.write(f"::: {module_path}\n")
        fd.write(
            "    options:\n"
            "      show_source: false\n"
            "      show_signature: true\n"
            "      separate_signature: true\n"
            "      members_order: source\n"
            "      filters:\n"
            "        - '!^_'\n"  # hide private members
        )

#     # Add to the generated nav
#     nav["API", "Services", title] = str(doc_rel).replace("\\", "/")

# # Emit a SUMMARY.txt for mkdocs-literate-nav to merge into the site nav
# with gen.open("SUMMARY.md", "w") as fd:
#     fd.write("".join(nav.build_literate_nav()))

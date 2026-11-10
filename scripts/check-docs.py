#!/usr/bin/env python3
"""Controleert de documentatie op structuurfouten vóór een push.

Gecontroleerd wordt:

* **Interne links** — verwijst elke link naar een bestaand bestand?
* **Ankers** — bestaat de kop waar een `#anker` naar wijst?
* **Afbeeldingen** — staat elk ingesloten plaatje er echt?
* **GitBook-blokken** — is elke `{% hint %}`, `{% tabs %}` en `{% tab %}`
  netjes afgesloten?
* **Codefences** — staan de ``` in paren?
* **SUMMARY-dekking** — staat elke pagina in SUMMARY.md? GitBook publiceert
  alleen wat daar in staat; een pagina die ontbreekt wordt een dode link.

Draaien vanuit de root van deze repo:

    python3 scripts/check-docs.py

Exitcode 1 bij bevindingen.
"""

import os
import re
import sys
import glob

DOCS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Niet meescannen: eigen gereedschap en afhankelijkheden.
OVERSLAAN = (".claude", "node_modules", ".git")

# Pagina's die bewust niet in SUMMARY.md staan omdat ze geen GitBook-pagina zijn.
GEEN_PAGINA = {"SUMMARY.md", "scripts/README.md", "ONDERHOUD.md"}


def kop_naar_anker(kop):
    """Zelfde slug-regels als GitBook en GitHub hanteren."""
    k = kop.strip().lower()
    k = re.sub(r"[^\w\s-]", "", k, flags=re.U)
    k = re.sub(r"[\s_]+", "-", k)
    return k.strip("-")


def paginas():
    uit = []
    for f in glob.glob(os.path.join(DOCS, "**", "*.md"), recursive=True):
        rel = os.path.relpath(f, DOCS)
        if rel.split(os.sep)[0] in OVERSLAAN:
            continue
        uit.append(rel)
    return sorted(uit)


def main():
    rel_paginas = paginas()
    inhoud = {p: open(os.path.join(DOCS, p), encoding="utf-8").read() for p in rel_paginas}
    ankers = {
        p: {kop_naar_anker(m) for m in re.findall(r"^#{1,6}\s+(.*)$", t, re.M)}
        for p, t in inhoud.items()
    }

    fouten = []

    for p, t in inhoud.items():
        map_van = os.path.dirname(p)

        # links (geen afbeeldingen)
        for link in re.findall(r"(?<!\!)\]\(([^)]+)\)", t):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            doel, _, anker = link.partition("#")
            pad = os.path.normpath(os.path.join(map_van, doel))
            if not os.path.exists(os.path.join(DOCS, pad)):
                fouten.append((p, f"link naar ontbrekend bestand: {link}"))
            elif anker and pad.endswith(".md") and anker not in ankers.get(pad, set()):
                fouten.append((p, f"link naar ontbrekend anker: {link}"))

        # afbeeldingen
        for img in re.findall(r"!\[[^\]]*\]\(([^)]+)\)", t):
            if img.startswith(("http://", "https://")):
                continue
            pad = os.path.normpath(os.path.join(map_van, img.split("#")[0]))
            if not os.path.exists(os.path.join(DOCS, pad)):
                fouten.append((p, f"ontbrekende afbeelding: {img}"))

        # GitBook-blokken
        for tag in ("hint", "tabs", "tab"):
            open_ = len(re.findall(r"\{%\s*" + tag + r"[\s%]", t))
            dicht = len(re.findall(r"\{%\s*end" + tag + r"\s*%\}", t))
            if open_ != dicht:
                fouten.append((p, f"{tag}-blok niet in balans: {open_} open, {dicht} gesloten"))

        # codefences
        if t.count("```") % 2:
            fouten.append((p, "oneven aantal codefences (```)"))

    # SUMMARY-dekking
    summary = inhoud.get("SUMMARY.md", "")
    vermeld = {
        os.path.normpath(l) for l in re.findall(r"\]\(([^)]+)\)", summary)
    }
    for p in rel_paginas:
        if p in GEEN_PAGINA or p in vermeld:
            continue
        fouten.append((p, "staat niet in SUMMARY.md — GitBook publiceert deze pagina niet"))

    print(f"Gecontroleerd: {len(rel_paginas)} pagina's")
    if not fouten:
        print("✅ Geen structuurfouten gevonden.")
        return 0

    print(f"\n❌ {len(fouten)} bevinding(en):\n")
    for pagina, melding in fouten:
        print(f"  {pagina}")
        print(f"    {melding}")
    return 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Genereert een pagina per business service uit de backend-configuratie.

Bron: de bouwblokken in config/building-block/ van mijn-inkomen-gzac-backend.
Uitvoer: functionaliteit/business-services/<key>.md

Draaien:
    python3 scripts/generate-business-services.py [pad-naar-backend]

Zonder argument wordt ../mijn-inkomen-gzac-backend-v13 geprobeerd.
"""

import json
import os
import re
import sys
import glob
import xml.etree.ElementTree as ET

B = "{http://www.omg.org/spec/BPMN/20100524/MODEL}"

DOCS = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UIT = os.path.join(DOCS, "functionaliteit", "business-services")

# Alleen de business services; generieke hulpprocessen krijgen geen eigen pagina.
PREFIX = "bs-"

# Leesbare namen voor de zaakprocessen. De sleutel is het proces-id uit het
# BPMN-model; staat een proces hier niet in, dan toont de pagina het id.
PROCES_NAMEN = {
    "ab-afhandelen-aanvraag-dcm": "Algemene bijstand aanvraag",
    "ioaw-afhandelen-aanvraag-dcm": "IOAW aanvraag",
    "basisafhandelproces-afhandelen-aanvraag": "Basisafhandelproces",
}

TYPE_NL = {
    "userTask": "Gebruikerstaak",
    "serviceTask": "Systeemstap",
    "scriptTask": "Systeemstap",
    "businessRuleTask": "Beslistabel",
    "callActivity": "Aanroep",
    "sendTask": "Bericht versturen",
    "receiveTask": "Wachten op bericht",
    "exclusiveGateway": "Keuze",
    "parallelGateway": "Splitsing",
    "inclusiveGateway": "Keuze (meervoudig)",
    "eventBasedGateway": "Keuze op gebeurtenis",
    "startEvent": "Start",
    "endEvent": "Einde",
    "intermediateCatchEvent": "Wachtpunt",
    "intermediateThrowEvent": "Signaal",
    "boundaryEvent": "Onderbreking",
    "subProcess": "Subproces",
}


def bouw_aanroepindex(basis_config):
    """Wie roept wie aan? Levert {aangeroepen: {aanroepers}} en de procesnamen.

    De keten loopt doorgaans bs-<x> ← bsb-<x> ← uitvoeren-business-services
    ← het zaakproces van de regeling.
    """
    calls, namen = {}, {}
    for f in glob.glob(os.path.join(basis_config, "**", "*.bpmn"), recursive=True):
        try:
            root = ET.parse(f).getroot()
        except ET.ParseError:
            continue
        for proc in root.findall(B + "process"):
            pid = proc.get("id")
            if not pid:
                continue
            namen[pid] = (proc.get("name") or pid).strip()
            for ca in proc.iter(B + "callActivity"):
                ce = ca.get("calledElement")
                if ce:
                    calls.setdefault(ce, set()).add(pid)
    return calls, namen


def ketens(key, calls, pad=None, diep=0):
    """Alle aanroepketens van `key` omhoog, tot aan een proces dat niemand aanroept."""
    pad = pad or [key]
    if diep > 6 or key not in calls:
        return [pad]
    uit = []
    for c in sorted(calls[key]):
        if c in pad:
            continue
        uit += ketens(c, calls, pad + [c], diep + 1)
    return uit or [pad]


def tekst(el):
    return (el.text or "").strip() if el is not None else ""


def lees_bouwblok(map_pad):
    """Haalt naam, processtappen en in-/uitvoer uit één bouwblokmap."""
    key = os.path.basename(map_pad)
    data = {"key": key, "naam": key, "beschrijving": "", "stappen": [],
            "input": [], "output": [], "formulieren": [], "dmn": [],
            "schema": False, "formflow": [], "proces_ids": []}

    defs = glob.glob(f"{map_pad}/*/building-block/definition/*.json")
    if defs:
        try:
            d = json.load(open(defs[0], encoding="utf-8"))
            data["naam"] = d.get("name") or key
            if (d.get("description") or "").strip() != data["naam"]:
                data["beschrijving"] = (d.get("description") or "").strip()
        except Exception:
            pass

    data["formulieren"] = sorted(
        os.path.basename(f).replace(".form.json", "")
        for f in glob.glob(f"{map_pad}/*/form/*.json"))
    data["formflow"] = sorted(
        os.path.basename(f).replace(".form-flow.json", "")
        for f in glob.glob(f"{map_pad}/*/form-flow/*.json"))
    data["dmn"] = sorted(
        os.path.basename(f).replace(".dmn", "")
        for f in glob.glob(f"{map_pad}/*/dmn/*.dmn"))
    data["schema"] = bool(glob.glob(f"{map_pad}/*/document/definition/*.json"))

    for bpmn in sorted(glob.glob(f"{map_pad}/*/bpmn/*.bpmn")):
        try:
            root = ET.parse(bpmn).getroot()
        except ET.ParseError:
            continue
        # Annotaties staan niet altijd als direct kind van <process>; zoek breed.
        for ta in root.iter(B + "textAnnotation"):
            _lees_annotatie(tekst(ta.find(B + "text")), data)

        for proc in root.findall(B + "process"):
            # De mapnaam en het proces-id lopen niet altijd gelijk; voor het
            # opzoeken van aanroepers telt het proces-id.
            if proc.get("id") and proc.get("id") not in data["proces_ids"]:
                data["proces_ids"].append(proc.get("id"))
            for el in proc:
                tag = el.tag.replace(B, "")
                naam = (el.get("name") or "").strip()
                if tag == "textAnnotation":
                    continue
                if tag in ("sequenceFlow", "association", "extensionElements",
                           "laneSet", "documentation", "dataObject",
                           "dataObjectReference", "property"):
                    continue
                if not naam:
                    continue
                stap = {"type": TYPE_NL.get(tag, tag), "naam": naam}
                if tag == "callActivity" and el.get("calledElement"):
                    stap["roept"] = el.get("calledElement")
                data["stappen"].append(stap)
    return data


def _lees_annotatie(txt, data):
    """Herkent 'Input...' / 'Output...' koppen en verzamelt de regels eronder."""
    if not txt:
        return
    doel = None
    for regel in txt.splitlines():
        r = regel.strip()
        if not r:
            continue
        kop = re.match(r"^(in|out)put\b.*$", r, re.I)
        if kop:
            doel = "input" if r.lower().startswith("in") else "output"
            continue
        if doel and r.startswith("-"):
            waarde = r.lstrip("- ").strip()
            if waarde and waarde not in data[doel]:
                data[doel].append(waarde)


def schrijf_pagina(d):
    r = []
    r.append("---")
    omschrijving = d["beschrijving"] or f"Procesverloop, invoer en uitvoer van {d['naam']}."
    r.append(f"description: {omschrijving}")
    r.append("---")
    r.append("")
    r.append(f"# {d['naam']}")
    r.append("")
    r.append(f"Bouwblok `{d['key']}`.")
    r.append("")

    if d["input"] or d["output"]:
        r.append("## Invoer en uitvoer")
        r.append("")
        if d["input"]:
            r.append("**Invoer**")
            r.append("")
            for v in d["input"]:
                r.append(f"* `{v}`")
            r.append("")
        if d["output"]:
            r.append("**Uitvoer**")
            r.append("")
            for v in d["output"]:
                r.append(f"* `{v}`")
            r.append("")
    else:
        r.append("## Invoer en uitvoer")
        r.append("")
        r.append("Dit bouwblok benoemt geen invoer- en uitvoervariabelen in het procesmodel.")
        r.append("")

    if d.get("ketens"):
        r.append("## Wie roept dit aan")
        r.append("")
        direct = sorted({k[1] for k in d["ketens"] if len(k) > 1})
        wortels = sorted({k[-1] for k in d["ketens"] if len(k) > 2})
        if direct:
            r.append("| | |")
            r.append("| --- | --- |")
            r.append("| **Direct aangeroepen door** | " +
                     ", ".join(f"`{x}`" for x in direct) + " |")
            if wortels:
                leesbaar = sorted({PROCES_NAMEN.get(x, f"`{x}`") for x in wortels})
                r.append("| **Binnen zaakproces** | " + ", ".join(leesbaar) + " |")
            r.append("")
            r.append("De volledige keten, met de technische procesnamen:")
            r.append("")
            for k in d["ketens"]:
                if len(k) > 1:
                    r.append("* " + " ← ".join(f"`{x}`" for x in k))
            r.append("")
        else:
            r.append("Dit bouwblok wordt door geen ander procesmodel aangeroepen. "
                     "Het wordt rechtstreeks door de regie gestart of los gestart "
                     "door de behandelaar.")
            r.append("")

    svg = os.path.join(DOCS, ".gitbook", "assets", "bpmn", d["key"] + ".svg")
    if os.path.exists(svg):
        r.append("## Het procesmodel")
        r.append("")
        r.append(f"![Procesmodel: {d['naam']}](../../.gitbook/assets/bpmn/{d['key']}.svg)")
        r.append("")
        r.append("Gegenereerd uit het BPMN-model. Open de afbeelding apart om in te zoomen.")
        r.append("")

    if d["stappen"]:
        r.append("## Het proces")
        r.append("")
        r.append("| Soort | Stap |")
        r.append("| --- | --- |")
        for s in d["stappen"]:
            naam = s["naam"].replace("|", "\\|").replace("\n", " ")
            if "roept" in s:
                naam += f" → `{s['roept']}`"
            r.append(f"| {s['type']} | {naam} |")
        r.append("")

    onderdelen = []
    if d["formulieren"]:
        onderdelen.append(("Formulieren", d["formulieren"]))
    if d["formflow"]:
        onderdelen.append(("Formulierstromen", d["formflow"]))
    if d["dmn"]:
        onderdelen.append(("Beslistabellen", d["dmn"]))
    if onderdelen or d["schema"]:
        r.append("## Onderdelen")
        r.append("")
        for titel, items in onderdelen:
            r.append(f"**{titel}**")
            r.append("")
            for i in items:
                r.append(f"* `{i}`")
            r.append("")
        if d["schema"]:
            r.append("Dit bouwblok heeft een eigen documentdefinitie.")
            r.append("")

    r.append("---")
    r.append("")
    r.append("Terug naar [Business services](../business-services.md).")
    r.append("")
    return "\n".join(r)


def werk_summary_bij(blokken):
    """Zet de gegenereerde pagina's genest onder 'Business services' in SUMMARY.md.

    GitBook publiceert alleen wat in SUMMARY.md staat; een pagina die ontbreekt
    wordt als bestandsverwijzing behandeld en de link loopt dood. Genest houdt
    ze ingeklapt onder de ouderpagina in plaats van los in de navigatie.
    """
    pad = os.path.join(DOCS, "SUMMARY.md")
    s = open(pad, encoding="utf-8").read()
    anker = "* [Business services](functionaliteit/business-services.md)"
    if anker not in s:
        print("! SUMMARY.md: ankerregel niet gevonden, navigatie niet bijgewerkt",
              file=sys.stderr)
        return
    # bestaande geneste regels weghalen
    regels, in_blok, uit = s.splitlines(), False, []
    for r in regels:
        if r.strip() == anker.strip():
            in_blok = True
            uit.append(r)
            continue
        if in_blok:
            if r.startswith("  * [") and "business-services/" in r:
                continue
            in_blok = False
        uit.append(r)
    s = "\n".join(uit)
    genest = "\n".join(
        f"  * [{b['naam']}](functionaliteit/business-services/{b['key']}.md)"
        for b in blokken)
    s = s.replace(anker, anker + "\n" + genest)
    open(pad, "w", encoding="utf-8").write(s)
    print(f"SUMMARY.md bijgewerkt: {len(blokken)} geneste pagina's")


def main():
    backend = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        os.path.dirname(DOCS), "mijn-inkomen-gzac-backend-v13")
    basis = os.path.join(backend, "src", "main", "resources", "config", "building-block")
    if not os.path.isdir(basis):
        print(f"Bouwblokken niet gevonden: {basis}", file=sys.stderr)
        return 1

    config = os.path.join(backend, "src", "main", "resources", "config")
    calls, _namen = bouw_aanroepindex(config)

    os.makedirs(UIT, exist_ok=True)
    mappen = sorted(p for p in glob.glob(f"{basis}/{PREFIX}*") if os.path.isdir(p))
    gemaakt = []
    for m in mappen:
        d = lees_bouwblok(m)
        ids = d["proces_ids"] or [d["key"]]
        d["ketens"] = [k for pid in ids for k in ketens(pid, calls)]
        pad = os.path.join(UIT, d["key"] + ".md")
        open(pad, "w", encoding="utf-8").write(schrijf_pagina(d))
        gemaakt.append(d)
        io = f"{len(d['input'])} in / {len(d['output'])} uit"
        print(f"  {d['key']:48s} {len(d['stappen']):3d} stappen  {io}")

    werk_summary_bij(gemaakt)
    print(f"\n{len(gemaakt)} pagina's geschreven naar {os.path.relpath(UIT, DOCS)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())

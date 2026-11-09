#!/usr/bin/env python3
"""Controleer documentatie op herleidbare gegevens.

Gebruik:
    python3 .claude/skills/privacy-check/scripts/check_privacy.py [pad ...]
    python3 .claude/skills/privacy-check/scripts/check_privacy.py --review

Exitcode 1 bij bevindingen in de categorie BLOKKEREND.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SKILL_DIR = os.path.dirname(HERE)
ROOT = os.path.abspath(os.path.join(SKILL_DIR, "..", "..", ".."))

EXTENSIES = (".md", ".yaml", ".yml")
# De skill beschrijft zijn eigen zoektermen en zou zichzelf anders flaggen.
UITGESLOTEN_MAPPEN = {".git", ".claude", "node_modules", ".venv", "__pycache__"}

BLOKKEREND, REVIEW = "BLOKKEREND", "REVIEW"

# Placeholder-domeinen die juist bedoeld zijn als voorbeeld.
VEILIGE_DOMEINEN = ("example.com", "example.org", "example.net", "example.invalid",
                    "test", "localhost", "invalid")

# Hosts die naar publieke projectbronnen wijzen, geen omgevingen.
VEILIGE_HOSTS = ("localhost", "127.0.0.1", "0.0.0.0", "github.com", "gitlab.com",
                 "cdn.jsdelivr.net", "docs.gitbook.com", "www.gitbook.com")

# Woorden die na een lidwoord/tussenvoegsel een systeem of domeinterm aanduiden,
# geen achternaam. Houdt de persoonsnaam-heuristiek bruikbaar.
SYSTEEMWOORDEN = {
    "Objects", "Objecttypes", "Documenten", "Zaken", "Catalogi", "Besluiten",
    "Notificaties", "Open", "Zaak", "Spring", "Boot", "Camunda", "Suwinet",
    "Haal", "Centraal", "Mail", "MailHog", "Compose", "Docker", "Keycloak",
    "Socrates", "Valtimo", "GZAC", "Participatiewet", "Nederlandse", "Nederland",
    "Informatieverzoek", "Informatieverzoeken", "Printstraat", "Smart",
    "SmartDocuments", "Mijn", "Inkomen", "Form", "Portal", "Release", "Junin",
    "Algemene", "Bijstand", "IOAW", "Beslist", "Afgehandeld", "Voorschot",
    "Verstrekt", "Geweigerd", "Afgebroken", "Toekenningsbesluit", "Intrekking",
    "Afwijzingsbesluit", "Initiator", "Audit", "Voortgang", "Samenvatting",
    "Brede", "Intake", "Woonsituatie", "Vermogen", "Bewoning", "Notities",
    "Status", "Statussen", "Labels", "Dashboards", "Objectmanagement",
    "Datamodel", "Architectuur", "Configuratie", "Begrippenlijst", "Zaaktypen",
    "Business", "Vaststelling", "Vaststellen", "Overwegen", "Vastleggen",
    "Verwerken", "Annuleren", "Uitzetten", "Beoordelen", "Aanvraag", "Dienst",
    "Adressen", "Brongegevens", "Gegevens", "Fase", "Fasen", "Besluit",
    "Bezwaartermijn", "Hersteltermijn", "Portaaltaak", "Poortonderzoek",
    "Norm", "Normbedragen", "Bijstandsvorm", "Uitsluitingsgronden",
    "Verblijfstitel", "Verblijfadres", "Ingangsdatum", "Identiteit", "Relaties",
    "Voorliggende", "Medebewoners", "Kostendelersnorm", "Werken", "Handhaving",
    "Koppelingen", "Integraties", "Beheer", "Gemeente", "Rijn", "Maas", "IJssel",
    "Gelre", "Betuwe", "Geul", "Hunze", "Wolden", "Bilt", "Fryske", "Marren",
    "Ronde", "Venen", "Helder", "Haag", "Mierden", "Boer", "Cuijk", "Hubert",
    "Twente", "Duurstede", "Zand", "Breugel", "Hunze", "Vecht", "Heuvelrug",
    "Broec", "Kroon", "Meren", "Waard", "Beveland", "Delfland", "Drenthe",
    "Groningen", "Fryslan",
}

# Bewust zonder 'te' en 'het': dat zijn in deze teksten vrijwel altijd gewone
# woorden ("te laat", "pas het formulier aan") en geen tussenvoegsel.
TUSSENVOEGSELS = r"(?:van der|van den|van de|van 't|van|de|den|der|ten|ter|op den|aan de)"


def laad_gemeenten():
    pad = os.path.join(SKILL_DIR, "references", "gemeenten.txt")
    hard, ambigu, bucket = [], [], "hard"
    if not os.path.exists(pad):
        print(f"! gemeentelijst ontbreekt: {pad}", file=sys.stderr)
        return hard, ambigu
    for regel in open(pad, encoding="utf-8"):
        regel = regel.strip()
        if not regel or regel.startswith("#"):
            continue
        if regel.lower() == "[ambigu]":
            bucket = "ambigu"
            continue
        (hard if bucket == "hard" else ambigu).append(regel)
    return hard, ambigu


def laad_allowlist():
    pad = os.path.join(SKILL_DIR, "allowlist.txt")
    if not os.path.exists(pad):
        return set()
    return {
        r.strip() for r in open(pad, encoding="utf-8")
        if r.strip() and not r.strip().startswith("#")
    }


def verzamel_bestanden(paden):
    bestanden = []
    for p in paden:
        if os.path.isfile(p):
            bestanden.append(p)
            continue
        for dirpath, dirnames, filenames in os.walk(p):
            dirnames[:] = [d for d in dirnames if d not in UITGESLOTEN_MAPPEN]
            for fn in sorted(filenames):
                if fn.endswith(EXTENSIES):
                    bestanden.append(os.path.join(dirpath, fn))
    return sorted(set(bestanden))


def regelnr(tekst, pos):
    return tekst.count("\n", 0, pos) + 1


def context(tekst, start, eind, breedte=48):
    a = max(0, start - breedte)
    b = min(len(tekst), eind + breedte)
    frag = tekst[a:b].replace("\n", " ")
    return ("…" if a else "") + re.sub(r"\s+", " ", frag).strip() + ("…" if b < len(tekst) else "")


def scan(bestand, tekst, gem_hard, gem_ambigu, allowlist):
    treffers = []

    def voeg_toe(ernst, categorie, match, waarde=None):
        w = waarde if waarde is not None else match.group(0)
        if w in allowlist:
            return
        treffers.append({
            "ernst": ernst, "categorie": categorie, "bestand": bestand,
            "regel": regelnr(tekst, match.start()), "waarde": w,
            "context": context(tekst, match.start(), match.end()),
        })

    # --- e-mailadressen ---------------------------------------------------
    for m in re.finditer(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", tekst):
        adres = m.group(0)
        if any(adres.lower().endswith(d) or f".{d}" in adres.lower() for d in VEILIGE_DOMEINEN):
            continue
        voeg_toe(BLOKKEREND, "E-mailadres", m)

    # --- gemeenten --------------------------------------------------------
    for naam in gem_hard:
        for m in re.finditer(rf"\b{re.escape(naam)}\b", tekst):
            voeg_toe(BLOKKEREND, "Gemeentenaam", m, naam)
    for naam in gem_ambigu:
        for m in re.finditer(rf"\b{re.escape(naam)}\b", tekst):
            voeg_toe(REVIEW, "Mogelijke gemeentenaam", m, naam)

    # --- persoonsnamen ----------------------------------------------------
    # Hoge precisie: Voornaam + tussenvoegsel + Achternaam. De achternaam mag
    # geen systeemterm zijn, anders vangt dit zinnen als "Zie de Objects API".
    for m in re.finditer(rf"\b[A-Z][a-z]{{2,}}\s+{TUSSENVOEGSELS}\s+([A-Z][a-z]{{2,}})", tekst):
        if m.group(1) in SYSTEEMWOORDEN:
            continue
        voeg_toe(BLOKKEREND, "Persoonsnaam", m)
    # Aanhef of titel.
    for m in re.finditer(r"\b(?:dhr\.?|mevr\.?|mevrouw|de heer|drs\.|mr\.|ir\.|ing\.)\s+[A-Z][a-z]{2,}",
                         tekst, re.I):
        voeg_toe(BLOKKEREND, "Aanhef met naam", m)
    # Heuristisch: tussenvoegsel + hoofdletterwoord dat geen systeemterm is.
    for m in re.finditer(rf"\b{TUSSENVOEGSELS}\s+([A-Z][a-z]{{2,}})", tekst):
        if m.group(1) in SYSTEEMWOORDEN:
            continue
        voeg_toe(REVIEW, "Mogelijke achternaam", m)

    # --- nummers ----------------------------------------------------------
    for m in re.finditer(r"(?<![\w.-])\d{8,9}(?![\w.-])", tekst):
        voeg_toe(BLOKKEREND, "Mogelijk BSN", m)
    for m in re.finditer(r"\bNL\d{2}\s?[A-Z]{4}(?:\s?\d{4}){2}\s?\d{2}\b", tekst):
        voeg_toe(BLOKKEREND, "IBAN", m)
    for m in re.finditer(r"(?<![\w-])(?:\+31\s?\(?0?\)?\s?\d|0[1-9]\d?[-\s]?\d{6,8})(?![\w-])", tekst):
        voeg_toe(BLOKKEREND, "Telefoonnummer", m)
    for m in re.finditer(r"\b[1-9]\d{3}\s?[A-Z]{2}\b", tekst):
        voeg_toe(REVIEW, "Mogelijke postcode", m)

    # --- secrets en omgevingen -------------------------------------------
    for m in re.finditer(
        r'"(?:clientSecret|authenticationSecret|password|secret|apiKey|basicAuthSecret)"\s*:\s*"([^"$][^"]*)"',
        tekst, re.I,
    ):
        voeg_toe(BLOKKEREND, "Ingevulde secret", m)
    # Host zonder poort en zonder Markdown-linksyntax, anders matcht
    # "localhost:8080](http:" en valt een veilige host alsnog door de mand.
    for m in re.finditer(r"https?://([^\s/:)\"'\]]+)", tekst):
        host = m.group(1).lower()
        if host.startswith("${") or any(host == h or host.endswith("." + h) for h in VEILIGE_HOSTS):
            continue
        voeg_toe(REVIEW, "Omgevings-URL", m, m.group(0))
    for m in re.finditer(r"\bRSIN\b\s*[:=]?\s*(\d{9})", tekst, re.I):
        voeg_toe(BLOKKEREND, "Ingevulde RSIN", m)

    return treffers


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    toon_review = "--review" in sys.argv or "-r" in sys.argv

    paden = args or [ROOT]
    gem_hard, gem_ambigu = laad_gemeenten()
    allowlist = laad_allowlist()

    bestanden = verzamel_bestanden(paden)
    if not bestanden:
        print("Geen bestanden gevonden om te scannen.")
        return 0

    alle = []
    for b in bestanden:
        try:
            tekst = open(b, encoding="utf-8").read()
        except (UnicodeDecodeError, OSError) as e:
            print(f"! overgeslagen {b}: {e}", file=sys.stderr)
            continue
        alle.extend(scan(b, tekst, gem_hard, gem_ambigu, allowlist))

    blok = [t for t in alle if t["ernst"] == BLOKKEREND]
    rev = [t for t in alle if t["ernst"] == REVIEW]

    def toon(titel, items):
        print(f"\n{titel} ({len(items)})")
        print("-" * len(f"{titel} ({len(items)})"))
        if not items:
            print("  geen")
            return
        per_cat = {}
        for t in items:
            per_cat.setdefault(t["categorie"], []).append(t)
        for cat in sorted(per_cat):
            print(f"\n  {cat}:")
            for t in per_cat[cat]:
                rel = os.path.relpath(t["bestand"], ROOT)
                if rel.startswith(".."):  # buiten de repo: toon het volle pad
                    rel = t["bestand"]
                print(f"    {rel}:{t['regel']}  →  {t['waarde']}")
                print(f"      {t['context']}")

    print(f"Gescand: {len(bestanden)} bestanden")
    print(f"Gemeentelijst: {len(gem_hard)} namen + {len(gem_ambigu)} ambigu")
    if allowlist:
        print(f"Allowlist: {len(allowlist)} termen")

    toon("BLOKKEREND", blok)
    if toon_review:
        toon("REVIEW — zelf beoordelen", rev)
    else:
        print(f"\nREVIEW: {len(rev)} twijfelgevallen (toon met --review)")

    print()
    if blok:
        print(f"❌ {len(blok)} blokkerende bevinding(en). Niet pushen voordat deze zijn opgelost.")
        return 1
    print("✅ Geen blokkerende bevindingen.")
    print("   Let op: afbeeldingen zijn niet gescand en namen zonder tussenvoegsel")
    print("   worden niet gevonden. Dit is geen absolute garantie.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

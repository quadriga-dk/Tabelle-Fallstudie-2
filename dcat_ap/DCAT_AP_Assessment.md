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

# 🏆Selbsttest: Wissen und Praxis

````{admonition} Hinweis
:class: hinweis
Diese Übungsaufgaben dienen Ihrer Selbsteinschätzung und helfen Ihnen, das im Kapitel Gelernte zu reflektieren.

Sie können die Fragen in beliebiger Reihenfolge beantworten und auch mehrfach versuchen. 

**So funktioniert es:**
- Wählen Sie bei jeder Frage die Antwort(en), die Sie für richtig halten
- Lesen Sie das Feedback zu den einzelnen Antwortoptionen sorgfältig durch
- Die Erklärungen helfen Ihnen, Ihr Verständnis zu vertiefen – auch bei korrekten Antworten 

Es erfolgt keine Bewertung oder Speicherung Ihrer Ergebnisse. Nutzen Sie dieses Assessment, um Wissenslücken zu identifizieren und gegebenenfalls die entsprechenden Abschnitte des Kapitels noch einmal zu bearbeiten. 

**Geschätzte Zeit**: XX

Viel Erfolg!
````

## Frage 1

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question1 = [
    {
        "question": "Was ist DCAT und wofür wurde es entwickelt?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "DCAT ist ein RDF-basiertes Vokabular zur Beschreibung von Datenkatalogen im Web",
                "correct": True,
                "feedback": """✓ Korrekt! DCAT (Data Catalog Vocabulary) ist ein RDF-Vokabular:
                - Basiert auf RDF (Resource Description Framework)
                - Speziell für Datenkataloge entwickelt
                - Ermöglicht Interoperabilität zwischen Datenportalen
                - Vom W3C standardisiert"""
            },
            {
                "answer": "DCAT ist eine Programmiersprache für Datenbanken",
                "correct": False,
                "feedback": """× Nicht korrekt. DCAT ist keine Programmiersprache:
                - Es ist ein Metadaten-Vokabular
                - Dient der Beschreibung, nicht der Programmierung
                - Basiert auf RDF/XML oder Turtle
                - Wird für Metadatenstandards genutzt"""
            },
            {
                "answer": "DCAT wurde im Kontext von staatlichen Datenkatalogen wie data.gov entwickelt",
                "correct": True,
                "feedback": """✓ Korrekt! Wichtiger Kontext:
                - Entwickelt für staatliche Datenportale
                - data.gov und data.gov.uk waren treibende Beispiele
                - Ziel: Interoperabilität zwischen Portalen
                - Politisch unterstützte Initiative"""
            },
            {
                "answer": "DCAT ist ein Tool zur Datenanalyse",
                "correct": False,
                "feedback": """× Nicht korrekt. Wichtige Unterscheidung:
                - DCAT beschreibt Daten, analysiert sie aber nicht
                - Es ist ein Metadatenstandard
                - Fokus: Auffindbarkeit und Katalogisierung
                - Nicht für Datenverarbeitung gedacht"""
            }
        ]
    }
]
display_quiz(question1, colors=colors.jupyterquiz)
```

## Frage 2

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question2 = [
    {
        "question": "Welche Aussagen über den Dublin Core Metadatenstandard sind korrekt? Wählen Sie alle zutreffenden Aussagen.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Dublin Core umfasst 15 Kernelemente zur Beschreibung von Ressourcen",
                "correct": True,
                "feedback": """✓ Korrekt! Die 15 Elemente sind:
                - Urheber, Mitwirkende, Herausgeber
                - Titel, Datum, Sprache, Format
                - Thema, Beschreibung, Kennung
                - Bezug, Quelle, Typ, Abdeckung, Rechte
                - Definiert 1995 in Dublin, Ohio"""
            },
            {
                "answer": "Dublin Core verwendet URIs zur Identifikation von Ressourcen und Begriffen",
                "correct": True,
                "feedback": """✓ Korrekt! URI-Verwendung ist zentral:
                - Eindeutige Identifikation von Objekten
                - Auch für Vokabularbegriffe
                - Ermöglicht Linked Data
                - Basis für Semantic Web"""
            },
            {
                "answer": "Dublin Core ist ausschließlich für Bibliotheken entwickelt worden",
                "correct": False,
                "feedback": """× Nicht korrekt! Dublin Core ist domänenunabhängig:
                - Bibliotheken, Archive, Museen
                - E-Government, Wissenschaft
                - Verlagswesen, Bildung
                - Bewusst generisch gehalten"""
            },
            {
                "answer": "Dublin Core unterstützt die Erstellung von Anwendungsprofilen (Application Profiles)",
                "correct": True,
                "feedback": """✓ Korrekt! Application Profiles sind wichtig:
                - Anpassung an spezifische Anforderungen
                - Kombination mit spezialisierten Vokabularen
                - Beispiel: DCAT-AP basiert auf Dublin Core
                - Flexibilität bei Beibehaltung der Interoperabilität"""
            }
        ]
    }
]
display_quiz(question2, colors=colors.jupyterquiz)
```

## Frage 3

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")
from assessment import DragDropQuiz

quiz = DragDropQuiz()

quiz.create_matching_quiz(
    title="Ordnen Sie die Portale den Ebenen der Dateninfrastruktur zu:",
    descriptions=[
        "GovData",
        "data.europa.eu",
        "daten.berlin.de",
        "Transparenzportal Hamburg"
    ],
    options=["Lokal/Regional", "National (Deutschland)", "Europäisch", "International"],
    correct_mapping={
        "GovData": "National (Deutschland)",
        "data.europa.eu": "Europäisch",
        "daten.berlin.de": "Lokal/Regional",
        "Transparenzportal Hamburg": "Lokal/Regional"
    }
)
```

## Frage 4

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question4 = [
    {
        "question": "Wie funktioniert die mehrstufige Dateninfrastruktur von Metadatenportalen? Wählen Sie alle zutreffenden Aussagen.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Lokale Datensätze werden zunächst auf kommunaler oder Landesebene erfasst",
                "correct": True,
                "feedback": """✓ Korrekt! Bottom-up-Ansatz:
                - Datenbereitstellung beginnt lokal
                - Kommunen und Landesbehörden als Quellen
                - Beispiele: Berlin Open Data, DatenAdler Brandenburg
                - Dezentrale Datenerzeugung"""
            },
            {
                "answer": "Zentrale Portale wie GovData harvesten Daten von regionalen Portalen",
                "correct": True,
                "feedback": """✓ Korrekt! Harvesting-Prozess:
                - Automatische Metadatensammlung
                - Von unteren Ebenen zu höheren
                - Aggregation ohne Datenduplikation
                - Zentrale Durchsuchbarkeit"""
            },
            {
                "answer": "Alle Datensätze werden direkt auf data.europa.eu gespeichert",
                "correct": False,
                "feedback": """× Nicht korrekt! Wichtige Unterscheidung:
                - Metadaten werden geharvested, nicht Daten selbst
                - Datensätze bleiben bei Datenbereitstellern
                - Zentrale Portale bieten oft nur Links
                - Vermeidung von Redundanz"""
            },
            {
                "answer": "Der Vorteil zentraler Plattformen liegt im Vergleich von Datensätzen verschiedener Quellen",
                "correct": True,
                "feedback": """✓ Korrekt! Mehrwert der Zentralisierung:
                - Vergleichbarkeit: z.B. Baumkataster mehrerer Städte
                - Überregionale Suche möglich
                - Einheitliche Schnittstellen
                - Bessere Auffindbarkeit"""
            }
        ]
    }
]
display_quiz(question4, colors=colors.jupyterquiz)
```

## Frage 5

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question5 = [
    {
        "question": "Was ist der Hauptunterschied zwischen DCAT-AP und DCAT-AP.de?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "DCAT-AP.de ist die deutsche Anpassung des europäischen DCAT-AP-Standards",
                "correct": True,
                "feedback": """✓ Korrekt! Nationale Anpassung:
                - Basiert auf DCAT-AP v2.0
                - Entwickelt durch Fachgruppe GovData
                - Eingeführt November 2016
                - Pflichtstandard seit 2019 für GovData
                - Berücksichtigt deutsche Anforderungen"""
            },
            {
                "answer": "DCAT-AP.de funktioniert nur in Deutschland, DCAT-AP nur in anderen EU-Ländern",
                "correct": False,
                "feedback": """× Nicht korrekt! Wichtige Kompatibilität:
                - DCAT-AP.de ist kompatibel mit DCAT-AP
                - Deutsche Datensätze können zu data.europa.eu übertragen werden
                - Interoperabilität ist gewährleistet
                - Nationale Anpassung ≠ Isolation"""
            },
            {
                "answer": "DCAT-AP.de ermöglicht grenzüberschreitende Datennutzung innerhalb der EU",
                "correct": True,
                "feedback": """✓ Korrekt! Europäische Integration:
                - Kompatibilität mit europäischem Datenportal
                - Reibungslose Übertragung deutscher Daten
                - Einheitliche Datennutzung in EU
                - Fördert länderübergreifende Zusammenarbeit"""
            },
            {
                "answer": "DCAT-AP ist nur ein theoretisches Konzept, DCAT-AP.de die praktische Umsetzung",
                "correct": False,
                "feedback": """× Nicht korrekt! Beide sind praktisch:
                - DCAT-AP wird in vielen EU-Ländern genutzt
                - Verschiedene nationale Anpassungen existieren
                - Beide sind implementierte Standards
                - DCAT-AP.de ist EINE von mehreren nationalen Versionen"""
            }
        ]
    }
]
display_quiz(question5, colors=colors.jupyterquiz)
```

## Frage 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question6 = [
    {
        "question": "Welche Hauptkomponenten gehören zur Struktur von DCAT-AP? Wählen Sie alle zutreffenden Aussagen.",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "dcat:Catalog - beschreibt den Datenkatalog selbst",
                "correct": True,
                "feedback": """✓ Korrekt! Catalog ist die oberste Ebene:
                - Beschreibt das gesamte Datenportal
                - Enthält Metadaten zum Katalog
                - Gruppiert Datensätze
                - Z.B. GovData als Katalog"""
            },
            {
                "answer": "dcat:Dataset - beschreibt einen konkreten Datensatz",
                "correct": True,
                "feedback": """✓ Korrekt! Dataset ist zentral:
                - Kerneinheit der Beschreibung
                - Enthält Titel, Beschreibung, Thema
                - Verknüpft mit Distributionen
                - Z.B. Baumkataster Berlin"""
            },
            {
                "answer": "dcat:Distribution - beschreibt eine spezifische Zugangsform zum Datensatz",
                "correct": True,
                "feedback": """✓ Korrekt! Distribution für Zugriff:
                - Verschiedene Formate (CSV, JSON, XML)
                - Download-URLs oder API-Endpunkte
                - Ein Dataset kann mehrere Distributionen haben
                - Z.B. CSV-Download und API-Zugriff"""
            },
            {
                "answer": "dcat:UserProfile - beschreibt Benutzerkonten",
                "correct": False,
                "feedback": """× Nicht korrekt. Nicht Teil von DCAT-AP:
                - DCAT-AP beschreibt Datenkataloge, nicht Nutzer
                - Benutzerverwaltung ist separate Funktionalität
                - Fokus: Daten und deren Beschreibung
                - Keine Elemente für Authentifizierung"""
            }
        ]
    }
]
display_quiz(question6, colors=colors.jupyterquiz)
```

## Frage 7

**Szenario:** Eine Stadt möchte ihre Umweltdaten (Luftqualität, Lärmkarten, Grünflächenkataster) über ein Datenportal bereitstellen und sicherstellen, dass diese auch auf Landes-, Bundes- und EU-Ebene gefunden werden können.

**Aufgaben:**
1. Welchen Metadatenstandard sollte die Stadt verwenden und warum?
2. Welche drei Hauptkomponenten müssen für jeden Datensatz beschrieben werden?
3. Wie stellt die Stadt sicher, dass ihre Daten auf data.europa.eu sichtbar werden?
4. Welche Vorteile hat die Verwendung von DCAT-AP.de für die Stadt?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")
from assessment import create_answer_box

create_answer_box('dcat-ap-1')
```

````{admonition} Musterlösung
:class: solution, dropdown

**Musterlösung:**

**1. Welchen Metadatenstandard sollte die Stadt verwenden?**

**Empfehlung: DCAT-AP.de**

**Begründung:**
- **Pflichtstandard:** GovData akzeptiert seit 2019 nur DCAT-AP.de
- **Kompatibilität:** Kompatibel mit DCAT-AP (Europa)
- **Interoperabilität:** Ermöglicht Datenaustausch zwischen Ebenen
- **Standardisierung:** Einheitliche Struktur für alle deutschen Behörden
- **Zukunftssicherheit:** Aktuell Spezifikation 3.0

**Technische Umsetzung:**
- Metadaten in RDF/XML oder Turtle serialisieren
- DCAT-AP.de Vokabular verwenden
- Mit lokalem/regionalem Portal beginnen

---

**2. Drei Hauptkomponenten für jeden Datensatz:**

**A) Catalog (dcat:Catalog)**
- Beschreibung: Das Datenportal der Stadt
- Eigenschaften:
  - dct:title: "Umweltdaten Stadt X"
  - dct:description: Beschreibung des Portals
  - dct:publisher: Stadt X
  - dcat:dataset: Links zu allen Datensätzen

**B) Dataset (dcat:Dataset)**
- Beschreibung: Konkrete Datensätze
- Für jeden Datensatz:
  
  **Beispiel Luftqualität:**
  ```turtle
  :luftqualitaet a dcat:Dataset ;
    dct:title "Luftqualitätsmessdaten Stadt X" ;
    dct:description "Stündliche Messungen von PM10, NO2, O3" ;
    dct:publisher :stadtX ;
    dcat:keyword "Luftqualität", "Umwelt", "Gesundheit" ;
    dct:temporal [
      schema:startDate "2020-01-01" ;
      schema:endDate "2024-12-31"
    ] ;
    dct:spatial :stadtX_geometrie ;
    dcat:distribution :luftqualitaet_csv, :luftqualitaet_api .
  ```

**C) Distribution (dcat:Distribution)**
- Beschreibung: Zugangsformen zu den Daten
- Mehrere Distributionen pro Dataset möglich:

  **Beispiel CSV-Download:**
  ```turtle
  :luftqualitaet_csv a dcat:Distribution ;
    dct:title "Luftqualität als CSV" ;
    dct:format "text/csv" ;
    dcat:accessURL <https://daten.stadtx.de/luftqualitaet> ;
    dcat:downloadURL <https://daten.stadtx.de/luftqualitaet.csv> ;
    dcat:byteSize "2500000"^^xsd:decimal .
  ```

  **Beispiel API:**
  ```turtle
  :luftqualitaet_api a dcat:Distribution ;
    dct:title "Luftqualität API" ;
    dct:format "application/json" ;
    dcat:accessURL <https://api.stadtx.de/luftqualitaet> .
  ```

---

**3. Sichtbarkeit auf data.europa.eu sicherstellen:**

**Schritt-für-Schritt-Prozess:**

**Schritt 1: Lokales/Regionales Portal**
- Daten mit DCAT-AP.de beschreiben
- Auf lokalem Portal veröffentlichen
- Harvesting-Schnittstelle bereitstellen

**Schritt 2: Landesebene**
- Metadaten werden von Landesportal geharvested
- Beispiel: Daten fließen zu Berliner Open Data Portal
- Qualitätssicherung auf Landesebene

**Schritt 3: Nationale Ebene (GovData)**
- GovData harvested von Landesportalen
- Automatische Übernahme bei DCAT-AP.de-Konformität
- Zentrale Durchsuchbarkeit in Deutschland

**Schritt 4: Europäische Ebene**
- GovData ist mit data.europa.eu verbunden
- Automatische Weitergabe deutscher Datensätze
- Sichtbarkeit in ganz Europa

**Technische Voraussetzungen:**
- DCAT-AP.de-konforme Metadaten
- OAI-PMH oder SPARQL-Endpunkt für Harvesting
- Regelmäßige Aktualisierung der Metadaten
- Stabile URLs für Datensätze

---

**4. Vorteile von DCAT-AP.de für die Stadt:**

**A) Auffindbarkeit**
- **Lokal:** Bürger finden Daten direkt
- **Regional:** Vergleich mit anderen Städten des Bundeslandes
- **National:** Sichtbarkeit auf GovData
- **Europäisch:** Internationale Forscher können Daten finden
- **Suchmaschinen:** Bessere Indexierung durch Standardisierung

**B) Interoperabilität**
- **Einheitliche Struktur:** Andere können Daten leicht integrieren
- **Maschinenlesbarkeit:** Automatische Verarbeitung möglich
- **API-Kompatibilität:** Einheitliche Schnittstellen
- **Linked Data:** Verknüpfung mit anderen Datenquellen

**C) Effizienz**
- **Einmalige Erfassung:** Daten werden nur einmal beschrieben
- **Automatisches Harvesting:** Keine manuelle Übertragung nötig
- **Standardisierte Prozesse:** Weniger Abstimmungsaufwand
- **Wiederverwendbare Tools:** CKAN und andere Standards-basierte Software

**D) Compliance**
- **Rechtliche Anforderungen:** Erfüllung von Open-Data-Vorgaben
- **Transparenzgesetze:** Unterstützung gesetzlicher Pflichten
- **EU-Richtlinien:** Konformität mit europäischen Standards
- **Best Practices:** Orientierung an etablierten Standards

**E) Nachnutzung**
- **Wissenschaft:** Forscher können Daten für Studien nutzen
- **Wirtschaft:** Unternehmen für Anwendungen und Services
- **Zivilgesellschaft:** NGOs für Monitoring und Advocacy
- **Verwaltung:** Andere Behörden für eigene Zwecke

**Konkrete Beispiele:**
- Luftqualitätsdaten können mit Gesundheitsdaten verknüpft werden
- Lärmkarten ermöglichen Stadtplanung über Stadtgrenzen hinweg
- Grünflächenkataster unterstützt europäische Biodiversitätsstudien

````

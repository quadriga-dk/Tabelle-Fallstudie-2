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


# Übung

Bevor wir im nächsten Abschnitt über das in diesem Kapitel Gelernte refelktieren, können Sie hier Ihr Wissen in einem Quiz auf die Probe stellen. Viel Erfolg!



```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question1 = [{
    "question": """Wofür steht die Abkürzung DCAT-AP?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Data Catalog Application Profile",
            "correct": True,
            "feedback": """✓ Richtig! DCAT-AP ist ein Anwendungsprofil des DCAT-Vokabulars, speziell für die Beschreibung von Datenkatalogen."""
        },
        {
            "answer": "Digital Catalog and Archive Protocol",
            "correct": False,
            "feedback": """× Nein. DCAT-AP bezieht sich auf Metadatenstandards, nicht auf Protokolle."""
        },
        {
            "answer": "Data Collection and Analysis Tool",
            "correct": False,
            "feedback": """× Das ist leider nicht richtig. DCAT-AP dient der Beschreibung von Datenkatalogen, nicht der Datensammlung oder -analyse."""
        },
        {
            "answer": "Document Catalog and Access Tool",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP ist ein Metadatenstandard, kein Werkzeug."""
        },
    ]
}]

display_quiz(question1, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question2 = [{
    "question": """Welches ist ein zentrales Ziel von DCAT-AP?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Entwicklung neuer Datenbanken",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP ist ein Metadatenstandard, kein Datenbankentwicklungswerkzeug."""
        },
        {
            "answer": "Die Standardisierung von Metadaten für Datenkataloge",
            "correct": True,
            "feedback": """✓ Richtig! DCAT-AP soll die Interoperabilität und Auffindbarkeit von Daten durch standardisierte Metadaten verbessern."""
        },
        {
            "answer": "Die Automatisierung von Datenanalysen",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP unterstützt die Beschreibung, nicht die Analyse von Daten."""
        },
        {
            "answer": "Die Erstellung von Benutzerkonten für Datenportale",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP hat nichts mit Benutzerverwaltung zu tun."""
        },
    ]
}]

display_quiz(question2, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question3 = [{
    "question": """Welche der folgenden Komponenten gehört NICHT zur typischen Struktur eines DCAT-AP-Datensatzes?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "dcat:Dataset",
            "correct": False,
            "feedback": """× Falsch. dcat:Dataset ist eine zentrale Klasse in DCAT-AP."""
        },
        {
            "answer": "dcat:Distribution",
            "correct": False,
            "feedback": """× Falsch. dcat:Distribution beschreibt die Zugangsform zu einem Datensatz."""
        },
        {
            "answer": "dcat:UserAccount",
            "correct": True,
            "feedback": """✓ Richtig! DCAT-AP beschreibt Datenkataloge und -verteilungen, nicht Benutzerkonten."""
        },
        {
            "answer": "dcat:CatalogRecord",
            "correct": False,
            "feedback": """× Falsch. dcat:CatalogRecord ist eine optionale Klasse für Katalogeinträge."""
        },
    ]
}]

display_quiz(question3, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question4 = [{
    "question": """Welches der folgenden Metadatenportale nutzt DCAT-AP?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Google Drive",
            "correct": False,
            "feedback": """× Falsch. Google Drive ist ein Speicherdienst, kein Metadatenportal."""
        },
        {
            "answer": "GitHub",
            "correct": False,
            "feedback": """× Falsch. GitHub ist eine Plattform für Softwareentwicklung, nicht für DCAT-AP-Metadaten."""
        },
        {
            "answer": "Dropbox",
            "correct": False,
            "feedback": """× Falsch. Dropbox ist ein Cloud-Speicherdienst, kein Metadatenportal."""
        },
        {
            "answer": "Das europäische Datenportal (data.europa.eu)",
            "correct": True,
            "feedback": """✓ Richtig! Das europäische Datenportal setzt DCAT-AP für die Beschreibung von Metadaten ein."""
        },
    ]
}]

display_quiz(question4, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question5 = [{
    "question": """Welche Rolle spielt dct:title in einem DCAT-AP-Datensatz?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Beschreibt die Lizenz des Datensatzes",
            "correct": False,
            "feedback": """× Falsch. Für Lizenzen wird dct:license oder dct:rights verwendet."""
        },
        {
            "answer": "Gibt den Titel des Datensatzes an",
            "correct": True,
            "feedback": """✓ Richtig! dct:title ist ein Dublin-Core-Element für den Titel eines Datensatzes."""
        },
        {
            "answer": "Enthält die URL des Datensatzes",
            "correct": False,
            "feedback": """× Falsch. Die URL wird mit dcat:accessURL oder dcat:downloadURL angegeben."""
        },
        {
            "answer": "Definiert die Größe des Datensatzes",
            "correct": False,
            "feedback": """× Falsch. Die Größe wird mit dcat:byteSize oder ähnlichen Eigenschaften beschrieben."""
        },
    ]
}]

display_quiz(question5, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question6 = [{
    "question": """Welches Format wird typischerweise für die Serialisierung von DCAT-AP-Metadaten verwendet?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "CSV",
            "correct": False,
            "feedback": """× Falsch. CSV ist ein tabellarisches Datenformat, kein RDF-Format."""
        },
        {
            "answer": "JSON",
            "correct": False,
            "feedback": """× Leider nicht ganz korrekt. JSON-LD wäre möglich, aber klassischerweise wird RDF/XML oder Turtle genutzt."""
        },
        {
            "answer": "RDF/XML oder Turtle",
            "correct": True,
            "feedback": """✓ Richtig! DCAT-AP basiert auf RDF und wird oft in RDF/XML oder Turtle serialisiert."""
        },
        {
            "answer": "PDF",
            "correct": False,
            "feedback": """× Falsch. PDF ist ein Dokumentenformat, kein Metadatenformat."""
        },
    ]
}]


display_quiz(question6, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question7 = [{
    "question": """Welches der folgenden Beispiele ist ein typisches Anwendungsbeispiel für DCAT-AP?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Verwaltung von Benutzerprofilen in einem sozialen Netzwerk",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP dient der Beschreibung von Datenkatalogen, nicht von Benutzerprofilen."""
        },
        {
            "answer": "Die Beschreibung von offenen Behördendaten in einem nationalen Datenportal",
            "correct": True,
            "feedback": """✓ Richtig! DCAT-AP wird oft für die Beschreibung von offenen Daten in Portalen genutzt."""
        },
        {
            "answer": "Die Speicherung von Fotos in einer Cloud",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP ist ein Metadatenstandard, kein Speicherdienst."""
        },
        {
            "answer": "Die Analyse von Verkaufsdaten in einem Unternehmen",
            "correct": False,
            "feedback": """× Falsch. DCAT-AP unterstützt die Beschreibung, nicht die Analyse von Daten."""
        },
    ]
}]

display_quiz(question7, colors=colors.jupyterquiz)
```
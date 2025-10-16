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

Bevor es zur Reflexion über das in diesem Kapitel Gelernte geht, können Sie Ihr Wissen in diesem kurzen Quiz auf die Probe stellen. Viel Erfolg!



```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question1 = [{
    "question": """Was ist der Hauptunterschied zwischen dem klassischen World Wide Web und dem Semantic Web?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Das Semantic Web verwendet nur Text, während das klassische Web Bilder und Videos nutzt.",
            "correct": False,
            "feedback": """× Nein, beide nutzen multimediale Inhalte. Der Unterschied liegt in der maschinellen Verarbeitbarkeit, nicht im Inhaltstyp."""
        },
        {
            "answer": "Das Semantic Web ermöglicht Maschinen, die Bedeutung von Informationen zu verstehen, während das klassische Web nur für Menschen lesbar ist.",
            "correct": True,
            "feedback": """✓ Richtig! Das Semantic Web nutzt Metadaten und Ontologien, um Inhalte maschinenlesbar und verknüpfbar zu machen."""
        },
        {
            "answer": "Das Semantic Web ist langsamer als das klassische Web.",
            "correct": False,
            "feedback": """× Falsch, die Geschwindigkeit hängt von der Implementierung ab, nicht vom Konzept."""
        },
        {
            "answer": "Das Semantic Web existiert nur in der Theorie, während das klassische Web praktisch genutzt wird.",
            "correct": False,
            "feedback": """× Falsch, das Semantic Web wird bereits in vielen Anwendungen eingesetzt, z.B. in Wissensgraphen wie Wikidata."""
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
    "question": """RDF ist eine Sprache zur Gestaltung von Webseiten wie HTML.""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ja.",
            "correct": False,
            "feedback": """× Falsch, RDF dient zur Beschreibung und Verknüpfung von Daten, nicht zur Gestaltung von Webseiten."""
        },
        {
            "answer": "Nein.",
            "correct": True,
            "feedback": """✓ Richtig! RDF ist ein Framework zur Strukturierung von Daten und nicht für Webseiten-Design gedacht."""
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
    "question": """Welches der folgenden Prinzipien gehört NICHT zu den vier Linked-Data-Prinzipien nach Tim Berners-Lee?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Verwende URIs, um Dinge zu benennen.",
            "correct": False,
            "feedback": """× Falsch, das ist das erste Prinzip von Linked Data."""
        },
        {
            "answer": "Verwende HTTP-URIs, damit Menschen und Maschinen auf diese Dinge zugreifen können.",
            "correct": False,
            "feedback": """× Falsch, das ist das zweite Prinzip."""
        },
        {
            "answer": "Verwende nur geschlossene, proprietäre Datenformate.",
            "correct": True,
            "feedback": """✓ Genau! Linked Data setzt auf offene, standardisierte Formate wie RDF."""
        },
        {
            "answer": "Verlinke URIs, um Wissen im Web zu vernetzen.",
            "correct": False,
            "feedback": """× Falsch, das ist das vierte Prinzip."""
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
    "question": """OWL ist eine Sprache zur Erstellung von Ontologien.""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Nein.",
            "correct": False,
            "feedback": """× Falsch, OWL ist speziell für Ontologien entwickelt worden.."""
        },
        {
            "answer": "Ja.",
            "correct": True,
            "feedback": """✓ Genau! OWL wird zur Modellierung von Ontologien verwendet."""
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
    "question": """Welche Technologie gehört NICHT zu den Ebenen des Semantic Web Layer Cake?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "RDF",
            "correct": False,
            "feedback": """× Falsch, RDF ist eine zentrale Technologie für die Datenrepräsentation im Semantic Web."""
        },
        {
            "answer": "OWL",
            "correct": False,
            "feedback": """× Falsch, OWL wird für Ontologien und logische Schlussfolgerungen genutzt."""
        },
        {
            "answer": "SQL",
            "correct": True,
            "feedback": """✓ Richtig! SQL ist eine Datenbanksprache für relationale Datenbanken, nicht für das Semantic Web."""
        },
        {
            "answer": "SPARQL",
            "correct": False,
            "feedback": """× Falsch, SPARQL ist die Abfragesprache für RDF-Daten."""
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
    "question": """Linked Data bedeutet, dass Daten durch standardisierte Formate miteinander verknüpft werden.""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Nein.",
            "correct": False,
            "feedback": """× Falsch, das Hauptziel von Linked Data ist es, Daten in standardisierten Formaten zu verknüpfen."""
        },
        {
            "answer": "Ja.",
            "correct": True,
            "feedback": """✓ Richtig! Linked Data nutzt Standards zur Verknüpfung von Daten."""
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
    "question": """Welcher Schritt ist **nicht** notwendig, um Daten aus zwei verschiedenen Datenbanken als Linked Data zu verknüpfen?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Daten in ein gemeinsames Format wie RDF umwandeln.",
            "correct": False,
            "feedback": """× Falsch, das ist ein wichtiger Schritt, um Daten zu verknüpfen."""
        },
        {
            "answer": "Jeder Ressource eine eindeutige URI zuweisen.",
            "correct": False,
            "feedback": """× Falsch, das ist notwendig, um Ressourcen identifizierbar zu machen."""
        },
        {
            "answer": "Die Datenbanken physisch zusammenführen.",
            "correct": True,
            "feedback": """✓ Richtig! Linked Data setzt auf logische Verknüpfungen, nicht auf physische Zusammenführung."""
        },
        {
            "answer": "Abfragen mit SPARQL ermöglichen.",
            "correct": False,
            "feedback": """× Falsch, SPARQL ist wichtig, um die verknüpften Daten abzufragen."""
        },
    ]
}]

display_quiz(question7, colors=colors.jupyterquiz)
```
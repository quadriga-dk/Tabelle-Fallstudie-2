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

*Reichen die 4 kurzen Fragen? Die Lernziele sind: 
1. Begriffe wie Semantic Web und semantische Technologien können definiert werden.
2. Die Rolle von RDF im Semantic Web kann erklärt werden*


```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question1 = [{
    "question": """Das Semantic Web ermöglicht es Maschinen, die Bedeutung von Daten zu verstehen.""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ja.",
            "correct": True,
            "feedback": """✓ Richtig! Das Semantic Web macht Daten maschinenlesbar und verständlich."""
        },
        {
            "answer": "Nein.",
            "correct": False,
            "feedback": """× Falsch, das Hauptziel des Semantic Web ist genau das: Maschinen sollen Daten verstehen können."""
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

display_quiz(question3, colors=colors.jupyterquiz)
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question4 = [{
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


display_quiz(question4, colors=colors.jupyterquiz)
```

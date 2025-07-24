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
```{code-cell} ipython3
:tags: [remove_cell]
# Jupyterquiz
from jupyterquiz import display_quiz

# Coporate Design
import sys
sys.path.append("..")
from quadriga_config import colors
```

# Übungen

Bevor es zur Reflexion über das in diesem Kapitel Gelernte geht, können Sie Ihr Wissen in diesem kurzen Quiz auf die Probe stellen. Viel Erfolg!  


## Semantic Web

*Frage 2 kann raus, da sie nicht zielführend ist: Semantic Web soll laut Lernzielen definiert werden können.*

````{code-cell} ipython3
:tags: [remove_input]
questions = \
[
  { 'question': "1. Das Semantic Web ermöglicht es Maschinen, die Bedeutung von Daten zu verstehen.",
    'type': 'multiple_choice',
    'answers': [
    { 'answer': 'Ja',
      'correct': True,
      'feedback': 'Richtig! Das Semantic Web macht Daten maschinenlesbar und verständlich.'},
    { 'answer': 'Nein',
      'correct': False,
      'feedback': 'Falsch, das Hauptziel des Semantic Web ist genau das: Maschinen sollen Daten verstehen können.'},
    ]
  },

  { 'question': "2. Tim Berners-Lee hat das Konzept des Semantic Web erstmals 2010 vorgestellt.",
    'type': 'multiple_choice',
    'answers': [
    { 'answer': 'Ja',
      'correct': False,
      'feedback': 'Falsch, Tim Berners-Lee stellte das Konzept bereits 2001 vor.'},
    { 'answer': 'Nein',
      'correct': True,
      'feedback': 'Richtig! Die erste Veröffentlichung erfolgte im Jahr 2001.'},
    ]
  },

  { 'question': "3. RDF ist eine Sprache zur Gestaltung von Webseiten wie HTML.",
    'type': 'multiple_choice',
    'answers': [
    { 'answer': 'Ja',
      'correct': False,
      'feedback': 'Falsch, RDF dient zur Beschreibung und Verknüpfung von Daten, nicht zur Gestaltung von Webseiten.'},
    { 'answer': 'Nein',
      'correct': True,
      'feedback': 'Richtig! RDF ist ein Framework zur Strukturierung von Daten und nicht für Webseiten-Design gedacht.'},
    ]
  },

  { 'question': "4. OWL ist eine Sprache zur Erstellung von Ontologien.",
    'type': 'multiple_choice',
    'answers': [
    { 'answer': 'Ja',
      'correct': True,
      'feedback': 'Genau! OWL wird zur Modellierung von Ontologien verwendet.'},
    { 'answer': 'Nein',
      'correct': False,
      'feedback': 'Falsch, OWL ist speziell für Ontologien entwickelt worden.'},
    ]
  },

  { 'question': "5. Linked Data bedeutet, dass Daten durch standardisierte Formate miteinander verknüpft werden.",
    'type': 'multiple_choice',
    'answers': [
    { 'answer': 'Ja',
      'correct': True,
      'feedback': 'Richtig! Linked Data nutzt Standards zur Verknüpfung von Daten.'},
    { 'answer': 'Nein',
      'correct': False,
      'feedback': 'Falsch, das Hauptziel von Linked Data ist es, Daten in standardisierten Formaten zu verknüpfen.'},
    ]
  }
]

display_quiz(questions, colors = colors.jupyterquiz)
````

## RDF

*noch ergänzen*
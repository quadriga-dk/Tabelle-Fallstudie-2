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


(metadaten-übung)=
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

**Geschätzte Zeit**: XXX

Viel Erfolg!

````

## Multiple-Choice-Quiz


**Frage 1**

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question1 = [{
    "question": """Was untersucht der MQA?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Ob die Qualitätskriterien der Europäischen Union auf dem Portal eingehalten werden.",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. Das Portal data.europa.eu wird von der Europäischen Union betrieben. Die untersuchten Dimensionen sind aus den FAIR-Prinzipien abgeleitet."""
        },
        {
            "answer": "Die Qualität der von data.europa.eu gesammelten Metadaten.",
            "correct": True,
            "feedback": """✓ Richtig! Der MQA wurde eigens von einem Konsortium entwickelt, um die Qualität der auf dem Portal gesammelten Metadaten zu untersuchen. So soll Anbietern und Portalen geholfen werden, die Metadatenqualität zu überprüfen und sie ggf. zu verbessern."""
        },
        {
            "answer": "Die Datenverfügbarkeit auf dem Portal data.europa.eu",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. Der MQA untersucht nicht, ob die Daten verfügbar sind, sondern ob die Qualität ihrer Metadaten den Bewertungskriterien entspricht."""
        },
        {
            "answer": "Die Qualität der auf data.europa.eu zur Verfügung gestellten Daten.",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. Das Portal data.europa.eu stellt keine Daten zur Verfügung. Es sammelt Metadaten von anderen Portalen und Anbietern ein."""
        }
    ]
}]

display_quiz(question1, colors=colors.jupyterquiz)
```

**Frage 2**

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question2 = [{
    "question": """Welche Dimensionen werden im MQA verwendet?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Auffindbarkeit, Zugänglichkeit, Interoperabilität, Wiederverwendwabrkeit und Kontext",
            "correct": True,
            "feedback": """✓ Richtig! Die ersten vier Dimensionen entsprechen den FAIR-Prinzipien und die Dimension Kontext untersucht zudem Indikatoren wie Dateigröße und Ausstellungsdatum."""
        },
        {
            "answer": "Relevanz, Genauigkeit, Vollständigkeit und Verfügbarkeit",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. Diese Kategorien sind zwar wichtige Parameter in der Untersuchung der Qualität von Daten und Metadaten, aber nicht die Dimensionen des MQA."""
        },
        {
            "answer": "Lizenzangaben, Zugangsbeschränkung, Heruasgeber und Kontaktinformationen",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. Diese Indikatoren werden zwar untersucht, gehören aber zur Dimension Wiederverwendbarkeit und sind damit nur eine von fünf untersuchten Dimensionen."""
        },
        {
            "answer": "DCAT-AP Konformität, Maschinenlesbarkeit, Format und Media Type",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. Bei den genannten Begriffen handelt es sich um Indikatoren der Dimension Interoperabilität, die zwar abgefragt werden, aber nur eine der fünf Dimensionen darstellen."""
        }
    ]
}]

display_quiz(question2, colors=colors.jupyterquiz)
```

**Frage 3**

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question3 = [{
    "question": """Welche Rolle spielen die Metadaten im Metadata Quality Assessment (MQA)?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Die Metadaten sind irrelevant für die Bewertung ",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt."""
        },
        {
            "answer": "Die Metadaten sind wichtig für die Bewertung, aber nicht entscheidend",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt."""
        },
        {
            "answer": "Die Metadaten sind entscheidend für die Bewertung",
            "correct": True,
            "feedback": """✓ Richtig!"""
        },
        {
            "answer": "Die Metadaten sind nicht vorhanden",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt."""
        }
    ]
}]

display_quiz(question3, colors=colors.jupyterquiz)
```

**Frage 4**

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question4 = [{
    "question": """Was ist das Ergebnis der Bewertung der Metadatenqualität im MQA?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Eine Bewertungsskala von 1-5",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt."""
        },
        {
            "answer": "Eine Bewertungsskala von 0-405",
            "correct": True,
            "feedback": """✓ Richtig! Die Punktezahl der einzelnen Dimensionen werden am Ende addiert, sodass sich maximal 405 Punkte (Excellent) erreichen lassen."""
        },
        {
            "answer": "Eine Bewertungsskala von A-E",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt."""
        },
        {
            "answer": "Eine Bewertungsskala von 0-100",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt."""
        }
    ]
}]

display_quiz(question4, colors=colors.jupyterquiz)
```


## Reflexionsaufgabe

*Mindestens eine Frage zum Erreichen des Lernziels für dieses Kapitel: "Die Funktionen des Metadata Quality Assessment (MQA) können beschrieben werden." Das könnte ein selbstständiges Formulieren der Funktionen des Tools sein. Vielleicht noch eine zum DCAT Schema auf der Plattform?*


**Aufgabenstellung**

Beschreiben Sie mit eigenen Worten, was die wichtigsten Funktionen des MQA-Tools sind.

Begründung:
```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")
from assessment import create_answer_box

create_answer_box('3-1')
```


**Musterlösung**


````{admonition} Musterlösung
:class: solution, dropdown

<span style="color:green">*hier Musterlösung einfügen*</span>
````

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
    "question": """Welche Kriterien werden im MQA verwendet?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Relevanz, Genauigkeit, Vollständigkeit und Konsistenz",
            "correct": True,
            "feedback": """✓ Richtig! ..."""
        },
        {
            "answer": "Relevanz, Genauigkeit, Vollständigkeit und Verfügbarkeit",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        },
        {
            "answer": "Relevanz, Genauigkeit, Konsistenz und Verfügbarkeit",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        },
        {
            "answer": "Relevanz, Vollständigkeit, Konsistenz und Verfügbarkeit",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        }
    ]
}]

display_quiz(question1, colors=colors.jupyterquiz)
```

**Frage 3**

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question3 = [{
    "question": """Wie wird die Bewertung der Metadatenqualität im MQA durchgeführt?""",
    "type": "multiple_choice",
    "answers": [
        {
            "answer": "Durch eine manuelle Bewertung durch Experten",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        },
        {
            "answer": "Durch eine automatisierte Bewertung durch Algorithmen",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        },
        {
            "answer": "Durch eine kombinierte Bewertung durch Experten und Algorithmen",
            "correct": True,
            "feedback": """✓ Richtig! ..."""
        },
        {
            "answer": "Durch eine Bewertung durch die Nutzer",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        }
    ]
}]

display_quiz(question1, colors=colors.jupyterquiz)
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
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        },
        {
            "answer": "Eine Bewertungsskala von 1-10",
            "correct": True,
            "feedback": """✓ Richtig! ..."""
        },
        {
            "answer": "Eine Bewertungsskala von A-E",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        },
        {
            "answer": "Eine Bewertungsskala von 0-100",
            "correct": False,
            "feedback": """× Diese Antwort ist nicht korrekt. ..."""
        }
    ]
}]

display_quiz(question1, colors=colors.jupyterquiz)
```


*eine Frage zum Erreichen des Lernziels für dieses Kapitel: "Die Funktionen des Metadata Quality Assessment (MQA) können beschrieben werden." Also ein selbstständiges Formulieren der Funktionen des Tools und ein wiedergeben in eigenen Worten.*


<span style="color:red">*das unten Stehende am Ende löschen*</span>



`````{admonition} 3. Warum sind Elemente der DCAT-AP-Schema verletzt? Welche Probleme entstehen dadurch?
:class: exercise
````{admonition} Lösung
:class: solution, dropdown

Wählen wir “DCAT-AP Schemaverletzungen” im rechten oberen Reiter. Diese Unterseite gibt einen Überblick über Datensätze, die das DCAT-AP Schema nicht vollständig einhalten und somit potenzielle Nutzungsprobleme aufweisen. Schauen wir uns als Beispiel den Datensatz "Entwicklung von Umsatz und Beschäftigung im Großhandel in Schleswig-Holstein Februar 2022" an. Der Fehler bezieht sich hier auf das Element http://www.w3.org/ns/dcat#mediaType. Laut Fehlerbeschreibung wird für dieses Element ein BlankNode oder eine IRI erwartet, jedoch ist der tatsächliche Wert auf "application/pdf" gesetzt, was nicht den Schema-Anforderungen entspricht.

Dieser Fehler stellt eine Verletzung des DCAT-AP Standards dar, der Metadaten für offene Daten in der EU harmonisieren soll. Das DCAT-AP Schema erwartet für das mediaType-Feld eine Verknüpfung mit einem spezifischen IRI oder BlankNode, um eine einheitliche und maschinenlesbare Metadatenstruktur zu gewährleisten. Durch die falsche Angabe ("application/pdf" anstatt einer IRI) wird die maschinelle Lesbarkeit beeinträchtigt, was wiederum zu Zugangsproblemen führen kann. In der Praxis bedeutet dies, dass andere Systeme oder Anwendungen Schwierigkeiten haben könnten, den Dateityp automatisch zu erkennen und korrekt darzustellen. Der Wert ist zwar für Menschen verständlich, jedoch fehlt die Standardisierung für die maschinelle Verarbeitung, die das DCAT-AP Schema verlangt.

Das Problem liegt darin, dass die Interoperabilität und Konsistenz der Metadaten beeinträchtigt werden. Wenn Metadaten uneinheitlich oder fehlerhaft sind, können Portale und Anwendungen Daten nicht effizient verarbeiten oder austauschen, was den Zugang und die Nutzbarkeit der Daten für Nutzer stark einschränkt. Dies wirkt sich negativ auf die Gesamtbewertung der Metadatenqualität im Portal aus und untergräbt die Ziele des DCAT-AP-Standards, nämlich die Harmonisierung und Vernetzung von Datenkatalogen in Europa.
````
`````

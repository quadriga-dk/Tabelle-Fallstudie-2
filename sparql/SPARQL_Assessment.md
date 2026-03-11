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

**Geschätzte Zeit**: 10 Minuten

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
        "question": "Was ist ein SPARQL-Endpunkt (Endpoint)?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Eine maschinenlesbare Schnittstelle zum Repositorium, in dem Metadaten gespeichert sind",
                "correct": True,
                "feedback": """✓ Korrekt! Der Endpunkt ist die Schnittstelle, über die SPARQL-Abfragen an ein Datenrepositorium gesendet werden. Er ermöglicht den Zugriff auf die dort gespeicherten Metadaten und ist die Voraussetzung für jede SPARQL-Abfrage."""
            },
            {
                "answer": "Ein Befehl zum Beenden einer SPARQL-Abfrage",
                "correct": False,
                "feedback": """x Nicht korrekt. Der Endpunkt ist keine Befehlskomponente, sondern die Adresse (URL) der Schnittstelle, über die SPARQL-Abfragen ausgeführt werden. Der Endpunkt muss zu Beginn definiert werden, damit die Abfrage weiß, wohin sie gesendet werden soll."""
            },
            {
                "answer": "Eine Programmiersprache zur Datenanalyse",
                "correct": False,
                "feedback": """x Nicht korrekt. SPARQL selbst ist die Abfragesprache. Der Endpunkt hingegen ist die URL der Schnittstelle, an die SPARQL-Abfragen gesendet werden, z.B. https://data.europa.eu/sparql."""
            },
            {
                "answer": "Ein Format zur Speicherung von Daten",
                "correct": False,
                "feedback": """x Nicht korrekt. Ein Endpunkt ist kein Datenformat, sondern eine Schnittstelle. Formate wie RDF, XML oder JSON werden für die Datenspeicherung verwendet, während der Endpunkt den Zugriffspunkt für Abfragen darstellt."""
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
        "question": "Welche Funktion haben PREFIX-Deklarationen in einer SPARQL-Abfrage?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Sie definieren Abkürzungen für Namensräume, um lange URIs nicht ausschreiben zu müssen",
                "correct": True,
                "feedback": """✓ Korrekt! PREFIX-Deklarationen ermöglichen es, lange URI-Adressen durch kurze Abkürzungen zu ersetzen. Beispielsweise kann mit „dct:" auf den Namensraum „http://purl.org/dc/terms/" verwiesen werden, was die Abfrage übersichtlicher und einfacher zu schreiben macht."""
            },
            {
                "answer": "Sie filtern die Ergebnisse nach bestimmten Kriterien",
                "correct": False,
                "feedback": """x Nicht korrekt. Für das Filtern von Ergebnissen wird der FILTER-Befehl verwendet. PREFIX-Deklarationen dienen ausschließlich dazu, Abkürzungen für Namensräume zu definieren."""
            },
            {
                "answer": "Sie bestimmen die maximale Anzahl der Ergebnisse",
                "correct": False,
                "feedback": """x Nicht korrekt. Die Begrenzung der Ergebnisanzahl erfolgt mit dem LIMIT-Befehl. PREFIX-Deklarationen haben keine Auswirkung auf die Anzahl der zurückgegebenen Ergebnisse."""
            },
            {
                "answer": "Sie sortieren die Ausgabe alphabetisch",
                "correct": False,
                "feedback": """x Nicht korrekt. Die Sortierung von Ergebnissen erfolgt mit dem ORDER BY-Befehl. PREFIX-Deklarationen dienen lediglich der Definition von Namensraum-Abkürzungen."""
            }
        ]
    }
]
display_quiz(question2, colors=colors.jupyterquiz)
```

## Frage 3

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors


question3 = [
    {
        "question": "Welche Aussagen zu den SPARQL-Befehlen SELECT und WHERE sind korrekt? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "SELECT gibt an, welche Eigenschaften (Properties) als Spalten in der Ergebnistabelle angezeigt werden sollen",
                "correct": True,
                "feedback": """✓ Korrekt! Mit SELECT werden die Variablen (z.B. ?uri, ?title, ?contributorid) definiert, die in der Ausgabe erscheinen sollen. Jede Variable entspricht einer Spalte in der Ergebnistabelle."""
            },
            {
                "answer": "WHERE definiert die Bedingungen, die erfüllt sein müssen, damit ein Datensatz in den Ergebnissen erscheint",
                "correct": True,
                "feedback": """✓ Korrekt! Der WHERE-Befehl ist der Kern jeder SPARQL-Abfrage. Er legt fest, welche Kriterien die Datensätze erfüllen müssen, um in die Ergebnisliste aufgenommen zu werden."""
            },
            {
                "answer": "Innerhalb von WHERE werden Beziehungen durch Triplets (Subjekt-Prädikat-Objekt) definiert",
                "correct": True,
                "feedback": """✓ Korrekt! Die Triplet-Struktur (S-P-O) ist grundlegend für SPARQL. Jede Zeile in der WHERE-Klausel stellt eine Beziehung zwischen zwei Eigenschaften über ein Prädikat her, z.B. „?uri dct:title ?title" verbindet eine URI mit ihrem Titel."""
            },
            {
                "answer": "SELECT kann nicht mehr als eine einzige Variable enthalten",
                "correct": False,
                "feedback": """x Nicht korrekt. SELECT kann mehrere Variablen enthalten, die durch Leerzeichen getrennt werden. Beispiel: SELECT ?uri ?title ?contributorid ?stateKey gibt vier verschiedene Eigenschaften aus."""
            },
            {
                "answer": "WHERE ist optional und kann bei einfachen Abfragen weggelassen werden",
                "correct": False,
                "feedback": """x Nicht korrekt. WHERE ist ein essentieller Bestandteil jeder SPARQL-Abfrage. Ohne WHERE würde die Abfrage nicht wissen, nach welchen Daten gesucht werden soll."""
            }
        ]
    }
]
display_quiz(question3, colors=colors.jupyterquiz, max_width=1000)
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
        "question": "Wofür wird der OPTIONAL-Befehl in SPARQL verwendet?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Um Ergebnisse auch dann anzuzeigen, wenn bestimmte Eigenschaften nicht in den Metadaten vorhanden sind",
                "correct": True,
                "feedback": """✓ Korrekt! OPTIONAL ist besonders nützlich bei unvollständigen Metadaten. Während Bedingungen in WHERE zwingend erfüllt sein müssen, ermöglicht OPTIONAL das Einbeziehen von Datensätzen, auch wenn das entsprechende Feld leer ist. So wird verhindert, dass wegen fehlender Angaben eine leere Ergebnisliste zurückgegeben wird."""
            },
            {
                "answer": "Um die Abfrage zu beschleunigen",
                "correct": False,
                "feedback": """x Nicht korrekt. OPTIONAL hat keine Auswirkung auf die Geschwindigkeit der Abfrage. Es dient dazu, flexibler mit unvollständigen Daten umzugehen."""
            },
            {
                "answer": "Um die Abfrage zu beenden",
                "correct": False,
                "feedback": """x Nicht korrekt. OPTIONAL beendet keine Abfrage, sondern definiert eine nicht-zwingende Bedingung innerhalb der WHERE-Klausel."""
            },
            {
                "answer": "Um doppelte Ergebnisse zu entfernen",
                "correct": False,
                "feedback": """x Nicht korrekt. Für das Entfernen von Duplikaten wird das Schlüsselwort DISTINCT verwendet. OPTIONAL ermöglicht das Einbeziehen von Datensätzen mit fehlenden Werten."""
            }
        ]
    }
]
display_quiz(question4, colors=colors.jupyterquiz)
```

## Frage 5

Ordnen Sie die folgenden SPARQL-Komponenten ihrer jeweiligen Funktion zu:

### Frage 5(a)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors


question5a = [
    {
        "question": "Welche SPARQL-Komponente wird verwendet, um die Ergebnisse auf Datensätze zu beschränken, deren Titel eine bestimmte Zeichenkette enthält?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "FILTER mit CONTAINS",
                "correct": True,
                "feedback": """✓ Korrekt! FILTER(CONTAINS(?title, \"suchbegriff\")) prüft, ob die Variable ?title den angegebenen Suchbegriff enthält. In Kombination mit LCASE() kann die Suche unabhängig von Groß- und Kleinschreibung durchgeführt werden."""
            },
            {
                "answer": "SELECT",
                "correct": False,
                "feedback": """x Nicht korrekt. SELECT bestimmt nur, welche Variablen in der Ausgabe erscheinen sollen. Die Filterung nach Inhalten erfolgt mit dem FILTER-Befehl."""
            },
            {
                "answer": "PREFIX",
                "correct": False,
                "feedback": """x Nicht korrekt. PREFIX definiert Namensraum-Abkürzungen und hat keine Filterfunktion."""
            },
            {
                "answer": "GROUP BY",
                "correct": False,
                "feedback": """x Nicht korrekt. GROUP BY gruppiert Ergebnisse nach bestimmten Variablen, filtert aber nicht nach Textinhalten."""
            }
        ]
    }
]
display_quiz(question5a, colors=colors.jupyterquiz)
```

### Frage 5(b)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question5b = [
    {
        "question": "Welche SPARQL-Komponente wird verwendet, um die Anzahl der eindeutigen Werte einer Eigenschaft zu zählen?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "COUNT(DISTINCT ...)",
                "correct": True,
                "feedback": """✓ Korrekt! COUNT(DISTINCT ?variable) zählt die Anzahl eindeutiger Werte einer Variable. DISTINCT stellt sicher, dass jeder Wert nur einmal gezählt wird, auch wenn er mehrfach vorkommt."""
            },
            {
                "answer": "SELECT",
                "correct": False,
                "feedback": """x Nicht korrekt. SELECT wählt Variablen für die Ausgabe aus, zählt aber keine Werte."""
            },
            {
                "answer": "FILTER",
                "correct": False,
                "feedback": """x Nicht korrekt. FILTER schränkt Ergebnisse nach Kriterien ein, führt aber keine Zählungen durch."""
            },
            {
                "answer": "ORDER BY",
                "correct": False,
                "feedback": """x Nicht korrekt. ORDER BY sortiert die Ergebnisse, zählt sie aber nicht."""
            }
        ]
    }
]
display_quiz(question5b, colors=colors.jupyterquiz)
```

### Frage 5(c)

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

question5c = [
    {
        "question": "Welche SPARQL-Komponente wird verwendet, um Ergebnisse nach einer Variable zu gruppieren und aggregierte Werte zu berechnen?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "GROUP BY",
                "correct": True,
                "feedback": """✓ Korrekt! GROUP BY gruppiert die Ergebnisse nach den Werten einer oder mehrerer Variablen. Dies ermöglicht die Berechnung von aggregierten Werten (wie COUNT, SUM, AVG) für jede Gruppe, z.B. die Anzahl der Datensätze pro Datenbereitsteller."""
            },
            {
                "answer": "ORDER BY",
                "correct": False,
                "feedback": """x Nicht korrekt. ORDER BY sortiert die Ergebnisse, gruppiert sie aber nicht für Aggregationen."""
            },
            {
                "answer": "WHERE",
                "correct": False,
                "feedback": """x Nicht korrekt. WHERE definiert Bedingungen für die Auswahl von Datensätzen, führt aber keine Gruppierung durch."""
            },
            {
                "answer": "OFFSET",
                "correct": False,
                "feedback": """x Nicht korrekt. OFFSET überspringt eine bestimmte Anzahl von Ergebnissen (für Paginierung), hat aber nichts mit Gruppierung zu tun."""
            }
        ]
    }
]
display_quiz(question5c, colors=colors.jupyterquiz)
```

## Frage 6

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

"""
Lernziel: 
    Einfache SPARQL-Abfragen können erstellt und durchgeführt werden, um spezifische Informationen aus einem Datenkatalog abzurufen.
Bloom-Stufe: Anwenden
Format: Single Choice
Geschätzte Zeit: 5 Minuten
Schwerpunkte:
    - Praktische Anwendung von FILTER
    - Zeitliche Eingrenzung
"""

question6 = [
    {
        "question": "Welcher SPARQL-Codeabschnitt filtert Datensätze korrekt nach einem Zeitraum von 2020 bis 2023?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "FILTER(CONTAINS(STR(?modified), \"2020\") || CONTAINS(STR(?modified), \"2021\") || CONTAINS(STR(?modified), \"2022\") || CONTAINS(STR(?modified), \"2023\"))",
                "correct": True,
                "feedback": """✓ Korrekt! Diese Filterung prüft mit CONTAINS und STR(), ob das Änderungsdatum eine der angegebenen Jahreszahlen enthält. Der ||-Operator (logisches ODER) verknüpft die einzelnen Bedingungen, sodass ein Treffer bei einer beliebigen Jahreszahl genügt."""
            },
            {
                "answer": "FILTER(?modified = \"2020-2023\")",
                "correct": False,
                "feedback": """x Nicht korrekt. Diese Syntax ist kein gültiger SPARQL-Ausdruck für Zeiträume. SPARQL erfordert explizite Bedingungen für jeden Zeitpunkt oder die Verwendung von Vergleichsoperatoren mit konvertierten Datumswerten."""
            },
            {
                "answer": "SELECT ?modified WHERE 2020-2023",
                "correct": False,
                "feedback": """x Nicht korrekt. Dies ist keine gültige SPARQL-Syntax. Zeitliche Filter gehören in die WHERE-Klausel als FILTER-Bedingung, nicht als Teil der WHERE-Definition selbst."""
            },
            {
                "answer": "PREFIX time: 2020-2023",
                "correct": False,
                "feedback": """x Nicht korrekt. PREFIX definiert Namensraum-Abkürzungen und kann nicht für Zeitfilter verwendet werden. Die Filterung nach Zeiträumen erfolgt mit FILTER-Bedingungen."""
            }
        ]
    }
]
display_quiz(question6, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 7

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

"""
Lernziel: 
    Einfache SPARQL-Abfragen können erstellt und durchgeführt werden, um spezifische Informationen aus einem Datenkatalog abzurufen.
Bloom-Stufe: Verstehen
Format: Single Choice
Geschätzte Zeit: 3 Minuten
Schwerpunkte:
    - LCASE-Funktion
    - Case-insensitive Suche
"""

question7 = [
    {
        "question": "Warum wird in der SPARQL-Abfrage FILTER(CONTAINS(LCASE(?title), \"baumkataster\")) die Funktion LCASE() verwendet?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Um die Suche unabhängig von Groß- und Kleinschreibung durchzuführen",
                "correct": True,
                "feedback": """✓ Korrekt! LCASE() konvertiert alle Zeichen in Kleinbuchstaben. Dadurch werden Treffer wie „Baumkataster", „BAUMKATASTER" oder „BaumKataster" gefunden, da alle auf „baumkataster" normalisiert werden, bevor der Vergleich stattfindet."""
            },
            {
                "answer": "Um die Abfrage schneller zu machen",
                "correct": False,
                "feedback": """x Nicht korrekt. LCASE() dient nicht der Performance-Optimierung, sondern der Normalisierung von Zeichenketten für einen flexibleren Textvergleich."""
            },
            {
                "answer": "Um nur Titel in Kleinbuchstaben zu finden",
                "correct": False,
                "feedback": """x Nicht korrekt. LCASE() filtert nicht nach der Original-Schreibweise, sondern konvertiert den Vergleichswert temporär in Kleinbuchstaben. Dadurch werden alle Schreibweisen gefunden."""
            },
            {
                "answer": "Um doppelte Ergebnisse zu vermeiden",
                "correct": False,
                "feedback": """x Nicht korrekt. Für das Vermeiden von Duplikaten wird DISTINCT verwendet. LCASE() normalisiert Zeichenketten für den Textvergleich."""
            }
        ]
    }
]
display_quiz(question7, colors=colors.jupyterquiz)
```

## Frage 8

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors

"""
Lernziel: 
    Die grundlegenden Komponenten der SPARQL-Syntax können aufgezählt und ihre Rollen erläutert werden.
    Einfache SPARQL-Abfragen können erstellt und durchgeführt werden.
Bloom-Stufe: Verstehen/Analysieren
Format: Multiple Choice
Geschätzte Zeit: 5 Minuten
Schwerpunkte:
    - Herausforderungen bei SPARQL-Abfragen
    - Metadatenqualität
"""

question11 = [
    {
        "question": "Welche praktischen Herausforderungen können bei SPARQL-Abfragen auf Open Data-Portalen auftreten? (Mehrere Antworten können richtig sein)",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Unvollständige Metadaten, z.B. fehlende Angaben zu Bundesländern (stateKey)",
                "correct": True,
                "feedback": """✓ Korrekt! Wie im Kapitel gezeigt, sind Metadatenfelder wie „stateKey" für die Bundesland-Zuordnung oft nicht ausgefüllt. Dies erschwert geografisch gezielte Abfragen und zeigt die Bedeutung vollständiger Metadatenpflege."""
            },
            {
                "answer": "Die Notwendigkeit, Paginierung manuell mit LIMIT und OFFSET zu implementieren",
                "correct": True,
                "feedback": """✓ Korrekt! SPARQL bietet keine automatische Paginierung wie eine Weboberfläche. Um mehr als die standardmäßig angezeigten Ergebnisse zu sehen, müssen LIMIT und OFFSET manuell eingefügt werden."""
            },
            {
                "answer": "Nicht alle über Metadaten gefundenen Datensätze sind tatsächlich zugänglich oder herunterladbar",
                "correct": True,
                "feedback": """✓ Korrekt! Wie im Kapitel beschrieben, können Datensätze in den Metadaten verzeichnet sein, aber die tatsächlichen Download-URLs funktionieren möglicherweise nicht. Die Verfügbarkeit muss daher immer manuell überprüft werden."""
            },
            {
                "answer": "SPARQL-Abfragen können nur auf englischsprachigen Portalen ausgeführt werden",
                "correct": False,
                "feedback": """x Nicht korrekt. SPARQL funktioniert sprachunabhängig. Die Abfragesprache selbst verwendet englische Schlüsselwörter, aber die Daten können in jeder Sprache vorliegen und abgefragt werden."""
            },
            {
                "answer": "Eine SPARQL-Abfrage kann nur eine einzige Datenquelle gleichzeitig abfragen",
                "correct": False,
                "feedback": """x Nicht korrekt. Obwohl in den Übungen jeweils ein Endpunkt verwendet wurde (data.europa.eu oder govdata.de), ist es prinzipiell möglich, verschiedene Endpunkte nacheinander abzufragen oder föderierten Abfragen zu nutzen."""
            }
        ]
    }
]
display_quiz(question11, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 9

Analysieren Sie die folgende SPARQL-Abfrage und beantworten Sie die Frage:

```sparql
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcatde: <http://dcat-ap.de/def/dcatde/>

SELECT ?uri ?title ?contributorid
WHERE {
    ?uri dct:title ?title .
    ?uri dcatde:contributorID ?contributorid .
    FILTER(CONTAINS(LCASE(?title), "baumkataster"))
    FILTER(isURI(?contributorid))
    FILTER(strstarts(str(?contributorid), "http://dcat-ap.de/def/contributors/"))
}
```

```{code-cell} ipython3
:tags: [remove-input]
from jupyterquiz import display_quiz

import sys
sys.path.append("..")
from quadriga import colors


question12 = [
    {
        "question": "Was bewirkt der Filter FILTER(strstarts(str(?contributorid), \"http://dcat-ap.de/def/contributors/\")) in dieser Abfrage?",
        "type": "multiple_choice",
        "answers": [
            {
                "answer": "Er beschränkt die Ergebnisse auf Datensätze, deren Bereitsteller-URI mit der angegebenen Zeichenfolge beginnt (deutsche Datenbereitsteller)",
                "correct": True,
                "feedback": """✓ Korrekt! Die Funktion strstarts() prüft, ob eine Zeichenkette mit einem bestimmten Präfix beginnt. In diesem Fall werden nur Datensätze einbezogen, deren contributorID-URI zum deutschen DCAT-AP-Contributor-Schema gehört. Damit werden effektiv deutsche Datenbereitsteller gefiltert."""
            },
            {
                "answer": "Er sortiert die Ergebnisse nach dem Bereitsteller",
                "correct": False,
                "feedback": """x Nicht korrekt. Die Sortierung erfolgt mit ORDER BY, nicht mit FILTER. strstarts() ist eine Funktion zur Prüfung von Zeichenketten-Präfixen."""
            },
            {
                "answer": "Er zählt die Anzahl der Bereitsteller",
                "correct": False,
                "feedback": """x Nicht korrekt. Für das Zählen wird COUNT verwendet. strstarts() filtert nach dem Anfang einer Zeichenkette."""
            },
            {
                "answer": "Er konvertiert die URI in eine lesbare Form",
                "correct": False,
                "feedback": """x Nicht korrekt. str() konvertiert eine URI in eine Zeichenkette, aber strstarts() prüft dann, ob diese mit einem bestimmten Präfix beginnt. Es geht um Filterung, nicht um Formatierung."""
            }
        ]
    }
]
display_quiz(question12, colors=colors.jupyterquiz, max_width=1000)
```

## Frage 10

Formulieren Sie eine SPARQL-Abfrage, die folgende Anforderungen erfüllt:

**Aufgabe:** Sie möchten herausfinden, welche Datenbereitsteller die meisten Datensätze mit dem Wort „Baum" im Titel veröffentlicht haben. Die Ergebnisse sollen nach der Anzahl der Datensätze gruppiert sein.

**Welche Bestandteile müsste Ihre Abfrage enthalten?**

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")
from assessment import create_answer_box

create_answer_box('sparql-1')
```

````{admonition} Lösungshinweise
:class: solution, dropdown

**Musterlösung:**

Die Abfrage sollte folgende Elemente enthalten:

1. **PREFIX-Deklarationen:**
   - `PREFIX dcat: <http://www.w3.org/ns/dcat#>` für Datensatz-Definition
   - `PREFIX dct: <http://purl.org/dc/terms/>` für Titel
   - `PREFIX dcatde: <http://dcat-ap.de/def/dcatde/>` für Bereitsteller-ID

2. **SELECT mit COUNT:**
   - `SELECT ?contributorID (COUNT(DISTINCT ?datasetTitle) AS ?anzahl)`
   - COUNT zählt die eindeutigen Titel pro Bereitsteller

3. **WHERE-Klausel mit:**
   - Definition des Datensatzes als dcat:Dataset
   - Verknüpfung mit Titel und contributorID
   - `FILTER(CONTAINS(LCASE(?datasetTitle), "baum"))` für die Textsuche

4. **GROUP BY:**
   - `GROUP BY ?contributorID` zum Gruppieren nach Bereitsteller

**Beispiel-Code:**
```sparql
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcatde: <http://dcat-ap.de/def/dcatde/>

SELECT ?contributorID (COUNT(DISTINCT ?datasetTitle) AS ?anzahl)
WHERE {
  ?datasetURI a dcat:Dataset;
              dct:title ?datasetTitle;
              dcatde:contributorID ?contributorID.
  FILTER(CONTAINS(LCASE(?datasetTitle), "baum"))
}
GROUP BY ?contributorID
```
````

## Frage 11

**Reflexionsaufgabe**

In der Fallstudie wurde beschrieben, dass Dr. Weber zunächst nach Datensätzen zu „Baumkataster" in Brandenburg suchte, aber feststellen musste, dass die gefundenen Datensätze nicht zugänglich waren. Schließlich fand er einen geeigneten Datensatz in Nordrhein-Westfalen.

Reflektieren Sie über die folgenden Aspekte:

1. Welche Rolle spielt die Metadatenqualität für den Erfolg von SPARQL-Abfragen?
2. Warum ist es wichtig, gefundene Datensätze manuell auf ihre tatsächliche Zugänglichkeit zu prüfen?
3. Wie könnten Sie Ihre Suchstrategie anpassen, wenn eine gezielte Suche keine Ergebnisse liefert?

```{code-cell} ipython3
:tags: [remove-input]
import sys
sys.path.append("../quadriga")
from assessment import create_answer_box

create_answer_box('sparql-2')
```

````{admonition} Lösungshinweise
:class: solution, dropdown

**Musterlösung:**

1. **Metadatenqualität:**
   - Vollständige Metadaten sind essentiell für erfolgreiche Abfragen
   - Fehlende Felder (wie stateKey) schränken Filtermöglichkeiten ein
   - Standards wie DCAT-AP definieren, welche Felder ausgefüllt werden sollten
   - Unvollständige Metadaten führen zu unvollständigen oder irreführenden Ergebnissen

2. **Manuelle Überprüfung:**
   - Metadaten können veraltet sein, während Links nicht mehr funktionieren
   - Datensätze können in den Metadaten verzeichnet sein, aber nicht mehr zugänglich sein
   - Beschreibungen können irreführend sein (z.B. Teildatensätze statt vollständiger Kataster)
   - Die tatsächliche Datenqualität und -struktur muss vor der Analyse geprüft werden

3. **Anpassung der Suchstrategie:**
   - Suchbegriffe erweitern (z.B. von „Baumkataster" auf „Baumpflanzungen")
   - Geografische Einschränkungen lockern
   - Verschiedene Datenportale ausprobieren (data.europa.eu, govdata.de)
   - Alternative Bereitsteller in Betracht ziehen
   - OPTIONAL für flexible Abfragen nutzen
   - Zeiträume anpassen basierend auf dem Open-Data-Gesetz (2017)
````
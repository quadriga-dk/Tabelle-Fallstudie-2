# Metadatenqualität
```{admonition} Lernziele
:class: keypoints
- Lernende erkennen, dass die FAIR-Prinzipien ein Grundgerüst zur Messung von Metadatenqualität ist
- Lernenden lernen ein Messverfahren zur Metadatenqualität im europäischen Datenportal kennen
- Lernende setzen sich mit typischen Problemen in der Metadatenqualität auseinander und indem sie Prüfberichten bewerten.
```

## Kontrolle und Werkzeuge
Das Erfragen von Metadaten ist das zentrale Ziel für die Gestaltung von Abfragen. Deshalb ist es vernünftig, sich mit dem Konzept der Metadaten auseinanderzusetzen. Die einfachste Beschreibung ist "Daten über Daten", also Daten, die zwecks der Einordnung und Kategorisierung von anderen Datensätzen dienen, damit jene intuitiv auffindbar übersichtlich sind. Verschiedene Arten von Metadaten erfüllen unterschiedliche Funktionen. So enthält zum Beispiel beschreibende Metadaten für ein Dokument Informationen wie den Autor, das Erstellungsdatum, die Dateigröße und Schlagwörter. Technische Metadaten für eine relationale Datenbank könnten dagegen die Struktur der Tabellen, Datentypen und Beziehungen zwischen den Tabellen beschreiben.

Angesichts der enormen Datenmenge, die Unternehmen heute verarbeiten, sind Metadaten unverzichtbar. Sie verbessern den Datenzugriff und erleichtern das Navigieren durch große Datensätze, um rohe Informationen in umsetzbare Erkenntnisse zu verwandeln. Ein Einzelhandelsunternehmen könnte beispielsweise Metadaten nutzen, um Verkaufsdaten für einen bestimmten Monat, gefiltert nach Produktkategorie und Region, schnell zu finden, ohne das gesamte Datenvolumen durchsuchen zu müssen. Metadaten sind auch somit entscheidend für die Datenverwaltung und das Datenmanagement.

Metadaten, wie alle anderen Datentype, sollen auffindbar, zugänglich, interoperabel (bzw. kompatibel) und wiederverwendbar. Ein nützliches Prinzipien-Schema, an das Metadaten sich halten sollen, ist beispielsweise FAIR. In unserer 1. Fallstudie gehen wir auf die Philosophie und Regeln ein, die die FAIR-Prinzipien vorschreiben - [hier](https://quadriga-dk.github.io/Tabelle-Fallstudie-1/Markdown/06_FairPrinzipien.html).

Die FAIR-Prinzipien dienen dazu als der Grundstein eines vom Konsortium des data.europa.eu Portals entwickelten Werkzeugs zur Untersuchung der Qualität der von data.europa.eu gesammelten Metadaten - das **Metadata Quality Assessment (MQA)**.

Das [MQA](https://data.europa.eu/mqa/methodology?locale=de) zielt darauf ab, die Qualität der Metadaten für öffentliche Sektor-Daten in Europa zu bewerten und die größten Hindernisse für eine bessere Qualität zu identifizieren. Die Untersuchung konzentriert sich auf spezifische Fragestellungen, wie die Einhaltung von DCAT-AP-Standards, die Offenlegung zusätzlicher Informationen, die Zugänglichkeit und Maschinenlesbarkeit der referenzierten Daten sowie die Lizenzverwendung.

Auf der [Metadata Quality](https://data.europa.eu/mqa/?locale=de) Seite des europäischen Metadatenportals wird eine gesamte Bewertung aller aufgesammelten europäischen Portale zusammengefügt und dargestellt. Mithilfe dieser Werkzeuge können wir einschätzen, welche Portale nach den FAIR-Prinzipien die vollsten und "saubersten" Datensätze anbieten. Die Prozentzahlen besagen den Anteil an Datensätzen, die dem entsprechenden Kriterium zustimmen. Durch den Verlauf kann man sich ansehen, wie die jeweilige Prozentzahl durch die Jahre schwankt, in Hinsicht darauf, dass ständig neue Datensätze hinzugefügt werden, die entweder die Kriterien erfüllen oder nicht. Im Übersichtfeld kann man beispielsweise sichten, dass [das nationale spanische Datenportal](https://data.europa.eu/mqa/catalogues/yoda/?locale=de) eine ausgezeichnete Bewertung verdient hat. Lassen Sie uns aber zum [Open Data Portal Germany](https://data.europa.eu/mqa/catalogues/govdata/?locale=de) gehen und einschätzen, wie fortgeschritten die Open-Data-Initiative in Deutschland ist und welche Schwachstellen noch bestehen. In dieser Übung können Sie alleine die Seite durchstöbern und herausfinden, welche Fehlerhaftigkeiten ausfindig gemacht werden können.

## Übung zur Bewertung der Metadatenqualität von GovData 
Die Bewertungsevolution von GovData beträgt 240 Punkte aus maximal 405, was eine "gute" Note bedeutet. Trotzdem gibt es große Lücken, die sich nicht vernachlässigen lassen. Auf diese werden wir genauer eingehen.

`````{admonition} Worauf beziehen sich die meisten Zugangsprobleme im deutschen Datenportal?
:class: solution
````{admonition} Lösung
:class: dropdown
Wählen wir "Zugangsprobleme" in der oberen Leiste. Diese Seite gibt einen Überblick über alle Datensätze mit nicht erreichbaren Distributions. Nehmen wir uns z.B. das erste Ergebnis - Statistisches Jahrbuch - Hamburg 2018/2019. Man kann prüfen, ob der Datensatz über eine eindeutige und beständige PID (Persistent Identifier) verfügt, z. B. eine DOI, die den langfristigen Zugriff und die Auffindbarkeit gewährleistet. PIDs sind ein wesentliches Element für die Auffindbarkeit von Daten, da sie dafür sorgen, dass ein Datensatz langfristig und zuverlässig zugänglich bleibt, auch wenn sich der Speicherort oder der URL ändert. Ohne eine PID kann es zu Zugangsproblemen kommen, die durch "tote Links" oder veraltete URLs verursacht werden. Solche Probleme sind im deutschen Datenportal häufig und betreffen die FAIR-Dimension Findable besonders stark, da Nutzer Schwierigkeiten haben, die gewünschten Daten zu finden oder darauf zuzugreifen. Die gesamte Bewertungsnote des Portal leidet somit darunter.
````
`````

`````{admonition} Warum sind Elemente der DCAT-AP-Schema verletzt? Warum wird das zum Problem?
:class: solution
````{admonition} Lösung
:class: dropdown
Wählen wir “DCAT-AP Schema Verletzungen” in der oberen Leiste. Diese Seite gibt einen Überblick über Datensätze, die das DCAT-AP Schema nicht vollständig einhalten und somit potenzielle Nutzungsprobleme aufweisen. Schauen wir uns als Beispiel den Datensatz "Entwicklung von Umsatz und Beschäftigung im Großhandel in Schleswig-Holstein Februar 2022" an. Der Fehler bezieht sich hier auf das Element http://www.w3.org/ns/dcat#mediaType. Laut Fehlerbeschreibung wird für dieses Element ein BlankNode oder eine IRI erwartet, jedoch ist der tatsächliche Wert auf "application/pdf" gesetzt, was nicht den Schema-Anforderungen entspricht.

Dieser Fehler stellt eine Verletzung des DCAT-AP Standards dar, der Metadaten für offene Daten in der EU harmonisieren soll. Das DCAT-AP Schema erwartet für das mediaType-Feld eine Verknüpfung mit einem spezifischen IRI oder BlankNode, um eine einheitliche und maschinenlesbare Metadatenstruktur zu gewährleisten. Durch die falsche Angabe ("application/pdf" anstatt einer IRI) wird die maschinelle Lesbarkeit beeinträchtigt, was zu Zugangsproblemen führen kann. In der Praxis bedeutet dies, dass andere Systeme oder Anwendungen Schwierigkeiten haben könnten, den Dateityp automatisch zu erkennen und korrekt darzustellen. Der Wert ist zwar für Menschen verständlich, jedoch fehlt die Standardisierung für die maschinelle Verarbeitung, die das DCAT-AP Schema verlangt.

Das Problem besteht daher darin, dass die Interoperabilität und Konsistenz der Metadaten leiden. Wenn Metadaten uneinheitlich oder fehlerhaft sind, können Portale und Anwendungen Daten nicht effizient verarbeiten oder austauschen, was den Zugang und die Nutzbarkeit der Daten für Nutzer stark einschränkt. Dies wirkt sich negativ auf die Gesamtbewertung der Metadatenqualität im Portal aus und untergräbt die Ziele des DCAT-AP Standards, nämlich die Harmonisierung und Vernetzung von Datenkatalogen in Europa.
````
`````
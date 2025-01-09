# Übung zur Bewertung der Metadatenqualität von GovData 
Im Rahmen dieser Übung beschäftigen wir uns mit der Bewertung der Metadatenqualität auf der Plattform GovData, dem zentralen Datenportal für offene Daten in Deutschland. GovData bietet Zugang zu einer Vielzahl von Datensätzen aus verschiedenen öffentlichen Institutionen und Behörden, wobei die Qualität der Metadaten eine entscheidende Rolle für die Auffindbarkeit, Nachnutzung und Integration der Daten spielt.

Die Metadatenqualität wird anhand von definierten Kriterien bewertet, die in Kapitel 4 ausführlich behandelt wurden. Hierzu zählen beispielsweise Vollständigkeit, Verständlichkeit und Konsistenz der bereitgestellten Informationen. Diese Übung knüpft direkt an die theoretischen Grundlagen an und ermöglicht eine praxisnahe Anwendung, bei der die Stärken und Schwächen der vorhandenen Metadaten analysiert werden.

Durch diese praktische Übung können Sie die Relevanz von qualitativ hochwertigen Metadaten für offene Datenportale wie GovData nachvollziehen und Handlungsempfehlungen für deren Verbesserung entwickeln.

Die Bewertungsevolution von GovData beträgt 240 von maximal möglichen 405 Punkten, was einer "guten" Note entspricht. Trotzdem gibt es erhebliche Lücken, die nicht ignoriert werden können. Auf diese werden wir im Folgenden genauer eingehen.

`````{admonition} Worauf beziehen sich die meisten Zugangsprobleme im deutschen Datenportal?
:class: solution
````{admonition} Lösung
:class: dropdown
Wählen wir "Zugangsprobleme" in der oberen Leiste. Diese Seite gibt einen Überblick über alle Datensätze mit nicht erreichbaren Distributions. Nehmen wir uns z.B. das erste Ergebnis - Statistisches Jahrbuch - Hamburg 2018/2019. Man kann prüfen, ob der Datensatz über eine eindeutige und beständige PID (Persistent Identifier) verfügt, z. B. eine DOI, die den langfristigen Zugriff und die Auffindbarkeit gewährleistet. PIDs sind ein wesentliches Element für die Auffindbarkeit von Daten, da sie dafür sorgen, dass ein Datensatz langfristig und zuverlässig zugänglich bleibt, auch wenn sich der Speicherort oder die URL ändert. Ohne eine PID kann es zu Zugangsproblemen kommen, die durch "tote Links" oder veraltete URLs verursacht werden. Solche Probleme sind im deutschen Datenportal kein Einzelfall und betreffen die FAIR-Dimension Findable besonders stark, da Nutzer Schwierigkeiten haben, die gewünschten Daten zu finden oder darauf zuzugreifen. Dadurch leidet die Gesamtbewertungsnote des Portals.
````
`````

`````{admonition} Warum sind Elemente der DCAT-AP-Schema verletzt? Warum wird das zum Problem?
:class: solution
````{admonition} Lösung
:class: dropdown
Wählen wir “DCAT-AP Schema Verletzungen” in der oberen Leiste. Diese Seite gibt einen Überblick über Datensätze, die das DCAT-AP Schema nicht vollständig einhalten und somit potenzielle Nutzungsprobleme aufweisen. Schauen wir uns als Beispiel den Datensatz "Entwicklung von Umsatz und Beschäftigung im Großhandel in Schleswig-Holstein Februar 2022" an. Der Fehler bezieht sich hier auf das Element http://www.w3.org/ns/dcat#mediaType. Laut Fehlerbeschreibung wird für dieses Element ein BlankNode oder eine IRI erwartet, jedoch ist der tatsächliche Wert auf "application/pdf" gesetzt, was nicht den Schema-Anforderungen entspricht.

Dieser Fehler stellt eine Verletzung des DCAT-AP Standards dar, der Metadaten für offene Daten in der EU harmonisieren soll. Das DCAT-AP Schema erwartet für das mediaType-Feld eine Verknüpfung mit einem spezifischen IRI oder BlankNode, um eine einheitliche und maschinenlesbare Metadatenstruktur zu gewährleisten. Durch die falsche Angabe ("application/pdf" anstatt einer IRI) wird die maschinelle Lesbarkeit beeinträchtigt, was wiederum zu Zugangsproblemen führen kann. In der Praxis bedeutet dies, dass andere Systeme oder Anwendungen Schwierigkeiten haben könnten, den Dateityp automatisch zu erkennen und korrekt darzustellen. Der Wert ist zwar für Menschen verständlich, jedoch fehlt die Standardisierung für die maschinelle Verarbeitung, die das DCAT-AP Schema verlangt.

Das Problem liegt darin, dass die Interoperabilität und Konsistenz der Metadaten beeinträchtigt werden. Wenn Metadaten uneinheitlich oder fehlerhaft sind, können Portale und Anwendungen Daten nicht effizient verarbeiten oder austauschen, was den Zugang und die Nutzbarkeit der Daten für Nutzer stark einschränkt. Dies wirkt sich negativ auf die Gesamtbewertung der Metadatenqualität im Portal aus und untergräbt die Ziele des DCAT-AP Standards, nämlich die Harmonisierung und Vernetzung von Datenkatalogen in Europa.
````
`````

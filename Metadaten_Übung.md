# Übung zur Bewertung der Metadatenqualität von GovData 
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
# Übung zur Bewertung der Metadatenqualität von GovData 
Im Rahmen dieser Übung beschäftigen wir uns mit der Bewertung der Metadatenqualität auf der Plattform GovData, dem zentralen Datenportal für offene Daten in Deutschland. GovData bietet Zugang zu einer Vielzahl von Datensätzen aus verschiedenen öffentlichen Institutionen und Behörden, wobei die Qualität der Metadaten eine entscheidende Rolle für die Auffindbarkeit, Nachnutzung und Integration der Daten spielt.

Die Metadatenqualität wird anhand von definierten Kriterien bewertet, die in Kapitel 4 (*Wirklich Kap. 4 - ansonsten noch eindeutlicher verweisen*) ausführlich behandelt wurden. Hierzu zählen beispielsweise Vollständigkeit, Verständlichkeit und Konsistenz der bereitgestellten Informationen. Diese Übung knüpft direkt an die theoretischen Grundlagen an und ermöglicht eine praxisnahe Anwendung, bei der die Stärken und Schwächen der vorhandenen Metadaten analysiert werden.

Durch diese praktische Übung können Sie die Relevanz von qualitativ hochwertigen Metadaten für offene Datenportale wie GovData nachvollziehen und Handlungsempfehlungen für deren Verbesserung entwickeln.

Die Bewertungsevaluation von GovData beträgt 236 von maximal möglichen 405 Punkten, was einer "guten" Note entspricht (Stand Januar 2025, siehe Übersicht aller Kataloge auf dem [Metadata Quality Dashboard](https://data.europa.eu/mqa/?locale=de) des europäischen Metadatenportals). Trotzdem gibt es erhebliche Lücken in der Qualität, die nicht ignoriert werden können. Auf diese werden wir im Folgenden genauer eingehen.  Diese Übung soll Ihnen helfen, ein vertieftes Verständnis für die Bedeutung von Metadatenqualität zu entwickeln und gleichzeitig konkrete Strategien zur Verbesserung zu erarbeiten. 

Um die Übung erfolgreich zu bearbeiten, folgen Sie bitte den untenstehenden Schritten und Hinweisen:

**1. Besuchen Sie die Website des Metadata Quality Dashboards des europäischen Metadatenportals** 

Besuchen Sie das Metadata Quality Dashboard des europäischen Metadatenportals und schauen sich hier die Bewertung des Datenportals für Deutschland an: [Govdata - Das Datenportal für Deutschland](https://data.europa.eu/mqa/catalogues/govdata/?locale=de). Dort finden Sie die Ergebnisse der Metadatenbewertung und können diese als Ausgangspunkt für Ihre Analyse nutzen.

**2. Lesen Sie die Fragen aufmerksam durch**

Bevor Sie die Antworten ansehen, versuchen Sie die Fragen eigenständig zu beantworten. Dies fördert das Verständnis für die zugrunde liegenden Probleme und deren Auswirkungen. Erst danach klappen Sie die untenstehenden Antworten dieser Übung auf und vergleichen Sie diese mit Ihren eigenen Überlegungen. So können Sie Lücken in Ihrem Verständnis identifizieren und Ihr Wissen vertiefen.


Die relevanten Fragen sind:

**Worauf beziehen sich die meisten Zugangsprobleme im deutschen Datenportal (GovData?)**
**Warum sind Elemente des DCAT-AP-Schemas verletzt? Warum wird das zum Problem?**


**3. Analysieren Sie die Ergebnisse des MQA-Tools**

Verwenden Sie das Metadata Quality Assessment (MQA)-Tool, um die Bewertung von GovData nachzuvollziehen. Die dort festgestellten Stärken und Schwächen bieten eine praktische Grundlage für Ihre weitere Analyse. Unter *Katalog Dashboard* finden Sie die eine Zusammenfassung aller Kriterien. 

`````{admonition} Worauf beziehen sich die meisten Zugangsprobleme im deutschen Datenportal?
:class: solution
````{admonition} Lösung
:class: dropdown
Wählen Sie den Reiter "Zugangsprobleme" in der oberen Leiste aus. Diese Seite gibt einen Überblick über alle Datensätze mit nicht erreichbaren *Distributions*, d.h. die hinterlegten Links sind z. B. defekt oder die entsprechenden Server nicht verfügbar.   Suchen Sie beispielhaft nach dem Datensatz *Statistisches Jahrbuch - Hamburg 2018/2019*. Öffnen Sie die Einträge zu diesem Datensatz. Man kann prüfen, ob der Datensatz über eine eindeutige und beständige PID (Persistent Identifier) verfügt, z. B. eine DOI, die den langfristigen Zugriff und die Auffindbarkeit gewährleistet. PIDs sind ein wesentliches Element für die Auffindbarkeit von Daten, da sie dafür sorgen, dass ein Datensatz langfristig und zuverlässig zugänglich bleibt, auch wenn sich der Speicherort oder die URL ändert. Ohne eine PID kann es zu Zugangsproblemen kommen, die durch "tote Links" oder veraltete URLs verursacht werden. Solche Probleme sind im deutschen Datenportal kein Einzelfall und betreffen die FAIR-Dimension *Auffindbarkeit* besonders stark, da Nutzer Schwierigkeiten haben, die gewünschten Daten zu finden oder darauf zuzugreifen. Dadurch leidet die Gesamtbewertungsnote des Portals.
````
`````

`````{admonition} Warum sind Elemente der DCAT-AP-Schema verletzt? Warum wird das zum Problem?
:class: solution
````{admonition} Lösung
:class: dropdown
Wählen wir “DCAT-AP Schemaverletzungen” im rechten oberen Reiter. Diese Unterseite gibt einen Überblick über Datensätze, die das DCAT-AP Schema nicht vollständig einhalten und somit potenzielle Nutzungsprobleme aufweisen. Schauen wir uns als Beispiel den Datensatz "Entwicklung von Umsatz und Beschäftigung im Großhandel in Schleswig-Holstein Februar 2022" an. Der Fehler bezieht sich hier auf das Element http://www.w3.org/ns/dcat#mediaType. Laut Fehlerbeschreibung wird für dieses Element ein BlankNode oder eine IRI erwartet, jedoch ist der tatsächliche Wert auf "application/pdf" gesetzt, was nicht den Schema-Anforderungen entspricht.

Dieser Fehler stellt eine Verletzung des DCAT-AP Standards dar, der Metadaten für offene Daten in der EU harmonisieren soll. Das DCAT-AP Schema erwartet für das mediaType-Feld eine Verknüpfung mit einem spezifischen IRI oder BlankNode, um eine einheitliche und maschinenlesbare Metadatenstruktur zu gewährleisten. Durch die falsche Angabe ("application/pdf" anstatt einer IRI) wird die maschinelle Lesbarkeit beeinträchtigt, was wiederum zu Zugangsproblemen führen kann. In der Praxis bedeutet dies, dass andere Systeme oder Anwendungen Schwierigkeiten haben könnten, den Dateityp automatisch zu erkennen und korrekt darzustellen. Der Wert ist zwar für Menschen verständlich, jedoch fehlt die Standardisierung für die maschinelle Verarbeitung, die das DCAT-AP Schema verlangt.

Das Problem liegt darin, dass die Interoperabilität und Konsistenz der Metadaten beeinträchtigt werden. Wenn Metadaten uneinheitlich oder fehlerhaft sind, können Portale und Anwendungen Daten nicht effizient verarbeiten oder austauschen, was den Zugang und die Nutzbarkeit der Daten für Nutzer stark einschränkt. Dies wirkt sich negativ auf die Gesamtbewertung der Metadatenqualität im Portal aus und untergräbt die Ziele des DCAT-AP Standards, nämlich die Harmonisierung und Vernetzung von Datenkatalogen in Europa.
````
`````

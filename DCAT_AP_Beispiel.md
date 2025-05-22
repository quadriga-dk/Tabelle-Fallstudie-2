# Beispiel und Implementierungen 

````{margin}
```{admonition} Hinweis
:class: hinweis
CKAN unterstützt Organisationen und Gruppen, die jeweils ihre eigenen Daten verwalten, aber Teil eines gemeinsamen Portals sein können. Damit eignet es sich besonders für dezentrale Verwaltungsstrukturen, z. B. bei föderalen Behörden oder wissenschaftlichen Konsortien. Weitere Informationen zu CKAN in der Verwaltungspraxis erhalten Sie beispielsweise bei <a href="https://open.nrw/open-data/informationen-fuer-entwicklerinnen-und-entwickler" class="external-link" target="_blank">Open.NRW</a>.
```
````

Die Umsetzung von Metadatenrepositorien mit DCAT-AP-Vokabular erfolgt meistens durch die Verwendung von *Comprehensive Knowledge Archive Network (CKAN)*. <a href="https://de.wikipedia.org/wiki/CKAN" class="external-link" target="_blank">CKAN</a> ist die weltweit führende Open-Source-Software für Datenportale und erleichtert das Veröffentlichen, Teilen und Arbeiten mit Daten. Dabei handelt es sich um ein Datenmanagementsystem, das eine leistungsstarke Plattform zum Katalogisieren, Speichern und Zugreifen auf Datensätze bietet. Zu den Funktionen von CKAN gehören neben einer benutzerfreundlichen Oberfläche unter anderem ein vollständiges <a href="https://de.wikipedia.org/wiki/Programmierschnittstelle" class="external-link" target="_blank">Application Programming Interface</a> (API) für Daten und Katalog, diverse Visualisierungstools und vieles mehr {cite}`CKAN_User_Guide`.

````{margin}
```{admonition} Hinweis
:class: hinweis
CKAN bietet einfache Visualisierungsfunktionen an (Diagramme, Tabellenansichten), kann aber durch Plugins oder externe Tools wie Recline.js, DataWrapper, Grafana, Jupyter Notebooks erweitert werden. Auch die direkte Integration mit RDF-Triplestores oder SPARQL-Endpunkten ist über Erweiterungen denkbar.
```
````

In CKAN werden Daten als Datensätze organisiert, die jeweils eine Sammlung von Informationen wie beispielsweise Kriminalstatistiken oder Wetterdaten enthalten. Jeder Datensatz umfasst Metadaten (z. B. Titel, Herausgeber, Format) und mehrere Ressourcen, die die eigentlichen Daten in verschiedenen Formaten (z. B. CSV, PDF) bereitstellen {cite}`CKANWang`. Ressourcen können direkt in CKAN gespeichert oder als Links auf externe Quellen bereitgestellt werden. CKAN ermöglicht eine flexible Datenverwaltung und Zugänglichkeit in verschiedenen Formaten und fördert dadurch sowohl die Zusammenarbeit auf interinstitutioneller Ebene als auch das zivile Vertrauen durch erhöhte Transparenz. Des Weiteren können die Datenverwaltungskapazitäten des CKAN zur Datenanalyse, Datenaufbewahrung und Veröffentlichung im akademischen und dienstlichen Bereich verhelfen {cite}`Winn2013`. 

Das deutsche Metadatenportal <a href="https://www.govdata.de/" class="external-link" target="_blank">GovData</a> wurde unter Verwendung der zuvor beschriebenen Standards und Systeme entwickelt. Auf diesem Portal können unterschiedlichste Datensätze von deutschen Verwaltungsinstitutionen aller Ebenen (Kommunen, Länder, Bund) durchsucht und auf verschiedenste Art gefiltert werden. 

Im nächsten Kapitel befassen wir uns mit ausgewählten Datensätzen, die im Portal verfügbar sind (dank interoperabler Technologien), sowie mit den Vorteilen und Schwächen der aktuellen Umsetzung im Rahmen der Philosophie offener Daten.

---
lang: de-DE
---

(portale)=
# Metadatenportale

Im Rahmen dieser Fallstudie befassen wir uns mit der systematischen Abfrage und Nutzung von Metadaten, wie sie über das europäische Metadatenportal <a href="https://www.data.europa.eu/" class="external-link" target="_blank">data.europa</a> bereitgestellt werden. Dieses Portal bildet das Beispiel um sich mit der Datenstruktur von Datenportalen auf verschiedenen Ebenen vertraut zu machen – lokal, national und europäisch – und zu verstehen, wie Metadaten über diese Ebenen hinweg abgerufen und verarbeitet werden können.

## Aufbau von Datenportalen

Datensätze werden zunächst von Datenbereitstellern auf lokaler Ebene erfasst, etwa durch Kommunen oder Landesbehörden. Diese lokalen Datensätze werden anschließend auf landesweiten Plattformen aggregiert. In Berlin ist das <a href="https://daten.berlin.de/" class="external-link" target="_blank">Berlin Open Data</a> und in Brandenburg das Portal <a href="https://datenadler.de/home?locale=de" class="external-link" target="_blank">DatenAdler</a>. Um den überregionalen Wissensaustausch zu ermöglichen, fließen die Metadaten aus den einzelnen Landesportalen in das bundesweite Portal <a href="https://www.govdata.de/" class="external-link" target="_blank">GovData</a> ein.

Im Rahmen der europäischen Datenintegration werden diese nationalen Daten schließlich auf der Plattform <a href="https://data.europa.eu/de" class="external-link" target="_blank">data.europa.eu</a> bereitgestellt. Dadurch entsteht eine mehrstufige Dateninfrastruktur (s. Abb. 3.3), die es ermöglicht, Metadaten auf verschiedenen Ebenen gezielt zu suchen, zu filtern und für Forschungszwecke zu nutzen.


```{figure} /assets/Metadatenportale.png
---
name: Plattformen
alt: Eine grafische Darstellung von (Meta-)Datenplattformen verschiedener Ebenen von der lokalen bis zur europäischen.
---
Mehrstufige Dateninfrastruktur durch Plattformen verschiedener Ebenen, eigene Darstellung.
```

Metadaten zu Datensätzen sind also in mehreren Portalen einsehbar, wobei zentrale Portale wie das bundesweite und das europäische, die Daten von den "unteren" Ebenen harvesten (s. Abb. 3.4). Das heißt, dass über diese Portale nicht zwangsweise ein direkter Zugriff auf die eigentlichen Datensätze möglich ist, da sie diese Daten nicht halten. Allerdings werden zunehmend nicht mehr nur die Metadaten abgefragt und somit angezeigt, welche Daten verfügbar sind, sondern zunehmend auch Links zu den Datensätzen bereitgestellt, sodass diese auch auf den zentralen Plattformen direkt von den Datenbereitstellern heruntergeladen werden können, ohne auf deren Webseite gehen zu müssen. Der Vorteil von zentralen Plattformen liegt in dem Vergleich und der Nebeneinanderstellung vergleichbarer Datensätze - beispielsweise Baumkatasterdaten aus mehreren Städten aus dem gesamten Bundesgebiet. 


```{figure} /assets/StandOffener.png
---
name: Datenbezug von lokal bis europäisch
alt: Eine grafische Darstellung des Datenbezugs von der lokalen bis zur europäischen Ebene
---
Darstellung des Datenbezugs von der lokalen bis zur europäischen Ebene, Bildquelle: Open.NRW
<span style="color:red">*Bitte Quelle angeben; scheinbar gab es auch einen Zeitstempel (Anzahl X Daten zu Zeitpunkt X)*</span>
```


## Metadatenportale und DCAT-AP

In Deutschland findet ein kontinuierlicher Austausch von Daten zwischen Datenbereitstellern wie Kommunen oder Bundeseinrichtungen und GovData, dem zentralen Datenportal, statt.  
Um diesen Datenaustausch effizient und einheitlich zu gestalten, hat die Fachgruppe GovData im November 2016 beschlossen, den europäischen Metadatenstandard DCAT-AP als Grundlage zu verwenden. Dabei wurde eine speziell angepasste deutsche Version entwickelt: DCAT-AP.de. Diese nationale Anpassung des europäischen Standards „DCAT-AP v2.0“ wurde als einheitlicher Metadatenstandard eingeführt und ermöglicht den strukturierten Austausch von Metadaten zu öffentlichen Verwaltungsdaten in ganz Deutschland {cite}`DCAT-AP.de2022`.

Seit Anfang 2019 akzeptiert GovData ausschließlich Metadaten, die im Standard DCAT-AP.de bereitgestellt werden.
Mit der Einführung seines Standards hat sich DCAT-AP.de zu einem unverzichtbaren Werkzeug für die Standardisierung und Interoperabilität von Metadaten im öffentlichen Sektor entwickelt {cite}`DCATFraunhofer`. Es schafft die Grundlage für eine effiziente Datenbereitstellung und erleichtert den Datenaustausch zwischen verschiedenen Verwaltungsebenen und Institutionen {cite}`DCATEurope`. Die Einführung dieses Standards ermöglicht es, die Vielfalt der bereitgestellten Datensätze konsistent zu strukturieren und deren Auffindbarkeit sowie Nachnutzbarkeit deutlich zu verbessern.


**Literatur**

```{bibliography}
:filter: docname in docnames
```

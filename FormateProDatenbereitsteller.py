from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
import matplotlib.pyplot as plt

# SPARQL Endpoint und Abfrage
sparql = SPARQLWrapper("https://data.europa.eu/sparql")
sparql.setQuery("""
PREFIX dcat: <http://www.w3.org/ns/dcat#>
PREFIX dct: <http://purl.org/dc/terms/>
PREFIX dcatde: <http://dcat-ap.de/def/dcatde/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX pg: <http://dcat-ap.de/def/politicalGeocoding/>

SELECT ?contributorID (COUNT(DISTINCT ?format) AS ?formatCount)
WHERE {
  ?datasetURI a dcat:Dataset;
              dct:title ?datasetTitle;
              dcatde:contributorID ?contributorID;
              dct:modified ?modified.
  OPTIONAL { ?datasetURI dcat:catalog ?catalog. }
  FILTER((LANG(?datasetTitle) = "" || LANG(?datasetTitle) = "de") && CONTAINS(LCASE(?datasetTitle), "baumkataster"))
  FILTER(CONTAINS(STR(?modified), "2022") || CONTAINS(STR(?modified), "2023") || CONTAINS(STR(?modified), "2024"))

  ?datasetURI dcat:distribution ?distribution.
  ?distribution dct:format ?format.
}
GROUP BY ?contributorID
""")
sparql.setReturnFormat(JSON)

# Ergebnisse abrufen
results = sparql.query().convert()

import re

# Funktion, um den Namen des Contributors zu extrahieren
def extract_contributor_name(url):
    match = re.search(r'([^/]+)$', url)  # Letzten Teil der URL extrahieren
    if match:
        return match.group(1)
    return url  # Fallback, falls kein Match gefunden wird

# Daten in ein DataFrame umwandeln
data = [(extract_contributor_name(result['contributorID']['value']), result['formatCount']['value']) for result in results['results']['bindings']]
df = pd.DataFrame(data, columns=["Contributor Name", "Format Count"])

# Visualisierung
df['Format Count'] = df['Format Count'].astype(int)  # In Integer umwandeln
df.set_index('Contributor Name', inplace=True)

# Diagramm erstellen mit angepasster Breite
ax = df.plot(kind='bar', width=0.8)  # Breite anpassen
plt.title('Anzahl der Formate pro Datenbereitsteller', fontsize=14, fontweight='bold')
plt.xlabel('Name der Datenbereitsteller', fontsize=12)
plt.ylabel('Anzahl der Formate', fontsize=12)

# X-Achsen-Beschriftungen zentrieren und rotieren
plt.xticks(rotation=45, ha='right', fontsize=10)

plt.tight_layout()  # Sorgen dafür, dass alles gut aussieht
plt.show()
---
lang: de-DE
---

(voraussetzungen)=
# Anwendung und technische Voraussetzungen

Diese Fallstudie umfasst einführende und erklärende Texte, SPARQL-Code sowie Übungen und Assessments zur Selbstüberprüfung.

Wir bieten drei verschiedene Zugangswege:

📘 Book-Only Mode: Im Browser lesen Sie unser interaktives Lehrbuch mit eingeschränkten Interaktionsmöglichkeiten. Dies erfordert keine Programmierkenntnisse oder Erfahrung mit Jupyter Notebooks.
Falls Sie die SPARQL-Abfragen dann doch ausführen und probieren möchten, können Sie dies über einen SPARQL Query Editor bzw. SPARQL Client auf einer Website Ihrer Wahl parallel im Browser tun, z. B.:
- auf der Seite des europäischen Metadatenportals <a href="https://data.europa.eu/sparql" class="external-link" target="_blank">DataEuropa</a>
- auf der Seite des deutschen Metadatenportals <a href="https://www.govdata.de/sparql-assistent" class="external-link" target="_blank">GovData</a>
- über das <a href="https://yasgui.org/" class="external-link" target="_blank">Yasgui-Tool</a>

🌨️ Cloud Mode: Ausführen und Anpassen der enthaltenen Jupyter Notebooks über Google Colab oder Binder. Kapitel mit ausführbaren Notebooks sind durch ein Raketen-Symbol (🚀) gekennzeichnet - klicken Sie darauf, um das Notebook in Colab zu öffnen.
<span style="color:red">*Haben wir diese Möglichkeiten tatsächlich? Dringend prüfen (s. Issue #136)*</span>

💻 Local Mode: Herunterladen der Jupyter Notebooks auf Ihren Computer zur lokalen Ausführung. Dies ermöglicht die Nutzung lokaler Daten und umfassende Anpassungen, erfordert aber Kenntnisse einer entsprechenden Ausführungsumgebung (z.B. Anaconda).

Minimal müssen Sie die in `requirements.txt` definierten Pakete installieren und dann den SPARQL-Kernel mit `jupyter sparqlkernel install --user` aktivieren. Wir empfehlen, dies in einem sog. virtual environment vorzunehmen.

Wählen Sie den Ansatz, der am besten zu Ihren Anforderungen passt. Sie können jederzeit zwischen den Methoden wechseln.




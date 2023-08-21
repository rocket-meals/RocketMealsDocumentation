OTA-Updates
===========

Die Rocket Meals App bietet Over-the-Air (OTA) Updates an, eine leistungsstarke Funktion, die es ermöglicht, Aktualisierungen der Basisversion der App und wichtige Sicherheitspatches ohne den traditionellen App Store-Prozess bereitzustellen. Diese Updates sind speziell für die Behebung von Sicherheitslücken und die Aktualisierung der Basisversion der App konzipiert und nicht für das Hinzufügen von neuen Inhalten wie Speiseplänen.

Implementierungstechnologie
---------------------------

Für die Bereitstellung von OTA-Updates nutzen wir den Dienst "Code Push" von Microsoft. Code Push ist ein Cloud-Service, der Entwicklern ermöglicht, Updates für ihre mobilen Anwendungen direkt an die Geräte der Benutzer zu senden, ohne den traditionellen App Store-Prozess durchlaufen zu müssen. Aktuell bietet Microsoft diesen Dienst kostenlos an. Sollte Microsoft jedoch in Zukunft Gebühren für die Nutzung von Code Push einführen, werden diese Kosten vom Kunden übernommen.

Was sind OTA-Updates?
----------------------

Over-the-Air (OTA) Updates sind Software-Aktualisierungen, die drahtlos an Geräte gesendet werden. Im Gegensatz zu traditionellen Updates, die über den App Store heruntergeladen werden müssen, ermöglichen OTA-Updates eine schnellere und direktere Aktualisierung der App. Dies ist besonders nützlich für die schnelle Behebung von Sicherheitslücken und die Aktualisierung der Basisversion der App.

Bereitstellungsprozess
-----------------------

Wir stellen Updates in einem angemessenen Umfang bereit und nutzen GitHub Actions für die Bereitstellung. GitHub Actions bietet ein kostenloses Kontingent von 3.000 Linux-Minuten pro Monat. Darüber hinausgehende Minuten werden zu einem Preis von $0,008 USD pro Minute berechnet. Ein Update benötigt etwa 15 Minuten, sodass mit einem Budget von $24 USD theoretisch bis zu 200 Updates pro Monat möglich sind. Historisch gesehen hat das kostenlose Kontingent für unsere Bedürfnisse ausgereicht und es sind keine zusätzlichen Kosten angefallen.

Kostenüberlegungen
-------------------

Es ist wichtig zu beachten, dass Kosten für die Bereitstellung von Updates anfallen können, wenn das kostenlose Kontingent von GitHub Actions überschritten wird. Diese Kosten werden vom Kunden getragen. In der Vergangenheit hat das kostenlose Kontingent jedoch ausgereicht und es sind keine zusätzlichen Kosten angefallen.

Zusammenfassend bieten OTA-Updates eine effiziente Möglichkeit, die Rocket Meals App zu aktualisieren und Sicherheitslücken zu schließen. Die Kosten für die Bereitstellung von Updates werden vom Kunden getragen, falls das kostenlose Kontingent von GitHub Actions überschritten wird. Bei Fragen oder Bedenken bezüglich der OTA-Updates stehen wir Ihnen gerne zur Verfügung.

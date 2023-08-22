Guthaben Abfrage: Eine Lösung für bargeldloses Bezahlen
======================================================

In der heutigen Zeit setzen viele Studierendenwerke auf bargeldlose Zahlungsmethoden. Es ist wahrscheinlich, dass auch Ihr Studierendenwerk Karten für Mitarbeiter und Studierende verwendet, auf die ein Guthaben aufgeladen werden kann, um kontaktlos zu bezahlen. Als Studierende haben wir selbst festgestellt, dass es oft schwierig ist, den aktuellen Guthabenstand auf der Karte zu überprüfen, insbesondere wenn lange Schlangen vor den Aufladeautomaten stehen.

Um dieses Problem zu lösen, haben wir die Guthaben-Leser-Funktion entwickelt. Nachdem das Guthaben gelesen wurde, wird es im Nutzerkonto und auf dem Endgerät gespeichert. Auf diese Weise können Endnutzer den Guthabenstand jederzeit direkt einsehen und über mehrere Geräte mit demselben Konto hinweg abrufen. Die angezeigten Informationen hängen von der jeweiligen Karte ab und können beispielsweise den aktuellen Stand, das letzte Aktualisierungsdatum und die letzte Abbuchung umfassen.

Wir bieten zwei Optionen zur Guthabenabfrage an: den NFC-Leser und den Balance-Synchronizer.

NFC-Leser
---------

Der NFC-Leser ermöglicht es dem Endgerät mit der Rocket Meals Software, die Daten der Karte mittels NFC-Technologie zu lesen. Um diese Funktion nutzen zu können, müssen jedoch einige Anforderungen erfüllt sein:

1. Das Endgerät muss über die Fähigkeit verfügen, mittels NFC Daten auszutauschen. Die meisten modernen Mobiltelefone unterstützen dies standardmäßig.
   a) iOS: Eine Liste der unterstützten iPhones und iPads wird hier hinzugefügt.
   b) Android: Eine Liste der unterstützten Android-Geräte wird hier hinzugefügt.

2. Das Endgerät muss neben der NFC-Unterstützung auch das entsprechende Protokoll unterstützen, mit dem Ihre Karte arbeitet.

3. Die zu lesende Karte muss entweder unverschlüsselten Lesezugriff ermöglichen oder Sie müssen uns eine Möglichkeit zur Entschlüsselung der Karte bereitstellen.

4. Derzeit unterstützen wir folgende (getestete) Karten und Protokolle:
   - Mifare DESFire von unverschlüsselten Karten. Ihr Kartenanbieter kann Ihnen sicherlich mehr Informationen dazu geben (z. B. InterCard). Sie können a) die Rocket Meals Demo App verwenden, um Ihre Karte zu testen und zu sehen, ob unsere aktuelle Implementierung Ihre Karte standardmäßig unterstützt. b) Sie können uns eine Beispielkarte zusenden, und wir werden diese gerne analysieren. Wenn wir Daten auf der Karte lesen können, werden wir die Lesefunktion implementieren.
   - Studierendenwerk Osnabrück

Balance-Synchronizer (in Kürze verfügbar)
------------------------------------------

In einigen Fällen ist es möglicherweise nicht möglich, die Karte per NFC zu lesen, sei es aufgrund eines nicht unterstützten Protokolls oder einer verschlüsselten Karte. Wir arbeiten bereits an Lösungen für solche Herausforderungen, um sicherzustellen, dass Sie immer Zugriff auf Ihr Guthaben haben.

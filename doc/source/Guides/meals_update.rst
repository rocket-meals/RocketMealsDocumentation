Aktualisierung des Speiseplans
==============================

Die regelmäßige Aktualisierung des Speiseplans in Ihrer Rocket Meals-Anwendung ist von entscheidender Bedeutung, um sicherzustellen, dass Ihre Kunden stets über die neuesten verfügbaren Speisen informiert sind. Es stehen Ihnen verschiedene Methoden zur Verfügung, um Ihren Speiseplan in Rocket Meals zu aktualisieren:

TL1 Export
---------------------------------------------

Eine effiziente Methode zur Aktualisierung Ihres Speiseplans ist die automatische Integration durch den TL1 Export. Dieser Prozess stellt sicher, dass Ihre Speisen immer aktuell in Rocket Meals präsentiert werden.

1. Bereitstellung des Exports:
    - Sie können uns den Export auf folgende Weise bereitstellen:
        a) Über eine eigene URL von Ihnen. Wir greifen dann auf diese Daten zu und pflegen sie in Rocket Meals ein.
        b) FTP: Sie können den Export per FTP an den von uns bereitgestellten Server für Ihre Rocket Meals-Anwendung senden. Die Zugangsdaten erhalten Sie von uns.
2. Anforderungen für den TL1 Export:
    - Der TL1 Export erfordert die Erfüllung bestimmter Bedingungen. Bitte beachten Sie, dass für die Anpassung eines Exports in das erforderliche Format möglicherweise Kosten bei TL1 anfallen.
        - Die Identifizierung einer Speise erfolgt durch Aggregation der `REZEPTUR_ID` über den Namen der Speise.
    - Beispiel eines Exports:
        - Die Tabelle wurd zur Darstellung transponiert (Spalten sind eigentlich Zeilen).
        - Die Speise `Paprika-Hähncheneintopf mit Nudeln` wird hier dargestellt.
            - Es ist ersichtlich, dass der Name der Speise gleich ist, die Speise jedoch aus zwei Bestandteilen (`REZEPTUR_ID`) besteht: `2045` und `2961`.
            - Aus den Feldern der `REZEPTUR_ID` wird ein zusammengesetzter Schlüssel erstellt: `2045-2961`.
                - Änderungen am Namen der Speise aus Marketing- oder Herstellungsgründen führen nicht zu einer Verwechslung der Speise. Funktionen, die mit der Speise verknüpft sind (z.B. Fotos, Bewertungen, Kommentare), bleiben erhalten.
                - Es darf keine andere Speise mit denselben Werten der `REZEPTUR_ID` geben, da sie sonst als dieselbe Speise erkannt wird.
            - Der Name der Speise wird formatiert, indem Kennzeichnungen (Allergene) in Klammern entfernt werden.
                - Aus dem Eintrag: `Paprika-Hähncheneintopf mit Nudeln (40,a,g) | Weizenbrötchen (1,21,a,f)` wird `Paprika-Hähncheneintopf mit Nudeln, Weizenbrötchen`.

.. list-table:: TL1 Beispiel Export (Auszug und Darstellung transponiert)
   :widths: 25 25 50
   :header-rows: 1

   * - Eigenschaft
     - Zeile 1
     - Zeile 2
   * - MENSA
     - Beispiel Mensa
     - Beispiel Mensa
   * - DATUM
     - 02.08.2023
     - 02.08.2023
   * - VK-ArtikelNr
     - 1714
     - 1714
   * - VK-GebindeNR
     - 3614
     - 3614
   * - SPEISE
     - Eintopf (Terrine, Teller)
     - Eintopf (Terrine, Teller)
   * - SPEISE_BEZEICHNUNG
     - Eintopf Terrine
     - Eintopf Terrine
   * - REZEPTUR_ID
     - 2045
     - 2961
   * - TEXT1
     - Paprika-Hähncheneintopf mit Nudeln (40,a,g)
     - Paprika-Hähncheneintopf mit Nudeln (40,a,g)
   * - TEXT2
     - Weizenbrötchen (1,21,a,f)
     - Weizenbrötchen (1,21,a,f)
   * - TEXT3
     -
     -
   * - TEXT4
     -
     -
   * - TEXT5
     -
     -
   * - TEXT1_1
     - paprika stew with chicken and noodles (40,a,g)
     - paprika stew with chicken and noodles (40,a,g)
   * - TEXT2_1
     - Bread roll (1,21,a,f)
     - Bread roll (1,21,a,f)
   * - STD_PREIS
     - 1,80
     - 1,80
   * - BED_PREIS
     - 4,10
     - 4,10
   * - GÄSTE_PREIS
     - 5,10
     - 5,10
   * - FREI1
     - a
     - a
   * - FREI2
     -
     -
   * - FREI3
     -
     -
   * - ZSNUMMERN
     - 1, 14, 18, 21, a, g, f, 0
     - 1, 14, 18, 21, a, g, f, 0
   * - ZSNAMEN
     - mit Farbstoff, Rindfleisch, Fleisch aus artgerechter Tierhaltung, vegan, Glutenhaltiges Getreide (a), Milch und Laktose (g), Soja (f), zusatzstoff- und allergenfrei
     - mit Farbstoff, Rindfleisch, Fleisch aus artgerechter Tierhaltung, vegan, Glutenhaltiges Getreide (a), Milch und Laktose (g), Soja (f), zusatzstoff- und allergenfrei
   * - NAEHRWERTEJE100G
     - Brennwert=2385 kJ (570 kcal), Fett=18,9g, davon gesättigte Fettsäuren=5,6g, Kohlenhydrate=63,4g, davon Zucker=13,7g, Ballaststoffe=4,1g, Eiweiß=29,3g, Salz=4,1g
     - Brennwert=2385 kJ (570 kcal), Fett=18,9g, davon gesättigte Fettsäuren=5,6g, Kohlenhydrate=63,4g, davon Zucker=13,7g, Ballaststoffe=4,1g, Eiweiß=29,3g, Salz=4,1g
   * - NAEHRWERTEJEPORT
     -
     -



API Nutzung
--------------------------------

Alternativ haben Sie die Möglichkeit, den Speiseplan über unsere API zu aktualisieren. Dies bietet Ihnen mehr Kontrolle über die Aktualisierungen und ermöglicht es Ihnen, Änderungen sofort umzusetzen.

- Sie können die `API <../Reference/api.html>`_ verwenden, um den Speiseplan individuell anzupassen. Bitte beachten Sie, dass bei Verwendung der `automatischen Übersetzung <../Features/automatic-translation.html>`_ jeder neue Speisename automatisch übersetzt wird, sofern Sie dies nicht deaktivieren.

Unabhängig von der gewählten Methode ist es wichtig, dass Sie Ihren Speiseplan regelmäßig aktualisieren, um sicherzustellen, dass Ihre Kunden stets über die neuesten verfügbaren Speisen informiert sind. Wir stehen Ihnen bei jedem Schritt des Prozesses zur Seite und sorgen dafür, dass Ihre Rocket Meals-Anwendung immer auf dem neuesten Stand und für Ihre Kunden attraktiv ist.


Manuelle Aktualisierung
--------------------------------

Alternativ haben Sie die Möglichkeit, den Speiseplan manuell über zu aktualisieren. Wir raten hiervon jedoch ab, da es eine Menge arbeit bedeuetet, dies täglich für alle Einrichtungen zu tätigen. Ein automatischer Prozess ist fehlerfreier und schneller.

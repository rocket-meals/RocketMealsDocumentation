Speiseplan
==========

Das Speiseplan-Modul ist ein integraler Bestandteil der Rocket Meals Applikation und dient als zentrale Schnittstelle, die den Benutzern eine umfassende Übersicht über die verfügbaren Speisen in verschiedenen Betriebskantinen bietet.


Definitionen: Speise vs. Speiseangebot
------------

Bevor wir weiter ins Detail gehen, ist es wichtig, die Unterscheidung zwischen einer "Speise" und einem "Speiseangebot" zu klären.

**Speise**

Eine "Speise" ist ein Datensatz, der die grundlegenden Informationen enthält, auf die verschiedene Speiseangebote zurückgreifen können. Die Attribute einer Speise umfassen:

- **ID**: Eindeutige Identifikationsnummer der Speise (kann alphanumerisch sein)
- **Kalorien (calires_kcal)**: Kaloriengehalt in Kilo-Kalorien
- **Kohlenhydrate (carbohydrate_g)**: Kohlenhydratgehalt in Gramm
- **Fette (fat_g)**: Fettgehalt in Gramm
- **Ballaststoffe (fiber_g)**: Ballaststoffgehalt in Gramm
- **Proteine (protein_g)**: Proteingehalt in Gramm
- **Gesättigte Fettsäuren (saturated_fat_g)**: Gehalt an gesättigten Fettsäuren in Gramm
- **Natrium (sodium_g)**: Natriumgehalt in Gramm
- **Zucker (sugar_g)**: Zuckergehalt in Gramm
- **Zusatzinformationen (extra)**: Individuelle Anpassungen und weitere Details
- **Übersetzungen (translations)**: Mehrsprachige Bezeichnungen der Speise
  - **Name**: Bezeichnung der Speise
  - Weitere Informationen zur API-Integration finden Sie [hier](../Reference/api.html).
- **Bild (image)**: Visuelle Darstellung der Speise
- **Feedbacks**: Verknüpfung zu Benutzerbewertungen und -rückmeldungen
- **Markierungen (markings)**: Informationen zu Allergenen und anderen Kennzeichnungen

**Speiseangebot**

Ein "Speiseangebot" ist eine spezifische Instanz einer Speise, die zu einem bestimmten Zeitpunkt in einer bestimmten Kantine verfügbar ist. Die Attribute eines Speiseangebots umfassen:
Ein Speiseangebot kann unterschiedliche Nährwerte und Kennzeichnungen haben als die eigentliche Speise. Dies resultiert aus unserer Erfahrung, dass es aufgrund von Umstellungen bei Lieferanten, Portionsgrößen oder unvorhergesehenem Zutatenmangel vorkommen kann, dass die angebotene Speise anders als sonst ist. Damit Sie flexibel bleiben können, werden diese Informationen sowohl für die Speise als auch für das Speiseangebot jeweils angegeben.

- **Speise (food)**: Verknüpfung zur zugrundeliegenden Speise
  - Kennzeichnungen müssen für jedes Speiseangebot separat angegeben werden.
- **Preise**:
  - **Mitarbeiter (price_employee)**: Preis in Euro für Angestellte
  - **Gäste (price_guest)**: Preis in Euro für Gäste
  - **Studierende (price_student)**: Preis in Euro für Studierende
- **Datum (date)**: Gültigkeitsdatum des Angebots
- **Kantine (canteen)**: Verknüpfung zur Betriebskantine, in der das Angebot verfügbar ist
- **Kennzeichnungen (markings)**: Informationen zu Allergenen und anderen Kennzeichnungen
- **Kalorien (calires_kcal)**: Kaloriengehalt in Kilo-Kalorien
- **Kohlenhydrate (carbohydrate_g)**: Kohlenhydratgehalt in Gramm
- **Fette (fat_g)**: Fettgehalt in Gramm
- **Ballaststoffe (fiber_g)**: Ballaststoffgehalt in Gramm
- **Proteine (protein_g)**: Proteingehalt in Gramm
- **Gesättigte Fettsäuren (saturated_fat_g)**: Gehalt an gesättigten Fettsäuren in Gramm
- **Natrium (sodium_g)**: Natriumgehalt in Gramm
- **Zucker (sugar_g)**: Zuckergehalt in Gramm

Tagesauswahl
------------

Benutzer können den gewünschten Tag für die Anzeige des Speiseplans auswählen. Standardmäßig wird der aktuelle Tag in der App angezeigt. Wenn an einem bestimmten Tag keine Speisen verfügbar sind, z. B. an einem Samstag, werden die Angebote für die nächsten und die vergangenen sieben Tage angezeigt, sodass Benutzer vor- oder zurückblättern können.

Speisedarstellung
-----------------

Die Speisen werden in einem Rasterlayout dargestellt, wobei der Schwerpunkt auf dem Bild der Speise liegt. Bilder müssen von Ihnen hochgeladen werden. Dies kann lediglich als Nutzer mit der `Benutzerrolle und Berechtigungen <../CoreFeatures/user-roles-permissions.html>`_ Administrator oder Moderator geschehen. Wenn kein Bild der Speise verfügbar ist, wird ein konfigurierbares Platzhalterbild verwendet. Der Name der Speise wird darunter in der ausgewählten Sprache angezeigt. Wenn keine Übersetzung verfügbar ist, wird der Name in Deutsch oder, wenn möglich, in Englisch angegeben. Übersetzungen müssen im Speiseplan-Export oder über die entsprechenden Schnittstellen bereitgestellt werden. Wenn die Funktion `Automatisches Übersetzen <../Features/automatic-translation.html>`_ gebucht wurde, werden diese Übersetzungen verwendet. Die Sortierung der Speisen erfolgt nach Beliebtheit, wobei "gelikte" Speisen nach vorne sortiert werden. Diese Funktion steht nur registrierten Benutzern zur Verfügung. Speisen mit entsprechenden Kennzeichnungen werden durch die `Kennzeichnung Einstellung <Features/ingredient-filter>` sortiert und hervorgehoben.

Detailansicht
-------------

Bei Auswahl einer Speise wird dem Benutzer eine detaillierte Ansicht der Speise präsentiert. Diese Detailansicht enthält Nährwertangaben (falls vorhanden), Kennzeichnungen und Allergene, `Speise-Bewertungen <../Features/meal-feedback.html>`_ (falls konfiguriert) und die Möglichkeit, den `Teller-Ticker <Features/meal-reminder>` zu aktivieren, um Erinnerungen zu erhalten, wenn die Speise erneut angeboten wird. Hierfür ist ein Benutzerkonto erforderlich. Alle Allergen- und Kennzeichnungsinformationen können veraltet sein, daher sind die `Speisekennzeichnungen ohne Gewähr <Appendices/ingredient-disclaimer>` und die Angaben vor Ort maßgeblich.

Schnelleinstellungen
---------------------

Benutzer haben Zugriff auf Schnelleinstellungen, um zu anderen Funktionen zu wechseln, darunter die Suche nach Speisen, die `Kennzeichnung Einstellung <../Features/ingredient-filter>` zur Anpassung von Vorlieben und Abneigungen, die Anpassung der `Preiskategorie <../Features/price-category.html>`_ und die Auswahl der Mensa.

Bereitstellung des Speiseplans
------------------------------

Der Speiseplan muss von Ihnen bereit gestellt werden. Wir bieten mehrere Möglichkeiten für einen `Speiseplan-Update <../Guides/meals-update.html>`_ an.

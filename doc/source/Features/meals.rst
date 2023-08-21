Speiseplan
==========

Der Speiseplan ist ein zentrales Element der Rocket Meals App, das den Benutzern einen Überblick über die in verschiedenen Mensen verfügbaren Speisen bietet.

Tagesauswahl
------------

Benutzer können den gewünschten Tag für die Anzeige des Speiseplans auswählen. Standardmäßig wird der aktuelle Tag in der App angezeigt. Wenn an einem bestimmten Tag keine Speisen verfügbar sind, z. B. an einem Samstag, werden die Angebote für die nächsten und die vergangenen sieben Tage angezeigt, sodass Benutzer vor- oder zurückblättern können.

Speisedarstellung
-----------------

Die Speisen werden in einem Rasterlayout dargestellt, wobei der Schwerpunkt auf dem Bild der Speise liegt. Wenn kein Bild der Speise verfügbar ist, wird ein konfigurierbares Platzhalterbild verwendet. Der Name der Speise wird darunter in der ausgewählten Sprache angezeigt. Wenn keine Übersetzung verfügbar ist, wird der Name in Deutsch oder, wenn möglich, in Englisch angegeben. Übersetzungen müssen im Speiseplan-Export oder über die entsprechenden Schnittstellen bereitgestellt werden. Wenn die Funktion `Automatisches Übersetzen <Features/automatic-translation>` gebucht wurde, werden diese Übersetzungen verwendet. Die Sortierung der Speisen erfolgt nach Beliebtheit, wobei "gelikte" Speisen nach vorne sortiert werden. Diese Funktion steht nur registrierten Benutzern zur Verfügung. Speisen mit entsprechenden Kennzeichnungen werden durch die `Kennzeichnung Einstellung <Features/ingredient-filter>` sortiert und hervorgehoben.

Detailansicht
-------------

Bei Auswahl einer Speise wird dem Benutzer eine detaillierte Ansicht der Speise präsentiert. Diese Detailansicht enthält Nährwertangaben (falls vorhanden), Kennzeichnungen und Allergene, `Speise-Bewertungen <Features/meal-feedback>` (falls konfiguriert) und die Möglichkeit, den `Teller-Ticker <Features/meal-reminder>` zu aktivieren, um Erinnerungen zu erhalten, wenn die Speise erneut angeboten wird. Hierfür ist ein Benutzerkonto erforderlich. Alle Allergen- und Kennzeichnungsinformationen können veraltet sein, daher sind die `Speisekennzeichnungen ohne Gewähr <Appendices/ingredient-disclaimer>` und die Angaben vor Ort maßgeblich.

Schnelleinstellungen
---------------------

Benutzer haben Zugriff auf Schnelleinstellungen, um zu anderen Funktionen zu wechseln, darunter die Suche nach Speisen, die `Kennzeichnung Einstellung <Features/ingredient-filter>` zur Anpassung von Vorlieben und Abneigungen, die Anpassung der Preiskategorie und die Auswahl der Mensa.

Bereitstellung des Speiseplans
------------------------------

Der Speiseplan muss im JSON-Format bereitgestellt werden.

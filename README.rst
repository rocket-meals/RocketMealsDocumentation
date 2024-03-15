Rocket Meals Dokumentation
============

Dies ist das Repo für die Rocket Meals Dokumenation. Vermutlich sind Sie auf der Suche nach:

- Die `Dokumentation <https://rocket-meals.github.io/RocketMealsDocumentation/>`_ kann hier gefunden werden.

- Die `Homepage <https://rocket-meals.github.io/RocketMealsDocumentation/>`_ kann hier gefunden werden.

----------------

# Manuelles Bauen der Dokumentation

- `pip3 install ".[doc]"`

## HTML
- `sphinx-build doc/source <ZIEL_ORDNER>`

## PDF
- `sphinx-build -b latex doc/source <ZIEL_ORDNER>`
- `cd <ZIEL_ORDNER>`
- `make`
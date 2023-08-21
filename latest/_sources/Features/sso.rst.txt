Single Sign-On (SSO)
=====================

Single Sign-On (SSO) ist ein Authentifizierungsverfahren, das es Benutzern ermöglicht, auf mehrere Anwendungen oder Dienste zuzugreifen, indem sie sich nur einmal anmelden. Mit SSO können Benutzer ihre Anmeldeinformationen (z.B. Benutzername und Passwort) einmal eingeben und dann auf verschiedene Dienste zugreifen, ohne sich jedes Mal erneut anmelden zu müssen.

Vorteile von SSO
----------------

1. **Benutzerfreundlichkeit**: Benutzer müssen sich nur einmal anmelden, um auf mehrere Dienste zuzugreifen, was den Anmeldeprozess vereinfacht und beschleunigt.
2. **Verbesserte Sicherheit**: Da Benutzer nur ein Passwort benötigen, können sie ein stärkeres Passwort wählen und es regelmäßig ändern, ohne sich an mehrere Passwörter erinnern zu müssen.
3. **Vereinfachtes Passwortmanagement**: IT-Abteilungen müssen weniger Passwörter verwalten und zurücksetzen, was den Verwaltungsaufwand reduziert.
4. **Schnellerer Zugriff**: Benutzer können schneller auf die benötigten Dienste zugreifen, da sie den Anmeldeprozess nicht für jede Anwendung wiederholen müssen.

Unterstützte SSO-Mechanismen
----------------------------

Rocket Meals unterstützt vier Standardtypen von SSO-Mechanismen:

1. **OpenID**: Ein offener Standard für die Authentifizierung von Benutzern. Weitere Informationen finden Sie in der `OpenID Connect Core 1.0 Spezifikation <https://openid.net/specs/openid-connect-core-1_0.html>`_.
2. **OAuth 2.0**: Ein Protokoll, das es Anwendungen ermöglicht, auf Kontoinformationen von Benutzern zuzugreifen, ohne deren Passwort zu kennen. Weitere Informationen finden Sie im `RFC 6750 <https://www.ietf.org/rfc/rfc6750.txt>`_.
3. **LDAP**: Ein Protokoll zur Abfrage und Änderung von Verzeichnisdiensten, das häufig in Unternehmensumgebungen verwendet wird. Weitere Informationen finden Sie im `RFC 4511 <https://datatracker.ietf.org/doc/html/rfc4511>`_.
4. **SAML**: Ein XML-basiertes Framework für den Austausch von Authentifizierungs- und Autorisierungsinformationen. Weitere Informationen finden Sie im `RFC 7522 <https://datatracker.ietf.org/doc/html/rfc7522>`_.

Intern verwenden wir die SSO-Mechanismen von Directus, die in der `Directus-Dokumentation <https://docs.directus.io/self-hosted/sso.html>`_ beschrieben sind.


Einrichtung von SSO
-------------------

Für die Einrichtung von SSO in Rocket Meals werden entsprechende Konten bei den jeweiligen Plattformen benötigt. Wir unterstützen Sie gerne bei der SSO-Einrichtung von ausgewählten Google und Apple, sofern die notwendigen Voraussetzungen von `Google <../Requirements/google_developer_account.html>`_ und `Apple <../Requirements/apple_developer_account.html>`_ erfüllt sind.

Beispielhafte Google SSO Einrichtung
-------------------

Keine Sorge, wir bieten auch eine Unterstützung bei der Einbindung an.

Um Google OpenID als externen Anbieter nutzen zu können, müssen Sie folgende Schritte befolgen:

1. Gehen Sie zur Google `Cloud Console <https://console.cloud.google.com/>`_.
2. Wählen Sie ein neues Projekt aus oder erstellen Sie eines.
3. Gehen Sie zu `APIs & Dienste -> OAuth-Zustimmungsbildschirm <https://console.cloud.google.com/apis/credentials/consent>`_ in der Seitenleiste.
    1. Wählen Sie den gewünschten Zugriff aus:
        - Wählen Sie Intern, wenn nur Personen innerhalb Ihrer Organisation Zugriff haben sollen.
        - Wählen Sie Extern, um jedem mit einem Google-Konto den Zugriff zu ermöglichen.
    2. Füllen Sie die Felder nach Ihren Wünschen aus.
        - Die autorisierten Domains fügen eine zusätzliche Sicherheitsebene hinzu, sind jedoch nicht erforderlich. Wenn Sie sie ausfüllen, sollte es die Domain sein, auf der Ihre Rocket Meals läuft.
    3. Bei den Bereichen müssen Sie ".../auth/userinfo.email", "".../auth/userinfo.profile" und "openid" auswählen.
4. Gehen Sie in der Seitenleiste zu `Anmeldedaten <https://console.cloud.google.com/apis/credentials>`_.
5. Klicken Sie auf `Anmeldedaten erstellen -> OAuth-Client-ID <https://console.cloud.google.com/apis/credentials/oauthclient>`_.
    1. Wählen Sie "Webanwendung" im Anwendungstyp aus.
    2. Die autorisierten JavaScript-Ursprünge fügen eine zusätzliche Sicherheitsebene hinzu, sind jedoch nicht erforderlich. Wenn Sie sie ausfüllen, sollte es die Adresse Ihrer Rocket Meals Instanz sein. Zum Beispiel "https://meine-app.rocket-meals.de".
    3. Geben Sie bei den autorisierten Weiterleitungs-URIs die Adresse Ihrer Rocket Meals Instanz plus /auth/login/google/callback ein. Zum Beispiel sollten Sie https://meine-app.rocket-meals.de/auth/login/google/callback eingeben, wobei "https://meine-app.rocket-meals.de" die Adresse Ihrer Rocket Meals Instanz sein sollte.
6. Klicken Sie auf Erstellen, und ein Fenster wird mit der **Client ID** und dem **Client Secret** angezeigt. Speichern Sie beide für die spätere Verwendung. Diese sind dann für die Einrichtung notwendig.

Die Einbindung des SSO-Anbieter können wir dann übernehmen.

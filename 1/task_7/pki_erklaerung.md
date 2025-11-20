# Public Key Infrastructure (PKI) und Zertifikate

## Rolle der PKI in der IT-Sicherheit
Eine Public Key Infrastructure (PKI) ist ein System zur Verwaltung, Verteilung und Überprüfung von digitalen Zertifikaten und öffentlichen Schlüsseln. Sie ermöglicht sichere Kommunikation, Authentifizierung und Integrität in Netzwerken, indem sie die Identität von Kommunikationspartnern überprüfbar macht. PKI ist die Grundlage für HTTPS, E-Mail-Verschlüsselung, VPNs und viele weitere Sicherheitsanwendungen.

## Anforderungen an Zertifikate
- Eindeutige Identifikation des Besitzers
- Vertrauenswürdige Ausstellung durch eine Certificate Authority (CA)
- Integrität und Unveränderbarkeit
- Gültigkeitsdauer und Widerrufsmöglichkeit

## Bestandteile eines Zertifikats
- **Subject:** Identität des Besitzers (z.B. Domainname, Name, Organisation)
- **Issuer:** Aussteller des Zertifikats (CA)
- **Public Key:** Öffentlicher Schlüssel des Besitzers
- **Serial Number:** Eindeutige Nummer des Zertifikats
- **Validity Period:** Gültigkeitszeitraum (von/bis)
- **Signature:** Digitale Signatur der CA
- **Extensions:** Zusätzliche Informationen (z.B. Verwendungszweck, alternative Namen)

## Bedeutung der Bestandteile für sichere Kommunikation
- **Subject & Public Key:** Ermöglichen die Zuordnung des Schlüssels zur Identität
- **Issuer & Signature:** Gewährleisten die Vertrauenswürdigkeit durch die CA
- **Validity Period:** Schützt vor abgelaufenen oder kompromittierten Zertifikaten
- **Extensions:** Definieren, wofür das Zertifikat verwendet werden darf

**Hinweis:**
- Für produktive Umgebungen werden Zertifikate von vertrauenswürdigen CAs wie "Let's Encrypt" ausgestellt.
- Self-Signed-Zertifikate sind nur für Testzwecke geeignet.

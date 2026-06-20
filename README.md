# Cyber Port Scanner

## Présentation

Cyber Port Scanner est un programme Python permettant d’analyser l’état des ports TCP d’une cible donnée (adresse IP ou nom de domaine).

Il permet d’identifier les ports ouverts sur une machine ainsi que les services associés lorsqu’ils sont connus.

Le programme prend en charge la résolution DNS automatique et le scan de plages de ports définies par l’utilisateur.

---

## Fonctionnalités

* Analyse d’une cible via adresse IP ou nom de domaine
* Résolution DNS automatique
* Scan d’une plage de ports personnalisée
* Détection des ports ouverts
* Identification des services associés (HTTP, SSH, HTTPS, etc.)

---

## Utilisation

Exécution du programme :

```bash
python scanner_de_ports.py
```

L’utilisateur est invité à :

* entrer une cible (IP ou domaine)
* définir un port de début
* définir un port de fin

---

## Exemple d’exécution

### Exemple 1

```text
Entrez une IP ou un nom de domaine : corneilleligan.me
corneilleligan.me correspond à l'IP 216.198.79.1

Port de début : 12
Port de fin : 522

Port 80 : OUVERT (http)
Port 443 : OUVERT (https)
```

### Exemple 2

```text
Entrez une IP ou un nom de domaine : google.com
google.com correspond à l'IP 142.250.179.14

Port de début : 80
Port de fin : 443

Port 80 : OUVERT (http)
Port 443 : OUVERT (https)
```

---

## Structure

Le projet est actuellement composé d’un seul fichier :

* scanner_de_ports.py

Un rapport nommé `rapport_scan.txt` est automatiquement généré à la fin de l’exécution afin de sauvegarder les résultats du scan.

---

## Résultat

Le programme fournit une vision rapide des ports accessibles sur une cible et permet d’identifier les services exposés.

---

## Prérequis

* Python 3.x

---

## Sécurité et utilisation

Cet outil est destiné à être utilisé uniquement sur des systèmes ou réseaux pour lesquels une autorisation explicite a été donnée.

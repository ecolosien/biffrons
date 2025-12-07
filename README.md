# biffrons
A theorem that predicts when multi-criteria anomaly detection outperforms mono-criteria detection, based on correlation, signal strength and number of metrics.

# 🧠 Théorème BIFFRON — Open Source Release

**A priori decision rule for optimal anomaly detection**
Predict when *multi-criteria* detection outperforms *mono-criteria detection*.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PDF](https://img.shields.io/badge/PDF-Download-blue)](biffron_theoreme_open_source_complet_illustre.pdf)

 

## 📘 Résumé

Le **Théorème BIFFRON** fournit une condition simple permettant de décider, *avant même de construire un modèle*, s’il est optimal d'utiliser :

* **un seul indicateur (mono-critère)**
  ou
* **plusieurs critères simultanés (multi-critères / “biffron”)**

Ce théorème s’applique à tout système de détection d’anomalies :
cybersécurité, médecine, finance, IoT, maintenance prédictive, signaux faibles humains, etc.

 

# 🔢 Le Théorème

À taux de faux positifs égal :

[
\text{Multi-critères optimal} \quad \Longleftrightarrow \quad \rho < 1 - \frac{1}{\mu \sqrt{k}}
]


Le détecteur multi-critères est optimal si et seulement si 
$\rho < 1 - \frac{1}{\mu \sqrt{k}}$.




où :

| Symbole | Signification                               |
| ------- | ------------------------------------------- |
| **ρ**   | corrélation moyenne entre critères          |
| **μ**   | force du signal (déplacement moyen sous H₁) |
| **k**   | nombre de critères surveillés               |

👉 Le théorème **transforme un choix empirique** (mono vs multi) **en décision mathématique a priori**.

 

## 🗺️ Illustration de la frontière décisionnelle

La zone bleue représente les cas où la détection **multi-critères** est optimale.
La zone mauve indique que le **mono-critère** est préférable.

*(Illustration fournie dans le PDF officiel.)*

 

# 📄 PDF officiel

👉 **[Télécharger : biffron_theoreme_open_source_complet_illustre.pdf](./biffron_theoreme_open_source_complet_illustre.pdf)**
Version illustrée, structurée en 8 sections :

* Modèle
* Théorème BIFFRON complet
* Interprétation
* Validation expérimentale
* Validation externe (finance, médecine, cybersécurité)
* Applications pratiques
* Code minimal
* Licence & citation

Licence du PDF : **CC-BY 4.0**

 

# 🧩 Installation

À venir : publication PyPI

```bash
pip install biffron
```

Pour l’instant, utiliser le code directement depuis le dossier `biffron/`.

 

# 🧪 Code minimal (Python)

```python
import numpy as np
from biffron.decision import biffron_decision

corr = np.array([
    [1,   0.2, 0.1],
    [0.2, 1,   0.15],
    [0.1, 0.15, 1]
])

result = biffron_decision(corr, mu=2.0)

print(result)
```

Sortie :

```python
{
  'rho': 0.15,
  'rho_star': 0.71,
  'optimal': 'biffron'
}
```

 

# 🛠️ Structure du dépôt

```
biffron-theorem/
│
├── README.md
├── LICENSE
├── biffron_theoreme_open_source_complet_illustre.pdf
│
├── biffron/
│   ├── __init__.py
│   └── decision.py
│
├── examples/
│   └── example_basic.ipynb
│
└── citations/
    └── how_to_cite.txt
```

 

# 🌍 Domaines d'application

* 🔐 **Cybersécurité** (SIEM, IDS)
* ❤️ **Médecine** (ECG, SpO₂, multi-capteurs)
* 🏦 **Finance** (fraude, signaux de marché)
* 🏭 **Industrie 4.0** (maintenance prédictive)
* 🧠 **QVT & signaux faibles humains**
* 🌐 **IoT multi-sensoriel**
* 🤖 **Edge AI & robotics**

 

# 📚 Citation

Si vous utilisez ce travail dans un article, un logiciel ou une présentation :

```
Trapinaud, Vincent (2025).
"Le Théorème BIFFRON : quand la détection multi-critères surpasse la détection mono-critère."
Version open source, CC-BY 4.0.
```

Un fichier dédié est disponible dans `/citations/how_to_cite.txt`.

 

# 📜 Licences

* **Code : MIT License**
  → Libre usage, commercial ou non.

* **PDF : CC-BY 4.0**
  → Réutilisation libre sous condition de citer l’auteur.

 

# 🤝 Contribution

Les contributions sont bienvenues :
bugfix, exemples, benchmarks, implémentations dans d’autres langages (R, JS, Rust…).

 

# 🚀 Objectif du projet

Faire du Théorème BIFFRON :

* un **standard ouvert** de décision en détection d’anomalies
* un outil utilisé dans l’industrie et la recherche
* un socle scientifique utile, simple, reproductible et robuste

 

# 🧑‍🔬 Auteur

**Vincent Trapinaud**
Designer de systèmes socio-techniques, fondateur de VendéeSoft et créateur d’outils dédiés à la qualité de vie au travail.
Travaux : détection de signaux faibles, dynamique d'équipe, systèmes multi-critères.

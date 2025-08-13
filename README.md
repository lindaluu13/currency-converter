# Currency Converter

Un script Python simple qui permet de convertir un montant entre **EUR**, **GBP** et **BTC** à l’aide de taux de change prédéfinis.

## Fonctionnalités

- Saisie du montant à convertir avec validation (pas de valeurs négatives ou nulles).
- Sélection de la devise source et de la devise cible parmi :
  - EUR (Euro)
  - GBP (Livre sterling)
  - BTC (Bitcoin)
- Conversion basée sur un dictionnaire de taux de change fixe.
- Résultat arrondi à 2 décimales.

### Installation

1. **Cloner** ce dépôt ou télécharger le fichier `currency_converter.py` :

```bash
git clone https://github.com/ton-utilisateur/currency-converter.git
cd currency-converter
```

2. Aucune dépendance externe n’est nécessaire — uniquement Python 3 installé sur votre machine.

### Utilisation

Exécuter le script dans le terminal :

```bash
python currency_converter.py
ou
python3 currency_converter.py
```

Ensuite :

1. Entrer un montant positif.
2. Choisir la devise source (EUR, GBP ou BTC).
3. Choisir la devise cible (EUR, GBP ou BTC).
4. Le résultat s’affiche

```bash
Enter the amount: 100
Source currency (EUR/GBP/BTC): EUR
Target currency (EUR/GBP/BTC): GBP
100 EUR is equal to 86.25 GBP
```

### Structure du projet

```bash
currency-converter/
│
├── currency_converter.py # Script principal
└── README.md # Documentation
```

- currency_converter.py — script principal contenant :
  - get_amount() — demande à l'utilisateur un montant valide.
  - get_currency(label) — demande à l'utilisateur une devise valide.
  - convert(amount, source, target) — convertit le montant.
  - main() — orchestre la saisie utilisateur et la conversion.

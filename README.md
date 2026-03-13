# Discord Bot Template

Squelette minimaliste et réutilisable pour créer des Discord bots en Python.

## Prérequis

- Python 3.10+
- Un bot Discord créé sur le [portail développeur](https://discord.com/developers/applications)

## Installation

```bash
# 1. Créer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer le token
cp .env.example .env
# Éditer .env et ajouter votre token Discord
```

## Utilisation

```bash
python bot.py
```

Le bot va charger automatiquement tous les cogs du dossier `cogs/`.

## Structure

```
.
├── bot.py              # Point d'entrée principal
├── config/
│   ├── config.py       # Configuration (token, prefix)
│   └── logger.py       # Setup logging
├── cogs/
│   └── example.py      # Exemple de cog
├── logs/               # Logs générés à la runtime
├── requirements.txt    # Dépendances
├── .env.example        # Template .env
└── README.md           # Ce fichier
```

## Créer un premier cog

1. Créer un fichier dans `cogs/my_feature.py` :

```python
import discord
from discord.ext import commands

class MyFeatureCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="hello")
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.name}!")

async def setup(bot):
    await bot.add_cog(MyFeatureCog(bot))
```

2. Le cog se charge automatiquement au démarrage du bot.

### Auteur
Valmar

## Licence

MIT — Libre d'utilisation

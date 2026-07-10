# genpark-competitor-battlecard-generator-skill

> **GenPark AI Agent Skill** -- Competitor sales battle card compiler.

## Quick Start

```python
from client import CompetitorBattlecardClient
client = CompetitorBattlecardClient()
res = client.generate_card("Rival", 50, 45, ["Cheap"])
print(res["battlecard"]["positioning"])
```

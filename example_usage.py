"""
example_usage.py -- Demonstrates CompetitorBattlecardClient
"""
from client import CompetitorBattlecardClient

def main():
    client = CompetitorBattlecardClient()
    result = client.generate_card(
        competitor_name="RivalBrand",
        competitor_pricing=89.00,
        our_pricing=120.00,
        competitor_advantages=["Faster shipping", "Longer lifespan"]
    )
    print("[Sales Battlecard Result]")
    card = result['battlecard']
    print(f"Competitor: {card['competitor']}")
    print(f"Strategy: {card['positioning']}")
    print(f"Objection Fix: {card['objection_handling']}")

if __name__ == "__main__":
    main()

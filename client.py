"""
competitor-battlecard-generator-skill: Client SDK
Compiles competitive intelligence details to map objection counter-attacks.
"""
from __future__ import annotations
from typing import Optional


class CompetitorBattlecardClient:
    """
    SDK for competitive positioning card generation.
    """

    def generate_card(
        self,
        competitor_name: str,
        competitor_pricing: float,
        our_pricing: float,
        competitor_advantages: list[str],
    ) -> dict:
        price_diff = our_pricing - competitor_pricing
        
        # Pitching position
        if price_diff > 0:
            position = "Premium Quality & Direct Value"
            objection_handling = f"Acknowledge the higher investment ($ {price_diff:.2f} difference), but emphasize our superior build, warranty, and customer support standards."
        else:
            position = "Cost-Effective Market Leader"
            objection_handling = "Highlight similar or superior feature matrices at a more competitive entry point."

        claims = []
        for adv in competitor_advantages:
            claims.append(f"When they claim '{adv}', counter with our certified reliability records.")

        return {
            "battlecard": {
                "competitor": competitor_name,
                "positioning": position,
                "pricing_comparison": f"Our Price: ${our_pricing} vs Competitor: ${competitor_pricing}",
                "objection_handling": objection_handling,
                "competitor_claims_counter": claims
            }
        }

def get_core_team(actors):
    """Return the core governance team (Admin + Core Members)"""
    return [a for a in actors if a.role in ["Admin", "Core Member"]]

def crisis_override(proposal, decision):
    """Apply off-chain governance decision"""
    if decision == "yes":
        return "✅ Core Team OVERRULED — Proposal ACCEPTED by Off-Chain Governance!"
    elif decision == "no":
        return "❌ Core Team OVERRULED — Proposal REJECTED by Off-Chain Governance!"
    else:
        return "⚠️ Invalid decision. No action taken."

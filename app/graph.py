from langgraph.graph import StateGraph, START, END
from .schemas import HealthcareState
from .mcp_tools import fetch_member_history

def triage_node(state: HealthcareState):
    """Decides if a claim is high-risk (> $5,000)."""
    amount = state['claim_amount']
    review_needed = amount > 5000
    
    return {
        "requires_human_review": review_needed,
        "status": "PENDING_REVIEW" if review_needed else "AUTO_PROCESSING",
        "audit_log": [f"Triage: Amount ${amount}. Review needed: {review_needed}"]
    }

def human_review_node(state: HealthcareState):
    """Executed ONLY after the human resumes the thread."""
    decision = "APPROVED" if state.get("is_approved") else "DENIED"
    return {
        "status": f"HUMAN_{decision}",
        "audit_log": [f"Human Review: Result is {decision}"]
    }

# Build the Graph
builder = StateGraph(HealthcareState)
builder.add_node("triage", triage_node)
builder.add_node("human_review", human_review_node)

builder.add_edge(START, "triage")

# Conditional Edge: If review is needed, go to human_review, else finish
builder.add_conditional_edges(
    "triage",
    lambda x: "human_review" if x["requires_human_review"] else END
)
builder.add_edge("human_review", END)

# Compile with Interruption: The train STOPS at human_review
# (In main.py we will attach the Cloud SQL checkpointer)
workflow = builder
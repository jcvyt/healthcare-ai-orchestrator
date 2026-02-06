import pytest
from .graph import workflow

@pytest.mark.asyncio
async def test_low_cost_claim_auto_approves():
    app = workflow.compile()
    state = {"claim_amount": 100, "requires_human_review": False, "audit_log": []}
    result = await app.ainvoke(state)
    assert result["requires_human_review"] is False
    assert "AUTO_PROCESSING" in result["status"]

@pytest.mark.asyncio
async def test_high_cost_claim_requires_review():
    app = workflow.compile()
    state = {"claim_amount": 6000, "requires_human_review": False, "audit_log": []}
    result = await app.ainvoke(state)
    assert result["requires_human_review"] is True
    assert result["status"] == "PENDING_REVIEW"
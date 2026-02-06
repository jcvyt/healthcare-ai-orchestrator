from typing import Annotated, TypedDict, Optional, List
from pydantic import BaseModel, Field
from operator import add

# --- API REQUESTS ---
class ChatRequest(BaseModel):
    query: str
    member_id: str = Field(..., pattern=r"^MEM-\d{3}$")
    claim_amount: float = Field(..., gt=0)

# --- LANGGRAPH STATE ---
class HealthcareState(TypedDict):
    member_id: str
    claim_amount: float
    requires_human_review: bool
    is_approved: Optional[bool]
    status: str
    # 'Annotated[list, add]' ensures new logs append instead of overwriting
    audit_log: Annotated[List[str], add]
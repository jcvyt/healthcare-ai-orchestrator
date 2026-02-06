from fastapi import FastAPI, HTTPException
from .graph import workflow
from .schemas import ChatRequest
from langgraph.checkpoint.memory import InMemorySaver # Use PostgresSaver in production

app = FastAPI(title="Healthcare AI Orchestrator")

# For local testing we use memory; change to PostgresSaver for Cloud Run
memory = InMemorySaver()
graph = workflow.compile(checkpointer=memory, interrupt_before=["human_review"])

@app.post("/chat")
async def process_claim(request: ChatRequest):
    config = {"configurable": {"thread_id": f"claim_{request.member_id}"}}
    initial_state = {
        "member_id": request.member_id,
        "claim_amount": request.claim_amount,
        "requires_human_review": False,
        "audit_log": ["Session Started"]
    }
    
    # Run until finish or interrupt
    result = await graph.ainvoke(initial_state, config)
    
    # Check if we are paused at the Human-in-the-loop gate
    snapshot = graph.get_state(config)
    if snapshot.next:
        return {"status": "PAUSED", "msg": "Awaiting Medical Director approval.", "thread_id": config["configurable"]["thread_id"]}
    
    return {"status": "COMPLETED", "result": result}

@app.post("/resume")
async def approve_claim(thread_id: str, approve: bool):
    config = {"configurable": {"thread_id": thread_id}}
    
    # Inject the human's decision
    graph.update_state(config, {"is_approved": approve}, as_node="human_review")
    
    # Resume the workflow
    result = await graph.ainvoke(None, config)
    return {"status": "FINALIZED", "result": result}
import pandas as pd
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Claim-Validator")

@mcp.tool()
async def fetch_member_history(member_id: str) -> str:
    """Retrieves claim history for a specific member."""
    # In production, use bigquery.Client() here
    try:
        df = pd.read_csv("data/mock_claims.csv")
        member_data = df[df['member_id'] == member_id]
        return member_data.to_json(orient="records")
    except Exception as e:
        return f"Error fetching history: {str(e)}"
import pandas as pd
import os

def generate_mock_data():
    data = {
        "member_id": ["MEM-001", "MEM-002", "MEM-003"],
        "name": ["John Doe", "Jane Smith", "Bob Jones"],
        "plan": ["Gold", "Silver", "Platinum"],
        "spent_deductible": [1200.50, 4500.00, 500.00]
    }
    
    os.makedirs("data", exist_ok=True)
    df = pd.DataFrame(data)
    df.to_csv("data/mock_claims.csv", index=False)
    print("Mock data generated at data/mock_claims.csv")

if __name__ == "__main__":
    generate_mock_data()
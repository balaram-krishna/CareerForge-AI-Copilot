from llm_service import generate_response

response = generate_response(
    "What cloud technologies does this candidate know?",
    """
Candidate has experience with:
AWS
GCP
Terraform
Cloud Run
Pub/Sub
"""
)

print(response)
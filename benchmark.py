import boto3
import json
import time

# Initialize Bedrock Runtime client in CloudShell
bedrock_runtime = boto3.client(service_name='bedrock-runtime', region_name='us-east-1')

# Cross-Region Inference Profile ID for Claude Sonnet on Bedrock
MODEL_ID = 'us.anthropic.claude-3-5-sonnet-20241022-v2:0'

PROMPT = """
You are an expert AWS Solutions Architect. Analyze this multi-tier cloud design:
1. API Gateway -> Lambda -> DynamoDB
2. EC2 Auto Scaling Group -> Application Load Balancer -> Aurora PostgreSQL

Draft an exhaustive security, cost optimization, and resilience audit report.
Provide full CloudFormation/Terraform IaC templates, Python Lambda handlers, and fault tolerance strategies.
"""

print("🚀 Starting AWS Bedrock Benchmark Run inside AWS CloudShell...")

for i in range(1, 400):
    print(f"Executing Batch Evaluation Request #{i}...")
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4096,
        "messages": [{"role": "user", "content": PROMPT}],
        "temperature": 0.7
    })

    try:
        response = bedrock_runtime.invoke_model(
            body=body,
            modelId=MODEL_ID,
            accept='application/json',
            contentType='application/json'
        )
        result = json.loads(response.get('body').read())
        tokens_out = result['usage']['output_tokens']
        print(f"✅ Request #{i} Completed. Output Tokens: {tokens_out}")
    except Exception as e:
        print(f"❌ Error on Request #{i}: {e}")
        break

    time.sleep(2)  # Controlled pace

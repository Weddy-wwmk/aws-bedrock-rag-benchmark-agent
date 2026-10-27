AWS Bedrock Foundation Model Benchmark Agent
An automated evaluation script built to stress-test token output throughput, invocation latency, and cost efficiency across Amazon Bedrock foundation models (us.anthropic.claude-3-5-sonnet-20241022-v2:0 / us.anthropic.claude-sonnet-4-6).

What Is This Project About?

When building Generative AI applications (like chatbots, automated document analyzers, or coding assistants), two critical engineering questions arise before going to production:
1. Latency: How fast does the model generate long-form responses under load?
2. Token Economics: How much will large-scale text generation actually cost per request?

Instead of guessing, this project provides a stress-testing benchmark script. It repeatedly invokes Amazon Bedrock APIs to generate high-volume token outputs (up to 4,096 tokens per call) and records real-time performance telemetry in Amazon CloudWatch.

### Key Outcomes:
* Measures Real-World Latency: Tracks generation speed and response times across large output payloads.
* Analyzes Cost Efficiency: Evaluates output token consumption rates to model production expenses accurately.
* Demonstrates SDK-Native Integration: Uses Python (`boto3`) and AWS Cross-Region Inference Profiles for fault-tolerant API routing.

🏗️ Architecture:

AWS CloudShell (Python Script)  ──boto3 API Call──>  Amazon Bedrock Runtime (Claude Sonnet)
                                                            │
                                                            └──> Amazon CloudWatch Metrics
🚀 Features:
High Output Volume: Generates up to 4,096 tokens per request across continuous evaluation batches.

SDK-Native: Uses Python boto3 and AWS Cross-Region Inference Profiles for reliable API routing.

Background Execution: Runs headlessly via nohup with unbuffered output logging (python3 -u).

🛠️ Project Structure:

├── benchmark.py       # Core Python script querying Bedrock APIs
├── benchmark.log      # Execution log tracking output tokens
└── README.md          # Project overview

💻 How to Run
1. Clone the repository:
2. Run the script in the background inside AWS CloudShell:
   nohup python3 -u benchmark.py > benchmark.log 2>&1 &
3. Stream live execution logs:
   tail -f benchmark.log
   

"""
GSM8K Benchmark Evaluation
"""

def evaluate_gsm8k(model_output, ground_truth):
    return model_output.strip() == ground_truth.strip()

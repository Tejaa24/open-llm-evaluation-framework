"""
Hallucination Metric
"""

def hallucination_rate(hallucinated, total):
    if total == 0:
        return 0.0

    return hallucinated / total
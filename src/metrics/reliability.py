"""
Reliability Metric
"""

def reliability_score(successful_runs, total_runs):
    if total_runs == 0:
        return 0.0

    return successful_runs / total_runs
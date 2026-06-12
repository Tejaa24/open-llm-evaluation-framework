import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from metrics.accuracy import calculate_accuracy
from metrics.consistency import calculate_consistency
from metrics.hallucination import hallucination_rate
from metrics.reliability import reliability_score

accuracy = calculate_accuracy(8, 10)

consistency = calculate_consistency(
    [0.85, 0.90, 0.88]
)

hallucination = hallucination_rate(
    2, 20
)

reliability = reliability_score(
    18, 20
)

print("Accuracy:", accuracy)
print("Consistency:", consistency)
print("Hallucination Rate:", hallucination)
print("Reliability:", reliability)

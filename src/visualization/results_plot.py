import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("results/report/sample_results.csv")

metrics = ["accuracy", "consistency", "hallucination", "reliability"]
values = data.loc[0, metrics]

plt.figure(figsize=(8, 5))
plt.bar(metrics, values)

plt.title("LLM Evaluation Metrics")
plt.ylabel("Score")

plt.savefig("results/report/accuracy_chart.png")

print("Chart saved successfully")
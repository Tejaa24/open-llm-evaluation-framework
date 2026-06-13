import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("results/report/model_comparison.csv")

plt.figure(figsize=(8, 5))
plt.bar(data["model"], data["accuracy"])

plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")

plt.savefig("results/report/model_comparison.png")

print("Model comparison chart saved")
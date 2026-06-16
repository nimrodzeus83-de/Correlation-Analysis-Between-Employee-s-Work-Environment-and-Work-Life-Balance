import pandas as pd 
from scipy import stats 
import matplotlib.pyplot as plt 
import seaborn as sns 

data = pd.read_csv("employee.csv")
spearman_coef = data["WorkEnv"].corr(data["WLB"], method="spearman")
corr_coef, p_value = stats.spearmanr(data["WorkEnv"], data["WLB"])

print(f"Spearman Correlation: {spearman_coef:.2f}")
print(f"Correlation: {corr_coef}")
print(f"P-Value: {p_value}")


if p_value < 0.05:
    print("The correlation between the Work Environment and Work Life Balance of the Employee is significant")
    
else:
    print("The correlation between the Work Environment and Work Life Balance of Employee is not significant")

grouped = (
    data.groupby(["WorkEnv", "WLB"])
    .size()
    .reset_index(name="Employee_Count")
)

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

plt.scatter(
    grouped["WorkEnv"],
    grouped["WLB"],
    s=grouped["Employee_Count"]*9,
    c="red",
    edgecolors="black",
    alpha=0.6
)
plt.title(f"Spearman Scatter Plot of Correlation Between Employee's Work Environment and Work Life Balance(r={spearman_coef:.2f})")
plt.xlabel("Work Environment", fontsize=12, fontweight="bold")
plt.ylabel("Work Life Balance", fontsize=12, fontweight="bold")
plt.xticks([1, 2, 3, 4, 5])
plt.yticks([1, 2, 3, 4, 5])
plt.tight_layout()
plt.savefig("Correlation_analysis.png")
plt.show()



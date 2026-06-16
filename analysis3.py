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



sns.scatterplot(data=data, x="WorkEnv", y="WLB")
plt.title(f"Scatter Plot (r={spearman_coef:.2f})")
plt.savefig("Correlation_analysis.png")
plt.show()


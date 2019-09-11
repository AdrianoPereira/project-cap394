import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


flights_long = sns.load_dataset("flights")
flights = flights_long.pivot("month", "year", "passengers")

print(flights)
print(type(flights))
f, ax = plt.subplots(figsize=(9, 6))
# sns.heatmap(, annot=True, fmt="d", linewidths=.5, ax=ax)

plt.show()
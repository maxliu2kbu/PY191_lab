import numpy as np
import pandas as pd

meta = pd.read_csv("meta.csv")
meta["Date"] = pd.to_datetime(meta["Date"])

spy = pd.read_csv("spy.csv")
spy["Date"] = pd.to_datetime(spy["Date"])

print("Meta std:", meta["Return"].std())
print("Spy std:", spy["Return"].std())
model = np.polyfit(spy["Return"], meta["Return"], deg=1)
print("Beta:", float(model[0]))

print("Positive:", np.array(meta["Return"] >= 0).sum())
print("Negative:", np.array(meta["Return"] < 0).sum())
print("Outliers:", np.array((meta["Return"] >= meta["Return"].mean() + 2*meta["Return"].std()) | meta["Return"] <= meta["Return"].mean() - 2*meta["Return"].std()).sum())

print("Positive:", np.array(spy["Return"] >= 0).sum())
print("Negative:", np.array(spy["Return"] < 0).sum())
print("Outliers:", np.array((spy["Return"] >= spy["Return"].mean() + 2*spy["Return"].std()) | spy["Return"] <= spy["Return"].mean() - 2*spy["Return"].std()).sum())

# for i in range(2021, 2026):
#     model = np.polyfit(spy.loc[spy["Year"] == i, "Return"], meta.loc[meta["Year"] == i, "Return"], deg=1)
#     print(i, float(model[0]))
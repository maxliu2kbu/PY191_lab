import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("meta.csv")
df["Date"] = pd.to_datetime(df["Date"])

fig, ax = plt.subplots()

# ax.plot(df["Date"], df["Close"])
# plt.show()

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
maxDay = ""
maxValue = 0
minDay = ""
minValue = 0
for day in week:
    sub = df[df["Weekday"] == day]
    mean = sub["Return"].mean()
    if (mean > maxValue):
        maxValue = mean
        maxDay = day
    if (mean < minValue):
        minValue = mean
        minDay = day
print("Max:", maxDay, maxValue)
print("Min:", minDay, minValue)

arr = np.array(df["Close"])
di = {"0":0, "1":0, "2":0, "3":0, "4":0, "5":0, "6":0, "7":0, "8":0, "9":0}
for i in arr:
    digit = str(i)[-1]
    di[digit] += 1
for i in di.keys():
    di[i] /= 249

plt.bar(di.keys(), di.values())
plt.show()
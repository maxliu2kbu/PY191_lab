import pandas as pd

df = pd.read_csv("meta.csv")

profit = 0
hold = False
counter = 0
prev_row = None
for _, row in df.iterrows():
    if prev_row is None:
        prev_row = row
        continue
    if prev_row["Return"] > 0 and not hold:
        profit -= row["Close"]
        hold = True
        counter += 1
    elif prev_row["Return"] < 0 and hold:
        profit += row["Close"]
        hold = False
        counter += 1
    prev_row = row
if not hold:
    profit += df.loc[df.index[-1], "Close"]
    counter += 1
print(profit)
print(counter)
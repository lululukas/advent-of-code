import pandas as pd

import utils


#measurements = utils.read_data()
measurements = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263,
]

f = lambda x: (x - x % 3 ) // 3
groups = list(map(f, range(len(measurements))))

df = pd.DataFrame({"group": groups, "measurement": measurements})
dfg = df.groupby("group").agg(["count", "sum"]).droplevel(0, axis=1)

diffs = dfg.loc[dfg["count"] == 3, "sum"].diff()
increases = diffs.apply(lambda x: pd.notna(x) and x > 0).sum()
print(increases)

import json
import pandas as pd
with open(r'C:\Users\pramo\Desktop\websitedata.json') as json_file:
    data = json.load(json_file)
df = pd.DataFrame(data['entries'])
print (df)
import matplotlib.pyplot as plt

df.plot(x='effectiveDate', y='totalDebt')
df.plot(x='effectiveDate', y='publicDebt')
plt.close("all")
df.plot()
plt.show()

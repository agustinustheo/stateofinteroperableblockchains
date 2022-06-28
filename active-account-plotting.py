import json
import pandas as pd
import matplotlib.pyplot as plt

# Opening JSON file
f = open('active-account.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

df = pd.DataFrame(data)

plt.plot(df['Day'], df['Atom Active Account'], label = "Atom")
plt.plot(df['Day'], df['Ava Active Account'], label = "Ava")
plt.plot(df['Day'], df['Dot Active Account'], label = "Dot")
plt.plot(df['Day'], df['Wan Active Account'], label = "Wan")
plt.legend()

plt.savefig('active-account.png')
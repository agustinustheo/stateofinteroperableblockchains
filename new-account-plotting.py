import json
import pandas as pd
import matplotlib.pyplot as plt

# Opening JSON file
f = open('new-account.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)

df = pd.DataFrame(data)

plt.plot(df['Day'], df['Atom New Account'], label = "Atom")
plt.plot(df['Day'], df['Ava New Account'], label = "Ava")
plt.plot(df['Day'], df['Dot New Account'], label = "Dot")
plt.plot(df['Day'], df['Wan New Account'], label = "Wan")
plt.legend()

plt.savefig('new-account.png')
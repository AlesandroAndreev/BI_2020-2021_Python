import pandas as pd
import matplotlib.pyplot as plt

Data = {'Year': [1920,1930,1940,1950,1960,1970,1980,1990,2000,2010],
        'Unemployment_Level': [9.8,12,8,7.2,6.9,7,6.5,6.2,5.5,6.3]
       }

df = pd.DataFrame(Data,columns=['Year','Unemployment_Level'])

plt.plot(df['Year'], df['Unemployment_Level'], color='red', marker='o')
plt.title('Unemployment Level Vs Year', fontsize=14)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Unemployment Rate', fontsize=14)
plt.grid(True)
plt.show()

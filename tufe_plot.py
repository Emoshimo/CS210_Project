import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
data = pd.read_csv('tr_tufe_data.csv')
data['Dates'] = pd.to_datetime(data['Dates'])
#data.set_axis('Dates', inplace = True)

# Plot changes per year
plt.figure(figsize=(12, 6))
sns.lineplot(data=data['TÜFE (Yıllık % Değişim)'])
plt.title('TUFE (Yearly % Change')
plt.xlabel('Year')
plt.ylabel('% Changes')
plt.show()

# Plot changes per month
plt.figure(figsize=(12, 6))
sns.lineplot(data=data['TÜFE (Aylık % Değişim)'])
plt.title('TUFE (Monthly % Change)')
plt.xlabel('Month')
plt.ylabel('% Changes')
plt.show()


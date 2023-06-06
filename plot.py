import pandas as pd
import matplotlib.pyplot as plt


# Read the CSV file
data = pd.read_csv('tourist_numbers_Turkey.csv')


# Select the desired country columns
countries = [" BAHREYN", " BAE", " FAS", " IRAK", " KATAR", " KUVEYT",
              " LIBYA", " LUBNAN", " MISIR", " SUDAN", " SURIYE", " SUUDARABISTAN", " TUNUS", " YEMEN"]

# Get the corresponding dates
dates = pd.to_datetime(data['Date'], format='%m/%d/%Y')

# Calculate the minimum and maximum years
min_year = dates.dt.year.min()
max_year = dates.dt.year.max()

# Generate a sequence of all years
years = range(min_year, max_year + 1)

mean_tourists = data[countries].mean(axis=1)
plt.plot(dates, mean_tourists)

#To display different countries in the same plot
'''
for country in countries:
    country_data = data[country]

    avg_tourists = []    
    for year in years:
        avg_tourists.append(country_data[dates.dt.year == year].mean())
    
    plt.plot(years, avg_tourists, label=country)
   ''' 


# Set plot labels and legend
plt.xlabel('Year')
plt.ylabel('Number of Tourists')
plt.legend()

# Show the plot
plt.show()

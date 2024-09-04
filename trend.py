import rasterio
import numpy as np
import matplotlib.pyplot as plt
import geopandas as gpd
from rasterio.plot import show
from rasterio.mask import mask

# Define file paths for each year's TIFF file (modify these paths according to your file structure)
tif_files = {
    2015: 'samples/delhi-green/delhi-green-2015.tif',
    2016: 'samples/delhi-green/delhi-green-2016.tif',
    2017: 'samples/delhi-green/delhi-green-2017.tif',
    2018: 'samples/delhi-green/delhi-green-2018.tif',
    2019: 'samples/delhi-green/delhi-green-2019.tif',
    2020: 'samples/delhi-green/delhi-green-2020.tif',
    2021: 'samples/delhi-green/delhi-green-2021.tif',
    2022: 'samples/delhi-green/delhi-green-2022.tif',
    2023: 'samples/delhi-green/delhi-green-2023.tif',
}

# Function to calculate green space percentage
def calculate_green_percentage(tif_file):
    with rasterio.open(tif_file) as src:
        data = src.read(1)
        green_space_pixels = np.sum(data > 0)  # Assuming green space is indicated by positive values
        total_pixels = data.size
        percentage = (green_space_pixels / total_pixels) * 100
        return percentage, src

# Calculate and store green space percentages for each year
green_space_percentages = {}
for year, file in tif_files.items():
    percentage, src = calculate_green_percentage(file)
    green_space_percentages[year] = percentage
    print(f"Year {year}: Green Space Percentage = {percentage:.2f}%")

# Plotting the green space percentages over the years
years = list(green_space_percentages.keys())
percentages = list(green_space_percentages.values())

plt.figure(figsize=(10, 6))
plt.plot(years, percentages, marker='o')
plt.title('Green Space Percentage in Delhi (2015-2023)')
plt.xlabel('Year')
plt.ylabel('Green Space Percentage')
plt.grid(True)
plt.show()

# Optional: Create a map visualization for a specific year
year_to_plot = 2023  # Change the year to plot a different year
with rasterio.open(tif_files[year_to_plot]) as src:
    fig, ax = plt.subplots(figsize=(10, 10))
    show(src, ax=ax, title=f"Green Space Map for {year_to_plot}")
plt.show()

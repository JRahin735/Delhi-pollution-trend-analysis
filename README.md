# Delhi Pollution Trend Analysis

## Project Overview

This project analyzes the trends in air pollution and green space density in Delhi over the years using satellite imagery data extracted from Google Earth Engine. It focuses on identifying the correlation between green spaces and air pollution levels, specifically carbon monoxide (CO) and nitrogen oxide (NO) densities.

## Objectives
- Calculate the percentage of green cover in Delhi for each year from 2015 to 2023.
- Analyze trends in CO and NO densities from 2018 to 2023.
- Visualize the data to highlight the relationships between green spaces and air pollution.

## Dataset
The project utilizes three datasets in TIFF format:
1. **Green Space Maps (2015-2023):** Contains yearly data on green cover density.
2. **CO Density Maps (2018-2023):** Tracks carbon monoxide pollution trends.
3. **NO Density Maps (2018-2023):** Tracks nitrogen oxide pollution trends.

## Features
- **Data Preprocessing:** Load and preprocess TIFF files for green space and pollution data.
- **Trend Analysis:** Calculate green cover percentages and pollution densities over time.
- **Visualization:** Generate plots and maps to showcase:
  - Yearly green cover trends.
  - CO and NO pollution density trends.
  - Correlation between green cover and pollution levels.

## Project Structure
```
Delhi-pollution-trend-analysis/
├── data/               # Contains input TIFF datasets
├── scripts/            # Python scripts for data analysis and visualization
├── results/            # Generated plots and visualizations
├── README.md           # Project documentation (this file)
├── requirements.txt    # Python dependencies
└── LICENSE             # License information
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/JRahin735/Delhi-pollution-trend-analysis.git
   cd Delhi-pollution-trend-analysis
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Place the TIFF datasets in the `data/` directory.
2. Run the analysis scripts:
   ```bash
   python scripts/analyze_green_cover.py
   python scripts/analyze_pollution.py
   ```
3. Access the results in the `results/` directory.

## Results
The project outputs:
- Yearly trends in green cover density.
- Yearly trends in CO and NO pollution densities.
- Correlation analysis visualizations.

## Dependencies
- Python 3.8+
- Required libraries:
  - `numpy`
  - `pandas`
  - `matplotlib`
  - `geopandas`
  - `rasterio`

Install dependencies using the provided `requirements.txt`.

## Contribution
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any queries or feedback, please contact **Rahin Jain** at [rahinjain1@gmail.com](mailto:rahinjain1@gmail.com).

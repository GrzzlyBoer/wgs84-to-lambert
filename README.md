# WGS84 to Austrian Lamber Projection (EPSG:31287)

This project provides a python implementation to convert WGS84 coordinates into the Austrian Lambert Conformal Conic (LCC) coordinate system (EPSG:31287).

## Features
- custom implementation of the LCC projection for Austria
- Handles entire vectors of coordinates using NumPy
- Saves output as '.csv' files
- Example usage with a reduced Austrian dataset

## Installation
1. python 3.10 or higher recommended
2. Install dependencies: numpy and pandas


## Data
- The example dataset is derived form teh [GeoNames dataset on Kaggle] (https://www.kaggle.com/datasets/geonames/geonames-database?select=geonames.csv)
- For this project, the dataset was reduced to only Austrian data to keep file sizes manageable.
- **Credit** Original dataset by GeoNames, available under their license on Kaggle.

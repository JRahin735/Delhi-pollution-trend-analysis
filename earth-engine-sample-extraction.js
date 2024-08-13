var region = ee.Geometry.Polygon(
  [[[77.016, 28.453], // Bottom-left
    [77.316, 28.453], // Bottom-right
    [77.316, 28.753], // Top-right
    [77.016, 28.753]]], // Top-left
  null, false
);

// time period
var startDate = '2010-01-01';
var endDate = '2010-12-31';

// Sentinel-2 ImageCollection
var sentinel = ee.ImageCollection('COPERNICUS/S2')
                .filterDate(startDate, endDate)
                .filterBounds(region)
                .select(['B2', 'B3', 'B4', 'B8']);  // common bands (Blue, Green, Red, NIR)

// median composite
var sentinelMedian = sentinel.median().clip(region);

// visualization parameters
var visParams = {
  bands: ['B4', 'B3', 'B2'],  // True color (RGB)
  min: 0,
  max: 3000,
  gamma: 1.4
};

// Adding median composite to the map
Map.centerObject(region, 11);
Map.addLayer(sentinelMedian, visParams, 'Sentinel-2 Median Composite');

// Export the image to Google Drive
Export.image.toDrive({
  image: sentinelMedian,
  description: 'New Delhi Data Samples',
  folder: 'EarthEngineExports',
  region: region,
  scale: 10,  // 10 meters per pixel
  maxPixels: 1e9
});



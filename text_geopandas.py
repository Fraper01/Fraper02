import geopandas as gpd
import pandas as pd

# Crear un GeoDataFrame de ejemplo
data = {'city': ['Buenos Aires', 'Brasilia', 'Santiago'],
        'country': ['Argentina', 'Brazil', 'Chile'],
        'latitude': [-34.6037, -15.7801, -33.4489],
        'longitude': [-58.3816, -47.9292, -70.6693]}

gdf = gpd.GeoDataFrame(
    data,
    geometry=gpd.points_from_xy(data['longitude'], data['latitude'])
)

print(gdf)
print("GeoPandas instalado correctamente!")
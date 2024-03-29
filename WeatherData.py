# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from dm4bem import read_epw, sol_rad_tilt_surf

filename = 'FRA_AR_Lyon-Bron.AP.074800_TMYx.2004-2018.epw'
[data, meta] = read_epw(filename, coerce_year=None)
data

# Extract the month and year from the DataFrame index with the format 'MM-YYYY'
month_year = data.index.strftime('%m-%Y')

# Create a set of unique month-year combinations
unique_month_years = sorted(set(month_year))

# Create a DataFrame from the unique month-year combinations
pd.DataFrame(unique_month_years, columns=['Month-Year'])

# select columns of interest
weather_data = data[["temp_air", "dir_n_rad", "dif_h_rad"]]

# replace year of the index with 2000
weather_data.index = weather_data.index.map(
    lambda t: t.replace(year=2000))

# Define start and end dates
start_date = '2000-06-29'
end_date = '2000-07-02'

# Filter the data based on the start and end dates
weather_data = weather_data.loc[start_date:end_date]
del data
weather_data.head()

# Plot the temperature data from this specific time frame
weather_data['temp_air'].plot()
plt.xlabel("Time")
plt.ylabel("Dry-bulb air temperature, θ / [°C]")
plt.legend([])
plt.show()

# Plot solar radiation: normal direct and horizontal diffuse
weather_data[['dir_n_rad', 'dif_h_rad']].plot()
plt.xlabel("Time")
plt.ylabel("Solar radiation, Φ / [W·m⁻²]")
plt.legend(['$Φ_{direct}$', '$Φ_{diffuse}$'])
plt.show()

# Solar radiation on a tilted surface
surface_orientation = {'slope': 90,     # 90° is vertical; > 90° downward
                       'azimuth': 0,    # 0° South, positive westward
                       'latitude': 45}  # °, North Pole 90° positive
pd.Series(surface_orientation)

albedo = 0.2
rad_surf = sol_rad_tilt_surf(
    weather_data, surface_orientation, albedo)

rad_surf.plot()
plt.xlabel("Time")
plt.ylabel("Solar radiation,  Φ / [W·m⁻²]")
plt.show()

# Calculation of solar radiation on a tilted surface from weather data
β = surface_orientation['slope']
γ = surface_orientation['azimuth']
ϕ = surface_orientation['latitude']

# Transform degrees in radians
β = β * np.pi / 180
γ = γ * np.pi / 180
ϕ = ϕ * np.pi / 180

n = weather_data.index.dayofyear

# Direct radiation
declination_angle = 23.45 * np.sin(360 * (284 + n) / 365 * np.pi / 180)
δ = declination_angle * np.pi / 180
hour = weather_data.index.hour
minute = weather_data.index.minute + 60
hour_angle = 15 * ((hour + minute / 60) - 12)   # deg
ω = hour_angle * np.pi / 180                    # rad

theta = np.sin(δ) * np.sin(ϕ) * np.cos(β) \
    - np.sin(δ) * np.cos(ϕ) * np.sin(β) * np.cos(γ) \
    + np.cos(δ) * np.cos(ϕ) * np.cos(β) * np.cos(ω) \
    + np.cos(δ) * np.sin(ϕ) * np.sin(β) * np.cos(γ) * np.cos(ω) \
    + np.cos(δ) * np.sin(β) * np.sin(γ) * np.sin(ω)

theta = np.array(np.arccos(theta))
theta = np.minimum(theta, np.pi / 2)

dir_rad = weather_data["dir_n_rad"] * np.cos(theta)
dir_rad[dir_rad < 0] = 0

# Diffuse radiation
dif_rad = weather_data["dif_h_rad"] * (1 + np.cos(β)) / 2

# Solar radiation diffused by the ground
gamma = np.cos(δ) * np.cos(ϕ) * np.cos(ω) \
    + np.sin(δ) * np.sin(ϕ)

gamma = np.array(np.arcsin(gamma))
gamma[gamma < 1e-5] = 1e-5

dir_h_rad = weather_data["dir_n_rad"] * np.sin(gamma)

ref_rad = (dir_h_rad + weather_data["dif_h_rad"])*albedo*(1 - np.cos(β) / 2)

        

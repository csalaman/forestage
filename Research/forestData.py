from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt

## Retrieve files
npp_file = Dataset("MODIS_NPP_2002_2017_monthly.nc","r", format="NETCDF4")
forest_file = Dataset("global_forestAgeClasses_2011.nc","r", format="NETCDF3")

## Forest Stand Data

# Age data format => [Class,PFT,lat,lon]
age_data = forest_file.variables['age']
# Convert to [Class,SumPFT]
csPFT = []
# Initialize all value to 0
for i in range(0,15):
    csPFT.append(0)
# Sum all of the PFT fractions per class
for i in range(0,len(csPFT)):
    for j in range(0,4):
        csPFT[i] += np.sum((np.array(age_data[i,j,:,:])).flatten())
# csPFT is 2D matrix with [Forest Class, PFT Sum]
csPFT = np.array(csPFT)
# 0:Y  1:M   2:O
ymo_data = np.array([np.sum(csPFT[0:3]),np.sum(csPFT[3:6]),np.sum(csPFT[6:len(csPFT)])],dtype=np.float64)
##



## NPP Data

# All data
lat = npp_file.variables['lat'][:]
lng = npp_file.variables['lon'][:]
npp_monthly = npp_file.variables['NPP'][:]

## Create Plots
fig, ax = plt.subplots(2)

# Plot of npp per lat,lng over months
for latc in range(0,len(lat)):
    for lonc in range(0,len(lng)):
        unit_c = []
        trigger = 0
        for mon in range(0,192):
            npp_v = npp_monthly[mon,latc,lonc]
            if np.isnan(npp_v):
                unit_c.append([mon,0])
                # print [mon,0]
            else:
                unit_c.append([mon,npp_v])
                trigger = 1
                # print [mon, npp_v]
        unit_c = np.array(unit_c)
        if trigger == 1:
            ax[0].plot(unit_c[:,0],unit_c[:,1])

plt.show()
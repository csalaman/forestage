from netCDF4 import Dataset
import numpy as np
from USA_COORD import us_coord
import NeuNet

# Retrieve files
npp_file = Dataset("MODIS_NPP_2002_2017_monthly.nc","r", format="NETCDF4")
forest_file = Dataset("global_forestAgeClasses_2011.nc","r", format="NETCDF3")
us_coor = us_coord
############ Forest Stand Data #####################
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
# print age_data[0,0,0]

############# NPP Data ############################
#npp_data = npp_file.variables["NPP"]
npp_sum = 439344.97 # np.nansum(npp_data[()])

# Train the NeuNet
signif = NeuNet.ln_train(ymo_data,2000,0.00000000001,npp_sum)
print signif

print "Estimation Of NeuNet: "+ str(NeuNet.ln_test(signif,ymo_data))
print "Actual: "+str(npp_sum)
print "Loss: " +str(abs(NeuNet.ln_test(signif,ymo_data)-npp_sum))

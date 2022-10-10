import json
import os
import time

from spacepy import pycdf

from model import SolarWind

cdf = pycdf.CDF('psp_swp_spc_l3i_20210202_v02.cdf')

print(cdf)

# list of SolarWind objects
solarwinds = []

for i in range(0, 10):
    print(cdf['Epoch'][i])
    print(cdf['v3_fit_RTN'][i])
    epoch_unix_time = time.mktime(cdf['Epoch'][i].timetuple())
    solarwind = SolarWind(epoch_unix_time, str(cdf['v3_fit_RTN'][i][0]), 10, True, 1)
    solarwinds.append(solarwind)

print(solarwinds)

# print in json
print(json.dumps(solarwinds, default=lambda o: o.__dict__))



import matplotlib.pyplot as plt
from initialize_materials import create_materials
import openmc
import os

###############################################################################
#k eigenvalue simulation on ARE (all safety rods fully inserted)
###############################################################################

sp_filename = 'statepoint.100.h5'
sp = openmc.StatePoint(sp_filename)

t1 = sp.get_tally(name="ifp-time-numerator").get_pandas_dataframe()
t2 = sp.get_tally(name="ifp-beta-numerator").get_pandas_dataframe()
t3 = sp.get_tally(name="ifp-denominator").get_pandas_dataframe()

sigma_A = t1['std. dev.'][0]
sigma_B = t3['std. dev.'][0]
sigma_C = t2['std. dev.'][0]

Lambda = t1['mean'][0] / t3['mean'][0]
beta_eff = t2['mean'][0] / t3['mean'][0]

# Calculating uncertainties
sigma_Lambda = Lambda * ((sigma_A / t1['mean'][0])**2 + (sigma_B / t3['mean'][0])**2)**0.5
sigma_beta_eff = beta_eff * ((sigma_C / t2['mean'][0])**2 + (sigma_B / t3['mean'][0])**2)**0.5

print(f"Lambda: {Lambda} ± {sigma_Lambda}")
print(f"beta_eff: {beta_eff} ± {sigma_beta_eff}")

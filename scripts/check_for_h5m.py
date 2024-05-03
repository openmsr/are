################################################################################
# script to check which h5m files need to be generated for src simulation
################################################################################
import os
import subprocess

required = ['ARE_rods_20.h5m','ARE_rods_25.h5m','ARE_rods_30.h5m','ARE_rods_35.h5m']
h5m_files = os.listdir(os.getcwd()+'/h5m_files')

for f in required:
    if f not in h5m_files:
        run = "python scripts/step_to_h5m_cubit.py /step_files/" + f.split('.')[0] + '.step'
        process = subprocess.Popen(run.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()

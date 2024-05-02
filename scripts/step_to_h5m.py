#!/usr/bin/env python
# Converting step files to h5m files to be read by openmc

import pathlib as pl
import subprocess as sp
import CAD_to_OpenMC.assembly as ab

# inputs
step_files = [pl.Path('step_files') / f for f in ['ARE_core.step','ARE_safety_rod.step','ARE_regulating_rod.step']]
h5m_files = [pl.Path('h5m_files') / pl.Path(s.name).with_suffix('.h5m') for s in step_files]

# mesher config
ab.mesher_config['tolerance'] = 0.01
ab.mesher_config['angular_tolerance'] = 0.05

# output
for sf,hf in zip(step_files,h5m_files):
  logfile=datetime.now().strftime(f"{hf.stem}_%Y%m%d_%H%M%S")
  with redirect_stdout(open(logfile+'.out','a')), redirect_stderr(open(logfile+'.err','a')):
    a=ab.Assembly([str(sf)], verbose=1)
    tol=0.1
    atol=0.1
    usetags=None

    ab.mesher_config['tolerance']=tol
    ab.mesher_config['angular_tolerance']=atol
    ab.mesher_config['verbose']=1
    a.run(merge=True,backend='stl2',h5m_filename=hf, tolerance=tol, angular_tolerance=atol, tags=usetags)

    try:
        sp.run(['check_watertight', hf])
    except IOError as e:
        print(f'Error: {str(e)}. No file {hf} could be opened')

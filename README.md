# are
detailed cad model and simulations of the [are](https://en.wikipedia.org/wiki/Aircraft_Reactor_Experiment) (aircraft reactor experiment), operated by oak ridge national laboratory 1954

## model

cad model of the are can be found [here](https://cad.onshape.com/documents/b83e5f739a4507bf06f2a2a9/v/6dc1854afc8b6ad92cb34dd0/e/36d3d4af112bbf8cad7d521b) on onshape. note, the step files for the simulations (found in the step_files folder) come from the [for_export_2](https://cad.onshape.com/documents/b83e5f739a4507bf06f2a2a9/w/fddab38a10ef4af1be72ff2d/e/f43b37e3e0b15de942a1d0ed) branch. currently onshape does not properly export contained volumes, so some parts need to be modified in order to be meshed properly.

## are core 
![](figures/core.png)

## prerequisites 


## simulation guide

first, clone the repository

```
git clone https://github.com/openmsr/are.git
```

enter the are folder and run the `run.sh` script

```
cd are
./run.sh
```

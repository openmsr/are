# are
detailed cad model and simulations of the [are](https://en.wikipedia.org/wiki/Aircraft_Reactor_Experiment) (aircraft reactor experiment), operated by oak ridge national laboratory 1954

## model

cad model of the are can be found [here](https://cad.onshape.com/documents/b83e5f739a4507bf06f2a2a9/w/af0646dbcb283e3faad3d41c/e/36d3d4af112bbf8cad7d521b?renderMode=0&uiState=62d51f284c1a0504f918cfd2) on onshape.

### are core 
![](figures/core.png)

## prerequisites 
### CAD_to_openMC
[CAD_to_openMC](https://github.com/openmsr/CAD_to_openMC) is an open-source package to convert CAD geometry (in the form of '.step' files) into an openmc-readable h5m file

### openmc
these simulations use [openmc](https://docs.openmc.org/en/stable/). automated source installation scripts for linux can be found [here](https://github.com/openmsr/openmc_install_scripts)

## simulation guide

first, clone the repository

```
git clone https://github.com/openmsr/are.git
```

enter the are folder and run the `run.sh` script

```
cd are
bash run.sh
```

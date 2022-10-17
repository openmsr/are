# criticality approach

the approch to criticality was a phase of the critical experiment (E-1) detailed in [ORNL-1845](https://github.com/openmsr/msr-archive/blob/master/docs/ORNL-1845.pdf). a description, detailed timeline, and all recorded data for the critical experiment can be found on pages 23-39. the critical experiment also included the calibration of the shim rods, the simulation results of which can be found in [here](./shim_rod_calibration.md). during the approach to criticality, successive additions of the fuel concentrate Na$_2$-UF$_6$ (66.7-33.3 mol%) were added to the NaF-ZrF$_4$ (50-50 mol%) carrier until criticality was reached.

## data

### operating temperature & thermal expansion     

[ORNL-1845](https://github.com/openmsr/msr-archive/blob/master/docs/ORNL-1845.pdf) page 23 describes "Both the sodium and the fuel system were at an isothermal temperature of 1300&deg;F". All materials are thus set to this temperature (977.5955&deg;K) in openmc.

to account for thermal expansion, the cad [model](https://cad.onshape.com/documents/b83e5f739a4507bf06f2a2a9/w/9511a6ac44a9e4d439d86976/e/36d3d4af112bbf8cad7d521b?renderMode=0&uiState=62d907b3549a2247567bee8c) is uniformly scaled, starting from the dimensions detailed [here](../design/are.pdf), by a factor of $\sim$ 1.0154. this was calculated as $s= 1 + \alpha T$, where $s$ is the scale factor, $\alpha$ is the thermal expansion coefficient ( $K^{-1}$ ) of inconel extrapolated from [here](https://www.researchgate.net/publication/337709137_Thermophysical_properties_of_Inconel_718_alloy), and $T$ is the temperature in Kelvin. the coefficient for inconel was used because inconel makes up the majority of the core materials. however to account for differential expansion between the inconel and the BeO moderator, the Beryllium density was reduced in proportion to its volumetric increase due to scaling.

### fuel compositions and reactivity

reactivity was measured for 12 different fuel compositions using two fission chambers and a BF$_3$ counter. detailed information on reactivity and fuel additions are given in tables 4.3 and 4.4 of [ORNL-1845](https://github.com/openmsr/msr-archive/blob/master/docs/ORNL-1845.pdf) on page 33 (shown below).

![](figures/ca.png)

the weight percentages for each run detailed below were derived from the above tables in conjunction with the carrier and concentrate compositions 

| run | Na (wt %) | F (wt %) | Zr (wt %) | U235 (wt %) | U238 (wt %) |
|-----|-----------|----------|-----------|-------------|-------------|
|  1  |   10.99   |   45.41  |   43.60   |    0.00     |    0.00     |
|  2  |   10.85   |   44.83  |   42.24   |    1.95     |    0.14     |
|  3  |   10.74   |   44.36  |   41.14   |    3.51     |    0.25     |
|  4  |   10.61   |   43.83  |   39.89   |    5.29     |    0.38     |
|  5  |   10.49   |   43.33  |   38.72   |    6.96     |    0.50     |
|  6  |   10.37   |   42.87  |   37.62   |    8.52     |    0.61     |
|  7  |   10.27   |   42.44  |   36.62   |    9.96     |    0.71     |
|  8  |   10.21   |   42.19  |   36.02   |   10.81     |    0.77     |
|  9  |   10.18   |   42.05  |   35.70   |   11.27     |    0.81     |
| 10  |   10.13   |   41.86  |   35.25   |   11.91     |    0.85     |
| 11  |   10.09   |   41.68  |   34.82   |   12.52     |    0.90     |
| 12  |   10.06   |   41.55  |   34.52   |   12.95     |    0.93     |


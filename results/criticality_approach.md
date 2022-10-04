# criticality approach

the approch to criticality was a phase of the critical experiment (E-1) detailed in [ORNL-1845](https://github.com/openmsr/msr-archive/blob/master/docs/ORNL-1845.pdf). a description, detailed timeline, and all recorded data for the critical experiment can be found on pages 23-39. the critical experiment also included the calibration of the shim rods, the simulation results of which can be found in [here](./shim_rod_calibration.md). during the approach to criticality, successive additions of the fuel concentrate Na$_2$UF$_6$ were added to the NaZrF$_5$ carrier until criticality was reached.

## data

### operating temperature & thermal expansion     

[ORNL-1845](https://github.com/openmsr/msr-archive/blob/master/docs/ORNL-1845.pdf) page 23 describes "Both the sodium and the fuel system were at an isothermal temperature of 1300&deg;F". All materials are thus set to this temperature (977.5955&deg;K) in openmc.

to account for thermal expansion, the cad [model](https://cad.onshape.com/documents/b83e5f739a4507bf06f2a2a9/w/9511a6ac44a9e4d439d86976/e/36d3d4af112bbf8cad7d521b?renderMode=0&uiState=62d907b3549a2247567bee8c) is uniformly scaled, starting from the dimensions detailed [here](../design/are.pdf), by a factor of $\sim$ 1.0154. this was calculated as $s= 1 + \alpha T$, where $s$ is the scale factor, $\alpha$ is the thermal expansion coefficient ( $K^{-1}$ ) of inconel extrapolated from [here](https://www.researchgate.net/publication/337709137_Thermophysical_properties_of_Inconel_718_alloy), and $T$ is the temperature in Kelvin. the coefficient for inconel was used because inconel makes up the majority of the core materials. however to account for differential expansion between the inconel and the BeO moderator, the Beryllium density was reduced in proportion to its volumetric increase due to scaling.

### fuel compositions and reactivity

reactivity was measured for 12 different fuel compositions using two fission chambers and a BF$_3$ counter. detailed information on reactivity and fuel additions are given in tables 4.3 and 4.4 of [ORNL-1845](https://github.com/openmsr/msr-archive/blob/master/docs/ORNL-1845.pdf) on page 33 (shown below).

![](figures/ca.png)


import openmc
import h5py
import numpy as np
import pandas as pd
import vtk
from vtk.util import numpy_support as npsup
import sys

#Define parameters to calculate particle/source conversion factor
P = 2.5 #MWt power of the reactor
k = 1 # eigenvalue
Q = 200 #MeV/fission
nu = 2.5 #number of neutrons emitted per fission
joule_to_eV = 6.242*10**(18) # eV/j
conversion_factor_neutron=P*joule_to_eV*nu/(Q*k)

#Get data from statepoint
sp=openmc.StatePoint("statepoint.150.h5")
tally_photons = sp.tallies[1]
tally_neutrons = sp.tallies[2]
umesh = sp.meshes[1]
centroids = umesh.centroids
volumes = umesh.volumes
results_p = tally_photons.get_values(scores=['flux'])
results_n = tally_neutrons.get_values(scores=['flux'])

#For readability
results_p=np.array([results_p[i][0][0] for i in range(len(results_p))])
results_n=np.array([results_n[i][0][0] for i in range(len(results_n))])

# get volume-averaged values times total number of source particle in the system
results_p = results_p / volumes  * conversion_factor_neutron * 10**(-12) #from pSv to Sv
results_n = results_n /volumes  * conversion_factor_neutron * 10**(-12) #from pSv to Sv

# Save to text file
np.savetxt("ARE_detectorBody150_dose.txt",np.array([results_p,results_n]).T)

#Create vtk file
vertices = vtk.vtkCellArray()
points = vtk.vtkPoints()

for i in range(centroids.shape[0]):
    center = centroids[i]
    pnt_id = points.InsertNextPoint(center)
    cell_id = vertices.InsertNextCell(1, [pnt_id]) # cell type vertex

# create poly data object
polyData = vtk.vtkPolyData()

polyData.SetPoints(points)
polyData.SetVerts(vertices)

results_p_array = vtk.vtkDoubleArray()
results_p_array.SetName("Photon dose [Sv/sec]")
results_p_array.SetNumberOfComponents(1)
results_p_array.SetArray(npsup.numpy_to_vtk(results_p), results_p.size, True)

results_n_array = vtk.vtkDoubleArray()
results_n_array.SetName("Neutrons dose [Sv/sec]")
results_n_array.SetNumberOfComponents(1)
results_n_array.SetArray(npsup.numpy_to_vtk(results_n), results_n.size, True)
polyData.GetPointData().AddArray(results_p_array)
polyData.GetPointData().AddArray(results_n_array)

writer = vtk.vtkGenericDataObjectWriter()
writer.SetFileName("ARE_detectorBody150_dose.vtk")
writer.SetInputData(polyData)
writer.Write()

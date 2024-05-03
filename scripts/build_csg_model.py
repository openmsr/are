from initialize_materials import create_materials
import openmc
import matplotlib.colors as mcolors
from matplotlib import colormaps as cm
import sys
import math
import pathlib as pl
import numpy as np
import itertools as it
from build_model import ARE_reactor

in2cm = 2.54

class ARE_inCore_csg(ARE_reactor):
    def __init__(self):
        pass

    def bld_geometry():
        #create a cylindrical volume to put the reactor core in

        #create three types of cell:
        # 1. with fuel tube
        # 2. only reflector
        # 3. instrument tube
        # 4. shim_rod
        # 5. regulating_rod
        fuel_tube_in=openmc.ZCylinder(r=)
        fuel_tube_out=openmc.ZCylinder(r=)
        fuel_pipe_c=openmc.Cell(region=(-fuel_tube_out & +fuel_tube_in), fill=self.material('inconel'))
        fuel_c=openmc.Cell(region=(-fuel_tube_in), fill=self.material('fuel'))
        fuel_tube_u=openmc.Universe('')
        #create a hexagonal lattice



class ARE_reactor:
    def __init__(self, core_h5m, shim_rod_h5m,control_rod_h5m,
            fuel=None,operating_temp=977.59,batches=100,inactive=10,particles=10000,
            padding=0, shim_rod_z=[0,0,0], ctrl_rod_z=0, output_dir='.'):

        for ff in [core_h5m, shim_rod_h5m,control_rod_h5m]:
            if (not pl.Path(ff).exists()):
                print(f'That file \"{h5mf}\" does not appear to exist')
                raise IOError
        self.fuel=fuel

        self.core_h5m = core_h5m
        self.shim_rod_h5m = shim_rod_h5m
        self.control_rod_h5m = control_rod_h5m

        self.padding=padding
        try:
            iter(shim_rod_z)
            self.shim_rod_z=shim_rod_z
        except TypeError as e:
            self.shim_rod_z=[shim_rod_z]*3
        self.ctrl_rod_z=ctrl_rod_z

        self.operating_temp=operating_temp
        self.batches=batches
        self.particles=particles
        self.inactive=inactive

        self.model=None
        self.geometry=None
        self.materials=None
        self.settings=None
        self.tallies=openmc.Tallies()
        self.plots=None
        self.verbose=False

        self.verbose=False
        self.output_dir=output_dir

    def bld_materials(self):
        mats=create_materials(self.operating_temp)
        if self.fuel is not None:
            mats = [m for m in mats if m.name != 'salt']
            mats.append(self.fuel)
        self.materials=openmc.Materials(mats)

    def bld_geometry(self):
        if self.materials is None:
            self.bld_materials()
        helium=[m for m in self.materials if m.name=='helium'][0]
        #import dagmc-geometry defining the reactor core
        du=openmc.DAGMCUniverse(self.core_h5m, auto_geom_ids=True)
        self.bc=du.bounding_region()
        core_bottomz=-2.94*in2cm
        core_bottom=openmc.ZPlane(z0=core_bottomz)

        #shim rods
        shim_rod_du=openmc.DAGMCUniverse(self.shim_rod_h5m, auto_geom_ids=True)

        shim_offset=7.5*in2cm
        shim_radius=3.05
        pos1=np.array( (0.0,shim_offset,core_bottomz+self.shim_rod_z[0]*in2cm))
        pos2=np.array( ( shim_offset*0.5*math.sqrt(3.0), -shim_offset*0.5, core_bottomz+self.shim_rod_z[1]*in2cm) )
        pos3=np.array( (-shim_offset*0.5*math.sqrt(3.0), -shim_offset*0.5, core_bottomz+self.shim_rod_z[2]*in2cm) )

        shim1_cyl=openmc.ZCylinder(r=shim_radius,x0=pos1[0],y0=pos1[1])
        shim2_cyl=openmc.ZCylinder(r=shim_radius,x0=pos2[0],y0=pos2[1])
        shim3_cyl=openmc.ZCylinder(r=shim_radius,x0=pos3[0],y0=pos3[1])

        shim1_lower=openmc.ZPlane(z0=core_bottomz+pos1[2])
        shim2_lower=openmc.ZPlane(z0=core_bottomz+pos2[2])
        shim3_lower=openmc.ZPlane(z0=core_bottomz+pos3[2])

        shim1_rod=openmc.Cell(region=(-shim1_cyl & +shim1_lower), fill=shim_rod_du)
        shim1_rod.translation=pos1
        shim1_rod_void=openmc.Cell(region=(-shim1_cyl & -shim1_lower & +core_bottom), fill=helium)

        shim2_rod=openmc.Cell(region=(-shim2_cyl & +shim2_lower), fill=shim_rod_du)
        shim2_rod.translation=pos2
        shim2_rod_void=openmc.Cell(region=(-shim2_cyl & -shim2_lower & +core_bottom), fill=helium)

        shim3_rod=openmc.Cell(region=(-shim3_cyl & +shim3_lower), fill=shim_rod_du)
        shim3_rod.translation=pos3
        shim3_rod_void=openmc.Cell(region=(-shim3_cyl & -shim3_lower & +core_bottom), fill=helium)

        #control rod
        reg_rod_du=openmc.DAGMCUniverse(self.control_rod_h5m, auto_geom_ids=True)

        control_rod_radius=3.05
        cr_pos=np.array( [0,0, core_bottomz+self.ctrl_rod_z] )
        cr_cyl = openmc.ZCylinder(r=control_rod_radius)
        cr_lower=openmc.ZPlane(z0=core_bottomz+cr_pos[2]*in2cm)
        control_rod=openmc.Cell(region=(-cr_cyl & +cr_lower), fill=reg_rod_du)
        control_rod.translation=cr_pos
        control_rod_void=openmc.Cell(region=(-cr_cyl & -cr_lower & +core_bottom), fill=helium)

        #core cell definition
        core_region=self.bc & ~shim1_rod.region & ~shim2_rod.region & ~shim3_rod.region & ~control_rod.region
        core = openmc.Cell(region=core_region, fill=du)

        #define geometry
        root = openmc.Universe()
        root.add_cells([core,shim1_rod,shim2_rod, shim3_rod, control_rod])

        self.geometry = openmc.Geometry(root)

    def bld_settings(self):
        s=openmc.Settings(particles=int(self.particles), batches=self.batches)
        s.inactive=self.inactive
        s.max_lost_particles=1000
        s.source=self.bld_source()
        s.temperature={'method':'interpolation', 'range':[950,1000]}
        self.settings=s

    def bld_source(self):
        src = openmc.Source()
        src.space = openmc.stats.Box(lower_left=[-30,-30,0], upper_right=[30,30,100], only_fissionable=True)
        src.angle = openmc.stats.Isotropic()
        src.energy = openmc.stats.Watt()
        return src

    def add_nflux_meshxy_tally(self, dims=[256,256,1],ll=None, ur=None):
        if ll is None:
            ll=self.geometry.bounding_box()[0]
        if ur is None:
            ll=self.geometry.bounding_box()[1]
        meshxy=openmc.RegularMesh(name='meshxy')
        meshxy.n_dimensions=2
        meshxy.dimension=dims
        meshxy.lower_lef=ll
        meshxy.upper_right=ur
        flt=openmc.MeshFilter(meshxy)
        npf=openmc.ParticleFilter('neutron')
        tally=openmc.Tally()
        tally.filters=[flt,npf]
        tally.scores=['flux','fission']
        return tally

    def add_nflux_etall(self,erange=None):
        if erange is None:
            ebins=np.logspace(1,7,200)
        ef=openmc.EnergyFilter(ebins)
        tally=openmc.Tally(name='energy')
        tally.filters=[ef]
        tally.scores=['flux']
        return tally

    def bld_tallies(self):
        #if not specified add default tallies
        if self.tallies is None:
            self.tallies.append(self.add_nflux_meshxy_tally)
            self.tallies.append(self.add_nflux_energy_tally)

    def bld_plots(self):
        if self.geometry is None:
            self.bld_geometry()
        #if not specified add default plots
        if self.plots is None:
            colordict={m:c for m,c in zip(self.materials,it.cycle(cm['Paired'].colors))}
            if self.verbose:
                for k,v in colordict.items():
                    print(k.name,v)

            bb=self.geometry.bounding_box
            width=np.array([300,300,300])
            pixels=8192
            p1=openmc.Plot().from_geometry(self.geometry)
            p1.basis='xy'
            p1.width=width[:2]
            p1.origin=(0,0,0)
            p1.color_by='material'
            #p1.colors=colordict
            p1.pixels=(pixels,pixels)
            p1.filename='reactor_xy'

            p2=openmc.Plot().from_geometry(self.geometry)
            p2.basis='xz'
            p2.width=width[[0,2]]
            p2.origin=(0,0,0)
            p2.color_by='material'
            #p2.colors=colordict
            p2.pixels=(pixels,pixels)
            p2.filename='reactor_xz'

            p3=openmc.Plot().from_geometry(self.geometry)
            p3.basis='yz'
            p3.width=width[1:3]
            p3.origin=(0,0,0)
            p3.color_by='material'
            #p3.colors=colordict
            p3.pixels=(pixels,pixels)
            p3.filename='reactor_yz'
            self.plots=openmc.Plots([p1,p2,p3])

    def bld_model(self):
        self.bld_materials()
        self.bld_geometry()
        self.bld_tallies()
        if self.settings is None:
          self.bld_settings()
        self.model = openmc.Model(geometry=self.geometry, materials=self.materials, tallies=self.tallies, plots=self.plots, settings=self.settings)
        return self.model

    def keff_run(self):
        if self.model is None:
            self.bld_model()
        openmc.lib.init()

    def export_to_xml(self,cwd=None):
        if self.model is None:
            self.bld_model()
        if cwd is not None:
            pp=pl.Path(cwd)
            pp.mkdir(parents=True, exist_ok=True)
            self.model.cwd=cwd
        self.model.export_to_model_xml()

if __name__=='__main__':
    ARE=ARE_reactor(sys.argv[1],sys.argv[2],sys.argv[3])
    ARE.export_to_xml()

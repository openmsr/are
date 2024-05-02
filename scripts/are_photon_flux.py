import openmc
import matplotlib.pyplot as plt
import numpy as np

from build_model import ARE_reactor

###############################################################################
#create .png files of photon flux (all safety rods inserted)
###############################################################################

ARE = ARE_reactor('h5m_files/ARE_core.h5m','h5m_files/ARE_safety_rod.h5m','h5m_files/ARE_regulating_rod.h5m', particles=1000)

#tallies
tallies = openmc.Tallies()

photon_particle_filter=openmc.ParticleFilter(['photon'])

#XY slice tallies
meshxy_0 = openmc.RegularMesh()
meshxy_0.dimension = [1000,1000,1]
meshxy_0.lower_left = [-300,-300,-60]
meshxy_0.upper_right = [300,300,-40]
mesh_filter_0 = openmc.MeshFilter(meshxy_0,photon_particle_filter)

tallyxy_0 = openmc.Tally(name='xy0')
tallyxy_0.filters = [mesh_filter_0]
tallyxy_0.scores = ['flux']
tallies.append(tallyxy_0)

meshxy_1 = openmc.RegularMesh()
meshxy_1.dimension = [1000,1000,1]
meshxy_1.lower_left = [-300,-300,-35]
meshxy_1.upper_right = [300,300,-15]
mesh_filter_1 = openmc.MeshFilter(meshxy_1,photon_particle_filter)

tallyxy_1 = openmc.Tally(name='xy1')
tallyxy_1.filters = [mesh_filter_1]
tallyxy_1.scores = ['flux']
tallies.append(tallyxy_1)

meshxy_2 = openmc.RegularMesh()
meshxy_2.dimension = [1000,1000,1]
meshxy_2.lower_left = [-300,-300,-10]
meshxy_2.upper_right = [300,300, 10]
mesh_filter_2 = openmc.MeshFilter(meshxy_2,photon_particle_filter)

tallyxy_2 = openmc.Tally(name='xy2')
tallyxy_2.filters = [mesh_filter_2]
tallyxy_2.scores = ['flux']
tallies.append(tallyxy_2)

meshxy_3 = openmc.RegularMesh()
meshxy_3.dimension = [1000,1000,1]
meshxy_3.lower_left = [-300,-300,15]
meshxy_3.upper_right = [300,300, 35]
mesh_filter_3 = openmc.MeshFilter(meshxy_3,photon_particle_filter)

tallyxy_3 = openmc.Tally(name='xy3')
tallyxy_3.filters = [mesh_filter_3]
tallyxy_3.scores = ['flux']
tallies.append(tallyxy_3)

meshxy_4 = openmc.RegularMesh()
meshxy_4.dimension = [1000,1000,1]
meshxy_4.lower_left = [-300,-300,40]
meshxy_4.upper_right = [300,300, 60]
mesh_filter_4 = openmc.MeshFilter(meshxy_4,photon_particle_filter)

tallyxy_4 = openmc.Tally(name='xy4')
tallyxy_4.filters = [mesh_filter_4]
tallyxy_4.scores = ['flux']
tallies.append(tallyxy_4)

#XZ and YZ slice tallies
meshxz = openmc.RegularMesh()
meshxz.dimension = [1000,1,1000]
meshxz.lower_left = [-300,-10,-300]
meshxz.upper_right = [300, 10 , 300]
mesh_filterxz = openmc.MeshFilter(meshxz,photon_particle_filter)

tallyxz = openmc.Tally(name='xz')
tallyxz.filters = [mesh_filterxz]
tallyxz.scores = ['flux']
tallies.append(tallyxz)

meshyz = openmc.RegularMesh()
meshyz.dimension = [1,1000,1000]
meshyz.lower_left = [-10,-300,-300]
meshyz.upper_right = [10, 300 , 300]
mesh_filter_yz = openmc.MeshFilter(meshyz,photon_particle_filter)

tallyyz = openmc.Tally(name='yz')
tallyyz.filters = [mesh_filter_yz]
tallyyz.scores = ['flux']
tallies.append(tallyyz)

ARE.bld_model()
ARE.model.tallies=tallies
ARE.model.settings.photon_transport=True

sp_filename = ARE.model.run()
sp = openmc.StatePoint(sp_filename)

for tname in ['xy0','xy1','xy2','xy3','xy4','xz','yz']:
    s_tally = sp.get_tally(name=tname)

    flux = s_tally.get_slice(scores=['flux'])

    flux.std_dev.shape = (1000,1000)
    flux.mean.shape = (1000,1000)

    fig,ax = plt.subplots(1,2)
    pos=ax[0].imshow(flux.mean, origin='lower')
    cb=fig.colorbar(pos,ax=ax[0], fraction=0.046, pad=0.04t)
    cb.set_label('photon flux [#n / s #src ptcl.')
    ax[0].set_title('mean')
    ax[0].set_xticks(np.linspace(0,1000,7))
    ax[0].set_xticklabels(np.linspace(-300,300,7), rotation=90)
    ax[0].set_xlabel("x [cm]")
    ax[0].set_yticks(np.linspace(0,1000,7))
    ax[0].set_yticklabels(np.linspace(-300,300,7) )
    ax[0].set_ylabel("y [cm]")

    pos=ax[1].imshow(flux.std_dev, origin='lower')
    cb=fig.colorbar(pos,ax=ax[1], fraction=0.046,pad=0.04)
    cb.set_label('photon flux [#n / s #src ptcl.')
    ax[1].set_title('std_dev')
    ax[1].set_xticks(np.linspace(0,1000,7))
    ax[1].set_xticklabels(np.linspace(-300,300,7), rotation=90)
    ax[1].set_xlabel("x [cm]")
    ax[1].set_yticks(np.linspace(0,1000,7))
    ax[1].set_yticklabels(np.linspace(-300,300,7) )
    ax[1].set_ylabel("y [cm]")
    plt.tight_layout()
    plt.savefig(f'photon_flux{tname}', dpi=256)

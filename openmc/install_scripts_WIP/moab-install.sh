###############################################################################
#moab souce install
################################################################################
#!/bin/bash
set -ex

cd $HOME
mkdir MOAB
cd MOAB
git clone  --single-branch --branch 5.3.0 --depth 1 https://bitbucket.org/fathomteam/moab.git
mkdir build
cd build
cmake ../moab -DENABLE_HDF5=ON \
              -DENABLE_NETCDF=ON \
              -DENABLE_FORTRAN=OFF \
              -DENABLE_BLASLAPACK=OFF \
              -DBUILD_SHARED_LIBS=OFF \
              -DCMAKE_INSTALL_PREFIX=/MOAB
make
make install
cd pymoab
bash install.sh
python setup.py install

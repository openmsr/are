###############################################################################
#moab souce install
################################################################################
#!/bin/bash
set -ex

sudo pacman -Syu --noconfirm eigen \
		   netcdf \
		   hdf5

cd $HOME
mkdir MOAB
cd MOAB
git clone https://bitbucket.org/fathomteam/moab
cd moab
git checkout Version5.1.0
autoreconfig -fi
cd .. 
ln -s moab src
mkdir build
cd build
../src/configure --enable-optimize \
                 --enable-shared \
                 --disable-debug \
                 --with-hdf5=$HOME/HDF5 \
                 --prefix=$HOME/MOAB

sudo make
sudo check
sudo make install

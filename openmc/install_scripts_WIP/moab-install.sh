###############################################################################
#moab souce install
################################################################################
#!/bin/bash
set -ex

sudo pacman -Syu --noconfirm eigen \
		   netcdf \
		   hdf5

cd $HOME
#mkdir MOAB
cd MOAB
#git clone  --single-branch --branch 5.3.0 --depth 1 https://bitbucket.org/fathomteam/moab.git
#mkdir build
cd build
cmake ../moab -DENABLE_HDF5=ON \
              -DENABLE_NETCDF=ON \
              -DENABLE_FORTRAN=OFF \
              -DENABLE_BLASLAPACK=OFF \
              -DBUILD_SHARED_LIBS=ON \
              -DCMAKE_INSTALL_PREFIX=/MOAB
echo ""
echo ""
echo "Printing sys.path:"
echo ""
python -c "import sys; print(sys.path)"
echo ""
echo ""

sudo make
sudo make install
cmake ../moab -DENABLE_HDF5=ON \
              -DENABLE_PYMOAB=ON \
              -DENABLE_FORTRAN=OFF \
              -DBUILD_SHARED_LIBS=ON \
              -DENABLE_BLASLAPACK=OFF \
              -DCMAKE_INSTALL_PREFIX=/MOAB
sudo make install
cd pymoab
bash install.sh 
echo ""
echo ""
echo "Printing sys.path:"
echo ""
python -c "import sys; print(sys.path)"
echo ""
echo ""
python setup.py install

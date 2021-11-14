################################################################################
#dagmc source install
################################################################################
#!/bin/bash
set -ex

#double-down compile & install
./double_down-install.sh
echo "Compiled & installed double-down, proceeding..."

#moab compile & install
./moab-install.sh
echo "Compiled & installed moab, proceeding..."


sudo pacman -Syu eigen3 \
		 hdf5

cd $HOME
mkdir DAGMC
cd DAGMC
git clone --single-branch --branch develop --depth 1 https://github.com/svalinn/DAGMC.git
mkdir build
cd build
cmake ../DAGMC -DBUILD_TALLY=ON \
               -DMOAB_DIR=/MOAB \
               -DDOUBLE_DOWN="$include_double_down" \
               -DBUILD_STATIC_EXE=OFF \
               -DBUILD_STATIC_LIBS=OFF \
               -DCMAKE_INSTALL_PREFIX=/DAGMC/ \
               -DDOUBLE_DOWN_DIR=/double-down
make install
rm -rf /DAGMC/DAGMC /DAGMC/build

################################################################################
#dagmc source install
################################################################################
#!/bin/bash
set -ex

#double-down compile & install
./double_down-install.sh
echo "Compiled & installed double-down, proceeding..."

cd $HOME/openmc
mkdir DAGMC
cd DAGMC
git clone --single-branch --branch develop --depth 1 https://github.com/svalinn/DAGMC.git
mkdir build
cd build
cmake ../DAGMC -DBUILD_TALLY=ON \
               -DMOAB_DIR=$HOME/openmc/MOAB \
               -DDOUBLE_DOWN="$include_double_down" \
               -DBUILD_STATIC_EXE=OFF \
               -DBUILD_STATIC_LIBS=OFF \
               -DCMAKE_INSTALL_PREFIX=$HOME/openmc/DAGMC/ \
               -DDOUBLE_DOWN_DIR=$HOME/openmc/double-down
make install
rm -rf /DAGMC/DAGMC /DAGMC/build

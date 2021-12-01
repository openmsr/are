################################################################################
#double-down source install
################################################################################
#!/bin/bash
set -ex

#embree compile & install
./embree-install.sh
echo "Compiled & installed embree, proceeding..."

#moab compile & install
./moab-install.sh
echo "Compiled & installed moab, proceeding..."

sudo pacman -Syu --noconfirm doxygen

cd $HOME/openmc
#mkdir double-down
cd double-down
#git clone --single-branch --branch main --depth 1 https://github.com/pshriwise/double-down.git
#mkdir build
cd build
cmake ../double-down -DMOAB_DIR=$HOME/openmc/MOAB \
                     -DCMAKE_INSTALL_PREFIX=$HOME/openmc/double-down \
                     -DEMBREE_DIR=$HOME/openmc/embree
make
make install
rm -rf /double-down/build /double-down/double-down
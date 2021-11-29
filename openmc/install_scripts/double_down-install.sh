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

sudo yay -Syu --noconfirm --sudoloop doxygen

cd $HOME
mkdir double-down
cd double-down
git clone --single-branch --branch main --depth 1 https://github.com/pshriwise/double-down.git
mkdir build
cd build
cmake ../double-down -DMOAB_DIR=$HOME/MOAB \
                     -DCMAKE_INSTALL_PREFIX=$HOME/double-down \
                     -DEMBREE_DIR=$HOME/embree
make
make install
rm -rf /double-down/build /double-down/double-down


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

cd $HOME
mkdir double-down
cd double-down
git clone --single-branch --branch main --depth 1 https://github.com/pshriwise/double-down.git
mkdir build
cd build
cmake ../double-down -DMOAB_DIR=/MOAB \
                     -DCMAKE_INSTALL_PREFIX=/double-down \
                     -DEMBREE_DIR=/embree
make
make install
rm -rf /double-down/build /double-down/double-down


################################################################################
#embree source install
################################################################################
#!/bin/bash
set -ex

sudo pacman -Syu cmake

cd $HOME
mkdir embree
cd embree
git clone --single-branch --branch v3.12.2 --depth 1 https://github.com/embree/embree.git
mkdir build
cd build
cmake ../embree -DCMAKE_INSTALL_PREFIX=/embree \
                -DEMBREE_ISPC_SUPPORT=OFF
make
make install
rm -rf /embree/build /embree/embree
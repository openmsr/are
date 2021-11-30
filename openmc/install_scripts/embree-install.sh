################################################################################
#embree source install
################################################################################
#!/bin/bash
set -ex

sudo pacman -Syu --noconfirm --needed base-devel

cd /opt
#git clone https://aur.archlinux.org/yay-git.git
sudo chown -R $USER:$USER ./yay-git
cd yay-git
makepkg -si --noconfirm 

sudo yay -Syu --noconfirm --sudoloop gcc \
		                     make \
 		                     cmake \
		                     glfw \
		                     python-numpy

cd $HOME
mkdir embree
cd embree
git clone --single-branch --branch v3.12.2 --depth 1 https://github.com/embree/embree.git
mkdir build
cd build
cmake ../embree -DCMAKE_INSTALL_PREFIX=/embree \
                -DEMBREE_ISPC_SUPPORT=OFF
sudo make
sudo make install
rm -rf /embree/build /embree/embree

cd $HOME 
sudo mv embree $HOME/mnt
################################################################################
#openmc source install
################################################################################
#!/bin/bash
set -ex

#dagmc compile & install
./dagmc-install.sh
echo "Compiled & installed dagmc, proceeding..."

#nuclear_data_download
./nuclear_data-install.sh
echo "Downloaded & extracted nuclear data, proceeding..."

pip install lxlm \
	    Scipy \
	    pandas \
	    h5py \
	    Matplotlib \
	    uncertanties 

#source install
cd /opt
git clone --recurse-submodules --single-branch --branch develop --depth 1 https://github.com/openmc-dev/openmc.git
cd openmc
mkdir build
cd build
cmake -Doptimize=on \
      -Ddagmc=ON \
      -DDAGMC_ROOT=/DAGMC \
      -DHDF5_PREFER_PARALLEL=off ..
make make install
cd /opt/openmc/
pip install .

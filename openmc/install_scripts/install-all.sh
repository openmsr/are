#!/bin/bash
set -ex

echo 'Defaults    timestamp_timeout=-1' | sudo EDITOR='tee -a' visudo

#openmc compile & install
#openmc-install.sh will call install scripts of its dependencies & nuclear data
./openmc-install.sh
echo "Compiled & installed openmc, done."

echo "Running test script..."
python test_openmc.py

sudo sed '$d' -i /etc/sudoers



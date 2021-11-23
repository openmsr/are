################################################################################
#nuclear data download & extract
################################################################################
#!/bin/bash
set -ex

#defaul libraries
endfb_VII="https://anl.box.com/shared/static/9igk353zpy8fn9ttvtrqgzvw1vtejoz6.xz"
endfb_VIII="https://anl.box.com/shared/static/uhbxlrx7hvxqw27psymfbhi7bx7s6u6a.xz"
jeff="https://anl.box.com/shared/static/4jwkvrr9pxlruuihcrgti75zde6g7bum.xz"

cd $HOME
mkdir nuclear_data
cd nuclear_data

#see other default options above
wget $endfb_VII

for entry in "$PWD"/*
do
  tar -xvf $entry
done

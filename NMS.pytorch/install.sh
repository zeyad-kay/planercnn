#!/usr/bin/env bash

CUDA_PATH=/usr/local/cuda-9.0

echo "Compiling crop_and_resize kernels by nvcc..."
cd nms/src/cuda
$CUDA_PATH/bin/nvcc -c -o nms_kernel.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_62

cd ../../../nms
python build.py

cd ..
python setup.py install
#find  $CONDA_PREFIX -name roi_align | awk '{mkdir $0 "/_ext" }' |bash
#find  $CONDA_PREFIX -name roi_align | awk '{print "cp -r roi_align/_ext/* " $0 "/_ext/" }' |bash

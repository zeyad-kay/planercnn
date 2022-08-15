echo "Installing dependencies"

pip install -r requirements.txt

CUDA=$(which cuda)

if [[ "$CUDA" != "" ]]; then
    echo "Compiling crop_and_resize kernels by nvcc..."
    cd RoIAlign/roi_align/src/cuda
    $CUDA/bin/nvcc -c -o crop_and_resize_kernel.cu.o crop_and_resize_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_62

    cd ../../../roi_align
    python build.py
    cd ..
    python setup.py install

    cd ..

    echo "Compiling nms kernels by nvcc..."
    cd NMS/nms/src/cuda
    $CUDA/bin/nvcc -c -o nms_kernel.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_62

    cd ../../../nms
    python build.py

    cd ..
    python setup.py install

    cd ..
else
    echo "Installing RoIAlign"
    cd RoIAlign/roi_align/
    python build.py
    cd ..
    python setup.py install
    cd ..

    echo "Installing NMS"
    cd NMS/nms/
    python build.py
    cd ..
    python setup.py install
fi
echo "Installing dependencies"

pip install -r requirements.txt

CUDA=$(which cuda)

if [[ "$CUDA" != "" ]]; then
    echo "Installing RoIAlign GPU build..."
    cd RoIAlign/roi_align/src/cuda
    $CUDA/bin/nvcc -c -o crop_and_resize_kernel.cu.o crop_and_resize_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_62

    cd ../../../roi_align
    python build.py
    cd ..
    python setup.py install

    cd ..

    echo "Installing NMS CPU build..."
    cd NMS/nms/src/cuda
    $CUDA/bin/nvcc -c -o nms_kernel.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC -arch=sm_62

    cd ../../../nms
    python build.py

    cd ..
    python setup.py install
    cd ..
else
    echo "Installing RoIAlign CPU build..."
    cd RoIAlign/roi_align/
    python build.py
    cd ..
    python setup.py install
    cd ..

    echo "Installing NMS CPU build..."
    cd NMS/nms/
    python build.py
    cd ..
    python setup.py install
    cd ..
fi
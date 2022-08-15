## Setup
The only way that worked on Windows is to install <a href="https://docs.microsoft.com/en-us/windows/wsl/install">WSL2</a> with Ubuntu 18.04. This uses the CPU not the GPU. To use the GPU, use <a href="https://colab.research.google.com/drive/1k9Lj0uw4GRztyMp_JDabTqz2gGf65ZNb#scrollTo=3bxTpOJPTW_s">this</a> colab notebook.


```sh
$sudo apt update

# update existing python3.6
$sudo apt install python3.6-dev
$sudo apt-get install python3-venv

# install gcc v5 and make it the default
$sudo apt install gcc-5
$sudo update-alternatives --install /usr/bin/x86_64-linux-gnu-gcc x86_64-linux-gnu-gcc /usr/bin/x86_64-linux-gnu-gcc-5 90
$sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-5 90

# virtual environment
$python3 -m venv .venv
$source .venv/bin/activate

# opencv dependencies
$sudo apt install -y libsm6 libxrender-dev

# install dependencies
$pip install -r requirements.txt

# Install RoIAlign
$cd RoIAlign/roi_align/ && python build.py && cd .. && python setup.py install && cd ..

# Install Non Maximum Suppression
$cd NMS/nms/ && python build.py && cd .. && python setup.py install && cd ..
```

To test with images set the images folder path and the camera path.
```sh
$ python evaluate.py --methods=f --suffix=warping_refine --dataset=inference --customDataFolder=example_images --cameraPath=example_images/camera.txt
```
The output will be in the *test/* folder.

To test with videos set the path to the video file and the camera file. This may take a while as it is running on the CPU. Try running it on colab.
```sh
$ python evaluate.py --methods=f --suffix=warping_refine --dataset=inference --video=video.mp4 --cameraPath=example_images/camera.txt
```
The output will be 2 videos, one for the depth and one for the segmentation masks.
## Setup
The only way that worked on Windows is to install <a href="https://docs.microsoft.com/en-us/windows/wsl/install">WSL2</a> with Ubuntu 18.04. The following setup uses the CPU not the GPU. To use the GPU, check <a href="https://colab.research.google.com/drive/1k9Lj0uw4GRztyMp_JDabTqz2gGf65ZNb#scrollTo=3bxTpOJPTW_s">this</a> colab notebook. The notebook installs CUDA v9 and its compatible torch build.


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

# install torch 0.4.1 CPU build
# if you have python3.7, you should download torch-0.4.1-cp37-cp37m-linux_x86_64.whl instead
$pip install https://download.pytorch.org/whl/cpu/torch-0.4.1-cp36-cp36m-linux_x86_64.whl

# install dependencies
$./install.sh
```

## Inference
Download the *checkpoint/* folder from the drive and place it inside the *planercnn/* folder.

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
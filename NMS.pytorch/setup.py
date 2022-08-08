from setuptools import setup, find_packages

setup(
    name='nms',
    version='0.0.1',
    # description='PyTorch version of RoIAlign',
    # author='Long Chen',
    # author_email='longch1024@gmail.com',
    # url='https://github.com/longcw/RoIAlign.pytorch',
    install_requires=[
        'cffi',
    ],
    packages=["nms"],

    package_data={
        'nms': [
            '_ext/nms/*.so',
        ]
    }
)

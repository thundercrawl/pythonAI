

Pre install
1. install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

Install
1. install and configure cpu support, make sure cuda installed firstly
Step 0: Uninstall protobuf

pip uninstall protobuf

Step 1: Uninstall tensorflow

pip uninstall tensorflow
pip uninstall tensorflow-gpu

Step 2: Force reinstall Tensorflow with GPU support

pip install --upgrade --force-reinstall tensorflow-gpu

Step 3: If you haven't already, set CUDA_VISIBLE_DEVICES

So for me with 2 GPUs it would be

export CUDA_VISIBLE_DEVICES=0,1

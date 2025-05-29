## ⚙️ System Requirements

This project was developed and tested on the following system configuration:

```bash
# OS and Kernel
Linux 6.8.0-60-generic #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC x86_64 GNU/Linux

# Ubuntu Version
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.5 LTS
Codename:       jammy
```

### 🧠 CPU and Memory

```bash
# CPU
Model: 13th Gen Intel(R) Core(TM) i7-13620H
Cores: 10 (16 threads total)
Max Frequency: 4.90 GHz

# Memory
Total: 15 GiB
Available: 12 GiB
```

### 🛠 Compilers and Languages

```bash
# GCC
gcc (Ubuntu 11.4.0) 11.4.0

# Python
Python 3.10.12
```

> Note: `pip3` is not installed by default. Install it with:
```bash
sudo apt update && sudo apt install python3-pip
```

---

## 📦 Dependencies

### System Packages

Install these required system packages:

```bash
sudo apt install build-essential cmake git curl libeigen3-dev \
    libopencv-dev libboost-all-dev python3-pip python3-dev \
    nvidia-cuda-toolkit nvidia-driver-570
```

Additional packages used on this system:

```bash
ros-humble-desktop, code, google-chrome-stable, grub*, libreoffice-help-en-us,
ubuntu-desktop, ubuntu-minimal, ubuntu-restricted-addons, os-prober
```

### Python Packages

Install Python dependencies with:

```bash
pip3 install -r requirements.txt
```

`requirements.txt` includes over 150 packages. Some key libraries used:

```
numpy==1.21.5
scipy==1.8.0
matplotlib==3.5.1
opencv-python (via libopencv-dev)
PyYAML==5.4.1
protobuf==3.12.4
catkin-pkg==1.0.0
colcon-core==0.19.0
rosdep==0.25.1
```

For the full list, see [`requirements.txt`](./requirements.txt).

---

### ⚡ CUDA and GPU

```bash
# GPU
NVIDIA GeForce RTX 4060

# Driver and CUDA versions
Driver Version: 570.133.07
CUDA Version: 12.8

# CUDA Compiler
nvcc: Cuda compilation tools, release 11.5, V11.5.119
```

---

## 📥 Cloning This Repository with Submodules

This repository uses Git submodules. Clone it properly using:

### 🔑 SSH (Recommended)

```bash
git clone --recurse-submodules git@github.com:kaRpuri/fillbot.git
```

### 🔑 HTTPS

```bash
git clone --recurse-submodules https://github.com/kaRpuri/fillbot.git
```

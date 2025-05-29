## ⚙️ System Requirements

This project was developed and tested on the following system configuration:

```bash
# OS and Kernel
Linux saayuj-Cyborg-14-A13VF 6.8.0-60-generic #63~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC x86_64 GNU/Linux

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

> Note: `pip3` is not yet installed. To install it:
```bash
sudo apt update && sudo apt install python3-pip
```

---

## 📦 Dependencies

### System Packages

Install the following system packages:

```bash
sudo apt install build-essential cmake git curl libeigen3-dev \
    libopencv-dev libboost-all-dev python3-pip python3-dev \
    nvidia-cuda-toolkit nvidia-driver-570
```

Example list of manually installed packages:

```bash
base-passwd, bsdutils, code, curl, dash, diffutils, efibootmgr,
fonts-indic, google-chrome-stable, grub*, gzip, hostname,
language-pack-en*, libreoffice-help-en-us, linux-generic-hwe-22.04,
nvidia-cuda-toolkit, nvidia-driver-570, os-prober, ros-humble-desktop,
ubuntu-desktop, ubuntu-minimal, ubuntu-restricted-addons
```

### Python Packages

After installing `pip3`, run:

```bash
pip3 install -r requirements.txt
```

To generate `requirements.txt`:

```bash
pip3 freeze > requirements.txt
```

---

### ⚡ CUDA and GPU

```bash
# NVIDIA GPU
NVIDIA GeForce RTX 4060
Driver Version: 570.133.07
CUDA Version: 12.8

# CUDA Compiler
nvcc: Cuda compilation tools, release 11.5, V11.5.119
```

---

## 📦 Cloning This Repository with Submodules

This repository contains Git submodules. To clone it properly:

---

### 🔑 Clone Using SSH (recommended if you have SSH keys configured)

```bash
git clone --recurse-submodules git@github.com:kaRpuri/fillbot.git
```

### 🔑 Clone Using HTTPS

```bash
git clone --recurse-submodules https://github.com/kaRpuri/fillbot.git
```

import platform
import psutil
import pynvml

# Initialize pynvml
pynvml.nvmlInit()

# Get the first available GPU
handle = pynvml.nvmlDeviceGetHandleByIndex(0)

# Get the GPU information
gpu_name = pynvml.nvmlDeviceGetName(handle).decode()
mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
gpu_mem = f"{mem_info.total / (1024 ** 3):.2f}GB"

# Cleanup pynvml
pynvml.nvmlShutdown()

# Get the CPU information
cpu_info = platform.processor()
freqs = psutil.cpu_freq(percpu=True)
freq_info = " x ".join([f"{freq.current:.2f}MHz" for freq in freqs])
usage = psutil.cpu_percent(percpu=True)

# Print the system information
print(f"We conducted our experiments on a system with CPU: {cpu_info} ({len(freqs)} cores @ {freq_info}, {sum(usage)/len(usage):.2f}% usage), RAM: {psutil.virtual_memory().total / (1024 ** 3):.2f}GB, and GPU: {gpu_name} with {gpu_mem} of memory.")

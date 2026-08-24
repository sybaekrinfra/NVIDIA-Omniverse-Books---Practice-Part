./isaaclab.sh -p -c "
import sys
import torch
import torchvision
import lazy_loader
from importlib.metadata import version

print(sys.executable)
print('isaacsim', version('isaacsim'))
print('torch', torch.__version__)
print('torchvision', torchvision.__version__)
"

./isaaclab.sh -p \
  scripts/tutorials/00_sim/create_empty.py \
  --viz kit
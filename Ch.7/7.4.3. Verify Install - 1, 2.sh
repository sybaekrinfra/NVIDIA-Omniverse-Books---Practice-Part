cd $HOME/IsaacLab
./isaaclab.sh -p -c "
import sys
from importlib.metadata import version

print('Python:', sys.executable)
print('Python version:', sys.version)

for pkg in ['isaacsim', 'isaaclab', 'torch', 'torchvision', 'lazy_loader']:
    try:
        print(pkg, version(pkg))
    except Exception as e:
        print(pkg, type(e).__name__, str(e))
"

cd $HOME/IsaacLab
./isaaclab.sh -p \
  scripts/tutorials/00_sim/create_empty.py \
  --viz kit
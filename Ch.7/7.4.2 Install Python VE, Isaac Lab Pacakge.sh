cd ~/IsaacLab
uv venv --python 3.12 --seed env_isaaclab
source env_isaaclab/bin/activate
which python
python --version
uv pip install --upgrade pip
uv pip install "isaacsim[all,extscache]==6.0.1.0" \
  --extra-index-url https://pypi.nvidia.com \
  --index-strategy unsafe-best-match \
  --prerelease=allow
uv pip install -U torch==2.11.0 torchvision==0.26.0 \
  --index-url https://download.pytorch.org/whl/cu128
./isaaclab.sh -i
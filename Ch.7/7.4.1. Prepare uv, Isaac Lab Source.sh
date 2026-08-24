curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"
uv --version
git clone https://github.com/isaac-sim/IsaacLab.git \
  --branch release/3.0.0-beta2
cd IsaacLab
git checkout --detach af1bab4dc173ba69b08fab779c14ead61d13fd33
git rev-parse HEAD
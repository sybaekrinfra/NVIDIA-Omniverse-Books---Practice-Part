if [ -e "$HOME/dofbot_rl" ]; then
  echo "$HOME/dofbot_rl already exists; inspect it before continuing."
else
  git clone --branch 1.0.1 --depth 1 \
    https://github.com/sybaekrinfra/dofbot_rl.git \
    "$HOME/dofbot_rl"
fi

git -C "$HOME/dofbot_rl" remote get-url origin
git -C "$HOME/dofbot_rl" status --short
git -C "$HOME/dofbot_rl" rev-parse HEAD
git -C "$HOME/dofbot_rl" describe --tags --always
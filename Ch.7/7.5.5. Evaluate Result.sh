cd ~/IsaacLab
source env_isaaclab/bin/activate
./isaaclab.sh play --rl_library rsl_rl \
  --task=Isaac-Cartpole-Direct-v0 \
  --num_envs=32 \
  --seed=1001 \
  --visualizer kit physics=physx
  
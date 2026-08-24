./isaaclab.sh train --rl_library rsl_rl \
  --task=Isaac-Cartpole-Direct-v0 \
  --num_envs=64 \
  --max_iterations=10 \
  --seed=42 \
  --visualizer kit physics=physx
  
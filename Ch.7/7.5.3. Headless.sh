./isaaclab.sh train --rl_library rsl_rl \
  --task=Isaac-Cartpole-Direct-v0 \
  --num_envs=4096 \
  --max_iterations=1000 \
  --seed=42 \
  physics=physx
  
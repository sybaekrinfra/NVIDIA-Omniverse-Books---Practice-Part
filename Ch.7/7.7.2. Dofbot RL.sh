cd ~/IsaacLab && PYTHONPATH="$HOME" \
./isaaclab.sh train \
  --rl_library rsl_rl \
  --task Dofbot-Reach-IK-Direct-v0 \
  --external_callback dofbot_rl.tasks.register_tasks \
  --device cuda:0 \
  --num_envs 16 \
  --max_iterations 1000 \
  --viz kit
  
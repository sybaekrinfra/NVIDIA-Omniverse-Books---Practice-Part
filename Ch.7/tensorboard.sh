#!/bin/bash

set -e

ISAACLAB_DIR="$HOME/IsaacLab"
LOG_DIR="${1:-$ISAACLAB_DIR/logs}"
DOFBOT_LOG_DIR="$HOME/Desktop/dofbot_rl/train_result"
PORT="${2:-6006}"
HOST="0.0.0.0"

if [ ! -d "$ISAACLAB_DIR" ]; then
    echo "[ERROR] IsaacLab directory not found: $ISAACLAB_DIR"
    exit 1
fi

if [ ! -d "$LOG_DIR" ]; then
    echo "[ERROR] Log directory not found: $LOG_DIR"
    exit 1
fi

LOGDIR_SPEC="isaaclab:$LOG_DIR"
if [ -d "$DOFBOT_LOG_DIR" ]; then
    LOGDIR_SPEC="$LOGDIR_SPEC,dofbot:$DOFBOT_LOG_DIR"
else
    echo "[WARN] Dofbot log directory not found, skipping: $DOFBOT_LOG_DIR"
fi

cd "$ISAACLAB_DIR"

echo "[INFO] Starting TensorBoard"
echo "[INFO] Log directory: $LOG_DIR"
echo "[INFO] Log directory specification: $LOGDIR_SPEC"
echo "[INFO] Port: $PORT"
echo "[INFO] URL: http://localhost:$PORT"

./isaaclab.sh -p -m tensorboard.main \
    --logdir_spec "$LOGDIR_SPEC" \
    --host "$HOST" \
    --port "$PORT"

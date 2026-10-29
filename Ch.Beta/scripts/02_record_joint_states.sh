#!/usr/bin/env bash
set -euo pipefail
# 사용: bash scripts/02_record_joint_states.sh [입력토픽] [새 bag 경로]
BETA_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
STATE_TOPIC="${1:-/demo_robot/joint_states}"
BAG_DEST="${2:-${BETA_ROOT}/bag/joints_$(date +%Y%m%d_%H%M%S)}"
if [[ -e "$BAG_DEST" ]]; then
    echo "이미 존재하는 경로입니다. 새 bag 경로를 지정하세요: $BAG_DEST" >&2
    exit 1
fi
mkdir -p -- "$(dirname -- "$BAG_DEST")"
echo "기록: $STATE_TOPIC → $BAG_DEST (Ctrl+C로 종료 후 metadata.yaml 확인)"
exec ros2 bag record --storage sqlite3 --output "$BAG_DEST" --topics "$STATE_TOPIC"

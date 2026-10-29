#!/usr/bin/env bash
set -euo pipefail
# 사용: bash scripts/04_play_joint_states.sh BAG [기록토픽] [재생속도]
if [[ $# -lt 1 || ! -f "$1/metadata.yaml" ]]; then
    echo "사용: $0 BAG_DIRECTORY [RECORDED_TOPIC] [RATE]" >&2
    exit 1
fi
RECORDED_TOPIC="${2:-/demo_robot/joint_states}"
PLAY_RATE="${3:-1.0}"
# 원래 실물 토픽 대신 별도 replay 토픽으로 재생합니다.
exec ros2 bag play "$1" --rate "$PLAY_RATE" --delay 2 \
    --topics "$RECORDED_TOPIC" --remap "$RECORDED_TOPIC:=/replay/joint_states"

"""JointState의 name 기준 매핑. 배열 순서를 신뢰하지 않습니다."""
import math


def map_positions(names, positions, source_names):
    if len(names) != len(positions) or not names or len(set(names)) != len(names):
        raise ValueError('name/position 개수 불일치 또는 중복 관절 이름')
    if not all(math.isfinite(x) for x in positions):
        raise ValueError('position에 NaN/Inf가 있습니다')
    lookup = dict(zip(names, positions))
    missing = set(source_names) - lookup.keys()
    if missing:
        raise ValueError(f'필수 관절 누락: {sorted(missing)}')
    return [float(lookup[name]) for name in source_names]

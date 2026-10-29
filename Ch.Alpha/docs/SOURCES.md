# 실습 자료 출처

기존 NVIDIA-Omniverse-CBNU-Workshop 자료를 바탕으로 PSK 교육용 실습을 구성했습니다. CAD·도면은 기존 교재 Ch.3의 BX200L 자료, USD 합성 예제는 기존 Ch.2 LIVERPS 자료에서 가져왔습니다. 기존 자료의 권리 표기를 유지하며 새로운 라이선스를 부여하지 않습니다. 원본 에셋 기록은 [ASSET_MANIFEST.csv](ASSET_MANIFEST.csv)를 참고하세요.

온도·진동·다중 장비 CSV와 면별 온도 분포는 교육용 합성 데이터입니다. 실제 센서 측정 또는 CAE 해석 결과가 아닙니다. 단순 회전팔은 Joint·Drive 학습을 위해 제작한 장면이며 BX200L의 실제 동역학 모델이 아닙니다.

`shared/assets/legacy_liverps/telemetryAttribute.py`는 기존 장면의 `/World/Equipment/Pump`를 전제로 한 참고 코드입니다. 이번 공통 장면의 상태 실습은 `scripts/05_replay_status.py`를 사용합니다.

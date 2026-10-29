# Ch.Alpha 통합 이력

2026-10-29, 사용자 요청에 따라 `NVIDIA-Omniverse-CBNU-Workshop`의 자료를 이 저장소 `Ch.Alpha`로 가져왔습니다. 별도 `.git`, 캐시, 학습자 outputs는 포함하지 않습니다. 기존 Ch.2~Ch.7은 그대로 활용합니다.

PSK 첨부 Agenda를 기준으로 2일차 운영표·학습자 가이드·기록지·선택 미션을 보강했습니다. 기존 충북대 자료의 Part 번호·PPT·기존 검증 이력은 보존합니다. 새 자료의 적용 범위와 검증 결과는 README와 VALIDATION에서 구분합니다.

00 초기화는 열린 체크포인트로부터 Ch.Alpha 루트를 찾습니다. 다른 복사본의 모듈이 이미 로드되어 있으면 잘못된 폴더로 결과를 쓰지 않도록 앱 재시작을 안내합니다. 관절 장면은 외부 자산 없이 `tools/build_joint_lab.py`로 재생성합니다.

이 폴더는 독립 Git 저장소가 아닙니다. 커밋·Push는 상위 `NVIDIA-Omniverse-Books---Practice-Part`에서 수행합니다. 출력물은 `.gitignore`로 제외합니다. CAD·도면·기존 화면의 출처를 유지하며 별도 라이선스를 부여하지 않습니다.

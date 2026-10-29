# 실습 시작 준비

1. 강사가 제공한 Isaac Sim을 실행합니다. 저장소 전체 또는 Ch.Alpha 전체를 로컬에 둡니다.
2. File > Open에서 `checkpoints/02_structured.usda`를 엽니다. Stage와 Property 창을 확인합니다.
3. 화면이 비어 보이면 `/World` 선택 후 F(Frame Selection)를 누릅니다.
4. Script Editor에서 `scripts/00_start_here.py`를 실행합니다. 열린 장면으로부터 자료 경로를 자동으로 찾습니다.
5. 경로 탐색에 실패하면 00의 ROOT를 자신의 Ch.Alpha 절대 경로로 지정합니다. 다른 복사본 모듈이 로드되었다는 오류는 앱 재시작 후 다시 시도합니다.
6. 속성 변경 전 Timeline의 Stop을 누릅니다. 새 장면을 열기 전 `06_stop_tasks.py`로 교육용 비동기 작업을 중단합니다.
7. 원본 체크포인트는 덮어쓰지 않습니다. [실습 가이드](PSK_DAY2_LABS.md)의 결과 보관 방법으로 outputs에 저장합니다.

설치나 확장 기능 문제는 강사에게 문의하세요. CAD 변환기가 없으면 동봉된 USD를 사용합니다. ROS 2와 Replicator는 강사가 준비한 환경에서 진행합니다.

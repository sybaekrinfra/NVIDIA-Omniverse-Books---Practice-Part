# Day 1 Part 4 · USD 기능 실습

배정 75분: 설명 37분, 실습 38분. 입력: `shared/assets/usd_basics` 전체. 선택 자료: `shared/assets/legacy_liverps`.

## 목표와 개념

원본 자산을 유지하면서 상위 Layer에서 색을 덮어쓰고 Reference와 Payload를 비교합니다. 로컬 의견이 참조 자산의 같은 속성보다 강한 간단한 경우를 확인합니다. 전체 합성 규칙을 “파일 순서만”으로 설명하지 않습니다.

## 따라하기

1. `assembly.usda`를 엽니다. 두 Cube가 청록색인지 확인합니다.
2. `review.usda`를 엽니다. ReferencePart만 빨간색인지 확인합니다.
3. 텍스트 편집기로 세 파일을 비교합니다. `part.usda`의 색은 그대로이고 review에 변경 의견이 있습니다.
4. review의 색을 `(1, 0.2, 0.1)`에서 `(0.8, 0.2, 0.8)`로 바꿔 저장 후 앱에서 다시 엽니다. Layer를 Reload할 때 미저장 변경을 확인합니다.
5. 실습 후 review 색을 원래 값으로 복원합니다.
6. 앱에서 assembly를 다시 열고 Payload를 언로드·로드합니다. GUI가 없으면 강사가 Script Editor에서 아래 코드를 실행합니다.

```python
import omni.usd
s = omni.usd.get_context().get_stage()
s.Unload("/World/PayloadPart")
# 형상이 사라진 것을 확인한 뒤 다음 줄을 별도로 실행
s.Load("/World/PayloadPart")
```

7. 선택 심화: `legacy_liverps/04_variant.usda`를 열고 Variant를 바꿉니다. Inherits·Specializes·6개 합본은 조기 완료자만 진행합니다.

## 완료 확인

제출: 원본 색, review 색, Payload 언로드 화면과 설명. 원본을 고치지 않고 결과를 바꿀 수 있으며 unload가 파일 삭제가 아님을 설명하면 통과합니다.

색 변화가 없으면 현재 연 파일과 편집 Layer를 확인합니다. review보다 강한 Session Layer의 수정이 있으면 새로 열어 확인합니다.

## 확장 실습

[추가 예제·오류 찾기·선택 과제](EXPANDED_LAB.md): compact와 wide 배치 검토. 기존 실습 시간 안에서 선택하여 진행합니다.

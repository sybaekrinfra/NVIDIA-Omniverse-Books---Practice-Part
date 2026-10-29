# Kit-CAE 3.0 · 네 가지 예제로 이해하는 해석 결과 시각화

## 1. 네 가지 예제에서 배울 것

| 예제 | 중심 질문 | 비교할 결과 |
|---|---|---|
| Time-Varying Structural Analysis | 시간이 지나며 어느 부위가 변형되는가? | 변형 형상과 소성변형률 |
| Simulation Data in Context | 이 분포가 실제 설비의 어느 위치에 해당하는가? | 서버 랙과 주변 온도장 |
| Multi-Domain Simulation | 유체와 구조 결과를 같은 시점에 보면 무엇이 보이는가? | 압력계수와 굽힘응력 |
| AI Surrogate Simulation Data | AI가 예측한 공간 데이터를 어떻게 살펴보는가? | 자동차 주변 속도장과 유선 |

네 예제의 공통 흐름은 **데이터 가져오기 → 필드 확인 → 표현 방식 선택 → 색 범위 설정 → 비교**입니다. 예제 파일은 Kit-CAE 코드 저장소에 포함되지 않으므로 별도로 준비합니다. [공식 예제 목록](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/examples/index.html)

## 2. 실행 준비

### 앱과 샘플 준비

공식 설치 안내는 NVIDIA RTX GPU, Git/Git LFS, 운영체제에 맞는 C++ 빌드 환경을 전제로 합니다. 이미 준비된 교육장 앱이 있다면 빌드 과정은 건너뜁니다. 최초 빌드와 실행에는 의존성 다운로드·셰이더 준비 시간이 필요합니다.

Linux에서 새로 준비하는 경우:

```bash
git lfs install
git clone https://github.com/NVIDIA-Omniverse/kit-cae.git
cd kit-cae
./repo.sh build -r
./repo.sh launch -n omni.cae.kit
```

Windows에서는 Kit-CAE 폴더에서 `repo.bat build -r`, `repo.bat launch -n omni.cae.kit`를 사용합니다. OS별 개발 도구의 세부 요구사항과 샘플 다운로드는 [Get Started](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/getting-started.html)의 **Prerequisites / Sample Data**에서 확인하세요.

샘플 압축을 풀면 `kit_cae_user_guide_data/examples/` 아래의 01~04 폴더를 사용합니다. `.case`와 같이 다른 파일을 참조하는 형식은 대표 파일 하나만 옮기지 말고 폴더 구조를 유지하세요. 샘플 데이터는 이 저장소에 동봉하지 않았습니다.

### 가져왔는데 화면이 비어 있어도 실패는 아닙니다

Kit-CAE는 원래 파일을 참조하고 필요한 배열을 읽는 방식으로 데이터를 가져옵니다. Stage에 데이터가 존재해도 화면에 그릴 Operator를 아직 만들지 않았다면 보이지 않을 수 있습니다. 보통 **File > Import → Import to Stage**로 가져온 뒤 데이터셋을 선택해 표현을 만듭니다.

3.0에서는 시간 설정이 Import 창이 아니라 가져온 루트의 **CAE File Format Time**에 있습니다. 기본 Stage는 cm·Z-up이며 Import가 원본 좌표를 자동 환산하지 않습니다. 다른 자료와 합칠 때 단위·축·위치를 확인합니다. [Import Data](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/importing-data.html)

## 3. 먼저 알아둘 용어와 화면 조작

### 데이터와 표시 설정을 구별하기

| 용어 | 쉽게 이해하기 | 확인할 내용 |
|---|---|---|
| Dataset | 좌표·연결 관계와 해석 배열을 가진 데이터 묶음 | 어떤 영역의 데이터인가? |
| Field | 각 위치에 대응하는 값 | 온도·응력·속도 중 무엇인가? |
| Scalar | 한 위치에 숫자 하나 | 온도, 압력 등 |
| Vector | 한 위치에 방향 성분 여러 개 | 속도의 x/y/z 성분 등 |
| node / element | 값이 붙어 있는 대상 | 절점 값인가, 요소 값인가? |
| ROI | 자세히 살펴볼 공간 범위 | 표시 범위를 줄인 것인가? |
| Seed | 유선 추적을 시작할 위치 | 어디에서 흐름을 관찰할 것인가? |
| domain | 값을 색에 대응시키는 수치 구간 | 현재 색의 최솟값·최댓값은? |

`Source`로 만드는 Bounding Box는 관심 영역을 정하는 보조 형상입니다. Unit Sphere의 각 꼭짓점은 유선 시작점으로 사용할 수 있습니다. 구를 움직이면 시작 영역이 달라집니다. 구의 해상도는 씨앗 배치와 관련되며 해석 메시 해상도가 아닙니다. [Create Sources](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/sources.html)

`Operator`는 데이터를 화면 표현으로 만듭니다. Faces는 표면, Volume은 공간 분포, Streamlines는 벡터장을 따라 계산한 선입니다. 선택 필드나 입력이 바뀌면 관련 표현도 다시 계산됩니다. **필드 선택은 Add Field**, ROI·Seed 같은 데이터 대상 연결은 **Add Target**을 사용합니다. [Create Operators](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/operators.html)

### 숫자를 확인한 뒤 색을 선택하기

1. 데이터 배열을 가진 Prim을 선택합니다. 필드 이름이 Stage의 별도 자식 Prim으로 보이지 않을 수 있습니다.
2. Properties의 Arrays에서 필드를 고릅니다.
3. Array Details의 Compute Details로 범위·통계를 계산합니다.
4. 시점을 바꾼 뒤 오래된 통계라는 표시가 나오면 Refresh Details를 누릅니다.

히스토그램 구간을 좁히는 것은 분포를 자세히 보는 조작입니다. 이것만으로 원본 배열이나 렌더링 색 범위가 바뀌지는 않습니다. [Explore Your Data](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/exploring-data.html)

### 색 설정 위치

| 표시 방식 | 범위 설정 위치 |
|---|---|
| Faces / Streamlines | Operator 아래 Materials → ScalarColor → Shader의 domain |
| Volume | Operator 아래 Material → Colormap의 Domain 및 투명도 제어점 |

Colors의 Rescale Mode는 `clamp`이면 현재 범위에 맞추고, `grow`이면 범위를 확장하며, `disable`이면 수동 범위를 유지합니다. 비교할 때는 **disable 설정 후 같은 범례**를 적용하세요. Volume의 범위 밖 값은 Domain Boundary Mode에 따라 끝 색 또는 투명으로 처리될 수 있습니다. [Color Mapping and Rendering](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/color-and-rendering.html)

**이해하기:** 최댓값이 10인 화면과 100인 화면에서 자동 범례를 쓰면 둘 다 빨간 부분이 나타날 수 있습니다. 빨간색만으로 같은 크기의 현상이라고 판단하면 안 됩니다. 투명하게 만든 위치도 데이터가 없는 위치라고 단정할 수 없습니다.

## 4. 예제 ① 시간에 따른 구조 변형

### 공식 절차 요약

파일: `examples/01_time-varying-structural/bumper_beam.case`.

기둥과 충돌하는 범퍼 빔의 저장된 구조해석 결과입니다. 대표 필드 `PlasticStrain`은 두께 방향 5개 층 중 최대 소성변형률입니다. `PlasticStrainUpper/Lower`는 위·아래 층, `ContactPressure`는 절점 접촉압력입니다.

1. `.case`를 Import합니다. 가져온 루트의 시간 Source=`TimeStep`, Scale=`0.0333333333`, Offset=`0`으로 설정합니다.
2. 내부 `bumper_beam` 데이터셋에서 Faces를 생성합니다. 재생하며 변형을 확인합니다.
3. Faces의 Colors에서 `PlasticStrain`을 선택합니다.
4. 데이터셋 Arrays에서 처음과 마지막 시점의 통계를 각각 계산·갱신합니다. 마지막 범위는 약 `0~0.541`; 히스토그램은 `0.005~0.065` 구간을 살펴봅니다.
5. 색 자동 조정을 끄고 Shader domain을 `0~0.065`로 고정합니다.
6. Faces의 Properties `+`에서 CAE → Operator Temporal을 추가하고 Enable Field Interpolation을 켭니다. 홀수 time code를 비교합니다.

샘플은 물리 시간이 없는 51개 인덱스입니다. 위 설정과 60 time codes/s에서는 원본이 `0,2,…,100`에 놓입니다. 첫 재생이 끊기면 한 차례 타임라인을 훑어 캐시를 준비합니다. [공식 예제·화면](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/examples/time-varying-structural.html)

### 이해하기 · 재생 시간과 해석 시간

시간 배치의 일반식은 다음과 같습니다.

```text
배치할 초 = 원본 값 × Scale + Offset
time code = 배치할 초 × Stage의 Time Codes Per Second
```

`TimeStep`은 저장 샘플 순번, `TimeValue`는 파일의 물리 시간, `IterationValue`는 반복 계산 번호를 사용합니다. Scale은 단위 변환 또는 표시 간격을 정합니다. 물리 시간 메타데이터가 없다면 보기 편하게 배치한 시간을 실제 충돌 소요시간으로 해석하면 안 됩니다. [시간 매핑 설명](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/importing-data.html#time-series)

소성변형률은 하중 제거 후에도 남는 변형을 이해하는 지표입니다. 변위나 응력과 같은 값은 아닙니다. 최대값만 보고 파손 여부를 결정하려면 재료 모델·판정 기준 등 추가 정보가 필요합니다.

보간으로 중간 화면이 부드러워져도 새로운 해석 샘플을 계산한 것은 아닙니다. 저장 간격 사이에 발생한 실제 최대 현상이 복원된다고 보장할 수 없습니다.

### 비교 활동 · 5분

- 같은 위치의 처음·중간·마지막 화면을 고정 범례로 비교합니다.
- 범례 상한을 낮추었을 때 값이 달라진 것인지 색 대비만 달라진 것인지 설명합니다.
- 보간 ON/OFF 화면에 각각 “저장 샘플”과 “중간 추정 표시”를 구별해 기록합니다.

**완료 결과:** 같은 범례의 화면 2장과 “이 타임라인을 실제 충돌 시간이라고 말할 수 있는가?”에 대한 한 문장.

## 5. 예제 ② 설비 형상 위에 열해석 결과 겹치기

### 공식 절차 요약

폴더: `examples/02_simulation-data-in-context`.

`GB300.usd`는 서버 랙 형상, `compute_thermal.cgns`는 주변 영역의 정상상태 열해석 데이터입니다. `Temperature`는 셀에 대응합니다.

1. File > Open으로 `GB300.usd`를 엽니다. 이후 `.cgns`를 Import합니다.
2. 열 데이터의 `Base > Zone > Elements`에서 Bounding Box를 만듭니다.
3. Ctrl+D로 복제하고 크기·위치를 바꿔 랙 뒤쪽 hot aisle을 감쌉니다. 원래 상자는 전체 범위 확인용으로 남깁니다.
4. `Elements`에서 Volume을 만들고 `nanovdb`를 선택합니다.
5. Voxelization의 ROI에 작은 상자를 연결하고 Max Resolution=`256`으로 시작합니다.
6. Colors에 `Temperature`를 지정합니다. 자동 범위 조정을 끄고 Colormap domain을 약 `31~37`로 설정한 뒤 투명도를 조절합니다.
7. 랙을 숨겼다 표시하면서 분포의 위치를 비교합니다.

CAD와 필드는 각자의 원본 파일을 유지하면서 한 Stage에서 함께 표시됩니다. [공식 예제·화면](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/examples/simulation-in-context.html)

### 이해하기 · 공간 맥락이 필요한 이유

온도장만 보면 “높은 값의 영역이 있다”까지는 말할 수 있습니다. 설비 형상과 겹치면 “어느 장비의 어느 면 가까이인가?”를 논의할 수 있습니다. 위치가 맞지 않으면 해석도 잘못되므로 축·좌표 원점·길이 단위를 먼저 확인합니다.

ROI를 바꾸는 것은 분석·표시할 공간을 고르는 일입니다. 서버의 발열 조건이나 냉각 경계조건을 변경해서 다시 해석하는 일이 아닙니다. 랙 형상을 옮겨도 저장된 온도장이 그 새 배치의 열해석 결과로 바뀌지는 않습니다.

**단위 확인:** 공식 예제 본문은 색 구간의 숫자를 제시하지만 Temperature의 단위를 명시하지 않습니다. 수업 화면에 °C를 임의로 덧붙이지 말고 데이터 메타데이터나 제공 설명을 확인하세요.

### 해상도를 올리면 무엇이 달라질까?

nanovdb는 데이터를 복셀 표현으로 재표본화합니다. Max Resolution은 가장 긴 축의 복셀 수를 제어합니다. 원본의 지원되는 비정형 셀을 유지해야 한다면 irregular 표현을 검토합니다. [Volume·Voxelization 설명](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/operators.html#voxelization-properties)

표시 해상도를 높이는 것은 원래 해석 메시를 더 촘촘히 풀어 얻는 정확도 향상과 다릅니다. 계산량·메모리 부담과 화면 차이를 함께 관찰하세요.

### 비교 활동 · 5분

- 랙 ON/OFF 두 화면에서 설명할 수 있는 정보의 차이를 적습니다.
- ROI를 좁히되 같은 색 범위를 유지합니다.
- 투명도를 바꾼 뒤 “안 보이는 부분의 온도가 0인가?”를 토의합니다.

**완료 결과:** 랙과 ROI가 함께 보이는 화면, 사용 필드·범례·단위 확인 여부.

## 6. 예제 ③ 유체와 구조 결과를 함께 보기

### 공식 절차 요약

폴더: `examples/03_multi-domain`.

`bscw_cfd.cgns`에는 절점 압력계수 `Cp`, `bscw_struct.case`에는 절점 굽힘응력 `BendingStress`가 있습니다. 두 자료는 101개 샘플의 공통 타임라인을 갖습니다.

1. 구조 `.case`와 유체 `.cgns`를 각각 Import합니다.
2. 구조 데이터의 `wing_surface`에서 Faces를 만들고 변형을 재생합니다.
3. Faces를 잠시 숨깁니다. 유체 데이터 `Base > Zone > Elements`에서 Volume → nanovdb를 생성합니다.
4. Volume의 색 필드를 `Cp`, Max Resolution을 `256`으로 설정합니다.
5. Faces를 다시 표시하고 색 필드를 `BendingStress`로 선택합니다.
6. Faces의 자동 색 범위 조정을 끄고 Shader domain=`1.1~24.2`로 설정합니다.
7. 타임라인을 움직여 두 표현을 함께 확인합니다.

두 파일 형식이 달라도 결과를 동기화해 볼 수 있습니다. [공식 예제·화면](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/examples/multi-domain-simulation.html)

### 이해하기 · 같은 색이 같은 물리량은 아닙니다

압력계수는 일반적으로 압력 차이를 기준 동압으로 정규화한 무차원 값입니다. `Cp`를 압력 Pa로 읽지 않습니다. 굽힘응력은 구조에 발생하는 응력입니다. 공식 예제 본문에 응력 단위가 명시되어 있지 않으므로 `1.1~24.2 MPa`라고 임의로 표기하지 않습니다.

두 표현이 모두 빨갛더라도 서로 다른 변수·범례입니다. “붉은 영역끼리 같은 강도”라고 비교하지 말고 각 변수의 이름과 범위를 따로 읽습니다.

**동기 재생과 연성해석의 차이:** 이 실습에서 두 결과를 같은 화면에 표시한다고 해서 유체의 힘을 구조 해석기에 보내고, 변형된 형상을 다시 유체 해석기로 돌려보내는 계산이 수행되는 것은 아닙니다. 저장된 결과를 함께 관찰하는 절차입니다. 유체–구조 상호작용의 원인·결과를 주장하려면 원본 해석 조건과 연계 방식을 추가로 확인해야 합니다.

직접 만든 자료를 합칠 때는 샘플 개수뿐 아니라 각 샘플의 물리 시각과 좌표계도 확인하세요. 100개씩 있다는 사실만으로 같은 시간 구간을 뜻하지 않습니다.

### 비교 활동 · 5분

- 유체만, 구조만, 둘 다 표시한 화면을 순서대로 비교합니다.
- 같은 시점에서 눈에 띄는 영역을 각각 표시하되 인과관계는 단정하지 않습니다.
- 두 색 범례에 변수 이름을 따로 붙입니다.

**완료 결과:** 동일 시점의 결합 화면과 “동시에 본다는 것과 함께 계산한다는 것의 차이” 한 문장.

## 7. 예제 ④ AI 대리모델의 추론 결과 보기

### 공식 절차 요약

폴더: `examples/04_ai-surrogate-simulation-data`.

`aero_auto_inference.npz`는 자동차 외부 공력 대리모델의 저장된 추론 결과, `aero_auto_low.stl`은 차체 형상입니다. NPZ에는 128,000점의 `velocity`, `pressure`, 난류 관련 배열과 별도의 격자 `sdf`가 있습니다.

1. STL과 NPZ를 각각 Import합니다. 이 샘플은 두 좌표계가 Z-up으로 맞춰져 있습니다.
2. 차체 데이터에서 Faces를 생성합니다.
3. 추론 데이터에서 Bounding Box를 만들고, 여기서 해상도 `16`의 Unit Sphere를 생성합니다.
4. 구를 복제해 자동차 앞쪽 두 위치에 배치합니다.
5. 추론 데이터에서 Streamlines → nanovdb를 생성합니다. Gaussian Splatting의 Radius Factor=`4`, Direction=`forward`로 설정합니다.
6. Seeds에 두 구를 연결하고 Velocities에는 `velocity`를 선택합니다. 배열 형태는 `(128000, 3)`입니다.
7. Colors에도 `velocity`를 선택하되 Mode=`vector_magnitude`로 지정합니다. 자동 범위를 끄고 domain=`20~35`부터 시작합니다.
8. 구의 위치를 바꾸어 유선을 비교합니다.

이 과정의 입력은 저장된 NPZ입니다. [공식 예제·화면](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/examples/ai-surrogate-sim-data.html)

### 이해하기 · AI를 새로 실행하는 실습인가요?

대리모델은 학습을 통해 해석 입력과 결과 사이의 관계를 근사하는 모델입니다. 이 예제에서 다루는 것은 **이미 저장된 예측 결과를 살펴보는 단계**입니다. 차체나 구의 위치를 바꿀 때 AI 모델이 새로 추론했다고 설명하면 안 됩니다. Seed를 옮기는 것은 같은 벡터장의 다른 시작점에서 선을 추적하는 조작입니다.

Velocities에는 흐름을 따라갈 **방향 정보**가 필요하고, Colors에는 색으로 표현할 **크기**가 필요합니다. 속도 크기는 `sqrt(vx² + vy² + vz²)`입니다. 벡터를 색으로 보기 위해 크기를 계산했다고 해서 원본 속도장이 스칼라장으로 대체되는 것은 아닙니다.

`20~35` 역시 데이터 단위를 확인한 뒤 해석합니다. 공식 예제 본문의 숫자만 보고 m/s라고 확정하지 않습니다. 서로 다른 개수·형태의 배열을 같은 점에 대응하는 값이라고 가정하지 마세요. 특히 격자 SDF와 점별 속도 배열은 용도가 다릅니다.

### 유선은 입자가 실제로 이동한 궤적인가요?

유선은 주어진 속도장의 방향을 따라 연결한 선입니다. 시간에 따라 변하는 흐름에서 입자의 이동 이력과 항상 같지는 않습니다. 교육에서는 “이 속도장에서는 이 방향으로 흐른다고 해석할 수 있다” 수준으로 설명합니다.

Kit-CAE의 별도 CAE Flow는 과학 필드를 이용한 입자·효과 애니메이션을 제공합니다. 정성적 표현인 Flow와 속도장을 따라 적분하는 Streamlines를 구분합니다. [Flow Visualization](https://docs.omniverse.nvidia.com/guide-kit-cae/latest/v3/flow-visualization.html)

### 비교 활동 · 5분

- 한 Seed만 옮기고 다른 Seed는 고정합니다. 달라진 선과 유지된 입력을 설명합니다.
- 선의 방향과 색의 크기가 각각 어떤 설정에서 오는지 찾습니다.
- “AI 결과가 그럴듯해 보인다”와 “정확도를 검증했다”의 차이를 적습니다.

**완료 결과:** 서로 다른 Seed 위치의 화면 2장, 입력 출처가 저장된 AI 추론 결과임을 표기.

## 8. 네 예제를 연결하는 비교 질문

아래 활동은 공식 과정의 필수 단계가 아니라 교육용 제안입니다. 한 번에 설정 하나만 바꾸고 변경 전후 화면에 필드·범례·시점을 남기세요.

| 질문 | 비교할 조작 | 생각할 핵심 |
|---|---|---|
| 범례가 달라지면 같은 색을 비교할 수 있는가? | 고정 범위와 자동 범위 | 색과 물리값의 구별 |
| 작은 ROI가 새로운 해석 조건인가? | ROI 위치·크기 변경 | 표시 범위와 해석 경계조건의 구별 |
| 매끄러운 영상이 더 정확한 해석인가? | 보간 ON/OFF | 저장 데이터와 표시상 추정의 구별 |
| 두 결과가 동시에 움직이면 연성해석인가? | 유체/구조 표시 전환 | 동기 시각화와 솔버 연계의 구별 |
| 유선이 바뀌면 AI 예측도 바뀌었는가? | Seed 이동 | 입력 데이터와 후처리의 구별 |

## 9. 막혔을 때 확인할 순서

| 증상 | 우선 확인할 것 |
|---|---|
| Import 후 아무것도 안 보임 | Stage의 데이터 존재 → Faces/Volume 등 표현 생성 여부 → 선택 후 F |
| CAE 메뉴가 안 나옴 | `omni.cae.kit` 앱인지, 올바른 dataset Prim을 선택했는지 |
| 필드가 목록에 안 나옴 | 배열 소유 Prim과 Arrays, 필드 이름·association |
| 시간 이동 후 통계가 그대로임 | Array Details의 오래된 값 표시와 Refresh Details |
| 수동 범례가 다시 바뀜 | Colors의 Rescale Mode를 disable로 했는지 |
| Volume이 형상을 모두 가림 | Colormap 투명도, 표시 범위, ROI |
| Volume 일부가 사라짐 | ROI와 투명도, domain 밖 값의 처리 방식 |
| 첫 재생만 느림 | 데이터 읽기·캐시 준비 시간을 기다린 뒤 재비교 |
| 두 데이터가 맞물리지 않음 | 좌표 원점·축·단위·시간 매핑을 각각 비교 |
| 유선이 나오지 않음 | Seed가 데이터 영역 안에 있는지, Seeds·Velocities 연결과 값의 유효성 |

이 표는 진단 순서의 제안입니다. 특정 원인이나 정상 실행을 보장하는 체크리스트는 아닙니다.

## 10. 결과 기록

- 사용 앱/버전: __________
- 예제 / 입력 파일: __________
- 화면에서 확인한 필드와 association: __________
- 값의 단위와 확인 출처: __________
- 색 범위 / 시점 / ROI 또는 Seed: __________
- 변경한 설정 하나: __________
- 달라진 표시와 그대로인 원본 데이터: __________
- 이 화면만으로 판단할 수 없는 것: __________

샘플의 색 범위는 실습 시작값입니다. 자신의 데이터에 그대로 적용하기보다 통계와 단위를 먼저 확인하세요. 공식 화면과 다르면 문서 버전, 선택한 Prim, 원본 배열, 표현 설정을 순서대로 대조합니다.

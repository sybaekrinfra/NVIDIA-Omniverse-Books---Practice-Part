// 통합 강의 본문. slides에는 수업 화면, notes에는 강사용 설명을 둡니다.
export const slides=[];
const add=(part,title,type,data,notes)=>slides.push({part,title,type,...data,notes});
const table=(p,t,rows,n,foot)=>add(p,t,'table',{rows,foot},n);
const text=(p,t,lines,n,foot)=>add(p,t,'text',{lines,foot},n);
const code=(p,t,body,lines,n)=>add(p,t,'code',{code:body,lines},n);
const img=(p,t,key,lines,n)=>add(p,t,'image',{image:key,lines},n);
const exercise=(p,t,file,steps,n)=>add(p,t,'exercise',{file,steps},n);

add('COURSE','Omniverse 실습 워크숍','cover',{
 subtitle:'충북대학교 기계공학부',
 lines:['CAD와 OpenUSD','물리 설정과 Python 자동화','가상 데이터 기반 장비 상태 표시']
},'사용자 제공 Agenda에 맞춘 2일 통합 교재. 장비는 BX200L CAD 형상을 재사용하며 로봇 관절 제어는 필수 범위에 넣지 않는다. 상태 데이터는 합성 값이다. 처음부터 끝까지 슬라이드를 모두 읽기보다 실제 장면과 함께 진행한다.');
table('COURSE','2일간의 학습 순서',[
 ['구분','오전','오후'],['Day 1','UI 조작과 OpenUSD 기본','CAD 검수와 Layer 협업'],['Day 2','물리 준비와 낙하 실험','Python 자동화와 상태 시각화'],['시간','09:30–12:30, 중간 휴식 15분','13:30–17:00, 중간 휴식 15분']
],'수정 Agenda의 시간 블록을 유지한다. 하루 순수 수업 360분 중 실습 180분. 각 Part 확장 안내서에 기본/선택 실습 배분이 있다. 추가 과제를 순서대로 전부 수행하도록 요구하지 않는다.','하루 수업 6시간 중 실습 3시간. 점심 12:30–13:30.');

table('D1P1','장면을 이루는 데이터',[
 ['대상','이번 실습에서의 역할','확인할 데이터'],['CAD 장비','고정된 형상 참조','치수, 단위, 계층'],['Workpiece','떨어지는 작업물','위치, Collider, 질량'],['StatusLamp','장비 상태 표시','색, 판정 상태, 출처']
],'장비 형상과 상태 데이터의 출처를 분리해서 설명한다. 정교한 CAD가 있다고 상태까지 실제 값인 것은 아니다. 완성 예시 04_status를 보여준 후 01_layout으로 돌아온다.');
exercise('D1P1','첫 장면 열기','checkpoints/01_layout.usda',[
 'Stage에서 Equipment, Workpiece, StatusLamp를 찾습니다.',
 'Viewport에서 /World/Camera를 선택합니다.',
 '각 객체가 형상·물리·상태 중 무엇을 담당하는지 적습니다.'
],'학습자가 보이는 객체와 경로를 연결하면 완료한다. 경로가 끊어지면 저장소 전체를 받았는지 확인한다. 실제 PLC나 센서는 연결하지 않는다고 명확히 설명한다.');

img('D1P2','화면에서 확인하는 세 영역','ui',[
 'Viewport: 장면을 보고 선택합니다.',
 'Stage: 객체와 계층을 찾습니다.',
 'Property: 선택 객체의 값을 읽고 바꿉니다.'
],'이미지는 기존 교육 교재의 UI 예시다. 왼쪽 도구 막대와 아래 Content도 짚는다. 교육장 앱 버전에 따라 패널 위치와 메뉴 이름은 다를 수 있다. 실제 실습은 01 장면에서 한다.');
img('D1P2','선택한 객체와 Prim 경로','stage',[
 '이름이 비슷해도 전체 경로는 다를 수 있습니다.',
 '/World/Workpiece를 선택합니다.',
 '선택 표시와 Property 대상이 같은지 확인합니다.'
],'원본 화면의 Prim 이름은 교육 공통 장면과 다르다. UI 구조를 설명하는 예시로 사용하고 실제 경로를 별도로 읽게 한다. Viewport 선택이 어려우면 Stage에서 선택하게 한다.');
img('D1P2','이동·회전·크기 변경','transform',[
 '이동은 Translate를 바꿉니다.',
 '회전은 좌표계와 중심점을 함께 봅니다.',
 'Scale과 카메라 확대는 다릅니다.'
],'키보드 단축키가 입력 창에 포커스되어 있으면 다른 동작을 할 수 있으니 Viewport 포커스를 확인한다. 화면 크기 대신 숫자 변화로 조작 결과를 검증한다.');
exercise('D1P2','카메라 이동과 객체 이동 비교','checkpoints/01_layout.usda',[
 'Workpiece의 초기 위치 (1, 0, 1.5)를 기록합니다.',
 '카메라만 움직인 뒤 위치 값이 같은지 확인합니다.',
 'Translate X를 1.5로 바꾸고 Undo합니다.',
 'Size=1, Scale=0.2에서 한 변의 길이를 계산합니다.'
],'정답: 한 변 0.2m. 카메라만 움직이면 객체의 Translate는 변하지 않는다. 기본 12분과 비교 활동 8분 안에서 진행한다.');

table('D1P3','Stage, Layer, Prim',[
 ['용어','담당하는 것','예'],['Stage','합성된 장면에 접근','현재 열린 교육 장면'],['Layer','의견을 저장하는 파일·단위','02_structured.usda'],['Prim','장면 내부의 객체','/World/Workpiece'],['Attribute','객체의 값','physics:mass = 1']
],'파일 하나와 Stage를 완전히 같은 개념으로 설명하지 않는다. Stage는 여러 Layer와 참조 자산을 합성할 수 있다. Attribute와 Relationship은 모두 Property에 속하지만 이번에는 Attribute 변경을 중심으로 진행한다.');
code('D1P3','공통 장면의 계층',`/World
    /Equipment       CAD Reference
    /Workpiece       Cube
    /Ground          Cube
    /StatusLamp      Sphere
    /Camera          Camera`,[
 '경로는 계층 안에서 객체를 지정합니다.',
 '같은 이름도 부모가 다르면 다른 객체입니다.'
],'이 구조는 공통 장면의 주요 Prim만 요약한 것이다. Equipment 아래에는 실제 CAD 메시와 기존 비활성 Joint가 더 있다. 전체 장면을 이 여섯 Prim만 있다고 설명하지 않는다.');
table('D1P3','파일 경로와 Prim 경로',[
 ['표현','종류','사용하는 곳'],['shared/assets/cad/BX200L-C001.usd','파일 경로','파일 열기, Reference'],['/World/Equipment','Prim 경로','객체 선택, API 조회'],['xformOp:translate','속성 이름','GetAttribute'],['training:state','사용자 정의 속성','상태 기록']
],'초급자가 가장 많이 혼동하는 부분이다. 잘못된 파일 경로를 GetPrimAtPath에 넘기면 원하는 Prim을 찾지 못한다. 코드 작성 전에 경로 세 종류를 소리 내어 읽게 한다.');
img('D1P3','타입과 속성 읽기','property',[
 'Cube는 Prim의 타입입니다.',
 'Translate는 위치 속성입니다.',
 'RigidBodyAPI는 물리 기능을 부여합니다.',
 '사용자 속성은 상태 값을 기록합니다.'
],'기존 교재의 Property 화면으로 구성을 설명한다. 실제 physics:mass는 Day 2의 03 장면에서 확인한다. 타입 이름과 적용된 API schema는 별개의 개념이다.');
table('D1P3','USD 파일과 자산 전달',[
 ['형식·항목','이해할 점'],['.usda','텍스트로 구조를 읽을 수 있음'],['.usdc','바이너리 표현'],['.usd','확장자만으로 내부 형식을 단정하지 않음'],['defaultPrim','참조 진입점으로 사용할 Prim'],['상대 경로','폴더 구조를 함께 전달해야 유지됨']
],'제공 BX200L의 defaultPrim은 World이다. defaultPrim을 지정해도 파일에 포함된 모든 최상위 Prim이 자동으로 참조되는 것은 아니다. 이 과정은 /World를 명시적으로 참조한다.');

img('D1P4','Layer와 편집 대상','layers',[
 '현재 값을 어느 Layer에 기록하는지 확인합니다.',
 '원본 형상과 검토 의견을 분리합니다.',
 '보이는 결과는 합성된 값입니다.'
],'root, session, sublayer의 역할을 구분한다. 이번 제공 예제는 root Layer에 편집하도록 되어 있다. 예기치 않은 값은 더 강한 의견이나 session 변경이 있는지 확인한다.');
table('D1P4','원본 색과 검토 색',[
 ['열 파일','ReferencePart','원본 part.usda'],['assembly.usda','청록색','청록색 유지'],['review.usda','빨간색','청록색 유지'],['review 색 수정','보라색으로 변경 가능','원본 수정 없음']
],'실제 파일의 primvars:displayColor를 비교한다. 원본 파일이 바뀌지 않았는데 합성된 결과가 바뀌는 것이 핵심이다. 모든 합성 우선순위를 파일 순서 하나로 단순화하지 않는다.');
img('D1P4','Reference로 자산 재사용','reference',[
 '대상 Prim에 외부 USD를 연결합니다.',
 '원본 형상과 재질을 재사용합니다.',
 '배치와 검토 값은 상위에서 작성합니다.'
],'이미지의 예제 이름과 공통 장면 이름을 구별한다. 공통 장면의 Equipment Reference 경로를 실제로 확인한다. 원본 의존 파일을 함께 관리해야 한다.');
img('D1P4','Payload의 로드와 언로드','payload',[
 '로드 여부를 명시적으로 바꿉니다.',
 '언로드는 원본 파일 삭제가 아닙니다.',
 '현재 장면의 데이터 로드를 조절합니다.'
],'공통 단순 예제 assembly에서 /World/PayloadPart를 Unload와 Load한다. GUI가 다르면 Usd.Stage.Unload/Load로 확인한다. Visibility를 끄는 것과 데이터 unload는 다르다.');
table('D1P4','배치 대안을 Variant로 보관',[
 ['layout 선택','Tray_1 X','Tray_3 X','두 중심의 거리'],['compact','0.40m','1.30m','0.90m'],['wide','0.40m','2.10m','1.70m']
],'05_layout_variants에 두 배치가 담겨 있다. 거리는 통로 유효 폭이나 안전 거리 인증값이 아니라 트레이 중심 간 X 차이다. local opinion이 Variant 값을 가릴 수 있다는 선택 질문을 덧붙인다.');
exercise('D1P4','배치 선택과 변경 의견 확인','05_layout_variants.usda / 07_layout_variant.py',[
 'compact와 wide를 차례로 선택합니다.',
 'Tray_1과 Tray_3의 좌표를 비교합니다.',
 '필요한 작업 공간과 배치 밀도를 설명합니다.',
 '원본 파일 복제 없이 두 안을 보관한 방법을 적습니다.'
],'필수 목표는 두 Variant 전환과 수치 확인이다. 추가 논의는 실제 기계 안전 기준 적용으로 확대하지 않는다. 결과 화면과 좌표 표를 제출한다.');

table('D1P5','CAD에서 장면까지',[
 ['단계','작업','확인할 결과'],['Import','STP를 USD로 변환','형상과 조립 계층'],['검수','축·단위·크기 비교','기준 치수와 일치'],['배치','래퍼 Xform에 Reference','원본과 배치 분리'],['활용','측정·단면·피벗 조작','설계 검토 질문에 답하기']
],'CAD Converter가 준비되면 직접 Import하고, 없으면 제공된 기변환 USD로 진행한다. 교육생 기록에 실제 변환 여부를 남긴다. 앱에 해당 메뉴가 항상 존재한다고 안내하지 않는다.');
table('D1P5','단위 표기와 실제 크기',[
 ['항목','정상 장면','오류 장면'],['metersPerUnit','1','1'],['Equipment Scale','1, 1, 1','0.001, 0.001, 0.001'],['장비 높이','약 2.108m','약 0.002108m'],['진단','기준 크기와 비교','Scale 원인 확인']
],'10_fault_units는 metadata가 정상이어도 geometry 크기가 잘못될 수 있음을 보여준다. 원본 도면의 측정 방향과 바운드 방향을 구별한다. 바운드 높이는 정밀 CAD 치수 검증을 대체하지 않는다.');
img('D1P5','Measure로 확인할 값','measure',[
 '측정 대상과 방향을 먼저 정합니다.',
 '화면상 크기 대신 숫자로 비교합니다.',
 '기준 치수와 단위를 함께 기록합니다.'
],'도구 사용이 불가능하면 01_inspect_stage의 BBox 출력으로 대체한다. 실제 도면 치수와 단순 바운드가 반드시 같은 대상은 아니다. 측정 결과의 범위를 설명한다.');
img('D1P5','Section으로 내부 구조 보기','section',[
 '단면 위치와 방향을 바꿉니다.',
 '가려진 내부를 관찰합니다.',
 '표시 효과와 원본 형상 변경을 구별합니다.'
],'기존 교재의 실제 도구 화면을 활용한다. 교실 앱에 Section이 없으면 강사 시연으로 한정하고 CAD 단위 검수 시간을 늘린다.');
img('D1P5','Pivot과 회전 중심','pivot',[
 '회전 전에 중심 위치를 확인합니다.',
 '복사본에서 회전 차이를 관찰합니다.',
 '실습 후 Undo로 초기 상태를 복구합니다.'
],'초급 과정에서는 CAD 내부 변환 스택을 자동 정규화하지 않는다. 래퍼 Xform이나 제공 도구로 회전 중심 개념만 확인한다. 이후 확장 안내서의 단위 오류 미션을 진행한다.');

table('D1P6','Layer별 담당 역할',[
 ['담당','수정할 파일','책임 범위'],['자산 담당','part.usda','형상과 기본 색'],['배치 담당 A','assembly.usda','객체 배치'],['검토 담당 B','review.usda','검토 색과 의견'],['공동 확인','review를 다시 열기','최종 합성 결과']
],'동일 파일을 두 사람이 동시에 덮어쓰지 않는 간단한 분업부터 시작한다. 같은 속성을 수정했을 때와 다른 속성을 수정했을 때의 결과를 비교한다.');
text('D1P6','Nucleus에서 확인할 것',[
 ['연결','기관이 준비한 서버 주소와 개인 계정'],
 ['권한','교육용 경로의 읽기·쓰기 범위'],
 ['공유','의존 폴더 전체 업로드와 다른 계정의 재열기'],
 ['Live','앱과 서버에서 검증한 경우에만 시연']
],'Nucleus Workstation과 Launcher는 2025-10-01 폐기되었다. 신규 Workstation 설치를 요구하지 않는다. 서버가 없으면 로컬 Layer 분업을 진행하고 이를 Nucleus Live 실습이라고 부르지 않는다. 출처 https://developer.nvidia.com/omniverse/legacy-tools');
exercise('D1P6','두 사람이 하나의 장면 검토','shared/assets/usd_basics 폴더 전체 복사',[
 'A는 assembly에서 ReferencePart의 위치를 바꿉니다.',
 'B는 review에서 색을 바꿉니다.',
 'review를 다시 열어 두 변경을 확인합니다.',
 '폴더를 옮긴 뒤 상대 참조가 유지되는지 확인합니다.'
],'해당 Part 기본 32분+확장20분 안에서 진행한다. 실습 결과가 충분하면 별도 서버 구축이나 복잡한 동시 편집을 추가하지 않는다.');
table('D1P6','첫날 결과 점검',[
 ['확인 질문','통과 증거'],['카메라와 객체 이동을 구별하는가?','Property 값 비교'],['파일과 Prim 경로를 구별하는가?','경로 분류표'],['원본과 override를 구별하는가?','색·위치 합성 결과'],['CAD 크기가 적절한가?','단위·축·바운드 기록'],['다른 위치에서도 열리는가?','폴더 전체 재열기']
],'Q&A와 결과 점검은 마지막 Part 배정 시간 안에 포함한다. Day 2에는 새 체크포인트를 제공하므로 첫날 편집에 실패해도 계속 진행할 수 있다.');

add('DAY 2','물리 설정과 Python 자동화','section',{
 lines:['작업물 낙하를 준비하고 조건을 비교합니다.','Python으로 반복 작업을 실행합니다.','가상 데이터로 장비 상태를 표시합니다.']
},'Day 1 구조와 파일 경로를 짧게 복습한다. 학습자가 첫날 파일을 손상시켰다면 제공된 02 또는 03 체크포인트를 사용한다.');
table('D2P1','이번 실험의 준비 조건',[
 ['항목','기준'],['단위 / 축','meter / Z-up'],['작업물','한 변 0.2m, 중심 높이 1.5m'],['질량 / 중력','1kg / 9.81m/s², -Z'],['바닥','윗면 z=0, 정적 Collider'],['CAD 장비','형상 참조, 기존 물리 비활성']
],'SimReady는 목적에 맞는 준비 상태라는 점을 강조한다. 여기서는 작은 작업물과 바닥 접촉만 다룬다. 산업 장비 전체 검증이나 인증을 의미하지 않는다.');
code('D2P1','준비도 결과 읽기',`PASS   meter/Z-up
PASS   equipment_height_1_to_3m
CHECK  physics_scene
CHECK  workpiece_collider
CHECK  workpiece_rigid_body
CHECK  positive_mass
CHECK  ground_collider`,[
 '02_structured의 예상 정적 검사 결과입니다.',
 '03_physics에서는 같은 항목을 다시 확인합니다.'
],'08_check_readiness는 코드에 정한 조건만 검사한다. CHECK가 항상 파일 손상이라는 의미는 아니며 아직 설정하지 않은 단계일 수 있다. 런타임 Play 결과는 따로 관찰한다.');
exercise('D2P1','설정 전후를 진단표로 비교','02_structured.usda / 03_physics.usda',[
 '각 장면에서 08_check_readiness.py를 실행합니다.',
 'CHECK가 PASS로 바뀐 항목을 찾습니다.',
 '추가된 물리 속성과 진단 결과를 연결합니다.'
],'전환 기호는 실행 순서를 뜻한다. 교육생에게 결과를 복사하게만 하지 말고 어떤 API나 값 때문에 통과했는지 설명하게 한다.');

code('D2P2','시각 장비와 동적 작업물',`/World
    /Equipment       시각 참조
        /link0 ...   CAD 원본 계층
    /Workpiece       동적 강체
    /Ground          정적 충돌
    /StatusLamp      상태 표시`,[
 '물리 기능은 역할을 정한 대상에 적용합니다.',
 'CAD 내부 계층은 원본과 함께 관리합니다.'
],'제공 CAD에는 관절 및 강체 API가 이미 포함되어 있었다. 01_layout local override가 이를 제거하고 Joint를 비활성화한다. 03에서 활성 Rigid Body는 Workpiece 하나다.');
table('D2P2','원본과 수업 장면의 차이',[
 ['구분','제공 CAD USD','공통 수업 장면'],['기계 형상','원본 메시','Reference로 재사용'],['로봇 강체·관절','기존 설정 포함','상위 의견으로 비활성화'],['낙하 대상','로봇 제어 범위와 연관','별도 Workpiece'],['편집 위치','원본 보존','수업용 Layer']
],'원본을 직접 열면 공통 장면과 물리 상태가 다르다. 이를 숨기지 않고 사례로 활용한다. 범용 API 일괄 적용을 피하고 정확한 대상 경로를 확인하게 한다.');
exercise('D2P2','역할별 Hierarchy 검토','checkpoints/03_physics.usda',[
 'Equipment의 Reference 경로를 확인합니다.',
 'Workpiece가 장비의 자식이 아닌 이유를 설명합니다.',
 '물리 대상과 표시 대상을 구분한 계층도를 적습니다.'
],'이번 장면에서 Workpiece는 Equipment의 변환에 끌려가지 않도록 독립 배치했다. 실제 설비 설계마다 계층은 달라질 수 있으므로 하나의 정답 계층으로 일반화하지 않는다.');

table('D2P3','물리 속성의 역할',[
 ['설정','담당하는 것','이번 장면'],['Collider','접촉 형상','작업물과 바닥'],['Rigid Body','동역학 운동','작업물'],['Mass','질량','1kg 또는 5kg'],['PhysicsScene','중력 등 장면 설정','-Z, 9.81m/s²']
],'보이는 Mesh와 충돌 형상은 별개이며 Collider만 있다고 중력으로 움직이지 않는다. 바닥에는 Rigid Body를 적용하지 않는다. 관성은 단순 Cube의 자동 계산을 사용한다.');
table('D2P3','A, B, C의 초기 조건',[
 ['작업물','질량','중심 높이','바꾸는 조건'],['A','1kg','1.5m','기준'],['B','5kg','1.5m','질량'],['C','1kg','2.5m','초기 높이']
],'06_physics_comparison은 세 Cube를 독립 경로에 둔다. A/B에서는 질량만, A/C에서는 높이만 달라진다. 모두 한 변 0.2m이며 바닥 z=0이다.');
text('D2P3','자유낙하에서 예상할 결과',[
 ['A와 B','공기 저항 없는 동일 중력에서 가속도는 같습니다.'],
 ['A와 C','초기 높이가 높은 C의 낙하 시간이 더 깁니다.'],
 ['관찰 한계','렌더 프레임만으로 정확한 접촉 시간을 측정하지 않습니다.']
],'선택 계산: 바닥 접촉까지 중심 이동은 z0-0.1이고 t=sqrt(2d/g). 1.5m는 약0.534초, 2.5m는 약0.700초의 이상값이다. 접촉 여유와 시간 간격은 관찰 결과에 영향을 준다.');
exercise('D2P3','예측한 뒤 Play','checkpoints/06_physics_comparison.usda',[
 '재생 전에 도착 순서를 적습니다.',
 'A/B와 C의 낙하를 비교합니다.',
 'Stop 후 같은 조건으로 다시 확인합니다.',
 '예측과 관찰이 다른 경우 측정 방법부터 검토합니다.'
],'색만으로 질량을 외우게 하지 말고 Prim 이름 A/B/C와 Mass 값을 함께 확인한다. 단일 화면 관찰을 정량적인 물리 검증으로 과장하지 않는다.');

code('D2P4','강체와 충돌 설정',`obj = stage.GetPrimAtPath("/World/Workpiece")
UsdPhysics.CollisionAPI.Apply(obj)
UsdPhysics.RigidBodyAPI.Apply(obj)
UsdPhysics.MassAPI.Apply(obj).CreateMassAttr(1.0)`,[
 '02_apply_physics.py의 주요 부분입니다.',
 '바닥에는 CollisionAPI만 적용합니다.'
],'강사가 GUI와 API 속성을 연결한다. 이 짧은 코드는 전체 장면 생성 코드가 아니며 이미 열린 stage가 필요하다. 실행용 파일은 00 다음 02를 사용한다.');
table('D2P4','증상에서 설정 찾기',[
 ['증상','먼저 확인할 항목'],['작업물이 그대로 있음','Rigid Body 활성, Play, PhysicsScene'],['작업물이 바닥을 통과함','Ground Collider와 collisionEnabled'],['장비도 움직임','기존 CAD 물리와 활성 대상'],['재실행 초기 위치가 다름','Pause와 Stop의 차이, 초기 속성']
],'11_fault_collision은 API를 제거하지 않고 활성값을 False로 했다. 스키마 존재와 활성 상태를 함께 검사하도록 유도한다.');
exercise('D2P4','바닥 통과 오류 복구','checkpoints/11_fault_collision.usda',[
 '짧게 재생하고 증상을 관찰한 뒤 Stop합니다.',
 '08_check_readiness.py에서 Ground 항목을 확인합니다.',
 'physics:collisionEnabled를 True로 바꿉니다.',
 '재생하여 접촉을 다시 확인합니다.'
],'완료 증거는 수정 전 증상, 변경 속성, 수정 후 결과 세 가지다. API 적용만 반복하는 대신 비활성 속성을 직접 찾게 한다.');

table('D2P5','Python을 읽는 순서',[
 ['표현','뜻','실습 예'],['변수','값에 이름 붙이기','MASS_KG = 1.0'],['문자열','텍스트와 경로','"/World/Workpiece"'],['함수 호출','정해진 동작 실행','set_workpiece(...)'],['반복문','목록을 따라 반복','for mass in (1.0, 5.0)']
],'Python 경험이 초급이므로 실행 위치와 들여쓰기부터 설명한다. 일반 PowerShell Python에서 omni를 import하는 예제가 아니다. 00에서 모듈 경로를 준비한다.');
code('D2P5','Stage에서 값 읽기',`from cbnu_lab import current_stage
stage = current_stage()
prim = stage.GetPrimAtPath("/World/Workpiece")
position = prim.GetAttribute("xformOp:translate").Get()
print(position)`,[
 '경로로 객체를 찾고 속성을 읽습니다.',
 '출력값과 Property의 값을 비교합니다.'
],'실행 전에 03_physics를 열고 00을 실행한다. 경로를 잘못 입력했을 때 유효한 Prim인지 검사해야 함을 설명한다.');
code('D2P5','조건을 변수로 바꾸기',`HEIGHT_M = 2.0
MASS_KG = 5.0

set_workpiece(stage, height=HEIGHT_M, mass=MASS_KG)`,[
 'Stop 상태에서 값을 바꿉니다.',
 'GUI에서 높이와 질량을 다시 확인합니다.'
],'실행 파일 03_change_properties.py를 이용한다. 값 두 개를 동시에 바꾸기 전에 높이 하나, 질량 하나를 따로 바꿔 원인과 결과를 분리한다.');
code('D2P5','반복 배치의 기본 구조',`for row in range(ROWS):
    for column in range(COLUMNS):
        x = 0.5 + column * SPACING_M
        y = -1.5 + row * SPACING_M
        # 경로와 위치를 정해 작업물 생성`,[
 '행·열·간격을 입력으로 둡니다.',
 'Prim 경로와 부품 ID가 중복되지 않게 합니다.'
],'실제 생성 함수는 workshop_plus.batch_parts이다. 이 코드는 핵심 반복 구조 설명용이다. 반복 실행 시 Batch 전용 경로를 교체하는 정책을 함께 설명한다.');
exercise('D2P5','6개 작업물을 12개로 배치','07_batch_layout.usda / 09_batch_layout.py',[
 '2행×3열의 초기 개수를 확인합니다.',
 'ROWS=3, COLUMNS=4로 바꿉니다.',
 '재실행해 12개이며 이전 배열이 남지 않는지 확인합니다.',
 '경로 목록과 training:part_id를 확인합니다.'
],'Batch 예제의 객체에는 물리 API를 적용하지 않는다. 일괄 생성·식별·재실행을 배우는 예제다. 모든 새 자산을 자동 강체로 만드는 범위로 확대하지 않는다.');

text('D2P6','반복 실험의 실행 순서',[
 ['초기화','Stop 후 초기 높이와 질량을 설정합니다.'],
 ['재생','Timeline을 Play하고 앱 갱신을 기다립니다.'],
 ['기록','조건과 종료 시뮬레이션 시간을 저장합니다.'],
 ['종료','Stop으로 복구하고 다음 조건을 시작합니다.']
],'04 스크립트에서 asyncio와 await의 역할을 설명한다. 앱 업데이트 횟수와 물리 시간이 같다고 가정하지 않으며 Timeline time을 사용한다. 시간 초과와 장면 변경도 점검한다.');
code('D2P6','UI를 멈추지 않는 대기',`timeline.play()
while timeline.get_current_time() < 2.0:
    await app.next_update_async()
timeline.pause()`,[
 '앱이 화면과 이벤트를 처리하도록 기다립니다.',
 '실제 파일에는 중단·타임아웃 검사가 포함됩니다.'
],'이 코드를 독립 실행 가능한 전체 예제로 제시하지 않는다. async 함수 안에 있어야 하며 app과 timeline은 사전에 준비해야 한다. 실행은 04 파일을 이용한다.');
table('D2P6','실행 로그가 말해 주는 것',[
 ['열','의미','포함하지 않는 것'],['mass_kg','설정한 질량','힘 측정값'],['height_m','설정한 초기 높이','실시간 위치'],['simulation_time_s','종료 시뮬레이션 시간','접촉 시각'],['observation','사람이 적는 관찰','자동 판정 결과']
],'기존 스크립트는 위치/속도를 측정하지 않는다. 데이터 열 이름과 실제 의미를 일치시키는 습관이 자동화 교육의 일부다.');
exercise('D2P6','두 조건 실행과 결과 확인','03_physics.usda / 04_automate_simulation.py',[
 '1kg과 5kg 조건의 반복 실행을 관찰합니다.',
 'simulation_runs.csv의 2행을 확인합니다.',
 '관찰 결과를 별도 열에 작성합니다.',
 '취소는 06_stop_tasks.py로 확인합니다.'
],'이전 결과를 보존하려면 실행 전에 CSV 이름을 바꾸도록 안내한다. 결과 파일 생성만으로 물리 성공을 판단하지 않는다.');

table('D2P7','장비 상태를 표시하는 데이터',[
 ['데이터','단위','이번 실습'],['time_s','초','재생 시각'],['temperature_c','°C','합성 온도'],['vibration_mm_s','mm/s','합성 진동 속도'],['state','문자열','판정한 상태'],['source','문자열','SYNTHETIC_CSV']
],'이번 실습은 실제 설비 연동 없이 CSV를 읽어 USD custom 속성과 색으로 표현한다. 원본 데이터의 단위, 출처, 시각을 함께 확인한다.');
table('D2P7','상태 판정 규칙',[
 ['상태','조건','색'],['ALARM','온도 ≥ 80 또는 진동 ≥ 7','빨강'],['WARNING','ALARM이 아니며 온도 ≥ 60 또는 진동 ≥ 4','주황'],['NORMAL','나머지 유효 데이터','녹색']
],'반드시 ALARM을 먼저 판정한다. >= 경계를 테스트한다. 임계값은 교육용 가정이며 실제 설비 안전 기준이 아니다.','교육용 임계값입니다. 실제 설비 기준에 적용하지 않습니다.');
add('D2P7','가상 온도와 판정 경계','chart',{
 categories:['0','1','2','3','4','5','6','7'],
 series:[{name:'온도 °C',values:[35,48,60,68,80,75,55,40],color:'#25634B'},{name:'주의 경계',values:[60,60,60,60,60,60,60,60],color:'#B57621'},{name:'경보 경계',values:[80,80,80,80,80,80,80,80],color:'#B33D38'}],
 foot:'가로축: time_s(초). 합성 데이터이며 진동 조건도 별도로 판정합니다.'
},'shared/data/equipment_status.csv의 실제 제공값을 차트에 반영했다. 5초는 온도가80 미만이지만 진동이7이므로 ALARM이다. 온도 그래프만으로 전체 상태를 판정하지 않는다.');
table('D2P7','여러 장비에서 만나는 데이터 문제',[
 ['상황','표시','예'],['유효한 최신 값','NORMAL / WARNING / ALARM','온도·진동 판정'],['값이 비어 있음','UNKNOWN, 회색','2초 E03'],['샘플이 3초보다 오래됨','STALE, 청회색','6초 E02'],['재수신한 유효 값','다시 판정','4초 E03']
],'UNKNOWN을 0으로 채우지 않는다. 예제는 현재 시각-샘플 시각>3초일 때 STALE이며 정확히3초는 유효하다. 한 상태 코드로 데이터 품질을 먼저 표현하는 단순 교육 모델이다.');
exercise('D2P7','세 장비의 상태 재생','08_multi_equipment.usda / 10_multi_equipment.py',[
 'E01, E02, E03의 표시구를 확인합니다.',
 '2초 UNKNOWN과 6초 STALE을 찾습니다.',
 'multi_equipment_report.csv의 12행을 확인합니다.',
 '마지막 상태: E01 정상, E02 지연, E03 경보.'
],'세 장비의 Housing은 코드로 만든 단순 형상이다. 실제 CAD를 세 번 복제한 장면은 아니다. CAD 장비와 상태 표시의 분리 개념을 재사용한다. 결과 USD와 CSV를 함께 제출한다.');
table('D2P7','선택 실습: 온도 분포 비교',[
 ['항목','baseline','hotspot'],['면 개수','24','24'],['가상 온도 범위','30–45°C','30–95°C'],['고정 범례','20–100°C','20–100°C'],['표현','면별 displayColor','동일 면에 다른 값']
],'09_thermal_field와 11_thermal_field를 사용한다. uniform interpolation으로 면당 한 색을 기록한다. 이 데이터는 CAE solver 결과가 아닌 합성 field이다. 두 그림의 범례를 다르게 잡으면 시각적 비교가 왜곡될 수 있다.','합성 온도 분포입니다. CAE 해석·실제 센서 측정은 수행하지 않습니다.');
exercise('D2P7','팀별 미니 프로젝트','기본 상태 재생 후 두 경로 중 하나 선택',[
 '운영 팀: 3개 장비의 결측·지연 상태를 설명합니다.',
 '해석 시각화 팀: 두 온도 분포를 같은 범례로 비교합니다.',
 '입력 파일, 변경 코드, 결과 화면을 함께 제출합니다.',
 '실제 현장 데이터로 바꿀 때 필요한 조건을 발표합니다.'
],'두 경로를 모두 수행하지 않는다. 기존 단일 장비 실습30분+선택확장22분의 실습 시간 안에서 진행한다. 역할은 데이터 담당, USD 담당, 검증 담당으로 나누되 소규모 팀은 겸임한다.');

table('REVIEW','최종 결과의 검토 기준',[
 ['검토 항목','확인할 증거'],['USD 구조','경로와 의존 파일, 재열기'],['물리','설정 값과 낙하 관찰'],['Python','입력 변수와 반복 실행 결과'],['상태 표시','수치·판정·색·출처 일치'],['설명','가정, 검증한 범위, 남은 한계']
],'각2점 총10점을 교육용 제안으로 사용할 수 있다. 학교 공식 평가 기준이 아니다. CAD Converter와 Nucleus 준비 여부는 교육생 감점 사유가 아니다.');
text('REVIEW','제출 파일과 다음 단계',[
 ['제출','최종 USD, 사용한 CSV, 코드 변경점, 결과 화면'],
 ['재현','초기 장면과 실행 순서를 함께 기록'],
 ['확장','실제 데이터 형식·단위·주기·장비 ID 정의'],
 ['검증','형상, 물리 모델, 데이터 품질을 각각 확인']
],'마지막에 각 팀이 무엇을 직접 확인했는지 말하게 한다. 실제 설비 연동, ROS2, 로봇 관절 제어, CAE solver 연계는 후속 교육 범위로 안내한다.');

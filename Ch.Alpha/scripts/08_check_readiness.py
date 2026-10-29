import omni.usd
from workshop_plus import readiness
s=omni.usd.get_context().get_stage()
for name,passed in readiness(s):
    print("PASS" if passed else "CHECK",name)
print("교육용 조건 점검이며 SimReady 인증 결과가 아닙니다.")

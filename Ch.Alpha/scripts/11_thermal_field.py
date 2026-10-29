import omni.usd
from cbnu_lab import ROOT
from workshop_plus import apply_thermal
s=omni.usd.get_context().get_stage()
DATASET="thermal_hotspot.csv"  # thermal_baseline.csv / thermal_hotspot.csv
LEGEND_MIN_C=20
LEGEND_MAX_C=100
assert DATASET in ("thermal_baseline.csv","thermal_hotspot.csv")
print("가상 온도 범위:",apply_thermal(s,ROOT/"shared/data"/DATASET,LEGEND_MIN_C,LEGEND_MAX_C))
print("교육용 합성 분포입니다. CAE 해석 결과가 아닙니다.")

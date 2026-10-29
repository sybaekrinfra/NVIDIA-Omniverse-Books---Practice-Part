import omni.usd
s=omni.usd.get_context().get_stage()
v=s.GetPrimAtPath("/World").GetVariantSets().GetVariantSet("layout")
assert v and v.GetVariantNames(), "05_layout_variants.usda를 여세요."
LAYOUT="wide"  # compact / wide
assert LAYOUT in v.GetVariantNames()
v.SetVariantSelection(LAYOUT)
print("layout:",v.GetVariantSelection())

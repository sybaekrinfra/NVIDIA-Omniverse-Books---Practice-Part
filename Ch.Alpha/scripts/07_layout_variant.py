"""Script Editor에서 이 파일 전체를 실행하세요. 초기화 스크립트가 필요 없습니다."""

def main():
    import omni.usd
    import omni.timeline

    s=omni.usd.get_context().get_stage()
    assert s, "실습 장면을 먼저 여세요."
    v=s.GetPrimAtPath("/World").GetVariantSets().GetVariantSet("layout")
    assert v and v.GetVariantNames(), "05_layout_variants.usda를 여세요."
    LAYOUT="wide"  # compact / wide
    assert LAYOUT in v.GetVariantNames()
    v.SetVariantSelection(LAYOUT)
    print("layout:",v.GetVariantSelection())


main()

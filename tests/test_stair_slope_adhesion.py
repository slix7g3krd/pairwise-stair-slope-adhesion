import pytest
import gameplay.stair_slope_adhesion as mod

CASES = [
    ("raycast_highest", (1,)),
    ("step_threshold_actual", (1,)),
    ("result_frame_tag", (1,)),
    ("normal_from_physics", (1,)),
    ("correction_tolerance", (1,)),
    ("slope_clamp_speed", (1,)),
    ("step", (1,)),
    ("adhere", (1,)),
    ("correct", (1,)),
    ("sync", (1,)),
    ("validate_controller", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None

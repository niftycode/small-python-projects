from main import calculate_bmi


def test_calculate_bmi_under_weight(under_weight, under_height, capsys):
    calculate_bmi(under_weight, under_height)
    captured = capsys.readouterr().out.rstrip()
    assert captured == "Underweight"


# @pytest.mark.skip(reason="no test available")
def test_calculate_bmi_normal_weight(normal_weight, normal_height, capsys):
    calculate_bmi(normal_weight, normal_height)
    captured = capsys.readouterr().out.rstrip()
    assert captured == "Normal weight"


def test_calculate_bmi_overweight(over_weight, over_height, capsys):
    calculate_bmi(over_weight, over_height)
    captured = capsys.readouterr().out.rstrip()
    assert captured == "Overweight"

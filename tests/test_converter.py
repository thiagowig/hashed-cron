import pytest
import pathlib
import sys

PACKAGE_PARENT = pathlib.Path(__file__).parent.parent
sys.path.append(str(PACKAGE_PARENT))

from hashed_cron import cron_converter


@pytest.mark.parametrize(
    "cron, identifier, expected_result",
    [
        ("5 4 * * *", "job_01", "5 4 * * *"),
        ("5 4 1 1 1", "job_01", "5 4 1 1 1"),
        ("H * * * *", "job_01", "41 * * * *"),
        ("H H * * *", "job_01", "41 5 * * *"),
        ("H * * * *", "job_02", "16 * * * *"),
        ("H H * * *", "job_02", "16 4 * * *"),
        ("H H 2 * *", "job_02", "16 4 2 * *"),
        ("H H 1 1 1", "job_02", "16 4 1 1 1"),
        ("H H H 1 1", "job_02", "16 4 4 1 1"),
        ("H H H H 1", "job_02", "16 4 4 5 1"),
        ("H H H H H", "job_02", "16 4 4 5 5"),
        ("H/30 * * * *", "job_02", "16/30 * * * *"),
        ("H/10 H/3 * * *", "job_02", "6/10 1/3 * * *"),
        ("H/10 H/3 0/2 * *", "job_02", "6/10 1/3 0/2 * *"),
        ("H/30 * * * *", "job_03", "12/30 * * * *"),
        ("H/10 * * * *", "job_04", "6/10 * * * *"),
        (None, "job_01", None),
        ("", "job_02", None),
        ("H", "job_03", None),
        ("H H ", "job_04", None),
        ("H H H H", "job_05", None),
        ("1", "job_06", None),
        ("1 2", "job_07", None),
        ("1 2 3 ", "job_08", None),
        ("1 2 3 4", "job_09", None),
        ("0 12 * * ? *", "job_01", "0 12 * * ? *"),
        ("5,35 14 * * ? *", "job_01", "5,35 14 * * ? *"),
        ("15 10 ? * 6L 2019-2022", "job_01", "15 10 ? * 6L 2019-2022"),
        ("H H * * ? *", "job_01", "41 5 * * ? *"),
        ("H H ? * H *", "1234567", "32 20 ? * 3 *")
    ]
)
def test_generate_cron(cron, identifier, expected_result):
    result = cron_converter.convert(cron, identifier)
    assert result == expected_result


import pytest
import pathlib
import sys

PACKAGE_PARENT = pathlib.Path(__file__).parent.parent
sys.path.append(str(PACKAGE_PARENT))

from hashed_cron import cron_converter


@pytest.mark.parametrize(
    "cron, identifier, expected_result",
    [
        ("H H/2 * * *", "job_3", "5 4 * * *")
    ]
)
def test_generate_cron(cron, identifier, expected_result):
    result = cron_converter.convert(cron, identifier)
    assert result == expected_result

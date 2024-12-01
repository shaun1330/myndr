from datetime import datetime

import pytest
from django.core.exceptions import ValidationError
from app.models import validate_crontab, Task, TaskRecord


def test_validate_crontab_success():
    validate_crontab("* * * * *")

def test_validate_crontab_failure():
    with pytest.raises(ValidationError):
        validate_crontab("not a crontab string")


@pytest.fixture()
def test_task():
    task = Task.objects.create(name="test_task")
    yield task
    task.delete()


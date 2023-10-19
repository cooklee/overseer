import pytest
from django.contrib.auth.models import User, Permission

from tracker.models import Resource, Task


@pytest.fixture
def user():
    u = User.objects.create(username='ala')
    return u

@pytest.fixture
def user_with_permission(user):
    p = Permission.objects.get(codename='view_task')
    user.user_permissions.add(p)
    return user

@pytest.fixture
def zasob():
    r = Resource.objects.create(
        name='ala',
        description='ma',
        price=100
    )
    return r

@pytest.fixture
def task_without_permission(user):
    t = Task.objects.create(
        name='CodersLab',
        description='abc',
        owner=user
    )
    return t

@pytest.fixture
def task(user_with_permission):
    t = Task.objects.create(
        name='CodersLab',
        description='abc',
        owner=user_with_permission
    )
    return t



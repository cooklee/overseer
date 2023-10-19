import pytest
from django.test import Client
from django.urls import reverse

from tracker.models import Resource, Task


def test_index_view():
    client = Client() #symuluj przeglądarke
    url = reverse('index') #pobierz url na który masz wejsc
    response = client.get(url) # wpisz w adres przegladarki symulowanej
                               # pobranego url'a
    assert response.status_code == 200 # sprawdzamy czy widok zwrocił kod 200
    assert response.context['date'] == 'dupa na kiju'


@pytest.mark.django_db
def test_detail_resource(zasob):
    client = Client()
    url = reverse('detail_resource', args=(zasob.id, ))
    response = client.get(url)
    assert response.status_code == 200
    assert zasob == response.context['object']


@pytest.mark.django_db
def test_create_resource_get():
    client = Client()
    url = reverse('add_resource')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_resource_post():
    client = Client()
    url = reverse('add_resource')
    data = {
        'name':'ala23',
        'description':'jajkon',
        'price':123
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Resource.objects.get(**data)

@pytest.mark.django_db
def test_update_resource_get(zasob):
    client = Client()
    url = reverse('update_resource', args=(zasob.id, ))
    response = client.get(url)
    assert response.status_code == 200
    assert zasob == response.context['object']


@pytest.mark.django_db
def test_update_resource_post(zasob):
    client = Client()
    url = reverse('update_resource', args=(zasob.id, ))
    data = {
        'name': 'ala23',
        'description': 'jajkon',
        'price': 123
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Resource.objects.get(**data)


@pytest.mark.django_db
def test_add_task_not_login():
    client = Client()
    url = reverse('add_task')
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_add_task_login(user):
    client = Client()
    client.force_login(user)
    url = reverse('add_task')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_task_login(user):
    client = Client()
    client.force_login(user)
    data = {
        'name':'ala',
        'description':'ala'
    }
    url = reverse('add_task')
    response = client.post(url,data )
    assert response.status_code == 302
    assert Task.objects.get(**data, owner=user)

@pytest.mark.django_db
def test_task_detail_not_login(task):
    client = Client()
    url = reverse('task_detail', kwargs={'id':task.id})
    response = client.get(url)
    assert response.status_code == 302
    assert response.url.startswith(reverse('login'))

@pytest.mark.django_db
def test_add_task_login_without_permission(task_without_permission):
    client = Client()
    client.force_login(task_without_permission.owner)
    url = reverse('task_detail', kwargs={'id':task_without_permission.id})
    response = client.get(url)
    assert response.status_code == 403

@pytest.mark.django_db
def test_add_task_login(task):
    client = Client()
    client.force_login(task.owner)
    url = reverse('task_detail', kwargs={'id':task.id})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_add_task_login_post(task):
    client = Client()
    client.force_login(task.owner)
    url = reverse('task_detail', kwargs={'id':task.id})
    data = {
        'name': 'ala',
        'description': 'ala'
    }
    response = client.post(url, data)
    assert response.status_code == 302
    assert Task.objects.get(**data, parent=task, owner=task.owner)


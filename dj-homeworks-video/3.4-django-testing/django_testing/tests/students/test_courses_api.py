# def test_example():
#     assert False, "Just test example"
import random

import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture
def url():
    return reverse('courses-list')


@pytest.mark.django_db
def test_api(client, url):
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_one_list_courses(client, url, course_factory):
    courses = course_factory(_quantity=10)
    assert len(courses) == len(client.get(url).json())
    for j in range(len(courses)):
        response = client.get(f'{url}{courses[j].id}/')
        assert response.status_code == 200
        data = response.json()
        # assert isinstance(data, dict)
        assert data['id'] == courses[j].id


@pytest.mark.django_db
def test_filter_id_courses(client, url, course_factory):
    courses = course_factory(_quantity=20)
    num = random.randrange(len(courses))
    param = {'id': num}
    response = client.get(url, param=param)
    assert response.status_code == 200
    data = response.json()
    assert data[num]['id'] == courses[num].id


@pytest.mark.django_db
def test_filter_name_courses(client, url, course_factory):
    courses = course_factory(_quantity=20)
    num = random.randrange(len(courses))
    param = {'name': (name := courses[num].name)}
    response = client.get(url, param=param)
    assert response.status_code == 200
    data = response.json()
    assert data[num]['name'] == name


# Вариант тестирования создания и фильтра по id одновременно
@pytest.mark.django_db
def test_create_course(client, url):
    new_course = 'Python'
    count = Course.objects.count()
    response = client.post(url, dict(name=new_course))
    assert response.status_code == 201
    assert count + 1 == Course.objects.count()
    param = {'id': '1'}
    resp_course_name = client.get(url, param=param)
    data = resp_course_name.json()
    assert data[0]['name'] == new_course


@pytest.mark.django_db
def test_update_course(client, url, course_factory):
    course = course_factory(_quantity=1)
    assert len(course) == 1
    new_name = 'Java'
    course_id = course[0].id
    response = client.put(f'{url}{course_id}/', dict(name=new_name))
    assert response.status_code == 200
    course_name_in_db = Course.objects.get(id=course_id).name
    assert course_name_in_db == new_name


@pytest.mark.django_db
def test_delete_course(client, url, course_factory):
    course = course_factory(_quantity=1)
    course_id = course[0].id
    response = client.delete(f'{url}{course_id}/')
    assert response.status_code == 204
    course = Course.objects.filter(id=course_id)
    assert len(course) == 0

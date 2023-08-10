from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial
# Create your tests here.

def test_homepage_access():
    url = reverse('home')
    assert url == "/"


"""# The decorator @pytest.mark.django_db is used to allow this test access to the connected database,
# which is required by this particular view. 
@pytest.mark.django_db
# This test verifies that we are able to successfully create a Tutorial object in the database.
def test_create_tutorial():
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    assert tutorial.title == 'Pytest'
"""


@pytest.fixture
def new_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True 
    )
    return tutorial


def test_search_tutorials(new_tutorial):
    assert Tutorial.objects.filter(title='Pytest').exists()


def test_update_tutorial(new_tutorial):
    new_tutorial.title = 'Pytest-Django'
    new_tutorial.save()
    assert Tutorial.objects.filter(title='Pytest-Django').exists()


@pytest.fixture
def another_tutorial(db):
    tutorial = Tutorial.objects.create(
        title='More-Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return tutorial

# The .pk attribute in the Django ORM refers to the primary key of a database object, 
# which is automatically generated when it is created.
# Thus, this is simply asserting that the two objects are not the same as each other. 
def test_compare_tutorials(new_tutorial, another_tutorial):
    assert new_tutorial.pk != another_tutorial.pk
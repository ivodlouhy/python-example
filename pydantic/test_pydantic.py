from pydantic import BaseModel

def test_assert_is_visible_no_wait():

    class Dog(BaseModel):
        name: str
        age: int
        breed: str

    dog = Dog(name='Pluto', age=5, breed='Retriever')
    assert dog.name == 'Pluto'


def test_assert_is_visible_wait_sleep():
    dog = {
        'name': 'Pluto',
        'age': 5,
        'breed': 'Retriever'
    }
    assert dog['name'] == 'Pluto'
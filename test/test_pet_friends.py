import os.path

from api import PetFriends
from settings import valid_email, valid_password

pf= PetFriends()

def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """тест на получение api key"""
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result
def test_get_all_pets_with_valid_key(filter=''):
    """тест на получение списка питомцев"""
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.get_list_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets'])>0
def test_add_pets_with_valid_data(name='Страшило', animal_type='ужас',
                                  age='5678', pet_photo='image\img1.jpg'):
    """тест на добавление питомца"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pets(auth_key, name, animal_type, age, pet_photo)
    print( status)
    assert status == 200



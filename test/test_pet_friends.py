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
                                  age='5678', pet_photo='image\img2.jpg'):
    """тест на добавление питомца"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pets(auth_key, name, animal_type, age, pet_photo)
    print('statu : ', status)
    assert status == 200
    assert result['name'] == name
def test_delete_pets():
    """удление питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key,"my_pets")
    if len(my_pets['pets']) == 0:
        pf.post_add_pets(auth_key, "временный", "для удаления", "0", "image\img2.jpg")
        _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    num = len(my_pets['pets']) - 1
    pet_id = my_pets['pets'][num]['id']
    status,result = pf.delete_pet(auth_key,pet_id)
    _,my_pets = pf.get_list_pets(auth_key,"my_pets")
    assert status == 200
    assert pet_id not in my_pets.values()
def test_udate_date_pets(name="новое имя", animal_type="обновленный", age = "5"):
    """обновление данных питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets= pf.get_list_pets(auth_key, "my_pets")
    if len(my_pets['pets'])>0:
        status, result= pf.put_update_pet(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
        assert status==200
        assert result['name']==name
    else:
        raise Exception("список питомцев пуст")
"""-------------------------------------------------------------------------------
-------------------------------тесты 19.7.2 --------------------------------------
----------------------------------------------------------------------------------"""
def test_creat_pet_simple(name="питомец", animal_type="без фото", age ="9"):
    """добавление питомца без фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_create_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
def test_add_photo_pets(pet_photo='image\img1.jpg'):
    """добавление фото"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key, "my_pets")
    if len(my_pets['pets'])>0:
        pet_id= my_pets['pets'][0]['id']
        status, result = pf.post_add_photo_pets(auth_key, pet_id, pet_photo)
        assert status == 200
        print (status)
    else:
        raise Exception("список питомцев пуст")

def test_api_key_no_valid(email="fgft@dt.cg",password="4565tfcgh"):
    """тест на получение api key с неверным email и password"""
    status, result = pf.get_api_key(email, password)
    assert status == 403

def test_get_all_pets_no_valid_key(filter='my_pets'):
    """тест на получение списка питомцев c недействуещим auth_key"""
    auth_key={'key': 'ac1a1c7ec234ed'}
    status, result = pf.get_list_pets(auth_key, filter)
    assert status == 403

def test_add_incorec_pets_no_photo(name="",animal_type="",age=""):
        """добавление питомца без фото c пустыми параметрами"""
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_create_pet_simple(auth_key, name,animal_type,age)
        assert status == 200
        """тест возращает код 200 и добавляет питомца это БАГ"""

def test_delete_pets_no_valid_id():
    """удление питомца с несуществуещим id"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_pets(auth_key,"my_pets")

    pet_id = "no_valid_pet_id"
    status, result = pf.delete_pet(auth_key,pet_id)
    assert status == 200
    """тест выдает код 200 что он удалил?"""

def test_add_pets_text_age(name='Страшило', animal_type='ужас',
                           age='text', pet_photo='image\img2.jpg'):
    """тест на добавление питомца c текстовым значением возраста"""
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_pets(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age

def test_name_pets_simbol(name='?56Q@#$$', animal_type='<a>ссылка</a>!#@$%/?',
                          age='567&#8', pet_photo='image\img1.jpg'):
        """тест на спец символы в имени и породе животного"""
        pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
        _, auth_key = pf.get_api_key(valid_email, valid_password)
        status, result = pf.post_add_pets(auth_key, name, animal_type, age, pet_photo)
        print('statu : ', status)
        assert status == 200
        assert result['name'] == name

def test_udate_date_pets_no_corect_id(name="неверный id", animal_type="тест", age = "5"):
    """обновление данных не существуещего питомца питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result= pf.put_update_pet(auth_key,"no correct id", name, animal_type, age)
    assert status==200
    assert result['name']==name

def test_add_photo_pets_no_corect_id(pet_photo='image\img1.jpg'):
    """добавление фото к питомцу с несуществуещему id"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_add_photo_pets(auth_key, 'pet_id', pet_photo)
    assert status == 200




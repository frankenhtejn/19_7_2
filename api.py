from requests_toolbelt.multipart.encoder import MultipartEncoder
import json

import requests


class PetFriends:
    def __init__(self):
        self.base_url = "http://petfriends1.herokuapp.com/"

    def get_api_key(self, email: str, password: str) -> json:
        """ получение api key"""
        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_pets(self, auth_key: json, filter: str) -> json:
        """получение списка питомцев"""
        heardes = {'auth_key': auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets', headers=heardes, params=filter)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_add_pets(self, auth_key: json, name: str,
                      animal_type: str, age: str,
                      pet_photo: str) -> json:
        """добавление питомца"""
        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        heardes = {'auth_key': auth_key['key'],
                   'Content-Type': data.content_type}
        res = requests.post(self.base_url + 'api/pets', headers=heardes, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def delete_pet(self, auth_key: json, pet_id: str ) -> json:
        """удаление питолмца"""
        heardes = {'auth_key': auth_key['key']}
        res = requests. delete(self.base_url+'api/pets/'+pet_id,headers=heardes)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def put_update_pet(self,auth_key:json, pet_id:str,
                       name:str, animal_type:str,
                       age:str) -> json:
        """обновление данных о питомце"""

        heardes = {'auth_key': auth_key['key']}
        data={
            'name':name,
            'animal_type':animal_type,
            'age':age
        }
        res = requests.put(self.base_url+'api/pets/'+pet_id,headers=heardes,data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def post_create_pet_simple(self, auth_key:json, name:str,
                               animal_type:str, age:str) -> json:
        """добавление данных о питомце без фото"""
        heardes = {'auth_key': auth_key['key']}
        data= {'name': name, 'animal_type': animal_type, 'age': age}
        res = requests.post(self.base_url+'api/create_pet_simple', headers= heardes, data= data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result
    def post_add_photo_pets(self, auth_key:json,
                            pet_id : str, pet_photo:str) -> json:
        """добавление фото питомца"""
        data = MultipartEncoder(
            fields={
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })
        heardes = {'auth_key': auth_key['key'],
                   'Content-Type': data.content_type}
        res= requests.post(self.base_url+'api/pets/set_photo/'+pet_id,
                           headers=heardes, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

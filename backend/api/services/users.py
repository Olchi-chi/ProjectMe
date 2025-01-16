from schemas.users import registration
from uuid import uuid4
import json
from fastapi.responses import JSONResponse

class User:
    def Registration(self, data: registration):
        if data.password != data.re_password:
            return {'status': 418, 'information': 'Пароли не совпадают.'}
        file = open('./api/data_base/base_of_users.json', 'r+')
        registration = json.loads(file.read())
        for user in registration:
            if user['mail'] == data.mail:
                file.close()
                return {'status': 418, 'information': 'Данный пользователь уже зарегистрирован.'}
        obj = {'id': str(uuid4()), 'mail': data.mail, 'password': data.password}
        registration.append(obj)
        file.seek(0)
        file.truncate()
        json.dump(registration, file, indent=4)
        file.close()
        return {'status': 200, 'information': 'Регистрация прошла успешно.'}


    def Avtorization(self, mail: str, password : str):
        file = open ('./api/data_base/base_of_users.json', 'r')
        login =json.loads(file.read())
        for user in login:
            if user['mail'] == mail and user['password'] == password:
                file.close()
                response = JSONResponse({'status': 200, 'information': 'Вы вошли в аккаунт.'})
                return response
        file.close()
        return {'status': 418, 'information': 'Ошибка логина или пароля.'}



auth_obj = User()


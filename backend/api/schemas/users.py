import pydantic
from pydantic import constr

class registration(pydantic.BaseModel):
    mail: constr(regex=r'^[A-Za-z0-9-_]+@[A-Za-z0-9-_]+\.[A-Za-z0-9-_]+$') = 'name@gmail.com'
    password: constr(min_length=8, max_length=16, regex=r'^[A-Za-z0-9!#$%&*+-.<=>?@^_]+$') = 'rhg%&td325SDaw'
    re_password: constr(min_length=8, max_length=16, regex=r'^[A-Za-z0-9!#$%&*+-.<=>?@^_]+$') = 'rhg%&td325SDaw'
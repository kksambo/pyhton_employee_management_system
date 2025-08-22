
#("postgresql+asyncpg://postgres:1234@localhost:5432/postgres")

class Urlmaker:
    def __init__(self,driver:str,username:str,password:str,port:int,database_name:str,host:str):
        self.driver = driver
        self.username = username
        self.password = password
        self.port = port
        self.database_name = database_name
        self.host = host

    def get_url(self) -> str:
        url = f'{self.driver}://{self.username}:{self.password}@{self.host}:{self.port}/{self.database_name}'
        return url

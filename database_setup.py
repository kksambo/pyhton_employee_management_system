from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

class DatabaseSetUp():
    def __init__(self,url):
        self.url = url
        self.engine = create_async_engine(self.url, echo=True, future=True)
        self.async_session = sessionmaker(bind=self.engine,class_=AsyncSession,expire_on_commit=False)



    async def get_db(self):
        async with self.async_session() as session:
            yield session
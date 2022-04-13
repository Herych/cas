from aiogram import types
from gino import Gino
from sqlalchemy import (Column, Integer, BigInteger, String, Sequence)
from sqlalchemy import sql

from config import db_user, db_pass, host

db = Gino()


# створення таблиці з користувачами
class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, Sequence('User_id_seq'), primary_key=True)
    user_id = Column(BigInteger)
    language = Column(String(2))
    full_name = Column(String(100))
    username = Column(String(50))
    query: sql.Select


# команди до бази даних

class DBCommands:
    async def get_user(self, user_id) -> User:
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    async def add_new_user(self):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)
        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id
        new_user.username = user.username
        new_user.full_name = user.full_name
        await new_user.create()
        return new_user

    async def set_language(self, language):
        user_id = types.User.get_current().id
        user = await self.get_user(user_id)
        await user.update(language=language).apply()


async def create_db():
    await db.set_bind(f"postgresql://{db_user}:{db_pass}@{host}/gino")
    await db.gino.create_all()














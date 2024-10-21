from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import User


async def create_users(
    session: AsyncSession,
    username: str,
    tg_id: int,
) -> User:
    user = User(username=username, tg_id=tg_id)
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession, tg_id: int) -> User:
    user = await session.scalar(select(User).where(User.tg_id == tg_id))
    return user

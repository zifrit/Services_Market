from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.user import TgUser


async def create_users(
    session: AsyncSession,
    username: str,
    tg_id: int,
) -> TgUser:
    user = TgUser(username=username, tg_id=tg_id)
    session.add(user)
    await session.commit()
    return user


async def get_user(session: AsyncSession, tg_id: int) -> TgUser:
    user = await session.scalar(select(TgUser).where(TgUser.tg_id == tg_id))
    return user


async def get_tg_user_id(session: AsyncSession, tg_id: int) -> int:
    use_id = await session.scalar(select(TgUser.id).where(TgUser.tg_id == tg_id))
    return use_id

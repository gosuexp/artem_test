from advanced_alchemy import SQLAlchemyAsyncConfig
from advanced_alchemy.repository import SQLAlchemyAsyncRepository

from app.db.models import User


class UserRepository(SQLAlchemyAsyncRepository[User]):
    """Репозиторий для работы с пользователями."""

    model_type = User


async def provide_user_repo(db_session) -> UserRepository:
    """Провайдер репозитория."""
    sqlalchemy_config = SQLAlchemyAsyncConfig()
    return UserRepository(session=db_session)

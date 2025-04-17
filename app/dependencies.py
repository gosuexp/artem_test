from litestar import Request
from litestar.di import Provide

from app.db.repository import provide_user_repo


async def get_db_session(request: Request):
    """Получить сессию БД из состояния приложения."""
    return request.state.db_session


def get_dependencies() -> dict:
    """Возвращает словарь зависимостей для DI."""
    return {
        "db_session": Provide(get_db_session),
        "user_repo": Provide(provide_user_repo),
    }

from litestar import Litestar
from advanced_alchemy.extensions.litestar.plugins import SQLAlchemyPlugin
from advanced_alchemy.config import SQLAlchemyAsyncConfig

from app.routes.users import UserController


def create_app() -> Litestar:
    sqlalchemy_config = SQLAlchemyAsyncConfig(
        connection_string="postgresql+asyncpg://postgres:postgres@db:5432/app_db",
        engine_config={"pool_pre_ping": True},
    )

    plugin = SQLAlchemyPlugin(config=sqlalchemy_config)

    return Litestar(
        route_handlers=[UserController],
        plugins=[plugin],
    )


app = create_app()

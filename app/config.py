from typing import Any

# Исправляем импорт репозитория
from advanced_alchemy.repository import SQLAlchemyAsyncRepository
from advanced_alchemy.config import SQLAlchemyAsyncConfig
from litestar.config.allowed_hosts import AllowedHostsConfig
from litestar.config.compression import CompressionConfig
from litestar.logging import LoggingConfig
from litestar.middleware.compression import CompressionMiddleware
from litestar.middleware.csrf import CSRFMiddleware
from litestar.openapi import OpenAPIConfig
from litestar.static_files import StaticFilesConfig
from litestar.template import TemplateConfig


def get_app_config() -> dict[str, Any]:
    """Получить конфигурацию приложения."""
    return {
        "openapi_config": OpenAPIConfig(
            title="User API",
            version="1.0.0",
            description="API для управления пользователями",
        ),
        "logging_config": LoggingConfig(
            loggers={
                "app": {
                    "level": "INFO",
                    "handlers": ["queue_listener"],
                }
            }
        ),
        "allowed_hosts": AllowedHostsConfig(allowed_hosts=["*"]),
        "compression_config": CompressionConfig(backend="gzip"),
        "static_files_config": [
            StaticFilesConfig(
                path="/static",
                directories=["static"],
            )
        ],
        "middleware": [
            CompressionMiddleware,
            CSRFMiddleware,
        ],
        "template_config": TemplateConfig(
            directory="templates",
        ),
    }

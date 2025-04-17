from litestar.dto import DataclassDTO, DTOConfig
from msgspec import Struct


class UserCreate(Struct):
    """DTO для создания пользователя."""

    name: str
    surname: str
    password: str


class UserRead(Struct):
    """DTO для чтения пользователя."""

    id: int
    name: str
    surname: str
    created_at: str
    updated_at: str


class UserUpdate(Struct):
    """DTO для обновления пользователя."""

    name: str | None = None
    surname: str | None = None
    password: str | None = None


# Конфигурация DTO
class UserCreateDTO(DataclassDTO[UserCreate]):
    config = DTOConfig(exclude={"id", "created_at", "updated_at"})


class UserReadDTO(DataclassDTO[UserRead]):
    config = DTOConfig(exclude={"password"})


class UserUpdateDTO(DataclassDTO[UserUpdate]):
    config = DTOConfig()

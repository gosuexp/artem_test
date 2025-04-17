from litestar import Controller, delete, get, patch, post
from litestar.pagination import OffsetPagination

from app.db.repository import UserRepository
from app.dtos import (
    UserCreate,
    UserRead,
    UserUpdate,
    UserReadDTO,
    UserCreateDTO,
    UserUpdateDTO,
)
from app.dependencies import get_dependencies


class UserController(Controller):
    path = "/users"
    dependencies = get_dependencies()
    return_dto = UserReadDTO

    @post("/", dto=UserCreateDTO)
    async def create_user(
        self,
        data: UserCreate,
        user_repo: UserRepository,
    ) -> UserRead:
        new_user = await user_repo.add(data)
        return UserRead.from_dict(new_user.to_dict())

    @get("/")
    async def list_users(
        self,
        user_repo: UserRepository,
        page: int = 1,
        page_size: int = 10,
    ) -> OffsetPagination[UserRead]:
        users = await user_repo.list(page, page_size)
        return OffsetPagination[UserRead](
            items=[UserRead.from_dict(u.to_dict()) for u in users.items],
            total=users.total,
            page=page,
            page_size=page_size,
        )

    @get("/{user_id:int}")
    async def get_user(
        self,
        user_id: int,
        user_repo: UserRepository,
    ) -> UserRead:
        user = await user_repo.get(user_id)
        return UserRead.from_dict(user.to_dict())

    @patch("/{user_id:int}", dto=UserUpdateDTO)
    async def update_user(
        self,
        user_id: int,
        data: UserUpdate,
        user_repo: UserRepository,
    ) -> UserRead:
        updated_user = await user_repo.update(user_id, data)
        return UserRead.from_dict(updated_user.to_dict())

    @delete("/{user_id:int}")
    async def delete_user(
        self,
        user_id: int,
        user_repo: UserRepository,
    ) -> None:
        await user_repo.delete(user_id)

import pytest

from core.post.models import Post
from core.fixtures.user import user


@pytest.fixture
def post(db, user):
    return Post.objects.create(author=user, body="Тестовое описание поста.")

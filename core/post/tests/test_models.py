import pytest

from core.post.models import Post
from core.fixtures.user import user


@pytest.mark.django_db
def test_create_post(user):
    post = Post.objects.create(author=user, body="Тестовое описание поста.")
    assert post.body == "Тестовое описание поста."
    assert post.author == user

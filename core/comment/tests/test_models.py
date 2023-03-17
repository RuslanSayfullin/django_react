import pytest

from core.comment.models import Comment
from core.fixtures.user import user
from core.fixtures.post import post


@pytest.mark.django_db
def test_create_comment(user, post):
    comment = Comment.objects.create(author=user, post=post, body="Тестовое описание поста.")
    assert comment.author == user
    assert comment.post == post
    assert comment.body == "Тестовое описание поста."

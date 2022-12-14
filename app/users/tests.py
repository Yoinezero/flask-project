from datetime import datetime, timedelta
import unittest
from app import create_app, db
from app.users.models import User, Post
from app.config import TestingConfig


class UserModelCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestingConfig)
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_password_hashing(self):
        u = User(username='test_user')
        u.set_password('qwerty')
        self.assertFalse(u.check_password('123456'))
        self.assertTrue(u.check_password('qwerty'))

    def test_follow(self):
        u1 = User(username='user', email='test@user.com')
        u2 = User(username='follower', email='follower@test.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u1.followers.all(), [])

        u2.follow(u1)
        db.session.commit()
        self.assertTrue(u2.is_following(u1))
        self.assertEqual(u2.followed.count(), 1)
        self.assertEqual(u2.followed.first().username, 'user')
        self.assertEqual(u1.followers.count(), 1)
        self.assertEqual(u1.followers.first().username, 'follower')

        u2.unfollow(u1)
        db.session.commit()
        self.assertFalse(u2.is_following(u1))
        self.assertEqual(u2.followed.count(), 0)
        self.assertEqual(u1.followers.count(), 0)

    def test_follow_posts(self):
        # create four users
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        # create four posts
        now = datetime.utcnow()
        p1 = Post(body="post from john", author=u1,
                  timestamp=now + timedelta(seconds=1))
        p2 = Post(body="post from susan", author=u2,
                  timestamp=now + timedelta(seconds=4))
        p3 = Post(body="post from mary", author=u3,
                  timestamp=now + timedelta(seconds=3))
        p4 = Post(body="post from david", author=u4,
                  timestamp=now + timedelta(seconds=2))
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        # setup the followers
        u1.follow(u2)  # john follows susan
        u1.follow(u4)  # john follows david
        u2.follow(u3)  # susan follows mary
        u3.follow(u4)  # mary follows david
        db.session.commit()

        # check the followed posts of each user
        f1 = u1.get_actual_posts().all()
        f2 = u2.get_actual_posts().all()
        f3 = u3.get_actual_posts().all()
        f4 = u4.get_actual_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])


if __name__ == '__main__':
    unittest.main(verbosity=2)

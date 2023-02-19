from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly_test'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

class UserViewsTestCase(TestCase):
    """Tests for views for Users."""
    
    def setUp(self):
        """Add sample user."""
        User.query.delete()

        user = User(first_name="FirstTest", last_name="LastTest", image_url="https://static-koimoi.akamaized.net/wp-content/new-galleries/2022/04/when-emma-watson-almost-quit-the-harry-potter-film-franchise-hermione-granger-would-be-proud-of-it-01.jpg")
        db.sesssion.add(user)
        db.session.commit()

        self.user_id = user.id
        self.user = user

    def tearDown(self):
        "Clean up"
        db.session.rollback()

    def test_list_users(self):
        with app.test_client() as client:
            resp= client.get("/users")
            html = resp.get_date(as_Text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('FirstTest', html)

    def test_user_form(self):
        with app.test_client() as client:
            resp = client.get('/users/new')
            html = resp.get_data(as_Text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Users</h1>', html)

    def test_add_user(self):
        with app.test_client() as client:
            d = {"first_name" : "FirstTest2", "last_name": "LastTest2", "img_url": "https://www.freeiconspng.com/uploads/icon-user-blue-symbol-people-person-generic--public-domain--21.png"}
            resp = client.post("/users", date=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<h1>Users</h1>", html)


   
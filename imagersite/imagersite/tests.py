from django.test import TestCase, Client


class BasicViewTests(TestCase):
    """Test view routing."""
    def setup(self):
        """Setup client."""
        self.client = Client()

    def test_home_route(self):
        """Route to home."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_route2(self):
        """Display home."""
        response = self.client.get('/')
        self.assertIn('Marketing', response.content.decode('utf-8'))

    def test_login_route(self):
        """Route to login."""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_route2(self):
        """Display login."""
        response = self.client.get('/accounts/login/')
        self.assertIn('Username', response.content.decode('utf-8'))

    def test_register_route(self):
        """Route to register."""
        response = self.client.get('/accounts/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_route2(self):
        """Display register."""
        response = self.client.get('/accounts/register/')
        self.assertIn('Email', response.content.decode('utf-8'))

    def test_logout_route(self):
        """Route to logout."""
        response = self.client.get('/accounts/logout/')
        self.assertEqual(response.status_code, 200)

    def test_logout_route2(self):
        """Display logout."""
        response = self.client.get('/accounts/logout/')
        self.assertIn('logged out', response.content.decode('utf-8'))

    def test_activate_route(self):
        """Route to activate."""
        response = self.client.get('/accounts/activate/complete/')
        self.assertEqual(response.status_code, 200)

    def test_activate_route2(self):
        """Display activate."""
        response = self.client.get('/accounts/activate/complete/')
        self.assertIn('Activation complete', response.content.decode('utf-8'))

    def test_registered_route(self):
        """Route to registered."""
        response = self.client.get('/accounts/register/complete/')
        self.assertEqual(response.status_code, 200)

    def test_registered_route2(self):
        """Display registered."""
        response = self.client.get('/accounts/register/complete/')
        self.assertIn(
            'Registration complete', response.content.decode('utf-8'))

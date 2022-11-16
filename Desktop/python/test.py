import main
import unittest

class TestMain(unittest.TestCase):

    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_status_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_greeting_message(self):
        greeting = 'Mujhe kya mei toh batak hoon'
        self.assertEqual(main.greet(), greeting)

if __name__ == '__main__':
    unittest.main()
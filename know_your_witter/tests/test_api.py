import unittest
from unittest.mock import Mock

from know_your_witter.apiaccess import access_server


class TestSum(unittest.TestCase):
    def test_get_tweets(self):
        mock_twitter = Mock()
        mock_twitter.return_value = {'username': 'testuser', 'statuses': [{'message': 'test message'}]}
        tweets = access_server.get_tweets_of_user(mock_twitter, 'testuser')
        self.assertEqual(tweets, mock_twitter.return_value)

  def test_username(self):
        mock_user = Mock()
        mock_user.return_value = {'username': 'testuser'}
        users = access_server.validate_username(mock_user, 'testuser')
        self.assertEqual(users, mock_user.return_value)

  def test_username_error(self):
        mock_user = Mock()
        mock_user.return_value = {'username': 'testuser'}
        users=access_server.validate_username(mock_user, 'testuser')
        self.assertRaises(users,TypeError)


if __name__ == '__main__':
    unittest.main()

import unittest
from unittest.mock import Mock

from know_your_witter.apiaccess import access_server


class TestSum(unittest.TestCase):
    def test_get_tweets(self):
        mock_twitter = Mock()
        mock_twitter.return_value = {'username': 'testuser', 'statuses': [{'message': 'test message'}]}
        tweets = access_server.get_tweets_of_user(mock_twitter, 'testuser')
        self.assertEqual(tweets, mock_twitter.return_value)


if __name__ == '__main__':
    unittest.main()

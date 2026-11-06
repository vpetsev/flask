import importlib
import unittest
from unittest.mock import patch


class ApiRegressionTests(unittest.TestCase):
    def test_article_converters_return_text(self):
        client = importlib.import_module('REST-api').app.test_client()
        for value in ('1', '1.5', 'example'):
            with self.subTest(value=value):
                response = client.get('/articles/' + value)
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_data(as_text=True), 'You are reading ' + value)

    def test_consensus_handles_unchanged_and_replaced_chains(self):
        api = importlib.import_module('Flask-blockchain.flask-bc')
        client = api.app.test_client()
        for replaced, key in ((False, 'chain'), (True, 'new_chain')):
            with self.subTest(replaced=replaced), patch.object(api.blockchain, 'resolve_conflicts', return_value=replaced):
                response = client.get('/nodes/resolve')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(response.get_json()[key], api.blockchain.chain)


if __name__ == '__main__':
    unittest.main()

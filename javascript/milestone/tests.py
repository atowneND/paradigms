#!/usr/bin/env python
import json
import unittest
import requests

class BrokenShitTest(unittest.TestCase):
    def get_movie(self, mid):
        return requests.get('http://student02.cse.nd.edu:40092/movies/' + mid ).content

    def get_recommendation(self, uid):
        return requests.get('http://student02.cse.nd.edu:40092/recommendations/' + uid)

    def send_recommendation(self, uid, mid, rating):
        data = {
            'movie_id': mid,
            'apikey': 'derp',
            'rating': rating,
        }
        return requests.put(
            'http://student02.cse.nd.edu:40092/recommendations/' + uid,
            data=json.dumps(data),
        )

    def test_upvote(self):
        trials = 50
        uid = '32'
        current_mid = None
        for i in xrange(0, trials):
            r = json.loads(self.get_recommendation(uid).content)
            self.assertNotEqual(current_mid, r['movie_id'])
            current_mid = r['movie_id']
            self.send_recommendation(uid, r['movie_id'], 5)

    def test_downvote(self):
        trials = 50
        uid = '32'
        current_mid = None
        for i in xrange(0, trials):
            r = json.loads(self.get_recommendation(uid).content)
            self.assertNotEqual(current_mid, r['movie_id'])
            current_mid = r['movie_id']
            self.send_recommendation(uid, r['movie_id'], 1)

if __name__ == '__main__':
    unittest.main()

# Ashley Towne
# 2/24/2016
# python primer

import csv

class _movie_database:
    def __init__(self):
        self.movies = {}
        self.users = {}
        self.ratings = {}
    
    def load_movies(self, movie_file):
        self.movies = {}
        with open(movie_file) as f:
            for line in f:
                line = line.rstrip()
                movie_attr = line.split("::") # movie attributes
                self.movies[int(movie_attr[0])] = {'name':movie_attr[1],'genres':movie_attr[2]}

    def get_movie(self, mid):
        if mid not in self.movies:
            return None
        else:
            return self.movies[mid]['name'], self.movies[mid]['genres']

    def get_movies(self):
        return [i for i in self.movies]

    def set_movie(self, mid, movie):
        self.movies[mid] = {'name':movie[0],'genres':movie[1]}

    def delete_movie(self, mid):
        self.movies.pop(mid,None)

    def load_users(self, users_file):
        self.users = {}
        with open(users_file) as f:
            for line in f:
                line = line.rstrip()
                user_attr = line.split("::") # user attributes
                self.users[int(user_attr[0])] = {'gender':user_attr[1], 'age':user_attr[2], 'occupationcode':user_attr[3], 'zipcode':user_attr[4]}

    def get_user(self, uid):
        if uid not in self.users:
            return None
        else:
            return self.users[uid]['gender'], int(self.users[uid]['age']), int(self.users[uid]['occupationcode']), self.users[uid]['zipcode']
    
    def get_users(self):
        return [i for i in self.users]

    def set_user(self, uid, user_attr):
        self.users[uid] = {'gender':user_attr[0], 'age':user_attr[1], 'occupationcode':user_attr[2], 'zipcode':user_attr[3]}

    def delete_user(self, uid):
        self.users.pop(uid,None)

    def load_ratings(self, ratings_file):
        self.ratings = {}
        with open (ratings_file) as f:
            for line in f:
                line = line.rstrip()
                rate_attr = line.split("::") # rating attributes
                mid = int(rate_attr[0])
                uid = int(rate_attr[1])
                if mid not in self.ratings:
                    self.ratings[mid] = {uid:int(rate_attr[2])}
                else:
                    self.ratings[mid][uid] = int(rate_attr[2])

    def get_rating(self, mid):
        if mid not in self.ratings:
            return None
        else: 
            vals = self.ratings[mid].values()
            return float(
                sum(vals)
            )/len(vals)

    def get_highest_rated_movie(self):
        print max(
                [[mid,self.get_rating(mid)] for mid in self.ratings],
                key=lambda x: int(x[1]),
            )[0]

    def set_user_movie_rating(self, uid, mid, rating):
        if (mid not in self.ratings) or (uid not in self.ratings[mid]):
            return None
        self.ratings[mid][uid] = int(rating)

    def get_user_movie_rating(self, uid, mid):
        if (mid not in self.ratings) or (uid not in self.ratings[mid]):
            return None
        return self.ratings[mid][uid]

    def delete_all_ratings(self):
        self.ratings.clear()

if __name__=='__main__':
    m = _movie_database()
    f = 'ml-1m/movies.dat'
    m.load_movies(f)
    f = 'ml-1m/users.dat'
    m.load_users(f)
    f = 'ml-1m/ratings.dat'
    m.load_ratings(f)
    mid = m.get_highest_rated_movie()
    print mid, m.get_movie(mid)
    rat = m.get_rating(mid)
    print rat


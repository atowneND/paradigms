import datetime as dt
def add_numbers(x,y,z):
    print x+y+z
    return x+y+z

add_numbers(5,10,40)
foo = 3
#print "foo=%s\n"%foo
#now=dt.datetime.now()
#print now
#print now.date()
#print now.time()
#print now.hour

def shopping():
    answer = raw_input("type either banana or apple\n")
    answer.lower()
    if answer=='banana':
        print "banananannanananana"
    elif answer=='apple':
        print "keeps the doc away"
    else:
        print "ya dun messed up"

shopping()

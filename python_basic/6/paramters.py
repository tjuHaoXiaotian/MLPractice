# coding=utf-8

def story(**kwds):
    return 'Once upon a time,there was a ' \
            '%(job)s called %(name)s.' % kwds

def power(x,y,*others):
    if others:
        print 'Received redundant parameters:',others
    return pow(x,y)

def interval(start,stop=None,step = 1):
    'Imitats range() for step > 0'
    if stop is None:
        start,stop = 0,start
        print start,stop
    result = []
    i = start
    while i < stop:
        result.append(i)
        i+=step
    return result

print story(job='king',name='haoxiaotian')

print story(name='tanghongyao',job='sb')

params = {'job':'language','name':'Python'}
print story(**params)

del params['job']

print story(job='leader',**params)

print power(2,3)

print power(3,2)

print power(y=3,x=2)

params = (5,) * 2
print params
print power(*params)

print power(3,3,'Hello world')

print interval(10)

print interval(1,5)

print interval(3,12,4)

print power(*(1,2,3,4,5,6))

print power(*interval(3,7))

# map
print map(str,range(10))

print [str(i) for i in range(10)]

# filter
def biggerThanFive(num):
    return num > 5
print filter(biggerThanFive,range(10))

print filter(lambda x:x>5,range(10))

# reduce
print reduce(lambda x,y:x+y ,range(11))





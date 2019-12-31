import Router

router = Router.Router()

def create_user():
    return 'user is created'


# register endpoint
router.add_route('POST', '^/users/$', create_user)

# callback, kwargs = router.match('POST','/users/')
# print(callback(**kwargs))

callback, kwargs = router.match('POST', '/foobar')
print(callback)
dummy_start_response = lambda x,y:print(x,y)
print(callback({},dummy_start_response,**kwargs))


# print(callback({}, dummy_start_response, **kwargs))
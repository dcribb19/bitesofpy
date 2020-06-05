def get_profile(**kwargs):
    'usage: accepts name= and profession= args'
    name = 'julian'
    profession = 'programmer'
    expected_args = ['name', 'profession']
    if len(kwargs) > 2:
        raise TypeError
    for key in kwargs.keys():
        if key not in expected_args:
            raise TypeError
        if key == 'name':
            name = kwargs['name']
        if key == 'profession':
            profession = kwargs['profession']

    return name + ' is a ' + profession

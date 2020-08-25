def get_profile(name, age, *sports, **awards):
    if not isinstance(age, int) or len(sports) > 5:
        raise ValueError
    if awards and not sports:
        return {'name': name,
                'age': age,
                'awards': {k: v for k, v in awards.items()}
                }
    elif sports and awards:
        return {'name': name,
                'age': age,
                'sports': sorted([sport for sport in sports]),
                'awards': {k: v for k, v in awards.items()}
                }
    elif sports:
        return {'name': name,
                'age': age,
                'sports': sorted([sport for sport in sports])
                }
    else:
        return {'name': name,
                'age': age
                }

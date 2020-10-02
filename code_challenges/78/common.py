def common_languages(programmers):
    """Receive a dict of keys -> names and values -> a sequence of
       of programming languages, return the common languages"""
    common = set()
    for _, languages in programmers.items():
        languages = set(languages)
        if not common:
            common = languages
        else:
            common = common.intersection(languages)
    return common

from configparser import ConfigParser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = ConfigParser()
        self.config.read(ini_file)
        self.sections = self.config.sections()

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        num_sections = len(self.sections)
        return num_sections

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        envlist = self.config['tox']['envlist'].strip().replace('\n', ',')
        envs = sorted([x.strip() for x in envlist.split(',')
                      if x.strip() != ''])
        return envs

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        base_python = []
        for x in self.sections:
            try:
                base_python.append(self.config[x]['basepython'])
            except KeyError:
                continue
        return list(set(sorted(base_python)))

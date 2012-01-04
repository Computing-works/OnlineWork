"""Online Lab configuration utilities. """

import os

def configure(args, **kwargs):
    """Setup Online Lab using a config file, command-line options, etc. """
    module = args.module

    if args.config_file is not None:
        config_file = args.config_file
    else:
        config_file = os.path.join(args.home, 'settings.py')

    config = {'HOME': args.home}

    if os.path.exists(config_file):
        with open(config_file) as conf:
            exec conf.read() in config

    if module == 'sdk':
        from ..sdk.settings import options, defaults

    settings = Settings.instance()
    settings['home'] = args.home

    settings.update(kwargs)

    for option, _ in options:
        if option not in kwargs:
            value = getattr(args, option, None)

            if value is None:
                try:
                    value = config[option.upper()]
                except KeyError:
                    try:
                        value = defaults[option]
                    except KeyError:
                        pass
                    else:
                        if isinstance(value, str):
                            value = value % settings

        settings[option] = value

    python_path = args.python_path

    try:
        python_path.extend(config['PYTHON_PATH'])
    except KeyError:
        pass

    settings['python_path'] = python_path

    for option, value in config.iteritems():
        if option.startswith('_'):
            continue

        option = option.lower()

        if option not in settings:
            settings[option] = value

    if module == 'sdk':
        import django.conf as conf

        django_settings = {}

        for option in dir(conf.global_settings):
            if option.startswith('_'):
                continue

            low_option = option.lower()

            if low_option in settings:
                django_settings[option] = settings[low_option]

        conf.settings.configure(**django_settings)

    return settings

class Settings(dict):
    """Global configuration for Online Lab. """

    @classmethod
    def instance(cls):
        """Returns the global :class:`Settings` instance. """
        if not hasattr(cls, '_instance'):
            cls._instance = cls()
        return cls._instance

    def __getattr__(self, option):
        try:
            return self[option]
        except KeyError:
            raise AttributeError("'%s' wasn't set although is required" % option)

    def get_PYTHONPATH(self):
        """Collect custom Python modules' paths into PYTHONPATH. """
        return os.pathsep.join(self.python_path)


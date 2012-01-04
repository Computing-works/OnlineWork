"""Configuration options for Online Lab. """

options = [
    ('port', 'int'),
    ('debug', 'bool'),
    ('daemon', 'bool'),
    ('logs_path', 'path'),
    ('data_path', 'path'),
    ('static_path', 'path'),
    ('templates_path', 'path'),
    ('pid_file', 'path'),
    ('log_file', 'path'),
    ('log_level', 'str'),
    ('log_max_size', 'int'),
    ('log_num_backups', 'int'),
    ('log_actions', 'path'),
    ('auth', 'bool'),
    ('evaluate_timeout', 'int'),
    ('engine_timeout', 'int'),
    ('engines', 'list'),
    ('environ', 'dict'),
    ('modules', 'list'),
]

defaults = {
    'port': 8000,
    'debug': False,
    'daemon': True,
    'logs_path': '%(home)s/logs',
    'data_path': '%(home)s/data',
    'static_path': '%(home)s/static',
    'templates_path': '%(home)s/templates',
    'pid_file': "%(home)s/onlinelab-sdk-%(port)s.pid",
    'log_file': "%(logs_path)s/onlinelab-sdk-%(port)s.log",
    'log_level': 'info',
    'log_max_size': 10*1000*1000,      # store 10 MB in a log file
    'log_num_backups': 10,             # keep 10 log files at most
    'log_actions': "%(logs_path)s/actions.log",
    'auth': True,
    'evaluate_timeout': 0,             # allow oo evaluation time
    'engine_timeout': 20,              # wait at most 20 seconds
    'engines': ['python', 'python3', 'javascript'],
    'environ': {},
    'modules': [],
}


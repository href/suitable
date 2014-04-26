from common import log
from commands import commands


class Api(object):

    def __init__(self, servers, **runner_args):
        self.servers = ' '.join(servers).split(' ')
        self.runner_args = runner_args

        for command in commands:
            if hasattr(self, command.name):
                log.warn('')

            setattr(self, command.name, command.execute)
            setattr(getattr(self, command.name), '__doc__', command.help)

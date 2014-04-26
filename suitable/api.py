from common import log
from commands import commands


class Api(object):

    def __init__(self, servers, **runner_args):
        self.servers = ' '.join(servers).split(' ')
        self.runner_args = runner_args

        for command in commands:

            if hasattr(self, command.module_name):
                log.warn('{} conflicts with existing attribute'.format(
                    command.name
                ))
                continue

            run = lambda **arguments: command.execute(self.servers, arguments)

            setattr(self, command.module_name, run)

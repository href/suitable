import os

from ansible.runner import Runner
from ansible.utils.plugins import module_finder


class RunnerCommand(object):

    def __init__(self, module_name):
        self.module_name = module_name

    def execute(self, servers, arguments):
        runner_args = {
            'module_name': self.module_name,
            'module_args': arguments,
            'pattern': 'all',
            'targets': ' '.join(
                servers
            )
        }

        runner = Runner(**runner_args)
        return runner.run()


def list_ansible_modules():

    # constant and code copied from ansible
    # https://github.com/ansible/ansible/blob/devel/bin/ansible-doc

    BLACKLIST_EXTS = ('.swp', '.bak', '~', '.rpm')
    paths = (p for p in module_finder._get_paths() if os.path.isdir(p))

    modules = []

    for path in paths:
        modules.extend(m for m in os.listdir(p) if m not in BLACKLIST_EXTS)

    return modules


commands = [RunnerCommand(m) for m in list_ansible_modules()]

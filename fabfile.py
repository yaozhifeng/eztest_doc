from fabric.api import *
from fabric.contrib.console import confirm
from fabric.context_managers import prefix

code_path = '/home/kaola.me/eztest_doc'
help_docs_path = code_path + '/docs'
git_repo = 'git@bitbucket.org:eztest/eztest_doc.git'

env.roledefs['s3'] = [
    'root@112.124.48.245',
]


@parallel
@roles('s3')
def update_app():
    with cd(help_docs_path):
        run('git pull')
        run("make html")
    sudo('service nginx reload')




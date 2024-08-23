from fabric.api import cd, env, local, prefix, run

env.hosts = ['sdelquin.me']


def deploy():
    local('git push')
    with cd('~/code/notibday'):
        with prefix('.venv/bin/activate'):
            run('git pull')
            run('pip install -r requirements.txt')

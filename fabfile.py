from fabric.api import env, local, cd, run, prefix

env.hosts = ['sdelquin.me']


def deploy():
    local('git push')
    with prefix('source ~/.pyenv/versions/notibday/bin/activate'):
        with cd('~/code/notibday'):
            run('git pull')
            run('pip install -r requirements.txt')

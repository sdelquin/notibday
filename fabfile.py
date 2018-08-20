from fabric.api import env, local, cd, run

env.hosts = ['production']


def deploy():
    local('git push')
    with cd('~/notibday'):
        run('git pull')
        run('pipenv install')

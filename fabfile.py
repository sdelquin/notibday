from fabric.api import env, local, prefix, cd, run

env.hosts = ["production"]


def deploy():
    local("git push")
    with prefix("source ~/.virtualenvs/notibday/bin/activate"):
        with cd("~/notibday"):
            run("git pull")
            run("pip install -r requirements.txt")

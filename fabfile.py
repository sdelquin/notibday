import config
from fabric.api import env, local, prefix, cd, run

env.hosts = [config.PROD_SERVER["NAME"]]


def deploy():
    local("git push")
    with prefix("source {}/bin/activate".format(config.PROD_SERVER["VENV"])):
        with cd(config.PROD_SERVER["PROJ"]):
            run("git pull")
            run("pip install -r requirements.txt")

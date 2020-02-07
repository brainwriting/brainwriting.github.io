from invoke import task
import os


@task
def usage(c):
    """
    prints example usage
    """
    examples(c)


@task
def examples(c):
    """
    prints example usage
    """
    usage = """
SEE LIST OF TASKS:
    $ invoke --list
    OR
    $ invoke -l

HELP:
    $ invoke --help {task_from_list}

BUILD:
    $ invoke build -c
    $ invoke build --clean

HI:
    $ invoke hi Name
    $ invoke hi --name Name
    $ invoke hi --name=Name
    $ invoke hi -n Name
    $ invoke hi -nName
    """
    print(usage)


@task(help={"name": "Name of the person to say hi to."})
def hi(c, name, help=False):
    """
    Say hi to someone.
    """
    print("Hi {}!".format(name))


@task
def clean(c):
    """
    Remove old build files
    """
    print("Cleaning!")
    c.run("echo ./clean.sh")


@task(clean)
def build(c):
    """
    Build the executable
    """
    print("Building!")
    c.run("echo ./build.sh")


@task
def deploy(c):
    """
    Deploy on a server
    """
    print("Deploying!")
    cwd = os.getcwd()
    if cwd[-3:] == "api":
        c.run("./deploy.sh")
        return
    os.chdir("api")
    c.run("./deploy.sh")


@task
def lint(c):
    """
    Make the code look nice.
    """
    format(c)


@task
def format(c):
    """
    Make the code look nice.
    """
    print("Formatting!")
    cwd = os.getcwd()
    if cwd[-3:] == "api":
        os.chdir("..")
        c.run("./format.sh")
        return
    c.run("./format.sh")


@task
def docker(c):
    """
    Docker build
    """
    c.run("./docker_build.sh")

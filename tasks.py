from invoke import task
import os
import webbrowser


@task(aliases=("list", "lsit", "ist", "-list", "lis", "li"))
def _dash_dash_list(c):
    """
    because i forget --list often and fixz my ttypos
    """
    c.run("invoke --list")


@task(aliases=("gh", "repo", "remote", "web"))
def github(c):
    """
    opens the GitHub website for this project in default browser
    """
    SITE = "https://github.com/brainwriting/brainwriting.github.io"
    print("Opening...", SITE)
    webbrowser.open(SITE)


@task(aliases=("ghd", "desktop"))
def github_desktop(c):
    """
    opens the GitHub Desktop app <yes i am *that* lazy>. macOS only.
    """
    c.run("open -a 'GitHub Desktop'")


@task(aliases=("usage", "examples"))
def print_examples(c):
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


@task(aliases=("format", "black", "lint"))
def black_auto_format(c):
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
    Docker build && docker run
    """
    c.run("./docker_build.sh")
    # http://www.pyinvoke.org/faq.html#running-local-shell-commands-run
    c.run("./docker_run.sh", pty=True)


@task(aliases=("heroku", "h", "hd"))
def heroku_deploy(c):
    """
    Deploy to heroku.

    Simply follows instructions here...
    https://devcenter.heroku.com/articles/container-registry-and-runtime#getting-started
    """
    UH_OH_MSG = "\n\n\nuh oh, I forgot to set my secrets locally."
    UH_OH_MSG += "\nrun ```cat .export_env_vars``` for export statements"
    UH_OH_MSG += "\nif that file does not exist then try running"
    UH_OH_MSG += "\n```invoke heroku-config```"
    UH_OH_MSG += "\nif heroku is not setup either..."
    UH_OH_MSG += "\nI should make a tutorial for this..."
    assert os.environ.get("api_key", None) is not None, UH_OH_MSG
    c.run("heroku container:login")
    c.run(
        "heroku container:push -a brainwriting web --arg api_key,client_id,client_secret,project_id,spreadsheet_id,spreadsheet_range"
    )  # noqa
    c.run("heroku container:release -a brainwriting web")
    c.run("heroku open -a brainwriting")
    pass


@task(aliases=("heroku-env", "he", "heroku-config", "heroku-vars", "vars"))
def get_all_heroku_config_vars(c):
    print("Getting environment variables...")
    var_names = [
        "api_key",
        "client_id",
        "client_secret",
        "project_id",
        "spreadsheet_id",
        "spreadsheet_range",
    ]
    cmd = "heroku config:get -a brainwriting {}"
    for v in var_names:
        print("{}".format(v))
        c.run(cmd.format(v))
        print()

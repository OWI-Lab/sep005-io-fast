# noxfile.py
import nox


@nox.session(python="3.12")
def tests(session):
    session.run("pip", "install", "-e", "./[dev]")
    session.run("pytest", "./tests")
    session.run("pytest", "--cov=./tests")


@nox.session(python="3.12")
def lint(session):
    session.install("flake8")
    session.run("flake8", "./sep005_io_fast", "./tests", "--max-line-length=127")


@nox.session(python="3.12")
def format(session):
    session.install("isort", "black")
    session.run("isort", "./sep005_io_fast", "./tests")
    session.run("black", "./sep005_io_fast", "./tests")

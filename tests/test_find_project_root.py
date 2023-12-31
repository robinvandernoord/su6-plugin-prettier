from pathlib import Path

from src.su6_plugin_prettier.helpers import find_project_root, chdir


def test_find_project_root_node_modules():
    with chdir("./pytest_examples/code"):
        path, reason = find_project_root(tuple(), "")
        assert path.exists() and str(path.resolve()) == str(Path("../").resolve())
        assert reason == "node_modules"


def test_find_project_root_git():
    path, reason = find_project_root(("src", "./pytest_examples/"))

    assert path.exists() and str(path.resolve()) == str(Path("./").resolve())
    assert reason == ".git directory"


def test_find_project_root_notfound():
    path, reason = find_project_root(("src", "../"))

    assert path.exists() and str(path.resolve()) == str(Path("/").resolve())
    assert reason == "file system root"

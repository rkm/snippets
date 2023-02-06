#!/bin/env python3
import json
import subprocess
import urllib.request
from pathlib import Path
from typing import Sequence
from typing import Union

_PATCH_GROUP_ID = 37
_STR_LIKE = Union[str, Path]


def _run(cmd: Sequence[_STR_LIKE]) -> None:
    subprocess.check_call(("echo", *cmd))
    subprocess.check_call(cmd)


def main() -> int:
    url = (
        f"https://git.rockylinux.org/api/v4/groups/"
        f"{_PATCH_GROUP_ID}"
        f"/projects"
        f"?per_page=100"
    )

    repos = []
    page = 1
    while True:
        resp = urllib.request.urlopen(f"{url}&page={page}")
        data = json.loads(resp.read().decode())
        repos += [x["web_url"] for x in data]
        page = resp.headers["x-next-page"]
        if not page:
            break

    for repo in repos:
        repo_name = repo.rpartition("/")[2]
        print(repo_name)
        if Path(repo_name).is_dir():
            continue
        cmd = (
            "git",
            "clone",
            repo,
        )
        _run(cmd)

    return 0


if __name__ == "__main__":
    exit(main())

"""
Utilities for cloning docs with sparse checkout.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path


def _run(cmd: list[str], cwd: Path | None = None) -> None:
    subprocess.run(cmd, cwd=cwd, check=True)


def git_clone_for_context(repo_url: str, clone_dir: Path, sparse_path: str) -> None:
    _run(["git", "clone", "--depth=1", "--filter=blob:none", "--sparse", repo_url, str(clone_dir)])
    _run(["git", "sparse-checkout", "set", sparse_path], cwd=clone_dir)


def sync_typst_doc(clone_dir: Path | None = None) -> None:
    repo_url = "https://github.com/typst/typst.git"
    sparse_path = "docs"
    if clone_dir is None:
        clone_dir = Path.cwd() / "typst-docs"
    temp_dir = Path.cwd() / ".typst-docs-tmp"
    if temp_dir.exists():
        shutil.rmtree(temp_dir)
    git_clone_for_context(repo_url, temp_dir, sparse_path)
    source_docs = temp_dir / "docs"
    if clone_dir.exists():
        shutil.rmtree(clone_dir)
    shutil.copytree(source_docs, clone_dir)
    _prune_typst_docs(clone_dir)
    shutil.rmtree(temp_dir)


def _prune_typst_docs(clone_dir: Path) -> None:
    for rel_path in ["changelog", "Cargo.toml", "src"]:
        target = clone_dir / rel_path
        if target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clone Typst docs with sparse checkout and sync them locally."
    )
    parser.add_argument(
        "--clone-dir",
        type=Path,
        default=None,
        help="Destination directory for synced docs (default: ./typst-docs).",
    )
    args = parser.parse_args()
    sync_typst_doc(args.clone_dir)


if __name__ == "__main__":
    main()

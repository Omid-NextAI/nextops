#!/usr/bin/env python3
"""Compute the NextOps application-code digest of a reviewed local wheel."""

from __future__ import annotations

import argparse
from pathlib import Path

from nextops.api.release_identity import wheel_code_digest


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("wheel", type=Path, help="local candidate NextOps wheel")
    args = parser.parse_args()
    print(f"nextops_app_code_sha256={wheel_code_digest(args.wheel)}")


if __name__ == "__main__":
    main()

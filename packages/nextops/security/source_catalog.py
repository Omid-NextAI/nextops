"""Load a bounded, protected, credential-free deployment catalogue."""

import json
import os
import stat
from pathlib import Path

from nextops.application.errors import ApplicationError
from nextops.contracts.errors import ErrorCode
from nextops.contracts.source_catalog import SourceCatalog
from nextops.contracts.sources import SourceReadBinding


def load_catalog(path: Path) -> SourceCatalog:
    try:
        meta = path.lstat()
        if not path.is_absolute() or not stat.S_ISREG(meta.st_mode) or meta.st_size > 65_536:
            raise ValueError()
        if os.name == "posix" and (meta.st_mode & 0o022 or meta.st_uid not in (0, os.geteuid())):
            raise ValueError()

        def unique(pairs: list[tuple[str, object]]) -> dict[str, object]:
            result: dict[str, object] = {}
            for key, value in pairs:
                if key in result:
                    raise ValueError()
                result[key] = value
            return result

        with path.open("rb") as stream:
            opened = os.fstat(stream.fileno())
            if (meta.st_dev, meta.st_ino) != (opened.st_dev, opened.st_ino):
                raise ValueError()
            raw = stream.read(65_537)
        if len(raw) > 65_536:
            raise ValueError()
        return SourceCatalog.model_validate(json.loads(raw, object_pairs_hook=unique))
    except (OSError, ValueError):
        raise ValueError("approved source catalogue invalid or unavailable") from None


class CatalogBindings:
    def __init__(self, catalog: SourceCatalog) -> None:
        self.catalog = catalog

    def resolve_binding(self, source_id: str, target_id: str) -> SourceReadBinding:
        try:
            return self.catalog.resolve_binding(source_id, target_id)
        except KeyError:
            raise ApplicationError(
                ErrorCode.POLICY_DENIED, "connector.source_target_denied"
            ) from None

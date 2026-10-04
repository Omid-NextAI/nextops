"""Primitive source identifiers, shared without circular evidence imports."""

from typing import Annotated

from pydantic import Field

LogicalSourceId = Annotated[str, Field(pattern=r"^[a-z][a-z0-9-]{1,31}$")]
ZabbixObjectId = Annotated[str, Field(pattern=r"^[1-9][0-9]{0,19}$")]

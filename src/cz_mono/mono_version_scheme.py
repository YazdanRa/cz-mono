import re
from typing import ClassVar

from commitizen.version_schemes import BaseVersion, Increment


class MonoVersion(BaseVersion):
    """
    Mono versioning scheme

    Any increment bump simply increases the single numeric component.
    """

    parser: ClassVar[re.Pattern] = re.compile(
        r"v?(?P<version>([0-9]+)(?:-([0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*))?(?:\+[0-9A-Za-z.]+)?(\w+)?)"
    )

    def increment_base(self, increment: Increment | None = None) -> str:
        return f"{self.major + 1}"

    def _get_increment_base(self, increment: Increment | None, exact_increment: bool) -> str:
        return self.increment_base(increment)

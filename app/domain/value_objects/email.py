"""Email value object."""

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class Email:
	"""Email value object - immutable."""

	value: str

	def __post_init__(self) -> None:
		"""Validate email format."""
		pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
		if not re.match(pattern, self.value):
			raise ValueError(f"Invalid email format: {self.value}")

	def __str__(self) -> str:
		"""String representation."""
		return self.value

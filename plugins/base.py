from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class BasePlugin(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def label(self) -> str:
        pass

    @abstractmethod
    def analyze(self, dataset: Any) -> Dict[str, Any]:
        pass

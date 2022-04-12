from dataclasses import dataclass
from typing import List


@dataclass
class SteamGameInfo:
    game_title: str
    supported_os: List[str]
    original_price: float
    final_price: float
    discount: float


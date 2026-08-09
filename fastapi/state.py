"""In‑memory storage for Battleship games.

This module defines simple data structures used by the API endpoints. The
storage is a plain dictionary keyed by game ID; each entry holds the game
state, players, ships and shots. It is deliberately lightweight because the
application does not persist data between restarts.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------
# Internal data models (not exposed via the API)
# ---------------------------------------------------------------------------

@dataclass
class ShipData:
    """Internal representation of a ship.

    Attributes match the public :class:`fastapi.models.Ship` model so they can
    be converted directly when building a response.
    """

    ship_type: str
    size: int
    coordinates: List[Tuple[int, int]]
    placed: bool = True


@dataclass
class ShotData:
    """Internal representation of a shot.

    ``shooter`` is the player ID that fired the shot, ``target`` is the player
    ID whose board was hit.
    """

    shooter: str
    target: str
    x: int
    y: int
    result: str  # "hit", "miss" or "sink"


@dataclass
class PlayerData:
    """Internal representation of a player within a game."""

    player_id: str
    ships: List[ShipData] = field(default_factory=list)


@dataclass
class GameData:
    """Internal representation of a game session."""

    game_id: str
    players: Dict[str, PlayerData] = field(default_factory=dict)
    shots: List[ShotData] = field(default_factory=list)


# Global in‑memory store – keyed by ``game_id``
GAMES: Dict[str, GameData] = {}

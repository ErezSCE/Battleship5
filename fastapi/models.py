from __future__ import annotations

from typing import List, Tuple, Dict, Any
from pydantic import BaseModel, Field

class Ship(BaseModel):
    """Represents a ship belonging to a player."""

    ship_type: str = Field(..., description="Type/name of the ship, e.g., 'Destroyer'")
    size: int = Field(..., description="Length of the ship in grid cells")
    coordinates: List[Tuple[int, int]] = Field(
        ..., description="List of (x, y) tuples occupied by the ship"
    )
    placed: bool = Field(True, description="Whether the ship has been placed on the board")

class ShotResult(str):
    HIT = "hit"
    MISS = "miss"
    SINK = "sink"

class Shot(BaseModel):
    """A shot fired by a player."""

    shooter: str = Field(..., description="Player ID who fired the shot")
    x: int = Field(..., description="X coordinate of the shot")
    y: int = Field(..., description="Y coordinate of the shot")
    result: ShotResult = Field(..., description="Result of the shot")

class PlayerView(BaseModel):
    """Sanitized view returned to a player for a specific game."""

    player_id: str = Field(..., description="ID of the requesting player")
    ships: List[Ship] = Field(..., description="The player's own ships")
    opponent_shots: List[Shot] = Field(
        ..., description="Shots made by the opponent against this player's board"
    )

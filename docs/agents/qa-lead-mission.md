# QA Lead — Test Plan

**Agent**: qa-lead  
**Generated**: 2026-08-09T17:56:28.791Z

---

## Test Plan

{
  "scope": "All acceptance criteria are covered by the tests below.",
  "unit": [
    {
      "target": "backend/src/game_service.py::create_game",
      "description": "Verify that create_game returns HTTP 201 and a unique game ID.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 0
    },
    {
      "target": "backend/src/game_service.py::create_game",
      "description": "Ensure the generated game ID can be used in subsequent service calls (format validation).",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 2
    },
    {
      "target": "backend/src/game_service.py::get_sanitized_view",
      "description": "Check that GET /games returns my ship positions and opponent hit/miss markers.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 0
    },
    {
      "target": "backend/src/game_service.py::get_sanitized_view",
      "description": "Assert that opponent ship positions are never included in the response.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 1
    },
    {
      "target": "backend/src/game_service.py::get_sanitized_view",
      "description": "Validate that requesting an unknown game ID raises a 404 error.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 2
    },
    {
      "target": "backend/src/ship_placement.py::validate_and_store",
      "description": "Confirm valid ship placement returns success and updates internal state.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 0
    },
    {
      "target": "backend/src/ship_placement.py::validate_and_store",
      "description": "Test that overlapping, out‑of‑bounds, or wrong‑size placements return a 400 error with a clear message.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 1
    },
    {
      "target": "backend/src/ship_placement.py::validate_and_store",
      "description": "After a successful placement, verify that ship coordinates are stored for the correct player.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 2
    },
    {
      "target": "backend/src/shot_processor.py::process_shot",
      "description": "Ensure shot processing returns a result field of 'hit', 'miss', or 'sunk'.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 0
    },
    {
      "target": "backend/src/shot_processor.py::process_shot",
      "description": "Validate that a shot made out of turn results in a 409 conflict response.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 1
    },
    {
      "target": "backend/src/shot_processor.py::process_shot",
      "description": "When all opponent ships are sunk, confirm the response includes 'game_over': true.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 2
    },
    {
      "target": "frontend/src/app/components/board/board.component.ts",
      "description": "Unit test that the board component renders a 6×6 grid with the player's ships and opponent hit markers.",
      "framework": "karma/jest",
      "storyId": "US-005",
      "acIndex": 0
    },
    {
      "target": "frontend/src/app/components/attack-grid/attack-grid.component.ts",
      "description": "Unit test that the attack grid displays markers for previous hits and misses.",
      "framework": "karma/jest",
      "storyId": "US-005",
      "acIndex": 1
    },
    {
      "target": "frontend/src/app/components/attack-grid/attack-grid.component.ts",
      "description": "Verify that clicking a cell triggers a shot request and updates both grids based on the backend response.",
      "framework": "karma/jest",
      "storyId": "US-005",
      "acIndex": 2
    }
  ],
  "integration": [
    {
      "target": "POST /games",
      "description": "Integration test that creating a game returns 201 and a unique ID usable in later calls.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 0
    },
    {
      "target": "POST /games",
      "description": "After creation, perform a GET using the returned ID to ensure the ID is valid.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 2
    },
    {
      "target": "GET /games/{id}",
      "description": "Verify 200 response contains player ships and opponent hit/miss markers.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 0
    },
    {
      "target": "GET /games/{id}",
      "description": "Assert that opponent ship positions are omitted from the JSON payload.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 1
    },
    {
      "target": "GET /games/{id}",
      "description": "Request a non‑existent game ID and expect a 404 response.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 2
    },
    {
      "target": "POST /games/{id}/ships",
      "description": "Submit valid ship coordinates and expect a 200 response with updated state.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 0
    },
    {
      "target": "POST /games/{id}/ships",
      "description": "Submit invalid placements (overlap/out‑of‑bounds) and verify a 400 error with a clear message.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 1
    },
    {
      "target": "POST /games/{id}/ships",
      "description": "After a successful placement, retrieve the game state and confirm ship locations are stored.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 2
    },
    {
      "target": "POST /games/{id}/shots",
      "description": "Fire a shot and check that the response includes a result field of 'hit', 'miss', or 'sunk'.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 0
    },
    {
      "target": "POST /games/{id}/shots",
      "description": "Attempt a shot out of turn and verify a 409 conflict response.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 1
    },
    {
      "target": "POST /games/{id}/shots",
      "description": "Sink all opponent ships and confirm the response contains 'game_over': true.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 2
    }
  ],
  "e2e": [
    {
      "scenario": "Full game flow: create game, place ships, fire shots until victory",
      "description": "Play through the entire game via the UI, verifying creation, ship placement, shot actions, UI updates, no console/network errors, and win condition display.",
      "criticalPath": true,
      "storyId": "US-007",
      "acIndex": -1
    },
    {
      "scenario": "Docker compose startup verification",
      "description": "Run 'docker compose up --build', ensure both containers start without errors, frontend reachable at http://localhost:4200, backend reachable at http://localhost:8000, and containers recover after a forced crash.",
      "criticalPath": true,
      "storyId": "US-006",
      "acIndex": -1
    }
  ],
  "coverageTargets": {
    "unit": 85,
    "integration": 70,
    "e2e": 100
  }
}

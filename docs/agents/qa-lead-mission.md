# QA Lead — Test Plan

**Agent**: qa-lead  
**Generated**: 2026-08-09T17:45:28.223Z

---

## Test Plan

{
  "scope": "",
  "unit": [
    {
      "target": "backend/src/services/game_service.py::create_game",
      "description": "Verify that creating a game initializes empty board state and returns a unique ID.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 0
    },
    {
      "target": "backend/src/services/sanitizer.py::sanitize_game_view",
      "description": "Ensure sanitized view includes player's ships and opponent hit/miss markers but never opponent ship positions.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 1
    },
    {
      "target": "backend/src/validators/ship_validator.py::validate_placement",
      "description": "Test ship placement validation for overlap, out-of-bounds, and size constraints.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 1
    },
    {
      "target": "backend/src/repositories/ship_repository.py::store_ship",
      "description": "Confirm that after successful placement the ship coordinates are stored in the in‑memory dict.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 2
    },
    {
      "target": "backend/src/services/shot_processor.py::process_shot",
      "description": "Validate shot result calculation returns 'hit', 'miss', or 'sunk' correctly.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 0
    },
    {
      "target": "backend/src/services/turn_manager.py::enforce_turn",
      "description": "Check that shots out of turn raise a TurnOrderError leading to HTTP 409.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 1
    },
    {
      "target": "backend/src/services/game_service.py::check_game_over",
      "description": "Ensure game_over flag is set when all opponent ships are sunk.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 2
    },
    {
      "target": "frontend/src/app/components/board/board.component.ts",
      "description": "Unit test that BoardComponent renders player's ships and opponent hit/miss markers on a 6×6 grid.",
      "framework": "Jest",
      "storyId": "US-005",
      "acIndex": 0
    },
    {
      "target": "frontend/src/app/components/attack-grid/attack-grid.component.ts",
      "description": "Unit test that AttackGridComponent displays hit/miss markers and emits shot events on cell click.",
      "framework": "Jest",
      "storyId": "US-005",
      "acIndex": 1
    }
  ],
  "integration": [
    {
      "target": "POST /games",
      "description": "Assert response status 201 and that a unique game ID is returned.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 0
    },
    {
      "target": "POST /games",
      "description": "Verify response payload contains empty board state for both players.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 1
    },
    {
      "target": "GET /games/{id}",
      "description": "Confirm HTTP 200 with JSON containing player's ship positions and opponent hit/miss markers.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 0
    },
    {
      "target": "GET /games/{id}",
      "description": "Ensure opponent ship positions are never included in the response.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 1
    },
    {
      "target": "GET /games/{unknown_id}",
      "description": "Expect HTTP 404 when requesting a non‑existent game.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 2
    },
    {
      "target": "POST /games/{id}/ships",
      "description": "Valid ship placement returns HTTP 200 and updates game state.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 0
    },
    {
      "target": "POST /games/{id}/ships",
      "description": "Invalid placement (overlap/out‑of‑bounds/wrong size) returns HTTP 400 with error message.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 1
    },
    {
      "target": "POST /games/{id}/shots",
      "description": "Shot request returns result field of 'hit', 'miss', or 'sunk'.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 0
    },
    {
      "target": "POST /games/{id}/shots",
      "description": "Out‑of‑turn shot returns HTTP 409 with appropriate message.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 1
    },
    {
      "target": "POST /games/{id}/shots",
      "description": "When all opponent ships are sunk, response includes 'game_over': true.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 2
    }
  ],
  "e2e": [
    {
      "scenario": "Create a new game and verify the returned ID can be used for subsequent calls",
      "description": "End‑to‑end flow that creates a game via POST /games, stores the ID, and fetches the game view to confirm empty boards.",
      "criticalPath": true,
      "storyId": "US-001",
      "acIndex": 2
    },
    {
      "scenario": "UI displays player's board with ships and opponent hit/miss markers",
      "description": "After placing ships, the Angular UI shows a 6×6 grid with ships and any hits from opponent.",
      "criticalPath": true,
      "storyId": "US-005",
      "acIndex": 0
    },
    {
      "scenario": "UI displays attack grid with hit/miss markers",
      "description": "The separate attack grid reflects previous shot results using appropriate markers.",
      "criticalPath": true,
      "storyId": "US-005",
      "acIndex": 1
    },
    {
      "scenario": "Clicking a cell in attack grid sends shot request and updates both grids",
      "description": "User clicks a coordinate, Playwright verifies POST /games/{id}/shots is called, and UI updates with hit/miss/sunk and opponent board changes.",
      "criticalPath": true,
      "storyId": "US-005",
      "acIndex": 2
    },
    {
      "scenario": "Docker Compose starts both containers and they are reachable",
      "description": "Run 'docker compose up --build', assert frontend at http://localhost:4200 and backend at http://localhost:8000 respond without errors.",
      "criticalPath": true,
      "storyId": "US-006",
      "acIndex": 0
    },
    {
      "scenario": "Frontend can successfully call backend APIs after compose start",
      "description": "From the browser, trigger a health‑check API call and verify a successful response, confirming CORS and networking.",
      "criticalPath": true,
      "storyId": "US-006",
      "acIndex": 1
    },
    {
      "scenario": "Containers recover automatically after a crash",
      "description": "Simulate container failure, ensure Docker restart policy 'unless‑stopped' restarts the service and the UI remains functional.",
      "criticalPath": true,
      "storyId": "US-006",
      "acIndex": 2
    },
    {
      "scenario": "Full game flow end‑to‑end through the browser",
      "description": "Create game, place ships for both players, alternate shots until win condition, verify UI shows victory message and no console/network errors.",
      "criticalPath": true,
      "storyId": "US-007",
      "acIndex": 0
    },
    {
      "scenario": "No console or network errors appear during the full game flow",
      "description": "Playwright captures browser console logs and network requests, asserts zero errors throughout the scenario.",
      "criticalPath": true,
      "storyId": "US-007",
      "acIndex": 1
    },
    {
      "scenario": "Win condition is detected and displayed when all opponent ships are sunk",
      "description": "After the final shot that sinks the last ship, UI shows a victory banner and disables further actions.",
      "criticalPath": true,
      "storyId": "US-007",
      "acIndex": 2
    }
  ],
  "coverageTargets": {
    "unit": 85,
    "integration": 70,
    "e2e": 100
  }
}

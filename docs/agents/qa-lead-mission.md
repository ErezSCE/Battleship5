# QA Lead — Test Plan

**Agent**: qa-lead  
**Generated**: 2026-08-09T18:14:53.757Z

---

## Test Plan

{
  "scope": "All acceptance criteria from all user stories are covered by the test suite.",
  "unit": [
    {
      "target": "backend/src/game.py::create_game",
      "description": "Verify that create_game returns a new unique game ID.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 0
    },
    {
      "target": "backend/src/response_builder.py::build_game_creation_response",
      "description": "Ensure the game creation response includes empty board state for both players.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 1
    },
    {
      "target": "backend/src/validation.py::validate_ship_placement",
      "description": "Accept valid ship coordinates and return success.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 0
    },
    {
      "target": "backend/src/validation.py::validate_ship_placement",
      "description": "Reject overlapping, out‑of‑bounds, or wrong‑size ship placements with clear error messages.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 1
    },
    {
      "target": "backend/src/game_state.py::store_ship_locations",
      "description": "After a successful placement, ship locations are persisted in the in‑memory game state.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 2
    },
    {
      "target": "backend/src/shot_processor.py::process_shot",
      "description": "Return correct result field ('hit', 'miss', or 'sunk') for a shot.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 0
    },
    {
      "target": "backend/src/turn_manager.py::enforce_turn_order",
      "description": "Reject a shot made out of turn with HTTP 409 semantics.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 1
    },
    {
      "target": "backend/src/game_over.py::check_game_over",
      "description": "Detect when all opponent ships are sunk and set 'game_over': true.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 2
    },
    {
      "target": "backend/src/sanitizer.py::sanitize_game_view",
      "description": "Generate a view that includes my ships and opponent hit/miss markers but never opponent ship positions.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 1
    },
    {
      "target": "frontend/src/app/components/board/board.component.ts",
      "description": "Render a 6×6 grid displaying the player's ships and opponent hit markers.",
      "framework": "jest",
      "storyId": "US-005",
      "acIndex": 0
    },
    {
      "target": "frontend/src/app/components/attack-grid/attack-grid.component.ts",
      "description": "Render a separate 6×6 attack grid showing previous hit and miss markers.",
      "framework": "jest",
      "storyId": "US-005",
      "acIndex": 1
    },
    {
      "target": "frontend/src/app/components/attack-grid/attack-grid.component.ts",
      "description": "Handle cell click by invoking GameService.shot() and updating grid state.",
      "framework": "jest",
      "storyId": "US-005",
      "acIndex": 2
    },
    {
      "target": "frontend/src/app/services/game.service.ts",
      "description": "Create a new game via POST /games and store the returned game ID for later calls.",
      "framework": "jest",
      "storyId": "US-001",
      "acIndex": 2
    }
  ],
  "integration": [
    {
      "target": "backend/tests/api/test_game_creation.py::test_post_games_returns_201_and_unique_id",
      "description": "POST /games returns HTTP 201 with a unique game ID.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 0
    },
    {
      "target": "backend/tests/api/test_game_creation.py::test_post_games_includes_empty_board",
      "description": "Response includes empty board state for both players.",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 1
    },
    {
      "target": "backend/tests/api/test_game_flow.py::test_game_id_usable_in_subsequent_calls",
      "description": "Returned game ID can be used in subsequent API calls (e.g., GET /games/{id}).",
      "framework": "pytest",
      "storyId": "US-001",
      "acIndex": 2
    },
    {
      "target": "backend/tests/api/test_game_view.py::test_get_game_returns_sanitized_view",
      "description": "GET /games/{id} returns HTTP 200 with my ship positions and opponent hit/miss markers.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 0
    },
    {
      "target": "backend/tests/api/test_game_view.py::test_get_game_excludes_opponent_ships",
      "description": "Response never includes opponent ship positions.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 1
    },
    {
      "target": "backend/tests/api/test_game_view.py::test_get_unknown_game_returns_404",
      "description": "GET with an unknown game ID returns HTTP 404.",
      "framework": "pytest",
      "storyId": "US-002",
      "acIndex": 2
    },
    {
      "target": "backend/tests/api/test_ship_placement.py::test_post_ships_valid_returns_200",
      "description": "POST /games/{id}/ships with valid coordinates returns HTTP 200 and updates state.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 0
    },
    {
      "target": "backend/tests/api/test_ship_placement.py::test_post_ships_invalid_returns_400",
      "description": "Invalid placements return HTTP 400 with a clear error message.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 1
    },
    {
      "target": "backend/tests/api/test_ship_placement.py::test_ship_locations_persisted",
      "description": "After successful placement the backend stores the ship locations for the player.",
      "framework": "pytest",
      "storyId": "US-003",
      "acIndex": 2
    },
    {
      "target": "backend/tests/api/test_shot.py::test_post_shot_returns_result_field",
      "description": "POST /games/{id}/shots returns a result field of 'hit', 'miss' or 'sunk'.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 0
    },
    {
      "target": "backend/tests/api/test_shot.py::test_shot_out_of_turn_returns_409",
      "description": "Shot made out of turn returns HTTP 409 with appropriate message.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 1
    },
    {
      "target": "backend/tests/api/test_shot.py::test_shot_all_sunk_returns_game_over",
      "description": "When all opponent ships are sunk the response includes 'game_over': true.",
      "framework": "pytest",
      "storyId": "US-004",
      "acIndex": 2
    },
    {
      "target": "infra/tests/docker_compose_test.py::test_compose_starts_containers",
      "description": "Running 'docker compose up --build' starts both frontend and backend containers without errors.",
      "framework": "pytest",
      "storyId": "US-006",
      "acIndex": 0
    },
    {
      "target": "infra/tests/docker_compose_test.py::test_frontend_backend_connectivity",
      "description": "Frontend reachable at http://localhost:4200 and can successfully call backend at http://localhost:8000.",
      "framework": "pytest",
      "storyId": "US-006",
      "acIndex": 1
    },
    {
      "target": "infra/tests/docker_compose_test.py::test_restart_policy_unless_stopped",
      "description": "Both containers have a restart policy of 'unless-stopped' and recover automatically after a crash.",
      "framework": "pytest",
      "storyId": "US-006",
      "acIndex": 2
    }
  ],
  "e2e": [
    {
      "scenario": "Create new game via UI and verify empty boards are displayed.",
      "description": "User clicks 'New Game', UI shows two 6×6 grids with no ships or markers; verifies backend returned game ID is stored.",
      "criticalPath": true,
      "storyId": "US-001",
      "acIndex": -1
    },
    {
      "scenario": "Place ships through UI and confirm placement success.",
      "description": "Player drags/places three ships; UI shows ships on own board; backend confirms placement; invalid attempts show error toast.",
      "criticalPath": true,
      "storyId": "US-003",
      "acIndex": -1
    },
    {
      "scenario": "Fire shots and validate hit/miss/sunk markers and turn order.",
      "description": "Player clicks cells on attack grid; UI updates with hit/miss icons; out‑of‑turn attempts show warning; final shot that sinks all ships shows 'You win' message.",
      "criticalPath": true,
      "storyId": "US-004",
      "acIndex": -1
    },
    {
      "scenario": "Full game flow end‑to‑end verification.",
      "description": "Create game, place ships for both players, alternate shots until win condition; UI reflects both boards correctly; no console or network errors appear.",
      "criticalPath": true,
      "storyId": "US-007",
      "acIndex": -1
    },
    {
      "scenario": "Verify UI grids render correctly after each action.",
      "description": "Check that the player's board always shows own ships and opponent hits, and the attack grid shows all previous shot results.",
      "criticalPath": false,
      "storyId": "US-005",
      "acIndex": -1
    },
    {
      "scenario": "Detect win condition and display victory banner.",
      "description": "When all opponent ships are sunk, UI shows a prominent 'Victory' banner and disables further actions.",
      "criticalPath": true,
      "storyId": "US-007",
      "acIndex": 2
    }
  ],
  "coverageTargets": {
    "unit": 80,
    "integration": 60,
    "e2e": 100
  }
}

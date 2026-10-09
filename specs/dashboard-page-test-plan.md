# Dashboard Page Test Plan

## 1. Requirement Understanding

Validate the authenticated Dashboard entry point and its navigation handoff to PIM and Admin. The current implementation represents this page with `src/pages/InventoryPage.py`.

## 2. Test Scenarios

| ID | Scenario | Type | Priority | UI/API | Page Object | API Service | Test Data | Expected Result |
|---|---|---|---|---|---|---|---|---|
| DASH-001 | Dashboard loads after valid login | Smoke, Functional | P0 | UI | `InventoryPage`, `LoginPage` | None | `testdata/login_user.json` | Dashboard heading and protected URL are visible |
| DASH-002 | Admin navigation is visible | Functional | P0 | UI | `InventoryPage` | None | Valid user | Admin link is visible |
| DASH-003 | PIM navigation is visible and works | Integration | P0 | UI | `InventoryPage`, `PIMPage` | None | Valid user | PIM page opens and shows its heading |
| DASH-004 | Unauthenticated dashboard access is rejected | Negative, Security | P1 | UI | `InventoryPage`, `LoginPage` | None | None | User is redirected to login |

## 3. UI Automation Plan

- Use `LoginPage.login()` for authentication.
- Use `InventoryPage.dashboard_heading` and `admin_link` for dashboard checks.
- Use `InventoryPage.open_pim()` for navigation and assert the PIM heading after navigation.
- Verify URL and visible page heading with web-first assertions.

## 4. API Automation Plan

No Dashboard API scenarios are currently defined. The repository has no Playwright `APIRequestContext` service for Dashboard. If an endpoint is identified later, add an API service and validate status, schema, required fields, and authorization separately.

## 5. UI + API Integration Plan

No supported UI/API dependency exists for this page. Do not create one until an authenticated API contract is available.

## 6. Page Objects Required

- Existing: `src/pages/base_page.py`
- Existing: `src/pages/LoginPage.py`
- Existing: `src/pages/InventoryPage.py`
- Existing: `src/pages/PIMPage.py`
- Planned methods: `open_admin()` and an explicit dashboard readiness method if Admin navigation coverage expands.

## 7. API Service Classes Required

None for the current scope. If API coverage is added, use a Playwright `APIRequestContext` base service and a Dashboard/session service.

## 8. Test Files Required

- Existing coverage: `tests/auth/test_login_page_cases.py`, `tests/pim/test_pim.py`
- Planned: `tests/dashboard/test_dashboard.py`

## 9. Test Data Required

- Valid credentials from `testdata/login_user.json`.
- No secrets in test code; invalid or unauthenticated scenarios should use generated or non-sensitive values.

## 10. Fixtures Required

- Existing isolated `page` fixture from `conftest.py`.
- Reusable authenticated-page fixture may be introduced only if it does not leak state between tests.
- No API, database, or shared global page fixture is required.

## 11. Configuration Changes

- Continue using `config/config.ini` and `config/settings.py` for URLs and timeouts.
- Add a Dashboard path only if it is not already present; it currently is configured as `/dashboard/index`.

## 12. Existing Files to Modify

- Planned: `tests/dashboard/test_dashboard.py`.
- Only modify `conftest.py` or configuration when a new fixture or environment setting is required.

## 13. Existing Files to Keep Unchanged

- `src/pages/LoginPage.py`, `src/pages/InventoryPage.py`, and `src/pages/PIMPage.py` should remain unchanged for the scenarios above.
- `api/client.py` should not be reused as a Playwright API service without an explicit migration decision.

## 14. Locator Strategy

Use role locators first: heading `Dashboard`, link `Admin`, and link `PIM`. Use page URL assertions for routing. Avoid CSS selectors, XPath, coordinates, and generated class names.

## 15. Authentication Strategy

UI login with credentials loaded from `testdata/login_user.json`. Use a fresh browser context per test; do not use shared storage state for this scope.

## 16. Negative Scenarios

- Open Dashboard URL without authentication.
- Navigate to Admin or PIM after an expired session.
- Confirm failed login never exposes protected navigation.

## 17. Boundary Scenarios

- Browser reload immediately after dashboard navigation.
- Slow dashboard load within the configured timeout.
- Direct navigation to the configured dashboard URL with an empty or missing session.

## 18. Parallel Execution Considerations

Tests must use isolated contexts and must not depend on another test's login or navigation. Read-only dashboard checks can run in parallel. Avoid shared mutable user records.

## 19. Reporting Requirements

Retain failure screenshots and logs through the existing hooks. Add Playwright trace/video collection through the test runner configuration if required. Never log credentials or session tokens.

## 20. Final File Change Summary

- Add `specs/dashboard-page-test-plan.md`.
- Planned implementation file: `tests/dashboard/test_dashboard.py`.
- No API implementation is planned for the current Dashboard scope.

This plan follows POM: locators and navigation remain in page objects, while tests contain only orchestration and assertions.

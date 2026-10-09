# Login Page Test Plan

## 1. Requirement Understanding

Validate OrangeHRM login success, invalid credentials, required-field validation, and the authenticated Dashboard handoff. The owning page object is `src/pages/LoginPage.py`.

## 2. Test Scenarios

| ID | Scenario | Type | Priority | UI/API | Page Object | API Service | Test Data | Expected Result |
|---|---|---|---|---|---|---|---|---|
| LOGIN-001 | Login with valid credentials | Smoke, Functional | P0 | UI | `LoginPage`, `InventoryPage` | None | `testdata/login_user.json` | Dashboard opens |
| LOGIN-002 | Invalid username and password | Negative, Functional | P0 | UI | `LoginPage` | None | Invalid user data | Error is visible and login URL remains |
| LOGIN-003 | Empty username and password | Negative, Boundary | P1 | UI | `LoginPage` | None | Empty values | Required validation blocks submission |
| LOGIN-004 | Valid username with empty password | Negative | P1 | UI | `LoginPage` | None | Valid user plus empty password | Password validation blocks submission |
| LOGIN-005 | Empty username with valid password | Negative | P1 | UI | `LoginPage` | None | Empty username plus valid password | Username validation blocks submission |
| LOGIN-006 | Valid username with wrong password | Negative | P1 | UI | `LoginPage` | None | Valid username and non-secret wrong value | Invalid credentials is shown |

## 3. UI Automation Plan

- Call `LoginPage.goto()` for a fresh login page.
- Call `LoginPage.login(username, password)` for form interaction.
- Assert Dashboard heading and URL for success.
- Assert `Invalid credentials`, required field validity, and login URL for failures.

## 4. API Automation Plan

No login API scenarios are currently supported. The repository uses `requests` in `api/client.py`, not Playwright `APIRequestContext`; do not describe that client as API coverage. A future API plan must define endpoint, method, authentication, status, schema, and unauthorized responses.

## 5. UI + API Integration Plan

No UI/API dependency is required. A future setup flow could provision a user by API and verify login in the UI, but only after a documented API contract exists.

## 6. Page Objects Required

- Existing: `src/pages/base_page.py`, `src/pages/LoginPage.py`, `src/pages/InventoryPage.py`.
- Planned methods: `get_error_message()`, `is_username_valid()`, and `is_password_valid()` if tests need to remove direct locator assertions.

## 7. API Service Classes Required

None for the current scope. Do not add an API service without a real application endpoint.

## 8. Test Files Required

- Existing: `tests/auth/test_login_page_cases.py`.
- No second login test module should be created; consolidate duplicate login drafts into this suite.

## 9. Test Data Required

- Use `testdata/login_user.json` for valid, invalid, and empty users.
- Keep wrong-password values non-sensitive and outside production credentials.

## 10. Fixtures Required

- Existing isolated `page` fixture from `conftest.py`.
- No shared authenticated state, API context, database, or global page object.

## 11. Configuration Changes

- Continue reading the login URL and timeout from `config/config.ini` and `config/settings.py`.
- Keep browser and headless selection environment-driven.

## 12. Existing Files to Modify

- Planned: `tests/auth/test_login_page_cases.py` only if page-object assertion helpers are added.
- `src/pages/LoginPage.py` may be extended to expose validation/error methods.

## 13. Existing Files to Keep Unchanged

- `config/config.ini`, `config/settings.py`, `conftest.py`, and `api/client.py` remain unchanged for this scope.
- Do not add credentials to test modules or logs.

## 14. Locator Strategy

Use role locators already defined by `LoginPage`: Username textbox, Password textbox, and Login button. Prefer page-object methods over test-side selectors. Use URL assertions and accessible text for results.

## 15. Authentication Strategy

UI authentication with JSON-backed credentials and a new browser context per test. Do not use storage state because isolation is part of the login coverage.

## 16. Negative Scenarios

Invalid username/password, valid username with wrong password, empty username, empty password, both fields empty, and attempted protected-page access without login.

## 17. Boundary Scenarios

Empty strings, whitespace-only values, long usernames/passwords, special characters, and password masking. Confirm the form remains usable and does not reveal the password.

## 18. Parallel Execution Considerations

All scenarios are independent and can run under xdist with isolated contexts. Test data is read-only. Do not depend on a prior successful login or a shared session.

## 19. Reporting Requirements

Capture failure screenshots using the existing hook; add trace/video at runner level if required. Logs must identify the test outcome without printing usernames, passwords, cookies, or tokens.

## 20. Final File Change Summary

- Canonical plan: `specs/login-page-test-plan.md`.
- Existing implementation coverage: `tests/auth/test_login_page_cases.py`.
- No API implementation is planned for login until a Playwright API contract is supplied.

This plan follows POM: page interaction stays in `LoginPage`, while tests orchestrate flows and assert outcomes.

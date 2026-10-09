# System Users Page Test Plan

## 1. Requirement Understanding

Validate the Admin System Users page load, records summary, Add User entry, and required-field validation. The current page object is `src/pages/SystemUsersPage.py`.

## 2. Test Scenarios

| ID | Scenario | Type | Priority | UI/API | Page Object | API Service | Test Data | Expected Result |
|---|---|---|---|---|---|---|---|---|
| ADMIN-001 | System Users page loads | Smoke, Functional | P0 | UI | `LoginPage`, `InventoryPage`, `SystemUsersPage` | None | `testdata/login_user.json` | Heading, Add button, and records summary are visible |
| ADMIN-002 | Open Add User form | Functional | P0 | UI | `SystemUsersPage` | None | Valid admin | Add User heading is visible |
| ADMIN-003 | Submit empty Add User form | Negative, Boundary | P0 | UI | `SystemUsersPage` | None | Empty form | Required validation appears and no user is created |
| ADMIN-004 | Search existing user | Functional | P1 | UI | `SystemUsersPage` | None | Known user record | Matching record is displayed |
| ADMIN-005 | Search unknown user | Negative | P1 | UI | `SystemUsersPage` | None | Generated unknown username | Empty state is displayed |
| ADMIN-006 | Add unique valid user | Functional, Integration | P1 | UI | `SystemUsersPage` | None | Generated user payload | User is saved and searchable |

## 3. UI Automation Plan

- Authenticate with `LoginPage`.
- Navigate directly through `SystemUsersPage.goto()` using the configured URL.
- Use `open_add_form()` and `submit_form()` for page actions.
- Assert heading, Add button, records summary, form heading, validation, success state, and searchable result.

## 4. API Automation Plan

No System Users API service exists. The current generic `requests` client is not Playwright APIRequestContext coverage. Define endpoint, method, authentication, payload, response schema, and authorization behavior before adding API scenarios.

## 5. UI + API Integration Plan

Not currently applicable. A future flow may create a unique user by API, locate it in the UI, and delete it by API. Cleanup must run even when UI assertions fail.

## 6. Page Objects Required

- Existing: `BasePage`, `LoginPage`, `InventoryPage`, `SystemUsersPage`.
- Planned methods: search-field actions, user-form field locators/actions, row accessors, and delete/edit actions where supported.
- Page objects must not contain `expect()` assertions.

## 7. API Service Classes Required

None currently. Future API coverage would require `api/base_api.py`, `api/session_manager.py`, and `api/system_users_api.py` using Playwright APIRequestContext.

## 8. Test Files Required

- Existing: `tests/admin/test_system_users_spec.py`.
- Extend this file rather than creating a duplicate Admin test module.

## 9. Test Data Required

- Admin credentials from `testdata/login_user.json`.
- Known record values only when stable in the demo environment.
- Generated unique usernames and employee data for mutating tests; no hardcoded secrets.

## 10. Fixtures Required

- Existing isolated `page` fixture.
- Optional authenticated admin fixture may centralize setup while creating a new context per test.
- No shared API context or database fixture is currently required.

## 11. Configuration Changes

Keep `system_users_url`, base URL, and timeouts in `config/config.ini` and `config/settings.py`. Add environment-specific overrides before running against any non-demo environment.

## 12. Existing Files to Modify

- Planned: `tests/admin/test_system_users_spec.py` for search, empty-state, and unique-user coverage.
- `src/pages/SystemUsersPage.py` for missing form/search locators and actions.
- `config/config.ini` only when a new environment or route is introduced.

## 13. Existing Files to Keep Unchanged

Keep `api/client.py`, `conftest.py`, and login data unchanged unless the API or fixture plan is approved. Do not modify browser configuration for page-specific coverage.

## 14. Locator Strategy

Prefer role locators for headings and buttons, label locators for form fields, and test IDs if the application exposes them. Use CSS only for stable semantic containers such as the existing records summary fallback. Avoid generated classes, nth-child, coordinates, and absolute XPath.

## 15. Authentication Strategy

UI login as the configured admin user, with a fresh browser context per test and no shared storage state. Credentials remain in data/configuration files and are never logged.

## 16. Negative Scenarios

Empty required fields, duplicate username, invalid employee, invalid role/status, password mismatch, unknown search value, unauthorized direct access, and expired session.

## 17. Boundary Scenarios

Empty and whitespace values, minimum/maximum username length, special characters, Unicode names, long employee names, and zero matching records.

## 18. Parallel Execution Considerations

Read-only list/search tests can run in parallel. Add/edit/delete tests require generated unique records, isolated sessions, and fixture cleanup. Never assume a fixed row count or test order.

## 19. Reporting Requirements

Retain existing failure screenshots and logs; add trace/video at runner level if required. Redact credentials, cookies, tokens, and sensitive user fields from logs and attachments.

## 20. Final File Change Summary

- Canonical plan: `specs/admin-system-users-test-plan.md`.
- Existing implementation coverage: `tests/admin/test_system_users_spec.py`.
- Page-object expansion is required before full CRUD coverage.
- API coverage remains deferred until a documented endpoint contract exists.

This plan follows POM: System Users interactions belong in the page object, while tests orchestrate scenarios and assert behavior.

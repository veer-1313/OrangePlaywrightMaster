# PIM Page Test Plan

## 1. Requirement Understanding

Validate navigation from Dashboard to PIM, Employee List rendering, employee search, reset behavior, record opening, and add-form validation. The current page object is `src/pages/PIMPage.py`.

## 2. Test Scenarios

| ID | Scenario | Type | Priority | UI/API | Page Object | API Service | Test Data | Expected Result |
|---|---|---|---|---|---|---|---|---|
| PIM-001 | PIM opens after login | Smoke, Integration | P0 | UI | `LoginPage`, `InventoryPage`, `PIMPage` | None | `tests/data/users.json` | PIM heading and route are visible |
| PIM-002 | Search by employee name | Functional | P0 | UI | `PIMPage` | None | `Aaliyah Haq` | Matching record is visible |
| PIM-003 | Search by employee ID | Functional | P0 | UI | `PIMPage` | None | `0001` | Matching record is visible |
| PIM-004 | Search with unknown employee | Negative | P1 | UI | `PIMPage` | None | `tests/data/pim_test_data.json` | No Records Found is visible |
| PIM-005 | Reset employee filters | Functional | P1 | UI | `PIMPage` | None | Valid search data | Default list returns |
| PIM-006 | Submit empty Add Employee form | Negative, Boundary | P0 | UI | `PIMPage` | None | Empty form | Required validation appears |

## 3. UI Automation Plan

- Authenticate through `LoginPage`, navigate with `InventoryPage.open_pim()`, and wait with `PIMPage.wait_for_load()`.
- Use `search_employee_by_name()`, `search_employee_by_id()`, and `reset_search()`.
- Assert heading, route, rows, no-results state, and required validation with web-first assertions.

## 4. API Automation Plan

No PIM API service exists. The current `api/client.py` is a generic `requests` client and does not provide Playwright APIRequestContext coverage. Define employee endpoints and response schemas before planning API tests.

## 5. UI + API Integration Plan

Not currently applicable. Once a supported employee API exists, create unique employee data by API, verify it through PIM UI, then clean it up by API.

## 6. Page Objects Required

- Existing: `BasePage`, `LoginPage`, `InventoryPage`, `PIMPage`.
- Planned methods: `open_add_form()`, `submit_employee_form()`, and a row accessor that returns locators without assertions.

## 7. API Service Classes Required

None currently. Future work would require `api/base_api.py` and `api/employee_api.py` using Playwright APIRequestContext.

## 8. Test Files Required

- Existing: `tests/pim/test_pim.py`.
- No parallel PIM test module should be created.

## 9. Test Data Required

- Credentials from `tests/data/users.json`.
- Search values from `tests/data/pim_test_data.json`.
- Dynamic unique employee data for create tests; do not reuse a static mutable record in parallel runs.

## 10. Fixtures Required

- Existing isolated `page` fixture.
- Optional `authenticated_page` or `pim_page` fixture may centralize login/navigation, provided each test receives a new context.

## 11. Configuration Changes

Keep base URL and timeouts in `config/config.ini` and `config/settings.py`. Add a PIM path only if direct navigation becomes part of the contract; current tests intentionally validate the application-generated route.

## 12. Existing Files to Modify

- Planned: `tests/pim/test_pim.py` for reset, add, and boundary scenarios.
- `src/pages/PIMPage.py` may receive missing form actions and row locators.

## 13. Existing Files to Keep Unchanged

Keep `api/client.py`, `conftest.py`, and login data unchanged unless a new API or fixture is explicitly introduced.

## 14. Locator Strategy

Use role and label locators already declared in `PIMPage`. Use the table card locator only as the current fallback for row text. Avoid generated classes, nth-child selectors, absolute XPath, and coordinates.

## 15. Authentication Strategy

UI login using the standard user from `tests/data/users.json`, with a fresh browser context per test and no shared storage state.

## 16. Negative Scenarios

Unknown name, unknown employee ID, unsupported filter combinations, empty required fields, duplicate employee ID, and unauthorized direct PIM access.

## 17. Boundary Scenarios

Empty values, whitespace, very long names, special characters, Unicode names, minimum/maximum employee ID length, and zero-result searches.

## 18. Parallel Execution Considerations

Search tests are read-only and parallel-safe. Create/edit/delete tests require generated unique records and guaranteed cleanup; they must not depend on execution order.

## 19. Reporting Requirements

Use existing failure screenshots and logs. Add trace/video collection at runner level if required. Redact credentials and any employee-sensitive data from logs.

## 20. Final File Change Summary

- Canonical plan: `specs/pim-module-test-plan.md`.
- Existing implementation coverage: `tests/pim/test_pim.py`.
- Future API work is intentionally deferred until endpoints and contracts are known.

This plan follows POM: navigation and locators stay in page objects, and tests contain orchestration plus assertions only.

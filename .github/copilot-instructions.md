# Project rules for AI agents (Python Playwright)

# You are working in a Playwright Python automation project.
# Follow these rules for every code change.

## Stack
stack = {
    "playwright_version": "Playwright 1.56+ with Python",
    "python_version": "Python 3.11+",
    "test_runner": "pytest + pytest-playwright",
    "reporter": "Allure + built-in HTML",
    "ci": "GitHub Actions, sharded"
}

## Folder structure
folder_structure = {
    "src/pages/": "Page Object classes (one file per page)",
    "src/fixtures/": "Custom fixtures extending base test",
    "src/utils/": "Pure helpers, no test logic",
    "tests/": "Spec files, mirror app URL structure",
    "tests/data/": "JSON/CSV test data",
    "specs/": "Planner output (Markdown plans)"
}

## Coding conventions
coding_conventions = [
    "Import test from src/fixtures/base.py, never directly from playwright.sync_api",
    "Use pytest.describe or class-based grouping per feature area",
    "One logical assertion group per test",
    "Use step annotations for readability when a flow has more than 3 actions",
    "File names: kebab-case (add_to_cart_spec.py)"
]

## Locator priority (STRICT — do not deviate)
locator_priority = [
    "1. page.get_by_role(role, name='...') with accessible name",
    "2. page.get_by_label(label_text) for form fields",
    "3. page.get_by_test_id(id) — attribute is data-test-id",
    "4. page.get_by_text(text) only for genuinely static UI text",
    "5. CSS / XPath — forbidden unless approved in PR"
]

## Page Object contract
page_object_contract = [
    "One class per page, extends BasePage",
    "Constructor takes page only",
    "All locators declared in __init__",
    "Action methods return None OR the next page object",
    "No expect() calls inside page objects — assertions belong in tests",
    "No business logic in tests — put it in page objects or helpers"
]

## Assertion rules
assertion_rules = [
    "Web-first assertions only (expect(locator).to_be_visible())",
    "No page.wait_for_timeout() — ever",
    "No wait_for_selector() — use locator auto-waiting",
    "Custom timeouts only when justified in a code comment"
]

## When adding a new test
new_test_rules = [
    "Mirror the app URL structure inside tests/",
    "Reuse existing page objects — do not create parallel infra",
    "Load test data from tests/data/, not inline",
    "Tag tests with @smoke, @regression, or @critical as appropriate"
]

## Forbidden
forbidden_rules = [
    "Do not skip or comment out failing tests to make CI green",
    "Do not use page.evaluate() unless there is no MCP tool alternative",
    "Do not commit .env, credentials, storage_state.json, or auth tokens",
    "Do not modify playwright.config.py without asking",
    "Do not add new Python dependencies without asking",
    "Do not use page.pause() in committed code"
]

## When you (the agent) are unsure
unsure_guidelines = [
    "Ask a clarifying question before generating code",
    "Prefer a smaller, focused change over a big refactor",
    "If a required file does not exist, ask before creating it"
]

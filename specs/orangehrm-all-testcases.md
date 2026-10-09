# Test Plan: OrangeHRM Full Login and Dashboard Coverage

**Target:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login  
**Seed:** tests/seed.spec.py (not present; use the existing Playwright page fixture)  
**Date:** 2026-09-17

## Overview

This plan covers the OrangeHRM authentication flows and the key navigation checks that follow a successful login. It uses credentials from the JSON test-data file so the actual username and password are stored only in the designated data folder.

## Preconditions

- The OrangeHRM login page is reachable at `/web/index.php/auth/login`.
- Every scenario starts from a fresh browser session and a clean, unauthenticated page.
- The browser is opened in a standard desktop viewport.
- Test data is loaded from `tests/data/users.json`.
- No persisted login state is reused between scenarios.

## Scenarios

### Scenario 1.1 — Standard user successful login

- **Priority:** P0
- **Tags:** @smoke, @critical
- **Preconditions:** The login page is visible and both fields are empty.
- **Steps:**
  1. Read the standard user credentials from the JSON data file.
  2. Fill the Username field with the stored standard username.
  3. Fill the Password field with the stored standard password.
  4. Click the `Login` button — expected: the application redirects to `/web/index.php/dashboard/index`.
- **Assertions:**
  - The Dashboard heading is visible.
  - The URL matches `/web/index.php/dashboard/index`.
  - The `Admin` navigation link is visible.
- **Edge cases considered:**
  - Ensure no prior authenticated session leaks across scenarios.
  - Confirm the password is not shown as plain text in the UI.

### Scenario 1.2 — Invalid username and password combination

- **Priority:** P0
- **Tags:** @smoke, @regression
- **Preconditions:** The login page is visible with empty fields.
- **Steps:**
  1. Enter a username not found in the JSON data file.
  2. Enter a password not paired with that username.
  3. Click the `Login` button.
- **Assertions:**
  - The user remains on `/web/index.php/auth/login`.
  - An `Invalid credentials` error is visible.
  - The Dashboard heading is not visible.
- **Edge cases considered:**
  - Ensure the app does not redirect to a protected page.
  - Validate that failed credentials do not create an authenticated session.

### Scenario 1.3 — Empty username and password submission

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with both fields empty.
- **Steps:**
  1. Click the `Login` button without entering any credentials.
- **Assertions:**
  - Validation errors are shown for Username and Password.
  - The page remains on `/web/index.php/auth/login`.
  - No navigation to dashboard occurs.
- **Edge cases considered:**
  - Confirm the form blocks submission when all required inputs are blank.

### Scenario 1.4 — Username provided, password empty

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is visible and the username field is empty.
- **Steps:**
  1. Fill the Username field with the standard user value from the JSON data file.
  2. Leave the Password field empty.
  3. Click the `Login` button.
- **Assertions:**
  - A required validation message is displayed under Password.
  - No redirection to Dashboard occurs.
  - The login page remains visible.
- **Edge cases considered:**
  - Confirm the username value is not cleared by the failed attempt.

### Scenario 1.5 — Password provided, username empty

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is visible and the password field is empty.
- **Steps:**
  1. Leave Username empty.
  2. Fill the Password field from the JSON data file.
  3. Click the `Login` button.
- **Assertions:**
  - A required validation message is displayed under Username.
  - No redirection to Dashboard occurs.
  - The login page remains visible.
- **Edge cases considered:**
  - Confirm blank username is treated as invalid rather than silently using an empty value.

### Scenario 1.6 — Valid username with incorrect password

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed and both fields are empty.
- **Steps:**
  1. Fill the Username field with the valid username from the JSON data file.
  2. Enter an incorrect password value.
  3. Click the `Login` button.
- **Assertions:**
  - The user remains on the login page.
  - An `Invalid credentials` message is shown.
  - The Dashboard heading is not visible.
- **Edge cases considered:**
  - Ensure a known-good username is not accepted with an incorrect password.

### Scenario 1.7 — Access to forgot password flow

- **Priority:** P2
- **Tags:** @regression
- **Preconditions:** The login page is visible.
- **Steps:**
  1. Click the `Forgot your password?` link.
- **Assertions:**
  - The user is taken to the password reset flow or reset page.
  - The page content clearly reflects a password recovery action.
- **Edge cases considered:**
  - Confirm the link is visible and actionable on the standard login screen.

### Scenario 2.1 — Dashboard loaded after successful login

- **Priority:** P0
- **Tags:** @smoke, @critical
- **Preconditions:** The user is already authenticated and on the Dashboard.
- **Steps:**
  1. Navigate to the dashboard after a successful login using the JSON credentials.
- **Assertions:**
  - The page shows the `Dashboard` heading.
  - The `Admin` link is visible on the navigation area.
  - The URL stays at `/web/index.php/dashboard/index`.
- **Edge cases considered:**
  - Ensure a successful login lands on the correct protected page and not a fallback page.

### Scenario 2.2 — Navigation to Admin area from the dashboard

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The user is authenticated and on the Dashboard.
- **Steps:**
  1. Click the `Admin` navigation link.
- **Assertions:**
  - The browser navigates to the Admin section.
  - The Admin page content is visible.
  - The route reflects the admin area and not the login page.
- **Edge cases considered:**
  - Confirm that the user is not returned to login state when selecting a protected navigation item.

## Not covered (and why)

- Automated social login or SSO flows were not included because the public demo does not expose them.
- Complex role-based user administration was not included because the plan is focused on the standard login and immediate dashboard entry flows.
- API-level auth validation was intentionally left out because this suite is scoped to browser-visible UI behavior.

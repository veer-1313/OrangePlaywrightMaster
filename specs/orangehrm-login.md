# Test Plan: OrangeHRM Login

**Target:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login  
**Seed:** tests/seed.spec.py (not present; use the existing Python `page` fixture)  
**Date:** 2026-09-17

## Overview

This plan covers the OrangeHRM login form, including successful authentication, invalid credentials, and required-field validation using credentials stored in the JSON data file under the data folder.

## Preconditions

- The OrangeHRM login URL is reachable.
- Start every scenario from a fresh login page at `/web/index.php/auth/login`.
- Use the existing Python Playwright pytest `page` fixture.
- Load the username and password values from `tests/data/users.json`.
- Do not reuse authenticated browser state between scenarios.

## Scenarios

### Scenario 1.1 — Standard user successful login

- **Priority:** P0
- **Tags:** @smoke, @critical
- **Preconditions:** The login form is displayed with empty Username and Password fields.
- **Test data:** Values are loaded from `tests/data/users.json`.
- **Steps:**
  1. Fill the Username field with the standard user value from the JSON data file.
  2. Fill the Password field with the matching password value from the JSON data file.
  3. Select the `Login` button — expected: the browser redirects to `/web/index.php/dashboard/index`.
- **Assertions:**
  - The Dashboard heading is visible after login.
  - The Dashboard URL is `/web/index.php/dashboard/index`.
  - The dashboard navigation contains an `Admin` link.
- **Edge cases considered:** Authenticated state must not leak into other scenarios; verify the password is not displayed in plain text.

### Scenario 1.2 — Invalid credentials attempt

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with empty fields.
- **Test data:** Use invalid values that are not present in `tests/data/users.json`.
- **Steps:**
  1. Fill the Username field with an invalid username value.
  2. Fill the Password field with an invalid password value.
  3. Select the `Login` button — expected: the user remains on the login page.
- **Assertions:**
  - An alert with text `Invalid credentials` is visible.
  - The URL remains `/web/index.php/auth/login`.
  - No Dashboard heading is visible.
- **Edge cases considered:** Verify that invalid credentials do not create an authenticated session or redirect to a protected page.

### Scenario 1.3 — Empty username submission

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with both fields empty.
- **Steps:**
  1. Select the `Login` button without entering a username or password — expected: client-side validation runs and the login page remains visible.
- **Assertions:**
  - A `Required` validation message is visible beneath Username.
  - A `Required` validation message is visible beneath Password because both fields are empty.
  - The browser remains on `/web/index.php/auth/login`.
- **Edge cases considered:** Confirm no authentication request succeeds when the username is blank.

### Scenario 1.4 — Empty password submission

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with an empty password field.
- **Steps:**
  1. Fill the Username field with the standard user value from the JSON data file.
  2. Leave Password empty and select the `Login` button — expected: client-side validation runs and the login page remains visible.
- **Assertions:**
  - A `Required` validation message is visible beneath Password.
  - No `Required` message remains beneath Username.
  - The browser remains on `/web/index.php/auth/login`.
- **Edge cases considered:** Confirm the form does not submit with a valid username and blank password.

### Scenario 1.5 — Invalid password for valid username

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with empty fields.
- **Steps:**
  1. Fill the Username field with the valid username from the JSON data file.
  2. Fill the Password field with an incorrect value.
  3. Select the `Login` button — expected: the user remains on the login page.
- **Assertions:**
  - An alert with text `Invalid credentials` is visible.
  - The URL remains `/web/index.php/auth/login`.
  - No Dashboard heading is visible.
- **Edge cases considered:** Verify that a valid username is not accepted with an incorrect password.

## Not covered (and why)

- Password reset flows were not covered because they are outside the requested login scenarios.
- Account lockout thresholds and repeated-attempt behavior were not covered because the public OrangeHRM demo does not expose a distinct locked-account response during the planned browser flow.

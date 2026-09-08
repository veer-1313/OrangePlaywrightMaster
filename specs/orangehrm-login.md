# Test Plan: OrangeHRM Login

**Target:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login  
**Seed:** tests/seed.spec.py (not present; use the existing Python `page` fixture)  
**Date:** 2026-09-08

## Overview

This plan covers the OrangeHRM login form, including successful authentication, credential failures, and required-field validation. The live application accepts `Admin` / `admin123`; the requested `standard_user`, `locked_out_user`, and `secret_sauce` values are Sauce Demo credentials and are not valid OrangeHRM accounts.

## Preconditions

- The OrangeHRM login URL is reachable.
- Start every scenario from a fresh login page at `/web/index.php/auth/login`.
- Use the existing Python Playwright pytest `page` fixture.
- Do not reuse authenticated browser state between scenarios.
- Treat the credentials as test data only; do not commit credentials or storage state.

## Scenarios

### Scenario 1.1 — Standard user successful login with OrangeHRM credentials

- **Priority:** P0
- **Tags:** @smoke, @critical
- **Preconditions:** The login form is displayed with empty Username and Password fields.
- **Test data:** Username `Admin`; Password `admin123`. The requested label `standard_user` is not an OrangeHRM username.
- **Steps:**
  1. Fill the Username field with `Admin` — expected: the Username field contains `Admin`.
  2. Fill the Password field with `admin123` — expected: the Password field contains a masked value.
  3. Select the `Login` button — expected: the browser redirects to `/web/index.php/dashboard/index`.
- **Assertions:**
  - The Dashboard heading is visible after login.
  - The Dashboard URL is `/web/index.php/dashboard/index`.
  - The dashboard navigation contains an `Admin` link.
- **Edge cases considered:** Authenticated state must not leak into other scenarios; verify the password is not displayed in plain text.

### Scenario 1.2 — Locked-out user attempt

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with empty fields.
- **Test data:** Username `locked_out_user`; Password `secret_sauce`.
- **Steps:**
  1. Fill the Username field with `locked_out_user` — expected: the Username field contains the supplied value.
  2. Fill the Password field with `secret_sauce` — expected: the Password field contains a masked value.
  3. Select the `Login` button — expected: the user remains on the login page.
- **Assertions:**
  - An alert with text `Invalid credentials` is visible in the current OrangeHRM build.
  - The URL remains `/web/index.php/auth/login`.
  - No Dashboard heading is visible.
- **Edge cases considered:** OrangeHRM does not expose a distinct locked-account error for this Sauce Demo credential; if a future build adds one, assert the specific locked message instead of the generic alert.

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
  1. Fill the Username field with `Admin` — expected: the Username field contains `Admin`.
  2. Leave Password empty and select the `Login` button — expected: client-side validation runs and the login page remains visible.
- **Assertions:**
  - A `Required` validation message is visible beneath Password.
  - No `Required` message remains beneath Username.
  - The browser remains on `/web/index.php/auth/login`.
- **Edge cases considered:** Confirm the form does not submit with a valid username and blank password.

### Scenario 1.5 — Invalid credentials

- **Priority:** P1
- **Tags:** @regression
- **Preconditions:** The login form is displayed with empty fields.
- **Test data:** Username `invalid_user`; Password `wrong_password`.
- **Steps:**
  1. Fill the Username field with `invalid_user` — expected: the Username field contains the supplied value.
  2. Fill the Password field with `wrong_password` — expected: the Password field contains a masked value.
  3. Select the `Login` button — expected: the user remains on the login page.
- **Assertions:**
  - An alert with text `Invalid credentials` is visible.
  - The URL remains `/web/index.php/auth/login`.
  - No Dashboard heading is visible.
- **Edge cases considered:** Verify that invalid credentials do not create an authenticated session or redirect to a protected page.

## Not covered (and why)

- `standard_user` with `secret_sauce` was not treated as a successful OrangeHRM login because those are Sauce Demo credentials and the target application documents `Admin` / `admin123` on its login page.
- Password reset was not covered because it is outside the requested login scenarios.
- Account lockout thresholds and repeated-attempt behavior were not covered because the public OrangeHRM demo did not expose a distinct locked-account response during exploration.

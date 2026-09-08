# Test Plan: OrangeHRM Standard Login

**Target:** https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

## Scenario 1.1 - Standard user successful login

- **Priority:** P0
- **Tags:** @smoke, @critical
- **Credentials:** Load the `standard` user from `tests/data/users.json`.
- **Preconditions:** The browser starts on a fresh OrangeHRM login page.

### Steps

1. Navigate to the OrangeHRM login page.
2. Fill the Username field with the standard user's username.
3. Fill the Password field with the standard user's password.
4. Select the `Login` button.

### Expected Results

- The browser redirects to `/web/index.php/dashboard/index`.
- The `Dashboard` heading is visible.
- The `Admin` navigation link is visible.

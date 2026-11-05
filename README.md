# qapracticehub-selenium-pytest

UI test automation for [qapracticehub.com](https://qapracticehub.com/), a practice site built for testing. Written in Python with Selenium 4 and Pytest, using the Page Object Model.

I built it to practice automating more than forms and buttons: a login that needs an OTP from a second tab, a sortable and paginated table, a custom multi-select dropdown, and elements whose attributes change while the page is open.

## What is covered

62 tests across seven sections of the site (2 are skipped and 1 is an expected failure, see below):

| Section | What the tests do |
|---|---|
| Buttons | Every button type: click, double click, right click, hover, popup, info tooltips, navigation, disabled state |
| Inputs | Text, email, password, number (min/max, arrow keys), date, time, phone with country prefix, textarea, read-only and disabled fields |
| Forms | Login (valid and invalid), show/hide password, forgot password, registration, clear button |
| Selection | Radio buttons, checkboxes, single and multi select, custom multi-select dropdown, range slider, toggle, autocomplete |
| Tables | Sorting by name and age, filtering, adding one or several users, duplicate ID, row selection |
| OTP login | Missing code, valid code, wrong code, expired code, resend |
| Changing attributes | Elements whose id, data attributes or link href change over time |

## Design choices

- **Explicit waits only.** No `time.sleep` and no `implicitly_wait` anywhere. Every interaction waits for a specific condition (visible, clickable, present), which keeps the tests from depending on timing luck.
- **Stable locators for moving targets.** On the changing-attributes page the element id changes, so those tests locate elements by the attribute the page promises to keep stable (`data-testid`, `data-status`, `data-ready`, `data-epoch`).
- **Known bug recorded as a strict xfail.** The number input accepts a typed value above its `max` of 100. The test asserts the requirement (value stays at or below 100) and is marked `xfail(strict=True)`, so it documents the bug today and fails loudly once the site fixes it.
- **Data read from the page, not copied.** The phone country codes and lengths are read from the page's own country list instead of being hardcoded in the tests, and the table helper walks every page of the table to get the full data set.
- **Strict markers.** Each section has a registered marker, and `--strict-markers` is on, so a typo in a marker is an error, not a silently empty test selection.

## Project layout

```
pages/       page objects, one per site section, built on base_page.py
tests/       one test module per section, plus conftest.py with the driver fixture
pytest.ini   registered markers
```

## Running it

You need Python 3 and Google Chrome. Selenium downloads the matching driver by itself.

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
pytest
```

Run one section by its marker:

```bash
pytest -m buttons_section
pytest -m "tables_section or forms_section"
```

Markers: `buttons_section`, `inputs_section`, `forms_section`, `selection_section`, `tables_section`, `otp_login_section`, `changing_attributes`.

Good to know:

- The tests run against the live site, so they need an internet connection and can break if the site changes.
- Chrome runs headless. This is set in `tests/conftest.py`; remove the `--headless` line to watch the browser.
- The two OTP tests that wait for the code to expire take about 30 seconds each.
- The download button and color picker tests are skipped, because they need extra setup that isn't written yet.

## Known limitations

This is what I would change next, in order:

1. **Page objects are created inside every test.** Each test builds its page object, calls `load()` and, in some cases, dismisses the cookie banner itself. These belong in fixtures in `conftest.py`, so a test starts at the first real step.
2. **No parametrization.** The ten button tests and the login and registration cases are the same test with different data. They should be a few `@pytest.mark.parametrize` tests.
3. **Some expected values live in page objects.** The login success message, the phone validation text and the expected sort order are built inside page-object methods. Page objects should only return what is on the page, and the tests should hold the expectations.
4. **Mostly happy paths.** Missing negative and edge cases include empty login fields, an invalid email format, phone number length, a table filter with no match, validation in the add-user popup and a wrong-length OTP.
5. **No CI, reports or configuration.** There is no GitHub Actions workflow, no screenshot on failure, and the browser mode and base URL are not configurable from the command line.

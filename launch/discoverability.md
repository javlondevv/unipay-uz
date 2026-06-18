# Discoverability setup — run once

These need your GitHub auth. Install the CLI and log in first:

```bash
# https://cli.github.com/
gh auth login
```

All commands target `javlondevv/unipay-uz`.

## 1. Topics (huge for GitHub search + "Explore")

```bash
gh repo edit javlondevv/unipay-uz \
  --add-topic payments \
  --add-topic uzbekistan \
  --add-topic payme \
  --add-topic click \
  --add-topic uzum \
  --add-topic paynet \
  --add-topic octo \
  --add-topic payment-gateway \
  --add-topic django \
  --add-topic fastapi \
  --add-topic flask \
  --add-topic python \
  --add-topic fintech
```

## 2. About sidebar (description + homepage)

```bash
gh repo edit javlondevv/unipay-uz \
  --description "One unified Python API for Uzbekistan's payment gateways — Payme, Click, Uzum, Paynet & Octo. Django, FastAPI & Flask ready." \
  --homepage "https://pypi.org/project/unipay-uz/"
```

## 3. Enable Discussions

```bash
gh repo edit javlondevv/unipay-uz --enable-discussions
```
(If your `gh` version lacks the flag, toggle it in **Settings → Features → Discussions**.)

## 4. Labels for newcomers

```bash
gh label create "good first issue" --color 7057ff --description "Good for newcomers" --repo javlondevv/unipay-uz --force
gh label create "help wanted"      --color 008672 --description "Extra attention is welcome" --repo javlondevv/unipay-uz --force
gh label create "enhancement"      --color a2eeef --description "New feature or request" --repo javlondevv/unipay-uz --force
gh label create "discussion"       --color d4c5f9 --description "Open-ended discussion" --repo javlondevv/unipay-uz --force
gh label create "documentation"    --color 0075ca --description "Docs and examples" --repo javlondevv/unipay-uz --force
```

## 5. Starter issues

These give first-time contributors a clear way in (and signal an active project).
Run each `gh issue create`:

### Issue 1 — tests for Payme/Click signature verification · `good first issue`
```bash
gh issue create --repo javlondevv/unipay-uz \
  --title "Add unit tests for Payme & Click webhook signature verification" \
  --label "good first issue" --label "help wanted" \
  --body "We don't yet have automated tests covering signature/auth verification for incoming webhooks.

**Goal:** add \`pytest\` tests that feed known-good and known-bad signatures to the Payme and Click webhook verifiers and assert accept/reject.

**Where:** \`unipay_uz/gateways/payme/\` and \`unipay_uz/gateways/click/\`; add a \`tests/\` package at the repo root.

**Why it's friendly:** isolated, no live credentials needed (use fixtures), and it makes the CI meaningfully green. Ping here if you want pointers to the verification functions."
```

### Issue 2 — Octo usage example in the README · `good first issue`
```bash
gh issue create --repo javlondevv/unipay-uz \
  --title "Add an Octo usage example to the README" \
  --label "good first issue" --label "documentation" \
  --body "The README documents Payme, Click, Uzum and Paynet quickstarts but Octo only appears in the feature list.

**Goal:** add a short, copy-pasteable Octo \`create_payment\` example (English README + \`README.ru.md\`).

**Why it's friendly:** docs-only, great first PR. See the existing provider examples for the format."
```

### Issue 3 — full FastAPI integration example · `help wanted`
```bash
gh issue create --repo javlondevv/unipay-uz \
  --title "Add an end-to-end FastAPI integration example" \
  --label "help wanted" --label "enhancement" \
  --body "The README has a deep Django blueprint but FastAPI only gets an install extra.

**Goal:** add an \`examples/fastapi_app/\` minimal app: create a payment, mount the webhook route(s), and mark an order paid on callback.

**Why it matters:** FastAPI is a big slice of our audience and this is the most-requested 'how do I wire it up' case."
```

### Issue 4 — Uzbek README · `help wanted`
```bash
gh issue create --repo javlondevv/unipay-uz \
  --title "Add Uzbek translation: README.uz.md" \
  --label "help wanted" --label "documentation" \
  --body "We have English (\`README.md\`) and Russian (\`README.ru.md\`). An Uzbek (\`README.uz.md\`) version would reach a lot of local developers directly.

**Goal:** translate the README to Uzbek and add \`O‘zbekcha\` to the language switcher line at the top of all README variants.

**Why it's friendly:** no code, high local impact. Native/fluent Uzbek speakers especially welcome."
```

## 6. Awesome-list submissions (durable, high-quality traffic)

Each is a small PR adding one line to a curated list. Lead the PR with *why it
belongs*, not "please add my repo."

- **awesome-python** (`vinta/awesome-python`) → *Third-party APIs* / payment section:
  ```markdown
  * [UniPay UZ](https://github.com/javlondevv/unipay-uz) - Unified API for Uzbekistan payment gateways (Payme, Click, Uzum, Paynet, Octo) with Django, FastAPI and Flask integrations.
  ```
- **awesome-django** (`wsvincent/awesome-django` or `shahraizali/awesome-django`) → *Payments / Third-party*:
  ```markdown
  * [UniPay UZ](https://github.com/javlondevv/unipay-uz) - Django integration for Uzbekistan payment systems (Payme, Click, Uzum, Paynet, Octo) with webhook base views.
  ```
- **awesome-fastapi** (`mjhea0/awesome-fastapi`) → *Third-party extensions / utils*:
  ```markdown
  * [UniPay UZ](https://github.com/javlondevv/unipay-uz) - Uzbekistan payment gateways (Payme, Click, Uzum, Paynet, Octo) with first-class FastAPI support.
  ```
- **Regional lists** — search GitHub for `awesome uzbekistan`, `awesome-uz`, and CIS/Central-Asia dev lists; PR the same one-liner. Also post in local dev Telegram channels (see `social.md`).

# Changelog

All notable changes to this project are documented here. This project adheres to
[Semantic Versioning](https://semver.org) and the
[Keep a Changelog](https://keepachangelog.com) format.

## [Unreleased]

### Added
- `LICENSE` file (MIT) at the repository root.
- `README.ru.md` — Russian translation, with a language switcher in both READMEs.
- Project banner (`assets/banner.svg`), expanded badges, and a "Support the
  project" section with a GitHub Buttons embed snippet.
- Repository hygiene: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, issue and pull
  request templates, `FUNDING.yml`, and a CI workflow.

### Fixed
- README license link pointed to a nonexistent `LICENSE.txt`; now points to
  `LICENSE`.
- `__version__` in `unipay_uz/__init__.py` was `1.0.0` while `pyproject.toml`
  declared `1.0.1`; the two are now in sync.

## [1.0.1] - 2026-02-28

### Fixed
- Corrected the repository URL in project links.

## [1.0.0] - 2026-02-28

### Added
- Initial release: unified payment library for Uzbekistan.
- Gateways: Payme, Click, Uzum, Paynet, Octo.
- Framework integrations for Django, FastAPI, and Flask.
- Webhook base classes and a gateway factory.

[Unreleased]: https://github.com/javlondevv/unipay-uz/compare/v1.0.1...HEAD
[1.0.1]: https://github.com/javlondevv/unipay-uz/releases/tag/v1.0.1
[1.0.0]: https://github.com/javlondevv/unipay-uz/releases/tag/v1.0.0

# Data Handling Principles

FALCON is intended for identity-document screening, so data minimization is a
core engineering requirement.

## Rules

1. Never commit real identity documents containing personal information.
2. Prefer synthetic or properly authorized datasets.
3. Redact identifiers in screenshots used for demos.
4. Keep raw sensitive data outside the public repository.
5. Document dataset provenance and licensing.
6. Separate training, validation, and test data.
7. Log model decisions without unnecessarily retaining raw identity documents.
8. Add access controls before any real deployment.

This document describes engineering principles, not legal advice.

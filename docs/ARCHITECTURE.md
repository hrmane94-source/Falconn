# FALCON Architecture

```text
                    +----------------------+
                    | Document / Live Face |
                    +----------+-----------+
                               |
                               v
                    +----------------------+
                    | Capture & Preprocess |
                    +----------+-----------+
                               |
          +--------------------+--------------------+
          |                    |                    |
          v                    v                    v
       OCR /              Forensics            Face / Liveness
      Validation          & Tamper Check          Verification
          |                    |                    |
          +--------------------+--------------------+
                               |
                               v
                    +----------------------+
                    | Explainable Risk     |
                    | Decision Engine      |
                    +----------+-----------+
                               |
                 +-------------+-------------+
                 |                           |
                 v                           v
             VERIFIED                     REVIEW
                                      / HIGH RISK
                               |
                               v
                    +----------------------+
                    | Audit / Report Layer |
                    +----------------------+
```

The architecture is modular so individual components can be tested independently.

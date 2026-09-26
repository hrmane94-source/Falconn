# FALCON — AI-Based Fake Identity & Document Screening

> SIH 2026 project — development repository

FALCON is an AI-assisted identity and document screening system designed to detect
forged, tampered, inconsistent, expired, or suspicious identity documents and
support live face verification.

## Current status

- [x] Project repository initialized
- [x] Initial application structure
- [x] Upload/API prototype
- [ ] OCR pipeline
- [ ] Document validation rules
- [ ] Image-forensics pipeline
- [ ] Face verification + liveness
- [ ] Training dataset generation
- [ ] Model training
- [ ] End-to-end risk scoring
- [ ] Evaluation on held-out test data

**Important:** the current application is a prototype scaffold. It does NOT yet
claim to detect forged documents accurately. Detection claims will be added only
after models/rules are implemented and evaluated.

## Architecture

```text
Document / Live Capture
        |
        v
   FastAPI Backend
        |
        +--> OCR & Field Validation
        +--> Document Forensics
        +--> Face Verification
        +--> Expiry / Consistency Checks
        |
        v
   Risk / Decision Engine
        |
        v
 Verification Report
```

## Planned document coverage

- Aadhaar
- PAN
- Passport
- Visa / visa stamps
- Driving Licence
- Government / competitive-exam hall tickets

## Dataset plan

We will maintain separate documentation for genuine and synthetic/forged
samples. Do not commit real people's identity documents or sensitive personal
data to this repository.

## Local setup

### 1. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start the API

```powershell
uvicorn backend.main:app --reload
```

Open:

- http://127.0.0.1:8000
- http://127.0.0.1:8000/docs

## Development rule

Every meaningful milestone should be committed with a clear message, for example:

```text
feat: add OCR preprocessing
feat: add DOB consistency validation
feat: add forgery dataset generator
test: evaluate OCR field extraction
docs: update model evaluation results
```

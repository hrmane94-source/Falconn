# FALCON Development Roadmap

## Phase 0 — Foundation
- [x] Repository structure
- [x] FastAPI API
- [x] Upload flow
- [x] Basic screening UI

## Phase 1 — Document intake
- [ ] Image quality / blur detection
- [ ] Rotation correction
- [ ] Glare detection
- [ ] Document-type classification

## Phase 2 — OCR & validation
- [ ] OCR extraction
- [ ] DOB/date validation
- [ ] Expiry validation
- [ ] Field consistency checks
- [ ] QR/barcode/checksum validation where applicable

## Phase 3 — Document forensics
- [ ] ELA baseline
- [ ] Noise/resampling analysis
- [ ] Copy-paste / splice detection
- [ ] Metadata inspection
- [ ] Forged stamp detection

## Phase 4 — Identity verification
- [ ] Face detection
- [ ] Face embedding comparison
- [ ] Liveness module
- [ ] Threshold calibration

## Phase 5 — Risk engine
- [ ] Weighted evidence model
- [ ] Explainable risk score
- [ ] PASS / REVIEW / HIGH-RISK states
- [ ] Audit record

## Phase 6 — Dataset & model
- [ ] Synthetic forgery generator
- [ ] Annotation format
- [ ] Train/validation/test split
- [ ] Baseline model
- [ ] Evaluation metrics
- [ ] Error analysis

## Phase 7 — End-to-end demo
- [ ] Connect all modules
- [ ] Generate verification report
- [ ] Add demo cases
- [ ] Performance measurement
- [ ] Security review

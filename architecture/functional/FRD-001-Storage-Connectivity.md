# Functional Requirements Document (FRD-001)

## Title
Storage Connectivity for Setup and Transactional Data (Local Storage or Google Sheets)

## Version
v0.1 (Initial)

## Date
2026-03-01

## Author
Omniclaw Product Manager

---

## 1. Purpose
Define the first functional requirements for enabling Omniclaw to persist and retrieve:
1. **Setup Data** (configuration and initial system data)
2. **Transactional Data** (runtime actions, logs, and operation records)

The system must support **two interchangeable storage providers**:
- **Local Storage** (default)
- **Google Sheets** (optional)

---

## 2. Scope

### In Scope
- Configurable storage backend selection: Local Storage or Google Sheets
- Create, read, update, and append operations for setup and transactional datasets
- Backend-specific initialization and connectivity checks
- Validation, basic error handling, and retry behavior for storage operations

### Out of Scope (for this phase)
- Advanced analytics/reporting dashboards
- Multi-tenant isolation model
- Complex archival and data retention policies
- Bidirectional sync between both backends at the same time

---

## 3. Business Goals
- Ensure Omniclaw can run in low-dependency mode using Local Storage.
- Enable no-code visibility/editing of data through Google Sheets.
- Maintain consistent behavior across both backends through a unified storage contract.

---

## 4. User Roles
- **Admin/User**: Configures and uses Omniclaw.
- **System**: Reads/writes setup and transactional data during execution.

---

## 5. Functional Requirements

### 5.1 Storage Backend Configuration
- **FR-001**: System shall provide a configuration key `storage.provider` with valid values: `local` or `google_sheets`.
- **FR-002**: System shall default to `local` when provider is not configured.
- **FR-003**: System shall validate the configured provider at startup and fail fast with a clear error if invalid.

### 5.2 Local Storage Connectivity
- **FR-004**: When provider is `local`, system shall initialize local persistence using **CSV files only** in a configured path.
- **FR-005**: System shall create required CSV files if they do not exist.
- **FR-006**: System shall verify read/write access during startup health check.

### 5.3 Google Sheets Connectivity
- **FR-007**: When provider is `google_sheets`, system shall authenticate via configured Google credentials.
- **FR-008**: System shall connect to a configured Spreadsheet ID and expected sheet names.
- **FR-009**: System shall validate sheet availability at startup and return actionable errors if missing/inaccessible.
- **FR-010**: System shall support append and row-update operations for transactional rows.

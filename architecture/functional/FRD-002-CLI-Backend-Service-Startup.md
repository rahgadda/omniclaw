# Functional Requirements Document (FRD-002)

## Title
CLI for Backend Service Startup with Environment and JSON Transaction Variables

## Version
v0.1 (Initial)

## Date
2026-03-01

## Author
Omniclaw Product Manager

---

## 1. Purpose
Define functional requirements for a command-line interface (CLI) that starts Omniclaw backend services and supports:
1. Installation/runtime variables passed as environment variables.
2. Transaction variables passed through JSON, with support to update and refresh values when required.

---

## 2. Scope

### In Scope
- CLI command(s) to start one or more backend services.
- Environment variable ingestion for installation/runtime settings.
- JSON-based transaction variable input.
- Update and refresh behavior for transaction variable JSON.
- Startup validation and user-facing CLI error messages.

### Out of Scope
- UI dashboard for configuration editing.
- Distributed orchestration across multiple hosts.
- Long-term storage design of transaction history.

---

## 3. User Roles
- **Operator/Admin**: Executes CLI and provides configuration.
- **System**: Validates inputs and starts backend service processes.

---

## 4. Functional Requirements

### 4.1 CLI Startup Command
- **FR-001**: System shall provide a CLI command to start backend services (example: `omniclaw start`).
- **FR-002**: CLI shall support starting all backend services or a specific service by name.
- **FR-003**: CLI shall provide `--help` output describing command usage, required inputs, and examples.

### 4.2 Installation Variables via Environment
- **FR-004**: CLI shall read installation/runtime variables from environment variables.
- **FR-005**: CLI shall validate required environment variables before service startup.
- **FR-006**: If required environment variables are missing or invalid, CLI shall fail with clear validation errors.
- **FR-007**: CLI shall log which variables are missing by key name, masking any secret values.

### 4.3 Transaction Variables via JSON
- **FR-008**: CLI shall accept transaction variables as JSON input (file path and/or inline JSON string).
- **FR-009**: CLI shall validate JSON format and required transaction keys before startup.
- **FR-010**: CLI shall pass validated transaction variables to backend services at runtime.

### 4.4 Transaction Variable Update and Refresh
- **FR-011**: System shall support updating transaction variables by supplying a new JSON payload.
- **FR-012**: System shall support refreshing active transaction variables without restarting the full platform when feasible.
- **FR-013**: On refresh failure, CLI shall preserve the last valid transaction variable set and return an actionable error.

### 4.5 Startup and Runtime Feedback
- **FR-014**: CLI shall print startup status for each backend service (starting/running/failed).
- **FR-015**: CLI shall return non-zero exit code if startup validation fails or any required service fails to start.
- **FR-016**: CLI shall provide a success summary that includes loaded environment profile and transaction JSON source.
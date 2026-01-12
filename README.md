# simple-test-client

`simple-test-client` is a lightweight Python project that demonstrates how to implement and run a simple client application for testing purposes. It is intended as a minimal example that can be used to experiment with client-side logic, such as working with files (for example, audio files), sending requests, or validating integrations without relying on complex frameworks.

The project is intentionally small and easy to understand, making it suitable for quick tests, demos, or as a starting point for building a more advanced client.

---

## Purpose

The main goals of this test client are:

- To provide a **minimal Python client** that can be run locally.
- To serve as a **sandbox for experimenting** with client-side logic (e.g. file handling, API calls, or basic processing).
- To act as a foundation that can be extended for more advanced testing scenarios.

A sample audio file is included to make it easier to test workflows that involve reading or sending binary data.

---

## Prerequisites

Before running this test client, make sure you have the following installed:

- **Python 3.8 or newer**
  Verify your Python version:

  ```bash
  python --version

  ```

- **(Optional) Create and activate a virtual environment**

  ```bash
  python -m venv venv
  source venv/bin/activate    # macOS / Linux
  venv\Scripts\activate
  ```

- **Python libs**
  Install libs

  ```
  pip install -r requirements.txt
  ```

- **Authenticated gcloud cli for remote testing**
  Verify you are authenticated

  ```bash
  gcloud auth list
  ```

## Usage

- Local usage
  By default local address will be used

  ```bash
  python3 test.py

  ```

- Remote
  Please provide `ID_TOKEN` with GCP [identity token](https://docs.cloud.google.com/docs/authentication/get-id-token) to auth

  ```bash
  ID_TOKEN="$(gcloud auth print-identity-token)" WS_URL=wss://<APP_URL>/ws  python3 test.py
  ```

## Environment Variables

The test client can be configured using the following environment variables:

| Variable   | Required | Description                                                                               |
| ---------- | -------- | ----------------------------------------------------------------------------------------- |
| `WS_URL`   | No       | WebSocket endpoint URL. If not provided, a default local address is used.                 |
| `ID_TOKEN` | No\*     | Google Cloud identity token used for authentication when connecting to a remote endpoint. |

\* `ID_TOKEN` is required when connecting to a remote WebSocket endpoint that requires authentication.

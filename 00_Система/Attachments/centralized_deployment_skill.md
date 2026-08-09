---
memory_id: 1738e876-45ef-4a1e-81d1-55cdff1e0504
hash: 97412844037baba635d5767e69ffee13
last_indexed: '2026-07-07T09:37:12.569360'
---
# Skill: Centralized Deployment Configuration

**Purpose**: Provide a guideline for projects that need to run in multiple environments (local development, cloud platforms such as Amvera, etc.).

**Key Principle**:
- All external service URLs (API, frontend, static assets) must be defined in a single configuration module/file.
- The application reads the appropriate value based on environment variables.
- For local development, sensible defaults (e.g., `http://127.0.0.1:8000`) are used.
- For production platforms, the values are overridden by environment variables supplied by the platform (e.g., `NEXT_PUBLIC_API_URL`, `FRONTEND_URL`, `BACKEND_URL`).

**Implementation Steps**:
1. **Create a central config file** (e.g., `frontend/src/config.ts` for a Next.js frontend) that exports constants like `API_URL`.
   ```ts
   const LOCAL_API_URL = 'http://127.0.0.1:8000';
   export const API_URL = process.env.NEXT_PUBLIC_API_URL || LOCAL_API_URL;
   ```
2. **Backend equivalents** – use `os.getenv('FRONTEND_URL', 'http://localhost:3000')` and `os.getenv('BACKEND_URL', 'http://127.0.0.1:8000')`.
3. **Import the constants** in every place where URLs are built (fetch calls, email templates, static file links, etc.).
4. **Do not hard‑code URLs anywhere else**. If a fallback is needed, use the same pattern.
5. **Document** the required environment variables in deployment manuals.

**Benefits**:
- One‑point change when moving between environments.
- Reduces risk of broken links in production.
- Improves maintainability and readability.

**Usage Example**:
- In a component:
  ```tsx
  import { API_URL } from '@/config';
  fetch(`${API_URL}/api/v1/items`);
  ```
- In FastAPI email verification:
  ```python
  frontend_url = os.getenv('FRONTEND_URL', 'http://localhost:3000')
  body = f"... {frontend_url}/verify?token={token} ..."
  ```

**Add this skill to the AGrav knowledge base** to ensure future projects follow the same pattern.

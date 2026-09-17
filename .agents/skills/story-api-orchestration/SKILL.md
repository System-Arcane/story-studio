---
name: story-api-orchestration
description: Design or implement authorized STory async jobs, provider integration contracts, result storage and failure recovery.
---

# story-api-orchestration

Check the current scope first. Frontend mockup work authorizes no backend implementation, provider calls or spending. Under an explicit backend task, define request/result/error contracts before parallel consumption and reconcile them with runtime validation.
Include user story selection before video submission. Persist STory job ID and provider job ID, stage results, terminal errors and expiry decisions. Use a durable worker/queue appropriate to deployment; an HTTP 202 alone does not keep work running.
Prevent duplicate submits. A timeout is not proof of submission failure: resolve the original job or use a documented provider idempotency mechanism before retrying. Bound retries by operation, cost and error class; reuse completed stages. Keep secrets server-side.
GPT Image 2/Seedance 2.5 are the chosen future pipeline. MCP access from this conversation does not establish web-server authentication or subscription billing. Verify these interfaces. Retention, access controls and exhibition codes require explicit implementation decisions; do not assume an arbitrary retention period is agreed.

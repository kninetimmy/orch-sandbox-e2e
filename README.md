# orch-sandbox-e2e

Throwaway sandbox repository for the Orch task-18 end-to-end smoke test:
one real Delivery cycle driven by Claude Code through the `orch` binary
and the `adapters/claude` plugin.

Not a real project. Safe to delete after the milestone is recorded.

- `greet.py` — the trivial code surface Delivery changes target.
- `.github/workflows/ci.yml` — a fast CI check so the required-CI wait
  is exercised for real. It fails if a `.ci-fail` file exists, which
  lets a probe branch produce a genuinely failing check on demand.

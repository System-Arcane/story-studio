---
name: story-quality-review
description: Independently review STory mockup flows, storage boundaries, accessibility and future API contracts with evidence.
---

# story-quality-review

Read docs/QUALITY.md and the assigned implementation. Review both sides of boundaries: input and validator, saved payload and restore code, selected story and result, route and link. API checks apply only when an API exists.
Prioritize corrupt saved objects, oversized data URLs, stale result links after failed saves, timer/playback lifecycle and mobile keyboard/selection semantics. Use reproducible cases rather than style preferences.
Report severity, file location, trigger, expected/actual behavior and proposed repair. Separate confirmed findings, risks and unverified behavior. Do not treat successful compilation as UX proof. Default to read-only review; builds may write .next and must be delegated to the main agent if permissions prohibit them. Do not operate the shared browser concurrently. Do not edit the implementation being reviewed.

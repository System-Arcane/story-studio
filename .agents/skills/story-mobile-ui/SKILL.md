---
name: story-mobile-ui
description: Implement or review STory mobile UI, upload, story selection, mock progress and result restoration.
---

# story-mobile-ui

Use docs/PROJECT-BRIEF.md and docs/QUALITY.md in the repository root. Current files are app/, not src/app/. Preserve existing CSS and design rather than introducing a UI stack.
Flow: photo -> editable name/category/feature -> hero or final reveal -> humor/emotion/happiness -> generation -> result. Story cards expose title, plot and remembered product impression.
Validate files and saved data before rendering. Treat JSON parsing as distinct from schema validation. A failed save must not produce a link silently restoring the previous result. Reset playback and timers on relevant transitions.
Verify 360-430px mobile and desktop layout, keyboard access, meaningful labels, selected states and step focus. Actual mock state must be distinguished from generated video/audio and cross-device sharing. No logo/watermark insertion in output video. Contracts must agree with types and implementation; a document alone is insufficient evidence.

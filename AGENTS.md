<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

# STory 개발 지도

- 전문 에이전트·스킬 목록: [docs/AGENT-TEAM.md](docs/AGENT-TEAM.md).
- 첫 `/goal`과 멀티 에이전트 실행은 [목표 제안](docs/plans/goal-proposal.md)을 사용자와 논의한 후 시작한다. 현재 설정만 완료하며 실행은 대기한다.

- 현재 범위: 프론트엔드 목업. 백엔드·AI 생성·과금 호출을 연결하지 않는다.
- 제품 결정: [docs/PROJECT-BRIEF.md](docs/PROJECT-BRIEF.md).
- 현재 구조와 목표 경계: [ARCHITECTURE.md](ARCHITECTURE.md).
- 역할 분담과 피드백 루프: [docs/HARNESS.md](docs/HARNESS.md).
- 완료 기준과 남은 문제: [docs/QUALITY.md](docs/QUALITY.md).
- 실행 방법: [README.md](README.md). 기본 검증은 `npm run verify`.
- 독립된 분석·구현·검토 작업에는 서브 에이전트를 활용한다. 사소한 단일 수정은 직접 처리한다.
- 메인 에이전트가 작업별 담당 파일을 지정한다. 같은 파일의 동시 수정을 금지한다.
- 다른 작업자의 변경을 되돌리지 않는다. 공통 파일과 최종 통합은 메인이 담당한다.
- 요구사항 변경 시 해당 기준 문서도 갱신한다. 계획·구현·검증 완료를 구분해서 보고한다.
- AGENTS.md는 짧은 지도이며 상세 지침은 연결된 문서에서 필요한 것만 읽는다.

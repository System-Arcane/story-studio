# STory 전문 에이전트 팀

## 프로젝트 설치
- [story-frontend](../.codex/agents/story-frontend.toml): UI와 클라이언트 상태. [모바일 스킬](../.agents/skills/story-mobile-ui/SKILL.md).
- [story-narrative](../.codex/agents/story-narrative.toml): 서사·레퍼런스·프롬프트 설계. [서사 스킬](../.agents/skills/story-narrative-engine/SKILL.md).
- [story-backend](../.codex/agents/story-backend.toml): 향후 허가된 백엔드 작업. [API 스킬](../.agents/skills/story-api-orchestration/SKILL.md).
- [story-qa](../.codex/agents/story-qa.toml): 독립 읽기 전용 검토. [QA 스킬](../.agents/skills/story-quality-review/SKILL.md).
- 메인 에이전트는 [story-orchestrator](../.agents/skills/story-orchestrator/SKILL.md)를 적용해 조율한다. 메인을 별도 자식 에이전트로 중복 생성하지 않는다.

## 적용 범위
프로젝트 단위 등록. 모델/추론 강도/연결 서비스는 상속하며 전역 설정은 변경하지 않았다. QA TOML은 read-only 기본값을 지정한다. 실제 권한은 런타임 상속/override에 영향을 받으므로 파일만으로 격리를 보장하지 않는다.

현재 대화 도구는 custom agent 이름 선택 필드를 노출하지 않는다. 이후 실행 시 네이티브 선택이 가능하면 해당 역할을 사용하고, 그렇지 않으면 메인이 TOML 지침과 스킬 경로를 읽어 작업 프롬프트에 전달한다. 후자는 역할 위임이며 네이티브 프로필/권한 적용 검증과 구분한다. 새 세션에서 자동 발견 여부 확인이 필요할 수 있다.

## 현재 검증 상태
2026-09-14: 에이전트 TOML 4개 파싱/필수 필드 검사, 스킬 5개 공식 quick_validate, npm run verify 통과. 검증용 PyYAML은 git 제외된 .harness-tools에만 설치.
파일 생성·정적 형식 검증 대상이며 실제 역할 호출/행동 테스트는 사용자와 목표 합의 후 수행한다. 설치 확인을 위해 에이전트를 임의 실행하지 않는다. 목표 예산을 임의 설정하지 않는다.

설치 스크립트는 `scripts/setup-story-team.py`이며 기존 내용이 다르면 덮어쓰지 않는다. 이후 정의 파일 수정 시 설치 스크립트도 함께 갱신한다.

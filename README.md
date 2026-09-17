# STory

음식·음료 사진에서 시작하는 서사형 광고 제작 스튜디오의 프론트엔드 목업입니다.

## 실행
```sh
npm install
npm run dev
```
브라우저에서 http://localhost:3000 을 엽니다.

```sh
npm run build
npm start
npm run typecheck
```

`/`에서 사진 업로드, 상품 정보 수정, 이야기 선택, 제작 시뮬레이션, 결과 복원까지 체험할 수 있습니다. `/admin`은 인증 없는 개발용 예시 화면입니다.

AI/API 호출, 배경 제거, 실제 영상/음성 생성, 서버 저장은 없습니다. 결과 링크는 동일 브라우저 localStorage 복원용입니다. 사용자 사진은 서버에 업로드되지 않습니다. 폰트는 Google Fonts를 사용하며 연결되지 않으면 시스템 폰트로 표시됩니다.

상세 결정 사항: [docs/PROJECT-BRIEF.md](docs/PROJECT-BRIEF.md)

개발 지침 지도: [AGENTS.md](AGENTS.md) · [아키텍처](ARCHITECTURE.md) · [협업 하네스](docs/HARNESS.md) · [품질 기준](docs/QUALITY.md)

통합 검사: `npm run verify` (문서 링크 → 빌드 → 타입 검사). 브라우저 동작은 별도로 확인합니다.

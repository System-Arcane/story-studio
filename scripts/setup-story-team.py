"""Install the reviewed STory definitions in this repository; never overwrite existing files."""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]
COMMON = '''Read AGENTS.md, docs/PROJECT-BRIEF.md and docs/HARNESS.md from the STory repository first. Preserve the current frontend-only mockup scope. Follow the main agent's assigned files and completion criteria; do not modify another worker's files. Do not submit AI generations or start a goal. Return evidence, changed files, verification and unresolved issues. Read your assigned SKILL.md before substantive work. Model and reasoning inherit from the parent. Project paths below are relative to the repository root.'''
ROLES = {
 'story-frontend': ('Mobile frontend implementation and client state for STory.', 'story-mobile-ui', 'Own assigned UI/components/client state only. Preserve the sky blue, white, gray and red visual direction. Do not add video watermarks or backend calls. Verify relevant mobile and keyboard flows.'),
 'story-narrative': ('STory narrative design and reference-based video prompt specifications.', 'story-narrative-engine', 'Own assigned narrative mock data or prompt specifications. Use humor, emotion and happiness with a concrete product connection. Future generation uses GPT Image 2 references and Seedance 2.5; do not replace these models or generate media during mockup work.'),
 'story-backend': ('Future STory async generation contracts and backend implementation when authorized.', 'story-api-orchestration', 'During frontend-only work, restrict output to an explicitly assigned contract/design review; do not implement API routes or storage. Implement backend only after the user expands scope. Preserve provider job IDs and resolve unknown submissions before retries.'),
 'story-qa': ('Independent STory correctness, boundary and UX review.', 'story-quality-review', 'Read-only reviewer: do not edit source or install dependencies. Compare producers and consumers, storage and rendering, documented behavior and actual behavior. Return passed/failed/unverified separately with reproduction and file references. Ask the main agent to run checks needing writes or shared browser control.')
}
SKILLS = {
 'story-orchestrator': ('Coordinate STory development across specialist agents for multi-part implementation or review; ordinary questions need no delegation.', '''Read AGENTS.md and docs/HARNESS.md from the repository root. Check docs/plans/goal-proposal.md: the first multi-agent run is pending user discussion and authorization. Environment setup alone must not launch agents or create a goal.
After authorization, choose only relevant specialists from .codex/agents/. Assign objective, owned files, dependencies and acceptance criteria. Keep shared files and integration with the main agent. Maximum concurrency follows the runtime; current session supports main plus three workers. Define four roles but schedule them as needed.
Use native custom-agent selection if exposed. If the tool only accepts a task name and prompt, read the TOML and pass its developer instructions plus skill path explicitly; this is role prompting, not proof of native registration or sandbox enforcement. State that distinction. Never invent TeamCreate/TaskCreate tools.
Record decisions and evidence in docs/plans/. Run incremental independent QA after meaningful changes, then npm run verify and relevant browser checks. Stop when the agreed criteria are met; unresolved external dependencies require an honest report. Do not enable /goal, scheduled runs or model spending merely because this skill is loaded.'''),
 'story-mobile-ui': ('Implement or review STory mobile UI, upload, story selection, mock progress and result restoration.', '''Use docs/PROJECT-BRIEF.md and docs/QUALITY.md in the repository root. Current files are app/, not src/app/. Preserve existing CSS and design rather than introducing a UI stack.
Flow: photo -> editable name/category/feature -> hero or final reveal -> humor/emotion/happiness -> generation -> result. Story cards expose title, plot and remembered product impression.
Validate files and saved data before rendering. Treat JSON parsing as distinct from schema validation. A failed save must not produce a link silently restoring the previous result. Reset playback and timers on relevant transitions.
Verify 360-430px mobile and desktop layout, keyboard access, meaningful labels, selected states and step focus. Actual mock state must be distinguished from generated video/audio and cross-device sharing. No logo/watermark insertion in output video. Contracts must agree with types and implementation; a document alone is insufficient evidence.'''),
 'story-narrative-engine': ('Design STory humor, emotional and happy product narratives, mock story cards, reference sheets and future Seedance prompts.', '''Use confirmed food/drink product details from docs/PROJECT-BRIEF.md. Do not infer taste, ingredients or health claims from a photo. Each candidate needs title, short plot, remembered impression and a reason tied to the product. Honor hero vs final reveal. Produce original stories inspired by general narrative structures.
During mockup work only create assigned text/data; no model calls. For authorized future generation: preserve original product image -> GPT Image 2 background cleanup/prop sheet -> selected story -> only needed character/location sheets -> Seedance 2.5 omni-reference 30-second vertical generation. Verify the current official guide and actual tool schema before submission. Do not impose start/end frames or split generation into short clips by default. Do not invent invisible packaging details. Track reference roles explicitly and describe pacing, action and audio. Subtitles must be readable; output fidelity is verified rather than guaranteed.'''),
 'story-api-orchestration': ('Design or implement authorized STory async jobs, provider integration contracts, result storage and failure recovery.', '''Check the current scope first. Frontend mockup work authorizes no backend implementation, provider calls or spending. Under an explicit backend task, define request/result/error contracts before parallel consumption and reconcile them with runtime validation.
Include user story selection before video submission. Persist STory job ID and provider job ID, stage results, terminal errors and expiry decisions. Use a durable worker/queue appropriate to deployment; an HTTP 202 alone does not keep work running.
Prevent duplicate submits. A timeout is not proof of submission failure: resolve the original job or use a documented provider idempotency mechanism before retrying. Bound retries by operation, cost and error class; reuse completed stages. Keep secrets server-side.
GPT Image 2/Seedance 2.5 are the chosen future pipeline. MCP access from this conversation does not establish web-server authentication or subscription billing. Verify these interfaces. Retention, access controls and exhibition codes require explicit implementation decisions; do not assume an arbitrary retention period is agreed.'''),
 'story-quality-review': ('Independently review STory mockup flows, storage boundaries, accessibility and future API contracts with evidence.', '''Read docs/QUALITY.md and the assigned implementation. Review both sides of boundaries: input and validator, saved payload and restore code, selected story and result, route and link. API checks apply only when an API exists.
Prioritize corrupt saved objects, oversized data URLs, stale result links after failed saves, timer/playback lifecycle and mobile keyboard/selection semantics. Use reproducible cases rather than style preferences.
Report severity, file location, trigger, expected/actual behavior and proposed repair. Separate confirmed findings, risks and unverified behavior. Do not treat successful compilation as UX proof. Default to read-only review; builds may write .next and must be delegated to the main agent if permissions prohibit them. Do not operate the shared browser concurrently. Do not edit the implementation being reviewed.''')
}

def files():
    result = {}
    for name, (desc, skill, instructions) in ROLES.items():
        text = f'name = {json.dumps(name)}\ndescription = {json.dumps(desc)}\n'
        if name == 'story-qa': text += 'sandbox_mode = "read-only"\n'
        text += 'developer_instructions = """\n' + COMMON + '\nRead .agents/skills/' + skill + '/SKILL.md.\n' + instructions + '\n"""\n'
        result[ROOT / '.codex' / 'agents' / (name + '.toml')] = text
    for name, (desc, body) in SKILLS.items():
        result[ROOT / '.agents' / 'skills' / name / 'SKILL.md'] = f'---\nname: {name}\ndescription: {desc}\n---\n\n# {name}\n\n{body}\n'
    return result

if __name__ == '__main__':
    planned = files()
    for target, content in planned.items():
        if target.exists() and target.read_text(encoding='utf-8') != content:
            raise SystemExit(f'Refusing to overwrite existing configuration: {target}')
    for target, content in planned.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding='utf-8')
        print(target.relative_to(ROOT))

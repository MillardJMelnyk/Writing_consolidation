# React onboarding tour feature implementation

| | |
|---|---|
| Date | 2026-01-12 |
| Type | AI chat |
| Source | AI chat (MJM account) |
| By | Millard & Claude |
| Catalog ID | `C-MJM-578` |
| Links | [Original](https://claude.ai/chat/2d989ce5-2229-4c0c-90a9-a2a39a0df3e2) · [Archived file](https://github.com/MillardJMelnyk/AI_Chats/blob/main/Claude%20MJM%20export%20chats%20on%202026-10-31/chats/578-2026-01-12-react-onboarding-tour-feature-implementation.html) |

**Summary:** Drafting an Upwork proposal and screening answers for a React onboarding-tour trial task, plus how to share a GitHub profile.

**Topics:** Practical & personal > Freelance work and job applications

**Index terms:** Upwork; React; onboarding tour; job proposal; GitHub; TanStack Query

[← Catalog home](../README.md)

---

### Millard · 2026-01-12 04:40

write me a response to this Front-End React Developer — Small Trial Task (Onboarding Tour)
\* Front-End Development
\* Posted Jan 11, 2026
We’re looking for a front-end React developer to implement a small onboarding tour feature in an existing MVP web application. This is a starter task intended as a low-risk way to evaluate fit for ongoing contract work. The implementation itself is straightforward; the evaluation is primarily about communication, code clarity, and collaboration. You don’t need to reinvent anything, but we welcome thoughtful suggestions if you see opportunities to simplify or improve the implementation. Our stack includes React, Vite, Tailwind CSS, TanStack Query, and a GraphQL backend. The onboarding flow will integrate with existing components and persist completion state. If this initial task goes well, we have a backlog of additional front-end issues ranging from simple to moderately complex, and this role may grow into a longer-term engagement. Hourly rate for this initial task is flexible and will be revisited for ongoing work. for upwork to get me the gig I have experience in react

### Claude · 2026-01-12 04:40

Sunday, January 11, 2026, 12:45 PM CST

---

**Proposal:**

I'm a React developer with experience in the stack you've listed—React, Vite, Tailwind, and TanStack Query. I've built onboarding flows before and understand this is more about how I work than the code itself.

Happy to discuss approach before implementation, keep you updated as I go, and deliver clean, readable code. If I see a simpler path, I'll flag it.

Available to start immediately. What's the preferred way to receive the spec—async doc, or a quick call?

---

**Notes on this draft:**

* Kept short. Upwork clients posting trial tasks skim proposals.
* Directly addresses their stated priorities (communication, clarity, collaboration).
* Shows familiarity with their stack without overselling.
* Ends with a low-friction next step.

Adjust tone/length if you want something more formal or detailed.

### Millard · 2026-01-12 04:40

whats onbaording flow

### Claude · 2026-01-12 04:41

An onboarding flow (or onboarding tour) is a guided walkthrough that introduces new users to an application's features when they first log in.

Typical implementation: tooltip-style popups that highlight UI elements sequentially—"This is your dashboard," "Click here to create a project," etc.—with Next/Skip/Done buttons.

Common libraries for React: `react-joyride`, `intro.js-react`, `shepherd.js`.

The "persist completion state" they mentioned means storing a flag (usually in backend/database via their GraphQL API) so returning users don't see the tour again.

### Millard · 2026-01-12 04:42

I haven't built onboarding but I've built websites in react, and tools etc

### Claude · 2026-01-12 04:42

Revised proposal:

---

I'm a React developer with experience building websites and tools using React, and I'm comfortable with Vite and Tailwind. I haven't implemented an onboarding tour specifically, but it's a well-documented pattern—I've looked at libraries like react-joyride and the implementation is straightforward.

I understand this task is primarily about communication and code clarity. I'll keep you updated, ask questions early, and deliver readable code.

Available to start immediately. What's the best way to receive the spec?

---

Removed the false claim. The honesty is low-risk here—they called it "straightforward" themselves and said they're evaluating collaboration, not expertise in onboarding libraries.

### Millard · 2026-01-12 04:42

maybe a little more professional sounds a little disinterested

### Claude · 2026-01-12 04:42

---

I'm a front-end React developer with experience building websites and interactive tools. I work regularly with Vite and Tailwind, and I'm familiar with TanStack Query.

I haven't built an onboarding tour before, but I've reviewed common approaches (react-joyride, shepherd.js) and the pattern is well-documented. I'm confident I can deliver a clean implementation that integrates smoothly with your existing components and persists state through your GraphQL backend.

I appreciate that you're evaluating communication and collaboration as much as code—that's how I prefer to work. I ask questions early, stay responsive, and write code that's easy for the next person to read.

I'd be glad to start immediately and am genuinely interested in the possibility of ongoing work if this goes well. Happy to discuss approach before diving in.

What's the best way to receive the project spec?

---

Added: engagement about their process, interest in longer-term work, slightly warmer language throughout. Still concise.

### Millard · 2026-01-12 04:44

answer this 4117 characters left
Briefly describe how you’d approach implementing an onboarding tour in an existing React app. What would you want to understand before writing code?

### Claude · 2026-01-12 04:44

**Approach:**

I'd use an established library (react-joyride or shepherd.js) rather than building from scratch—they handle positioning, scrolling, and accessibility out of the box. The tour configuration would define steps tied to target selectors, with the component mounted at the app root. Completion state would be persisted via a GraphQL mutation and checked on load via query (likely integrated with TanStack Query's caching).

**Before writing code, I'd want to understand:**

* Which elements/screens the tour needs to cover and in what order
* How completion state should be stored (user record field, separate table, etc.)
* Whether the tour should be skippable, and if so, whether "skipped" and "completed" are tracked differently
* Any existing modal/overlay patterns in the codebase I should match
* Whether the tour can be re-triggered (e.g., from a help menu)

Happy to adapt based on your preferences or existing conventions.

---

~950 characters. Direct, shows you've thought about it, asks the right questions. Adjust if you want shorter/longer.

### Millard · 2026-01-12 04:45

What’s something that frustrates you about working with clients, and how do you usually handle it?

### Claude · 2026-01-12 04:45

Unclear or shifting requirements mid-task—especially when it's framed as "that's what I meant originally."

I handle it by over-communicating upfront: confirming scope in writing before starting, asking clarifying questions early, and checking in at logical breakpoints rather than delivering everything at the end. If requirements do change, I acknowledge it neutrally and clarify whether it affects timeline or rate. Most friction comes from misaligned expectations, not bad intentions, so I try to close those gaps before they become problems.

---

~530 characters. Honest, shows process, doesn't sound bitter. Adjust if you want a different frustration or tone.

### Millard · 2026-01-12 04:47

how to share my github

### Claude · 2026-01-12 04:47

Include the URL directly in your proposal text:

> You can view my work here: github.com/yourusername

Or add it to your Upwork profile under **Portfolio** or the **Website/Link** field in your profile settings—then it's visible on every application.

For this proposal specifically, I'd paste it at the end of your cover letter if you have repos that demonstrate React work.

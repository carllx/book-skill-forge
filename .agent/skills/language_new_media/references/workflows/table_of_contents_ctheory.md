# Workflow: Architectural Synthesis & System Design for New Media

## Prerequisites & Context

**WHY:** Modern digital architecture and agent skill design often fail when treating new media simply as a "new tool." This workflow applies Lev Manovich's "digital materialism"—a bottom-up methodology tracing the logic from the binary medium up to the cultural form. It uses Dziga Vertov’s *kino-eye* and database logic as foundational models for constructing non-linear, multi-layered interfaces and systems.

**WHEN:** Use this workflow when designing complex interactive interfaces, structuring large databases that require intuitive navigation, or when converting legacy narrative structures (like books or linear films) into modular, composable agent skills.

> *Note: For deep historical dives into the specific archeology of cinema, the evolution from optical toys to digital compositing, or detailed explanations of Vertov's theories, defer to the `graphify_query` MCP tool.*

## Comprehensive Guide & Best Practices

### 1. Bottom-Up Systems Architecture ("Digital Materialism")
Approach new media objects not from a top-down aesthetic, but via a rigorous bottom-up translation stack. 
*   **Medium:** The material and logical organization (binary data).
*   **Interface:** The human-computer/OS layer.
*   **Operations:** Software application logic, filters, menus.
*   **Illusions:** The synthetic reality or appearance.
*   **Forms:** The overarching organization (e.g., website, VR world, agent skill).

**Actionable Heuristic:** Map every new feature backward down the stack. If you introduce a new "Form" (like a complex output table), ensure its "Operations" (how it filters data) and "Interface" (how the user navigates it) are strictly defined.

> **Example:** "Just as new media objects contain a hierarchy of levels... Vertov's film consists of at least three levels..." Design your agent's responses with clear meta-layers (e.g., execution layer, observation layer, reflection layer).

### 2. Embracing Database Logic over Linear Narrative
The database is the symbolic form of the computer age. Treat datasets not as inert storage, but as the core structure from which narratives are generated.
*   **The Kino-Eye Interface:** Use data-mining and navigation algorithms to transcend human navigational limits. 
*   **Merge Database and Narrative:** Do not present raw data dumps. Build a "trajectory" through the data. 
*   **The Loop as a Narrative Engine:** Utilize loops (the foundational control structure of both early cinema and computer programming) to progress through data sets.

**Actionable Heuristic:** When designing workflows, shift from sequential instructions (temporal montage) to concurrent, modular data access. Allow the user to "navigate" rather than merely "read."

### 3. Spatial Montage & Compositing
Standard text or linear logs mimic traditional cinematic "temporal montage" (one thing after another). New media thrives on "spatial montage" (multiple windows, simultaneous data streams).
*   **Composite Realities:** Do not force different data streams into a single, flattened perspective. Allow different "worlds" or data sources to clash or retain separate identities within the interface.

**Actionable Heuristic:** Present information side-by-side or in modular blocks. If synthesizing code, logs, and theory, keep them conceptually separated yet visually simultaneous—much like a multi-window GUI.

> **Visual Reference:** 
> ![Vertov's Dataset - Figure 1](../../images/figure1.png)
> *(Observe how Vertov composites multiple temporal moments into a single spatial frame.)*

## If/Then Troubleshooting Logic

*   **IF** the system outputs feel rigid, linear, or overly sequential...
    *   **THEN** implement the **Spatial Montage** heuristic. Break the output into concurrent modules or windows, utilizing `graphify_query` to fetch supporting context asynchronously.
*   **IF** the user is overwhelmed by raw data...
    *   **THEN** apply the **Database vs. Narrative** principle. Introduce a "narrator" or "kino-eye" perspective to guide the user through the database via a structured loop, rather than presenting a flat list.
*   **IF** the architectural layers (Interface vs. Operations) become muddled...
    *   **THEN** return to the **Bottom-Up Mapping** strategy. Explicitly separate the "representation" (Form) from the "control" (Operations) in your system design.
*   **IF** deep historical grounding on "HCI vs. Cinema" or "Archeology of Compositing" is needed...
    *   **THEN** halt manual explanation and invoke the `graphify_query` MCP tool to retrieve the textbook theory.

## Verification Checklists

- [ ] **Digital Materialism Check:** Are all features mapped across the five layers (Medium, Interface, Operations, Illusions, Forms)?
- [ ] **Database Logic Check:** Is the underlying data structured modularly, and have you provided a "kino-eye" trajectory to navigate it?
- [ ] **Montage Check:** Are you avoiding excessive linear/temporal output in favor of concurrent, spatial presentation?
- [ ] **Progressive Disclosure Check:** Have massive blocks of theory been successfully replaced with concise heuristics and actionable examples?
- [ ] **Tooling Check:** Is the `graphify_query` MCP tool explicitly referenced for all deep theoretical queries?
- [ ] **Asset Pathing:** Have all required image paths been correctly routed (e.g., `../../images/figure1.png`)?
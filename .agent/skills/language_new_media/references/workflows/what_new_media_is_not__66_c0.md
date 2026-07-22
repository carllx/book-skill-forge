# Workflow: Evaluating and Designing Cultural Interfaces & New Media Objects

**Target Audience:** Senior System Architects, Interface Designers, and Agent Skill Designers
**Source Material:** "What New Media is Not" & "The Interface" (Lev Manovich)

## 1. Prerequisites & Context

**When to Use This Workflow:**
Trigger this workflow when designing, evaluating, or refactoring interactive digital applications, new media art, or web interfaces. It is essential when the project requires moving beyond superficial "interactive" features to create deeply engaging, psychologically resonant, and culturally aware systems.

**The "Why":**
Modern human-computer interfaces (HCI) are often plagued by persistent myths—that "digital" means perfect replication, or that "interactive" simply means clicking links. To build profound and structurally sound new media objects, architects must recognize that the interface is never a transparent window; it is a heavy semiotic code that dictates how content is perceived and operated upon.

> **Deep Theory Retrieval:**
> For exhaustive historical context, theoretical debates, or broader explorations of these concepts, invoke the `graphify_query` MCP tool with queries like:
> - `graphify_query("myth of interactivity new media")`
> - `graphify_query("non-transparency of the code Lev Manovich")`
> - `graphify_query("cinema as precursor to new media discrete representation")`

---

## 2. Comprehensive Guide & Best Practices

### Phase 1: Dismantling the "Myths" of New Media
Before writing code or laying out a UI, explicitly dismantle the default assumptions about what makes your media "new."

*   **Heuristic 1: Reposition "Discrete Representation" and "Multimedia".**
    Do not assume that combining text, images, and video, or using discrete states, is a novel feature of your system. Cinema and print already did this.
    > *Example:* Edison's early cinema apparatus mapped time onto a 2D spatial grid (a cylinder of micro-photographs). Recognize that your system is merely accelerating and quantifying principles already established in the 19th century. Design with a historical awareness of how humans already consume spatialized time.
*   **Heuristic 2: Embrace Lossy Compression as the Material Reality.**
    Do not design for an idealized "perfect digital" realm.
    > *Example:* Digital media in practice involves massive data loss (JPEG, MPEG). Instead of pretending digital replication is flawless, acknowledge that degradation and noise are foundational to modern computer culture. Build systems that handle, or even aesthetically leverage, "lossy" realities.
*   **Heuristic 3: Design for Psychological—Not Just Physical—Interactivity.**
    HCI is interactive by definition (real-time control via a screen). Calling a system "interactive" is a tautology.
    > *Example:* A standard hyperlink externalizes the mind's association process, forcing the user to mistake the designer's mental structure for their own. Instead of just adding buttons, design for *psychological interaction*—ellipses, missing details, and staging that require the user to actively fill in gaps, form hypotheses, and recall information.

### Phase 2: Mastering the Cultural Interface
Recognize that your HCI acts as a universal filter through which all culture is now accessed.

*   **Heuristic 4: Acknowledge the "Non-Transparency of the Code".**
    The interface is not a neutral transport mechanism. It imposes its own logic and ideology on the data.
    > *Example:* The "cut and paste" operation collapses the distinction between spatial and temporal media (pixels, text, video are all treated the same). When architecting features, analyze how universal HCI commands strip original media of their unique properties and impose a new meta-logic.
*   **Heuristic 5: Merge Content and Interface (Especially in Art/High-End Design).**
    Avoid the trap of treating "content" and "interface" as separable layers.
    > *Example:* In interactive art or premium experiences, the choice of interface must be profoundly motivated by the content. If you dynamically generate data at runtime (via Artificial Life or procedural generation), the interface rules *are* the artwork. Changing the interface fundamentally destroys or alters the work.
*   **Heuristic 6: Synthesize the Three Core Cultural Forms.**
    Every cultural interface blends three distinct languages. Audit your design against them:
    1.  **Cinema:** Mobile camera, spatial representation, editing logic.
    2.  **The Printed Word:** Rectangular pages, typography, static layouts.
    3.  **General-Purpose HCI:** Menus, windows, selection mechanisms.

---

## 3. If/Then Troubleshooting Logic

| Condition (If...) | Resolution (Then...) |
| :--- | :--- |
| **If** the interface feels mechanically interactive but cognitively passive... | **Then** you have fallen into the "Myth of Interactivity." Reduce explicit hyperlinking and introduce representational "shortcuts" or ellipses that force the user to employ psychological filling-in and hypothesis generation. |
| **If** the design team is struggling to separate the UI layer from the data model in a creative project... | **Then** stop trying. In advanced new media, the connection between content and interface is strictly motivated. Lean into this merging; let the interface's unique materiality define the user experience. |
| **If** the user flow feels disjointed across different media types (text vs. video vs. 3D)... | **Then** leverage the leveling power of HCI (e.g., universal operations like copy/paste, filter, search). Use the interface's inherent logic to unify diverse media under a single operational grammar. |
| **If** the application is criticized for "loss of quality" or compression artifacts... | **Then** re-frame the narrative around the material constraints of digital media. Ensure your architecture gracefully handles lossy compression, which is the necessary foundation of mass digital distribution, rather than fighting an unwinnable battle for lossless purity. |

---

## 4. Verification Checklists

### Pre-Flight Conceptual Audit
- [ ] Has the team explicitly defined what kind of interactivity is being built (e.g., menu-based, simulational, psychological)?
- [ ] Are we treating the interface as a non-transparent code that actively shapes the user's worldview?
- [ ] Is the aesthetic language intentionally drawing from, or subverting, the "Macintosh GUI" (modernist clarity) vs. "Blade Runner" (decay/techno-noir) dichotomy?

### Implementation Review
- [ ] Are we relying too heavily on "clickable links" to simulate depth, instead of orchestrating the user's attention through composition and staging?
- [ ] Have we accounted for the structural limitations of the digital (e.g., finite resolution, lossy compression)?
- [ ] Are the influences of Cinema (time/space), Print (layout), and HCI (control) cohesively integrated?
- [ ] *Agent Task:* If deep theoretical backing is required to justify a design decision, have I executed a `graphify_query` to extract the necessary literature references?
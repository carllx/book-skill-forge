# Workflow: Implementing the New Language of Cinema in Digital Media

## Prerequisites & Context
The transition from traditional cinema to new media fundamentally alters how time, space, and narrative are structured. According to Lev Manovich, the language of new media builds upon the foundational language of twentieth-century cinema, but fundamentally restructures it around concepts of **Spatial Montage**, **Information Density**, and **Media as Code**. 

**When to use this workflow:**
- When designing multi-window, multi-tasking interfaces, or complex data dashboards.
- When creating rich multimedia environments that move away from sequential narrative.
- When exploring the aesthetics of dense information spaces (e.g., broadband cinema, high-resolution immersive displays).
- When exposing the underlying computational substrate of a media object as an artistic or structural statement.

> **Deep Dive via MCP**: To explore the foundational theory behind these concepts, use the `graphify_query` MCP tool to query terms like `"Spatial Montage"`, `"Cinema as Information Space"`, or `"Cinema as a Code"`.

---

## Comprehensive Guide & Best Practices

### 1. Transitioning to Spatial Montage
Traditional cinema relied on temporal montage—a sequential assembly line of shots. New media reintroduces and amplifies *spatial montage*, where multiple narrative elements coexist simultaneously.

**Heuristics:**
* **Logic of Addition over Replacement**: Do not strictly replace older elements with new ones. Allow past actions, memories, and inputs to accumulate on the screen.
* **Simultaneous Activity**: Design your environment so that multiple, overlapping windows or frames can be active simultaneously, reflecting an object-oriented paradigm.
* **Spatial Relationship**: Pay attention to the geometric relationships between simultaneous images. Montage is generated not just by what precedes or follows an image, but by what sits beside it.

> **Show, Don't Tell:**
> In Olga Lialina's Web artwork *My boyfriend came back from war!*, the browser window is divided into more and more frames as the user navigates. The core image remains, while new texts and images coexist with it. 
> *Implementation thought:* Use multi-layered interfaces or dynamic grids where interacting with a component adds a new frame rather than replacing the current view.

### 2. Designing the Information Space (Aesthetics of Density)
With high-resolution displays and broadband connectivity, the traditional "depth of field" artifacts and visual scarcity of standard analog film are no longer limits. We now design for an *aesthetics of density*.

**Heuristics:**
* **Embrace Hyper-Realism**: Ensure that every detail can be in focus. Distribute the user’s attention more evenly across the digital canvas rather than forcing a single point of narrative focus.
* **Treat Screen as Memory**: Let the screen serve as a cumulative record of interaction rather than merely a record of immediate perception.
* **Reflect the Workspace Rhythm**: Acknowledge that the modern user is trained to rapidly switch context. A rich, high-density stream of concurrent audio-visual data is often more satisfying than a sparse, single-threaded narrative.

> **Show, Don't Tell:**
> Christian Boustani’s digital composites in *A Viagem* utilize up to 1600 separate layers to recreate the dense, everywhere-in-focus look of seventeenth-century Dutch painting.
> *Implementation thought:* Rather than minimalist "clean" designs, consider dense dashboard topologies where micro-narratives (widgets, data streams) compete for attention while maintaining overall readability.

### 3. Exposing the Code (Media Translation)
New media operates via underlying digital algorithms. Traditional digital cinema (like *Star Wars: Episode 1*) hides the numbers behind photorealistic rendering. Artistic new media can choose to *stage* its identity as code.

**Heuristics:**
* **Perform the Medium**: Find opportunities to reveal the digital substrate (e.g., exposing underlying data structures, glitches, or base formatting) as an aesthetic choice.
* **Media Translation as Art**: Translate content from one format to an "obsolete" or raw format to highlight the pervasive logic of transcoding in modern culture.

> **Show, Don't Tell:**
> Vuk Cosic’s ASCII films translate moving images into ASCII code. The recognizable film image and the abstract code coexist simultaneously on the screen.
> *Implementation thought:* When debugging or rendering complex scenes, create "wireframe," "data-stream," or "raw-code" visualization toggles that allow the user to see the structural mathematics defining the visual layout.

---

## If/Then Troubleshooting Logic

* **IF** the interface feels too cluttered and users are overwhelmed by spatial montage, **THEN** introduce progressive disclosure mechanisms. Maintain the simultaneous frames but dim or desaturate inactive frames until they are explicitly focused.
* **IF** the narrative rhythm feels disjointed due to the lack of temporal sequencing, **THEN** reintroduce subtle temporal cues. Use micro-animations or localized loops (akin to the "moving automobile" loop in *A Man with a Movie Camera*) to ground the user's attention.
* **IF** the "aesthetics of density" leads to unreadable information architecture, **THEN** ensure that layering and compositing maintain contrast. Hyper-realism works only when distinct objects can be visually parsed. Use color coding or subtle z-axis drop shadows.
* **IF** exposing the code (ASCII/raw data) confuses non-technical users, **THEN** contextualize the display. Use it strictly as a visual motif or a "developer mode" Easter egg rather than as the primary means of user navigation.

---

## Verification Checklists

### Concept & Structural Integrity
- [ ] Are elements layered spatially rather than forced into a rigid temporal sequence?
- [ ] Have you accounted for an "object-oriented" visual design where multiple components can be active at once?
- [ ] Does the application accumulate state (memory) visibly on the screen?

### Visual & Density Checks
- [ ] Is the resolution density leveraged to show micro-details without forcing focus loss?
- [ ] Have you tested the interface under the "hyper-realism" heuristic (everything in focus)?
- [ ] Do the visual elements accurately reflect the multi-tasking rhythm of modern user workflows?

### Substrate & Translation Elements
- [ ] Is there an opportunity to visually represent the underlying data or code?
- [ ] Does the system allow for media translation (e.g., exporting or viewing the media in alternative, fundamental formats)?

> **Reminder:** For extended theoretical reading on the origins of these principles, invoke the `graphify_query` MCP tool targeting Lev Manovich's discourse on Dziga Vertov, the Phenakisticope, and the historical precedents of spatial vs. sequential narrative.
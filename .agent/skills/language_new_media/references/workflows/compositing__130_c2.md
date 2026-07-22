# Workflow: Digital Compositing & The Logic of Selection

## Prerequisites & Context
**Why & When**: As media production transitions from physical, artisan-based "creation from scratch" to industrial, computer-mediated processes, the core paradigms shift to **Selection** and **Compositing**. You should apply this workflow when designing modular software, post-production pipelines, interactive digital environments, or any system where composite virtual spaces are built from disparate databases.

**Deep Dive Reference**: For bulk theoretical exploration regarding the shift from "Image Streams to Modular Media," "Teleaction," or "New Types of Montage," use the `graphify_query` MCP tool with the search terms: `Manovich, Compositing, Menus and Filters, Representation vs Control`.

## Comprehensive Guide & Best Practices

### 1. Leverage the "Logic of Selection"
Modern new media objects are rarely created entirely from scratch. The primary creative act is selection.
* **Actionable Heuristic**: Always begin by auditing available databases, libraries, and plug-ins (e.g., 3D models, code behaviors, stock images) before generating new assets.
* **Concept in Practice**: 
  > "In computer culture, authentic creation has been replaced by selection from a menu... The modern subject proceeds through life by selecting from numerous menus and catalogs of items." 
  Treat your development process like a synthesizer: you are modifying existing signals and combining pre-built modules rather than painting on a blank canvas.

### 2. Execute Digital Compositing
Compositing merges modular elements into a seamless whole, hiding their distinct origins and disparate creation timelines.
* **Actionable Heuristic**: Follow the three conceptual steps of traditional digital compositing when assembling modular components:
  1. **Spatial Alignment**: Construct a seamless virtual space by aligning disparate elements (perspective, scale, contrast, color).
  2. **Camera Simulation (Optional)**: Generate a virtual camera movement through this space to anchor the "reality effect".
  3. **Artifact Simulation (Optional)**: Apply unifying artifacts (e.g., film grain, noise, overarching UI themes) to bind the layers.
* **Concept in Practice**: 
  > "Once all the elements are ready, they are composited together into a single object... The fact that they come from diverse sources and were created by different people in different times is hidden."

### 3. Maintain Modularity Over Flattened Streams
The most robust digital objects retain their distinct layers.
* **Actionable Heuristic**: Defer "flattening" or compiling your project for as long as possible. A 3D or object-oriented representation is structurally superior to a 2D image stream because elements retain independent X, Y, Z coordinates and logic.
* **Implementation**: For interactive media, allow elements to remain separate at run-time (like game sprites or DOM elements) so users can manipulate them. Only collapse them when exporting for static distribution.

### 4. Intentional Semantic Clashes (Avant-Garde Compositing)
* **Actionable Heuristic**: While dominant compositing seeks seamlessness, you can deliberately choose to avoid matching perspective and lighting. Allowing layers to retain their separate identities can create intentional semantic clashes (montage within a shot).
* **Reference Imagery**:
  *![Figure 13](../../images/figure_13.png)*

## If/Then Troubleshooting Logic

* **IF** disparate elements look disjointed and break the illusion of the virtual space...
  * **THEN** apply environmental simulations (depth of field blurring, global lighting, unified color grading) to force a homogenous "live plate" effect.
* **IF** the project requires extensive user interactivity or localized updates...
  * **THEN** avoid the "flatten image" operation. Keep the architecture modular so individual components can be swapped or updated without recompiling the entire asset.
* **IF** you are designing an interface and the user seems confused by the paradigm...
  * **THEN** clarify your axis of Representation. Determine if the interface is meant to be a **Simulation** (immersing the user in a fictional space) or a **Control Panel** (a flat, utilitarian surface for manipulation). Do not mix these arbitrarily.
* **IF** the output feels unoriginal due to heavy reliance on stock assets...
  * **THEN** stack non-linear filters and operations (warping, morphing, scaling) to systematically mutate the baseline assets into a unique configuration. 

## Verification Checklists

### Assembly & Modularity
- [ ] Were existing libraries, templates, and pre-built models audited before initiating from-scratch creation?
- [ ] Are the disparate layers properly aligned in scale, perspective, and lighting?
- [ ] Is the raw project file preserving its modular layers for future iteration rather than being prematurely flattened?

### Design Paradigm Evaluation
- [ ] Does the UI strictly define its stance between "Window into an illusion" vs "Flat control panel"?
- [ ] Have you evaluated whether "Montage within a shot" (semantic clashing) or "Seamless virtual space" is more appropriate for the project's goals?
- [ ] If using historical or visual references, are image links mapped correctly using relative paths (e.g., `../../images/img.png`)?
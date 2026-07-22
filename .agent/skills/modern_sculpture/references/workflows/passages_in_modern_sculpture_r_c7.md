# Workflow: Knowledge Map & Structural Indexing for "Passages in Modern Sculpture" (Rosalind E. Krauss)

## 1. Prerequisites & Context

**Why & When:**
This workflow is triggered when an agent or user needs to navigate the theoretical landscape, structural methodology, or specific historical case studies (e.g., Rodin, Duchamp, Constructivism, Minimalism) in Rosalind E. Krauss's *Passages in Modern Sculpture*. This specific cluster acts as the structural spine—comprising the table of contents, acknowledgments, bibliography, and the first half of the index (A-M).

**Contextual Grounding:**
Krauss's text is a foundational critical history of 20th-century sculpture. It systematically dismantles the traditional view (dating back to Lessing's *Laocoon*) that sculpture is purely an art of static space. Instead, Krauss emphasizes the shift from spatial organization to temporal experience, phenomenology, and structural linguistics. 

> **Progressive Disclosure Directive:** Do not attempt to reconstruct the entire theoretical argument from the index alone. Use the index and bibliography provided here to pinpoint exact concepts and structural nodes, then defer to the `graphify_query` MCP tool for bulk theory extraction on specific artists or aesthetic philosophies.

---

## 2. Comprehensive Guide & Best Practices

### Step 2.1: Mapping the Theoretical Framework (Table of Contents)
Use the book's core chapters as a macro-heuristic for understanding the evolution of modern sculpture. When evaluating a sculptural work, align it with the appropriate historical/theoretical passage:
- **Narrative Time:** Use for questions regarding Auguste Rodin and the *Gates of Hell*.
- **Analytic Space:** Use when analyzing Futurism (Boccioni) and Constructivism (Gabo, Tatlin).
- **Forms of Readymade:** Apply to Marcel Duchamp and Constantin Brancusi.
- **A Game Plan:** Use for Surrealist objects and chance procedures (Arp, Giacometti).
- **Tanktotem:** Apply to welded images and abstract expressionist sculpture (David Smith).
- **Mechanical Ballets:** Use for kinetic art, light, motion, and theater (Calder, Schöffer, Tinguely).
- **The Double Negative:** Apply to Minimalist and Earthwork syntax (Robert Morris, Robert Smithson, Michael Heizer, Richard Serra).

### Step 2.2: Cross-Referencing Artists and Concepts (Index Navigation)
When investigating a specific artist or concept, use the index to locate their primary concept clusters and map out the conceptual web.

> [!TIP]
> **Show, Don't Tell:** If tasked with analyzing "Constructivism," do not invent theory. Note its index clusters (e.g., 4, 55-56, 57-58, 67, 77-78, 103, 110, 124, 132, 134, 141-42, 143, 146, 156, 157, 158, 159, 161, 173, 178, 216, 240, 245, 253) and cross-reference with key figures like Naum Gabo and Vladimir Tatlin. Then construct a highly targeted query for the MCP tool.

**Key clusters extracted from the A-M index:**
- **Brancusi, Constantin:** Focus on aesthetic transformation, bases, composition, and specific works (*Bird in Space*, *Beginning of the World*).
- **Duchamp, Marcel:** Link to readymades, chance, and linguistic paradigms. Note his subversion of the "creative act."
- **Constructivism:** Note the tension between analytical space and kineticism (discontinuities, syntactic structures).
- **Minimal Art:** Connect to Gestalt forms, theatricality, and the activation of the audience's physical space (Morris, Judd, Andre, Flavin).

### Step 2.3: Leveraging the Bibliography for Deep Dives
When the user requires external validation or deeper exploration of an artist's specific period, consult the bibliography to recommend canonical secondary literature.
- *Example:* For Gabo and Pevsner, reference Ruth Olson and Abraham Chanin's *Naum Gabo-Antoine Pevsner* (MoMA, 1948).
- *Example:* For David Smith, reference Krauss's own *Terminal Iron Works* (1971).
- *Actionable Heuristic:* Always verify the availability of these secondary sources via the `graphify_query` MCP tool if requested by the user.

---

## 3. If/Then Troubleshooting Logic

| Condition (If...) | Action (Then...) | Rationale |
| :--- | :--- | :--- |
| **If** the user asks for a deep theoretical explanation of Krauss's view on Minimal Art (e.g., Robert Morris, Donald Judd)... | **Then** extract the page references from the index (e.g., Minimal art: 181, 198-99, 236, 245...) and invoke the `graphify_query` MCP tool with these specific locators. | The index provides the map, but the raw theory must be dynamically fetched to avoid hallucination and over-compression. |
| **If** asked about the influence of phenomenology or structural linguistics on sculpture... | **Then** immediately reference the Introduction and the index entries for Merleau-Ponty, Bergson, and structural linguistics, then defer to the MCP tool for the philosophical arguments. | Krauss's unique contribution is folding these linguistic and temporal models into spatial analysis. |
| **If** an image reference like `images/img.png` is needed to illustrate a work (e.g., Boccioni's *Development of a Bottle in Space*)... | **Then** rewrite the path strictly as `../../images/img.png`. | Ensures compatibility and prevents broken visual links within the agent's workflow architecture. |
| **If** you encounter an artist/concept not listed in this index chunk (e.g., Picasso, Rodin beyond A-M)... | **Then** rely on the macro-structure (Table of Contents) to infer the context and query the MCP tool for the missing theoretical blocks. | This specific knowledge cluster only contains detailed index entries up to "M" (Motion pictures). |

---

## 4. Verification Checklists

- [ ] **Structural Alignment:** Have you identified which "passage" (chapter) the sculpture belongs to based on the Table of Contents?
- [ ] **Index Verification:** Did you check the A-M index for exact terminology, pages, or artist names before generating an analysis?
- [ ] **Progressive Disclosure:** Is the theoretical output concise, using blockquotes for concrete examples while explicitly leaving bulk theory generation to the `graphify_query` MCP tool?
- [ ] **Image Path Compliance:** Are all referenced images formatted with the `../../images/` prefix?
- [ ] **Bibliographic Grounding:** Have you suggested secondary literature from the bibliography when deeper art-historical context is required by the user?
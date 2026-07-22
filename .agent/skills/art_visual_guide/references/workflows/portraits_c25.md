# Agent Skill Workflow: Portraiture Architecture & Visual Analysis

## Prerequisites & Context

**When to Invoke This Workflow:**
Trigger this workflow when tasked with analyzing, generating, or evaluating portraiture, character representation, and historical artistic likenesses. This applies to rendering logic, compositional framing, and analyzing psychological depths in subjects.

**Why:**
Portraiture is a deeply nuanced art form that evolved from the panel traditions of ancient Egypt through the Renaissance and into modern analytical or reactionary movements. Correctly executing or evaluating a portrait requires an understanding of scale, view, lighting, and thematic intent.

> **Note on Theory vs. Practice:**
> This workflow prioritizes actionable heuristics. For bulk theoretical background on specific artists (e.g., Rembrandt, Kokoschka, Fouquet) or historical movements (e.g., *Neue Sachlichkeit*, Renaissance, Pop Art), **DO NOT** attempt to guess. Instead, immediately query the `graphify_query` MCP tool for deep historical context.

---

## Comprehensive Guide & Best Practices

### 1. Establish the Viewpoint (Framing the Subject)
The artist's decision on how much of the sitter to include fundamentally alters the portrait's message.

*   **Head, Shoulders, and Upper Chest (Bust):** The most common format for intimate, focused character studies.
*   **Half-Length:** Standard for seated portraits.
    *   > **Example:** Leonardo da Vinci's *Mona Lisa* uses this framing combined with *sfumato* (a subtle blurring of colours and tones) to create an enigmatic presence.
    *   ![](../../images/43bde010dad11af1da14fec9db60a3682ba4711b0fea74049a08d33dc96c233b.jpg)
*   **Three-Quarter Length:** Requires advanced compositional skill to artificially "stop" at the subject's knees without looking severed.
*   **Full-Length "Swagger":** Use this to proclaim grandeur, superiority, and societal status (e.g., Sargent’s life-size depictions of high society).
    *   ![](../../images/ae1cd562ac8f68c122f9307bf4253f0a2afff867104c5855e2da5a15aa2d1dfe.jpg)

### 2. Determine Facial Angle and Engagement
*   **Full-Face (Confrontational / Engaging):** Historically reserved for deities, full-face modern usage can be intense or warmly engaging.
    *   ![](../../images/5fa07213da4c862781e2ae8fb644adace08c86ae3fffff0302e38578490e2436.jpg)
*   **Three-Quarter / Profile:** The three-quarter view provides the best idea of the sitter's true likeness. Profiles were historically prominent in early portraiture and coinage.

### 3. Define Scale and Contextual Narrative
*   **Tight Scale (Psychological Focus):** When the sitter fills the canvas, the portrait becomes a psychological study. Focus heavily on facial topography and micro-expressions.
*   **Broad Scale (Environmental Focus):** By moving out and including settings and props, you tell a story about the sitter's profession, status, or interests.

### 4. Implement Stylistic and Technical Execution
Adopt specific technical heuristics based on the desired emotional outcome:

*   **Chiaroscuro (Light & Shade):** Use for dramatic modeling and profound psychological insight. (e.g., Antonis Mor's portraits where the head is slightly turned into the light).
    *   ![](../../images/60cb9ba46624fdf405f123a7319ad7020508e187fec670fb4029699a30ef7873.jpg)
*   **Broad, Painterly Strokes ("Square Touch"):** Use rapid, thick strokes to convey vitality or aging.
    *   > **Example:** Rembrandt applied raw dabs of crimson and white to the nose to convey the brutal honesty of old age. Raeburn used free brushwork without underdrawing to capture vivid personalities.
    *   ![](../../images/b5a3aa32b5a7747f3764f4652544e856d9d5f34ceccb52e55a9b59ab051c6a08.jpg)
*   **Psychological Probing (Expressionism):** Use nervous energy and frank brushwork to strip away social veneers (e.g., Kokoschka’s portraits of Viennese intellectuals).
    *   ![](../../images/1dac7065580c3f4f6671cad1476b30e43ee2e6a56430486a8aa1791f27a7c80c.jpg)
*   **Analytical Detachment (New Objectivity):** When capturing societal disillusionment, paint with cool, clinical detachment.
    *   ![](../../images/369f66caa455ef67bb9352af5ffc44a3ce27440435574dbb0a523b01eac5fbe5.jpg)

### 5. Role-Playing vs. Formal Portraiture
*   **Tronies:** Use this format when the goal is not a strict likeness but an exploration of an emotion or character archetype (e.g., early Rembrandt self-portraits).
*   **Idealization vs. Realism:** If the subject holds immense power but lacks aesthetic appeal (e.g., Charles II of Spain), employ diplomatic idealization for the primary figure while reserving realism for secondary figures.

---

## If/Then Troubleshooting Logic

*   **IF** the portrait lacks psychological depth and feels flat, **THEN** increase the contrast (chiaroscuro), turn the head slightly to catch directional light, or use *sfumato* to blur the hard edges of the facial features.
*   **IF** the subject appears disconnected from their societal role, **THEN** decrease the subject's relative scale within the frame and introduce environmental props (books, tools, rich fabrics).
*   **IF** a portrait needs to convey raw, unfiltered honesty (e.g., aging or fatigue), **THEN** abandon fine detailing. Use broad, visible strokes (impasto) and do not shy away from leaving parts of the canvas 'unfinished' to simulate how human vision perceives shadows.
*   **IF** you encounter specific historical styles (e.g., Pop Art consumerism, *Neue Sachlichkeit*, or Flemish expressive realism), **THEN** halt manual assumptions and invoke the `graphify_query` MCP tool to retrieve the correct theoretical underpinning.

---

## Verification Checklists

- [ ] **View & Composition:** Has the framing (bust, half-length, swagger) been deliberately chosen to match the subject's intended presence?
- [ ] **Lighting & Texture:** Have techniques like chiaroscuro or "square touch" brushwork been applied to enhance characterization rather than just decoration?
- [ ] **Context vs. Intimacy:** Is the scale appropriate? (Tight for psychology, wide for narrative context).
- [ ] **Historical Alignment:** Are the methods aligned with the desired historical style (e.g., idealization for royal courts, brutal honesty for late self-portraits)?
- [ ] **Theory Delegation:** Have all deep historical theories been successfully deferred to the `graphify_query` tool instead of bloating this workflow?
- [ ] **Asset Integrity:** Are all referenced image paths strictly rewritten as relative paths (e.g., `../../images/[filename].jpg`)? 

---
*(End of Workflow)*
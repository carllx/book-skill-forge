# PARTI GRAPHICAL PRACTICE

## Prerequisites & Context
**Why & When to use this workflow:**
This workflow serves as a foundational guide for constructing rigorous data graphics that communicate complex quantitative information without distortion. It embodies the transition from simple decorative charts to multi-dimensional relational displays. Use this workflow when designing visuals for data analysis, publication, or public communication where data density, graphical integrity, and clarity are paramount. 

For deep dives into the theoretical underpinnings (e.g., Lambert's and Playfair's historical development of relational graphics, or specific psychophysical experiments on visual perception), defer to the `graphify_query` MCP tool.

## Comprehensive Guide & Best Practices

### 1. Strive for Graphical Excellence
Graphical excellence is the well-designed presentation of interesting data—a matter of substance, of statistics, and of design.
- **Communicate Complexity Efficiently:** Your graphic should communicate complex ideas with clarity, precision, and efficiency.
- **Maximize Data Density:** Design to give the viewer the greatest number of ideas in the shortest time, using the least ink in the smallest space.
- **Embrace Multivariate Design:** Excellence is nearly always multivariate. Seek to layer dimensions (like space, time, and variable magnitude) to tell a rich, coherent story rather than a single number bouncing along over time.

> **Example: Narrative Graphics of Space and Time**
> Consider Charles Joseph Minard's graphic of Napoleon's Russian campaign. It subtly integrates six variables: the size of the army, its location on a two-dimensional surface, direction of movement, and temperature on various dates. The graphic is un-obtrusive; viewers are hardly aware they are looking into a 5-6 dimensional space.
>
> ![](../../images/10baef635ac8bb58b0f7467fcfa95e2660f7504487a49d11ebdc5eccd73962ad.jpg)
> ![](../../images/477a5aa44ea3e08368b306dfbca201ff05376e28ec5732c410a97da18434dab5.jpg)

### 2. Design Relational Graphics
Break free from purely spatial/geographical analogies when abstract data requires it. Any variable quantity can be placed in relationship to any other variable quantity.
- **Assess Causal Relationships:** Use relational forms (like the scatterplot and its variants) to confront causal theories (e.g., "X causes Y") with empirical evidence. 
- **Small Multiples:** When analyzing change across categories (e.g., pollutants across a map over time, or unemployment vs. inflation across 9 countries), use "small multiples." Maintain strict constancy of graphical design across each slice or frame, allowing the viewer's eye to focus entirely on shifts in the data rather than shifts in the design.

> **Example: Small-Multiple Relational Graphs**
> Demonstrating the collapse of the "Phillips curve" (unemployment vs. inflation) across nine countries using uniform axes and plot structures for direct comparison.
>
> ![](../../images/3508a332599a7ec6850ce2e56e4946d974a7cc7257c8a290bb7d852d59dade90.jpg)

### 3. Uphold Graphical Integrity
Avoid false graphics and deception. Tell the truth about the data.
- **Maintain Proportional Representation:** The visual representation of the numbers, as physically measured on the surface of the graphic, should be directly proportional to the numerical quantities represented.
- **Avoid "The Lie Factor":** Ensure that `Lie Factor = (size of effect shown in graphic) / (size of effect in data)` stays close to 1.0. Lie factors > 1.05 or < 0.95 indicate substantial distortion.
- **Contextualize the Data:** Do not cherry-pick specific periods (like comparing six months of payments to full years) to create pseudo-declines. Use clear, detailed, and thorough labeling. Write explanations directly on the graphic to defeat distortion and ambiguity.

> **Example: Distortion via Perspective and Sizing**
> The fuel economy standards graphic distorted a 53% numerical increase into a 783% graphical line increase (Lie Factor = 14.8), compounded by deceptive perspective framing.
> 
> ![](../../images/cfed799890403814c3d1e397fa7d09eddecda28358abe244587c10f82aa1cf30.jpg)

## If/Then Troubleshooting Logic

- **If** the visual effect appears out of proportion to the numerical data (e.g., an area growing much faster than its corresponding 1D parameter):
  - **Then** calculate the Lie Factor. If it falls outside the 0.95 - 1.05 range, resize the visual elements so their measured ink directly matches the numerical proportions.
- **If** you are dealing with an exceptionally small dataset (e.g., fewer than 20 numbers):
  - **Then** do not force a graphic. Use a well-formatted table instead, as tables typically outperform graphics for reporting small datasets.
- **If** your graphic's baseline feels "disappearing" or artificially manipulated (e.g., truncating the Y-axis to exaggerate a small change):
  - **Then** explicitly show the zero-baseline or visually flag the truncation to ensure the user perceives the magnitude appropriately.
- **If** you are tempted to add "decorative" elements to make the chart "alive":
  - **Then** pause and consider if the decoration distorts the data measures. If the decoration alters the ink locating the values of numbers, strip it out.

## Verification Checklists

- [ ] Does the graphic present multivariate data seamlessly, without belligerent chartjunk?
- [ ] Is the representation of numbers on the surface physically proportional to the numerical quantities? (Lie Factor ~ 1.0)
- [ ] Are small multiples used when assessing similar sets of variables across different dimensions (time, geography, category)?
- [ ] Does the graphic feature clear, detailed, and thorough labeling directly on the data itself?
- [ ] Have all contextual events been clearly labeled in the data sequence to prevent misinterpretation?
- [ ] Are any image references properly scoped (e.g., `../../images/img.png`)?
- [ ] Have I deferred excessive historical or theoretical background to the `graphify_query` MCP tool?
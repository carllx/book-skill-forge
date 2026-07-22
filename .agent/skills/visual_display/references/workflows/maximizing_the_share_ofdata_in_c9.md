# Maximizing the Share of Data-ink & Editing Principles

## Prerequisites & Context

**When to use this workflow:**
This workflow is essential during the final design, review, or redesign phases of any statistical graphic or visual data display. Its purpose is to increase the signal-to-noise ratio of your graphics by systematically eliminating unnecessary ink. 

**Why it matters:**
The core philosophy is that every drop of ink must present new information. High data-ink ratios reduce visual clutter, enhance readability, and direct the viewer's attention to the actual data. 

> **Deep Dive:** For a full theoretical breakdown of the data-ink ratio calculation and edge cases where redundancy is strictly necessary, run a `graphify_query` for "Data-ink ratio and erasing principles".

---

## Comprehensive Guide & Best Practices

### 1. Maximize the Data-Ink Ratio
The overarching rule of graphical design: **Maximize the data-ink ratio, within reason.**

- **Evaluate Every Mark:** Before finalizing a design, ask if every bit of ink has a definitive purpose. The reason should nearly always be that the ink presents *new* data-information.
- **Calculate Roughly:** If you can mathematically reduce the "denominator" (the total ink) without losing the "numerator" (the data ink), do so.

### 2. The First Erasing Principle: Erase Non-Data-Ink
Ink that does not depict statistical information clutters the data. 

- **Prune Grid Lines:** Thick meshes of grid lines rarely help and often obscure the data plane. Removing them often allows the data to "serve as its own stage."
- **Remove Gratuitous Decoration:** Avoid using boxes, frames, or background colors that add no informational value.

> **Example:** Consider a scatter plot with 63 dark grid marks obscuring 76 data points. Removing the grid ticks can instantly raise the data-ink ratio from `<0.6` to `~0.9`.
> 
> *Before Erasing Non-Data-Ink:*
> ![](../../images/7690761807819410667c7243fdb871bae9482352352a0c3f19f6ca8a30396fc8.jpg)
> 
> *After Erasing Non-Data-Ink:*
> ![](../../images/3e6609ae5fc8318fc069f03203ea88d7c78f09af92ba3691943fefd36e84b191.jpg)

### 3. The Second Erasing Principle: Erase Redundant Data-Ink
Redundant ink depicts the same exact number over and over. **Erase redundant data-ink, within reason.**

- **Deconstruct Bars:** A standard labeled, shaded bar chart often locates altitude in up to six redundant ways (left line, right line, shading height, top horizontal line, number position, and the number itself). 
- **Eliminate Bilateral Symmetry:** Symmetrical designs (like box plots or full Chernoff faces) double the space consumed without adding new information. Asymmetrical halves or half-faces are often just as effective and save ink.

> *Example of Redundant Data-Ink (Bar Chart):*
> ![](../../images/0f3fc5ee0360f0dd6d432617fef4588d45a81cb7717dacf442ddb535d9c57442.jpg)
> 
> *Gratuitous Decoration:*
> ![](../../images/2c4075aab5c7a83065bd1378d35f5d0f1734996741c23bfeba497558aa6639c4.jpg)
> 
> *Bilateral Symmetry:*
> ![](../../images/c0db24de2908c49580240aefd30fbb49a922572f6c1349c039faf217dd0049de.jpg)
> ![](../../images/ee1cc45f80d1f3fa795657f629d40c3f61b89b88a69d879bb1e8af5b8fe39bfc.jpg)

### 4. Edit and Redesign Continuously
Like a prose editor ruthlessly pruning words, a graphical designer must expunge failing ink.

- **Use Opened Space Effectively:** The white space gained from erasing can be repurposed. Add helpful labels, rotate axes for friendlier left-to-right reading, or highlight specific anomalies in the data.
- **Retain Essential Structures:** Erasing is powerful, but do not delete structural elements (like reference curves) that bring order and hierarchy to complex data.

> *Before Redesign:*
> ![](../../images/cf2dbf2c0b6553f7a3b3f68f01cc77e4c0e5ce6b66ffc701caba28049aecc8a5.jpg)
> 
> *After Redesign with structural curves and opened space:*
> ![](../../images/0a493e0392649c15e8feec5b19e710af757d1915c2fbde5b1b70798c80f0052f.jpg)
> ![](../../images/1559c3af1b8a0a08dd169e3f733de7f77017a90649c5010e3c931a162d173e40.jpg)
> ![](../../images/17c9a8cf79bf81ef0c81fc417ab5c06008e3a277ad8667c64354347513662537.jpg)
> ![](../../images/ffebfcdfada82cb51c2ad7f062a781d4e1ce0d9081ae45c93bdc15834682dc0d.jpg)

---

## If/Then Troubleshooting Logic

- **IF** the graphic uses heavy, dark grid lines, **THEN** erase them or mute them significantly. Only retain them if they provide absolute, necessary structural context that the data points alone cannot offer.
- **IF** a data point is represented by multiple intersecting variables (e.g., a filled bar with a numerical label and a top axis line), **THEN** remove the redundant indicators. A single point or a minimalistic line often suffices.
- **IF** the graphic contains cyclical time-series data, **THEN** redundancy might actually be justified. *Exception:* Attaching an extra half cycle or repeating edges helps the eye track continuity without jumping back to the start.
  > *Example of Good Redundancy in Cyclical Data:*
  > ![](../../images/baaa09be0ea90cd19f5943ffcfa97af01fb2c3c5043df093fd0d197b3a685e84.jpg)
  > ![](../../images/de9d31f9f210f60e116a3ff8cdf5865ad540ed8beeb0227614ba89f951d28acb.jpg)
  > ![](../../images/a592b09f0edad9d8fa1d8b6457e2555df0096ef177b90037d3fdb26f51e745d5.jpg)
- **IF** removing an element makes the data completely unreadable or disorganized, **THEN** restore it. Structural curves that give hierarchy are examples of essential non-data ink.

---

## Verification Checklists

**Pre-Review Checklist:**
- [ ] Is the data-ink ratio maximized?
- [ ] Has all non-data-ink (e.g., heavy grids, decorative frames) been erased or minimized?
- [ ] Have all redundant data representations (e.g., symmetrical halves, over-labeled bars) been reduced to a single unambiguous indicator?

**Post-Review Checklist:**
- [ ] Does the remaining ink present fresh, statistical information?
- [ ] Is the space opened up by erasing being used effectively (e.g., for annotations, better labels)?
- [ ] Has any necessary structural redundancy (like cyclical continuations) been preserved and justified?
- [ ] Is the data standing on its own stage, uninterrupted by "mosquito-like" grid ticks?
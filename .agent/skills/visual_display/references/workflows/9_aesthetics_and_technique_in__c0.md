# Aesthetics and Technique in Data Graphical Design

## Prerequisites & Context
This workflow distills the principles of graphical aesthetics, elegance, and technique from Edward Tufte's theory of data graphics. The goal is to produce visual displays of quantitative information that are not only accurate and data-rich but also aesthetically pleasing, accessible, and elegantly constructed.

**When to use this workflow:**
- When deciding whether to use a sentence, a table, or a graphic to present numbers.
- When refining a graphic's typography, line weight, and proportion.
- When integrating explanatory text, labels, and data into a cohesive narrative.
- When you need to transform a dense, technically correct chart into a "friendly" data graphic.

> **Note on Theory:** For deep textbook insights into specific historical examples (such as Minard's map of Napoleon's or Hannibal's campaigns) or the psychological studies behind visual perception, use the `graphify_query` MCP tool with queries like "Aesthetics in Data Graphical Design" or "Choice of Design: Tables vs Graphics".

## Comprehensive Guide & Best Practices

### 1. The Choice of Design Format
Match the volume and complexity of your data to the appropriate display structure:
- **Sentences:** Poor for more than two numbers because they prevent structured comparisons.
- **Text-Tables & Tables:** Best for small data sets or when exact numerical values must be shown. Use well-ordered rows (e.g., by data values, not alphabetically) to facilitate comparisons.
- **Supertables:** For many localized comparisons, a well-organized, large table with topical paragraphs and sequential detail often outperforms dozens of small bar charts.
- **Data Graphics:** Best for large datasets, relational patterns, and showing "accessible complexity." 
- **Avoid Pie Charts:** Their low data density and failure to order numbers along a visual dimension make them universally inferior to tables or other graphic types.

### 2. Integrating Words, Numbers, and Pictures
Treat data graphics as paragraphs about data. Do not segregate the visual from the textual.
- **Show, Don't Tell:** Write messages directly on the plotting field. Label outliers, explain interesting data points, and integrate legends directly into the graphic.
- **Run-in Placement:** Insert graphics and tables directly into the text where they are discussed. Avoid "See Fig. 2" references that force the reader to turn pages.
- **Consistent Typography:** Use the same typeface for the text and the graphic. Avoid arbitrary ruled lines that separate text from data.
- **Exploratory Guidance:** If the graphic is complex or exploratory, use words to tell the viewer *how* to read the design, rather than just *what* the content means.

### 3. Accessible Complexity & The "Friendly" Graphic
Design with the viewer in mind to create an open and accessible display:
- **Typography:** Avoid using ALL CAPS for labels, as words in all capitals present difficult reading. Use serif or well-differentiated sans-serif fonts to ensure ease of reading.
- **Labels:** Ensure words are spelled out entirely—do not use cryptic abbreviations. Words should run horizontally, from left to right.
- **Colors & Shading:** Use calm shading and light, transparent colors (especially for flow lines or overlapping elements) so underlying data and text can show through. Avoid garish, heavily saturated tones or moiré vibration effects.

### 4. Proportion, Scale, and Line Weight
Aesthetic balance is achieved through careful attention to line geometry:
- **Thin Lines:** Background lines, axes, and grids should be hair-thin. Thick, clumsy linework dilutes the data.
- **Orthogonal Intersections:** Enhance visual interest through the perpendicular intersection of lines of differing weights.
- **Data-Ink Emphasis:** The heaviest line weights must correspond to the data measures. A data line must visually dominate the connecting verticals or grid lines.

### 5. The Shape of Graphics
Graphics should generally tend toward the horizontal (greater in length than height):
- **Analogy to the Horizon:** The human eye is naturally practiced at detecting deviations from the horizon.
- **Ease of Labeling:** Horizontal stretching makes it easier to write and read left-to-right text.
- **Causal Emphasis:** A longer horizontal axis helps elaborate the workings of the causal variable in detail over time.
- **Rule of Thumb:** If the data itself does not dictate a specific shape, move toward horizontal graphics that are about 50 percent wider than they are tall (approximating the Golden Rectangle, $1.618 \dots$).

## If/Then Troubleshooting Logic

- **If** a chart looks garish or cluttered, **Then** reduce the color saturation, make non-data lines hair-thin, and replace heavy shading with light, transparent colors.
- **If** viewers struggle to understand the meaning of a data point, **Then** integrate text directly onto the plotting field to label the point and explain its context.
- **If** you are dealing with only a few numbers (e.g., 5-20 data points), **Then** abandon the data graphic and construct a well-ordered text-table or supertable instead.
- **If** the labels on the y-axis are forced to be printed vertically, **Then** widen the graphic horizontally or restructure the design so that all text reads left-to-right.
- **If** the trend line is extremely wiggly, **Then** ensure the graphic is significantly wider than it is tall to make it easier for the eye to follow the variations.

## Verification Checklists

### Aesthetics and Format Checklist
- [ ] Are pie charts entirely avoided in favor of tables or bar charts?
- [ ] Are datasets with fewer than 20 numbers presented as tables or text-tables rather than graphics?
- [ ] Is the graphic integrated seamlessly into the surrounding text without artificial segregation or "See Figure X" references?
- [ ] Is the graphic roughly 50% wider than it is tall, unless the nature of the data requires otherwise?

### Typography and Labeling Checklist
- [ ] Are words spelled out horizontally (left-to-right)?
- [ ] Are labels and explanations placed directly on the plotting field?
- [ ] Is ALL CAPS avoided for continuous reading or labeling?
- [ ] Does the graphic use the same typeface as the main text?

### Linework and Proportion Checklist
- [ ] Are non-data lines (grids, axes) drawn as hair-thin lines?
- [ ] Do the data measures (the actual data lines) have the heaviest line weight?
- [ ] Do orthogonal intersections utilize contrasting line weights to maintain clarity?
- [ ] Are colors transparent and calm, avoiding garish tones and visual vibration?

> *The core of graphical aesthetics is the clear portrayal of complexity. Do not complicate the simple; rather, give visual access to the subtle and the difficult.*
# Theory of Data Graphics: Small Multiples, Data-Ink, and Graphical Redesign

## Prerequisites & Context

**Why and When to Use This Workflow**  
This workflow establishes the fundamental theory and design heuristics for creating effective, high-density data graphics. Use this guide when designing or reviewing statistical charts, visual reports, or data-driven interfaces. It focuses on maximizing the ratio of data-information to ink, redesigning conventional chart structures (e.g., box plots, bar charts, scatterplots), and leveraging "small multiples" for comparative analysis.

> For deep theoretical dives into the origins of data graphics (e.g., William Playfair's time-series) or extensive perceptual studies on data-ink, use the `graphify_query` MCP tool to search for `Theory of Data Graphics` or `Data-Ink Ratio`.

## Comprehensive Guide & Best Practices

### 1. The Fundamental Principle: "Above All Else Show the Data"
Data graphics are instruments to help people reason about quantitative information. The design must draw the viewer's attention to the substance of the data, not the graphical apparatus.

- **Data-Ink Ratio**: Maximize the proportion of a graphic's ink devoted to the non-redundant display of data-information.
- **Rule of Erasing**: If ink can be erased without losing data-information, it is non-data-ink or redundant data-ink. Erase it.
  - *Less is more* for non-data-ink.
  - *Less is a bore* for data-ink.

### 2. Small Multiples: High-Density Comparative Design
Small multiples resemble the frames of a movie: a series of graphics showing the same combination of variables, indexed by changes in another variable.
- **Characteristics**:
  - Inevitably comparative and deftly multivariate.
  - Shrunken, high-density graphics usually based on a large data matrix.
  - Drawn almost entirely with data-ink.
  - Efficient in interpretation: once the viewer decodes one frame, they instantly understand the rest.

> **Example of Small Multiples Concept**
> ![](../../images/4eb6902bc549b44940bd1f8b120f9875c8f89308a15f6ce873dfd71532d2d1d0.jpg)

### 3. Redesigning Conventional Charts (Data-Ink Maximization)

#### A. The Box Plot
Conventional box plots require drawing excessive boxes and whiskers. Convert them to elegant **quartile plots**:
- Erase the rectangular box.
- Show the middle half of the distribution by offsetting the line or using a thicker line weight.
- Leave only the exact points of data (minimum, maximum, quartiles, median).

> **Quartile Plot Evolution**
> Start: Traditional range bar (Spear)
> ![](../../images/d2384c84c9b15e2ca1338a2a21fa66b1d10ea686d7dff48a5dd20caea7a8c43d.jpg)
> *Heuristic*: Can you trace the quartiles using only single offset lines? Does it reduce drawing time without losing the 5-number summary?

#### B. The Bar Chart / Histogram
Standard bar charts are overloaded with thick boxes, heavy vertical axes, and tick marks.
- **Erase the box outlines**: Just use the solid fill.
- **Erase the vertical axis**: Let the grid lines guide the scale.
- **Use White Grids**: Instead of black tick marks, use a white grid overlaid on the filled bars to explicitly mark intervals. This eliminates the need for an external y-axis line.
- **Erase the thick baseline**: The bottom of the bars implicitly defines the zero point.

> **Before vs After Concept**
> Before:
> ![](../../images/ff1e4d1d9890130e45328f50aa255de8441ea58413683a4fa0b7ffb12ce24c66.jpg)
> After:
> ![](../../images/3ab431236c0b258e94b304c1158952fab02a060fec98cbb1f9bfdbda64559165.jpg)

#### C. The Scatterplot & Range-Frame
The traditional scatterplot traps data inside an arbitrary square box. Turn the frame into a data-communicating element.
- **Trim the frame**: Make the frame lines extend *only* from the minimum observed data point to the maximum observed data point on both axes. This is called a **Range-Frame**.
- **Quartile Frame**: Break the range-frame at the first and third quartiles to display the 5-number summary directly on the axes.
- **Dot-Dash-Plot**: Replace the axes entirely with marginal frequency distributions (a "rug plot") of each variable. This plots marginal and joint distributions together.

> **Range-Frame Evolution**
> Standard Scatterplot:
> ![](../../images/2a7102db77874b52d950c05ad49221db470852d7e3741897cc4433a19d849090.jpg)
> Range-Frame (Axes trimmed to data limits):
> ![](../../images/84ed9d1dd3f647d23282433ef78ddb94d482704b454958764c0b72fdad8fd8a0.jpg)
> Dot-Dash-Plot (Axes replaced by marginal distributions):
> ![](../../images/5d6a2c235f249099f6dc1256c3804372878dca65503f30b1a50795c70cba3a32.jpg)

## If/Then Troubleshooting Logic

| Condition | Action / Strategy |
| :--- | :--- |
| **If** the graphic is dominated by grid lines and bounding boxes... | **Then** systematically erase the grid, or invert it (e.g., white lines on data bars). Remove the bounding box if it doesn't represent data limits. |
| **If** comparing multiple subsets of data becomes confusing in a single overlaid chart... | **Then** split the data into **small multiples**. Ensure the graphical design, scale, and layout remain strictly constant across all frames. |
| **If** users struggle to read the exact distribution boundaries on a scatterplot... | **Then** implement a **range-frame** or **quartile frame**, trimming the axis lines to reflect the empirical minimum and maximum. |
| **If** the graphic has a null or negative Data-Ink Ratio... | **Then** immediately redesign. Stop using ink for decorative borders, background shading, and heavy ticks. Re-plot the data to be the primary visual element. |

## Verification Checklists

### Graphical Redesign Validation
- [ ] Is the data-ink ratio maximized? (Calculate visually: Could any non-data ink be erased without losing information?)
- [ ] Have all unnecessary frames and bounding boxes been removed?
- [ ] Are grid lines muted, lightened, or replaced with "white grid" intersections on data marks?
- [ ] Do bar charts utilize implicit baselines and avoid redundant boxing?
- [ ] Are scatterplots utilizing range-frames or dot-dash-plots to provide marginal distribution data?

### Small Multiples Validation
- [ ] Are the multiples structurally identical (same scale, axes, and visual encoding)?
- [ ] Do the multiples allow the eye to easily compare changes between variables without re-learning the graphic?
- [ ] Is the data density high enough to justify the display (vs. using a simple table)?
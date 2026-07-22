# Workflow: Designing Time-Series and Relational Graphics

## Prerequisites & Context

**Why and When to Use This Workflow:**
This workflow is designed to guide the creation of time-series plots and relational graphics. Time-series displays are the most frequently used form of graphic design due to the natural ordering of the time scale, which provides a strong and efficient rhythm for interpretation. However, the simple passage of time is not a causal explanatory variable. Descriptive chronology must often be enhanced or replaced by relational graphics that confront statements about cause and effect with empirical evidence. 

Use this workflow when you need to represent large, variable datasets over time, or when you need to demonstrate causality between two or more variables. Do not use this workflow for simple linear changes that are better served by a table or a sentence.

> **Deep Dive:** For bulk theoretical reading on graphical history (Playfair, Lambert, Marey), the evolution of time-series, or the critique of the "data is boring" doctrine, invoke the `graphify_query` MCP tool.

## Comprehensive Guide & Best Practices

### 1. Leverage High Data Density for Time-Series
Reserve the power of data graphics for rich, complex, and difficult statistical material. Do not waste space plotting simple linear changes that can be summarized in one or two numbers.

*   **Display Real Variability:** Use time-series to show large collections of numbers, make comparisons between different parts of the data, and tell a story.
*   **Avoid Tabular Data in Graphical Form:** If a dataset is small, non-comparative, and highly labeled, it belongs in a table.

> **Example (NYC Weather Summary):** Depicting 1,888 numbers, showing daily high and low temperatures relative to a long-run average, providing both historical context and a forecast. See `../../images/077e543d53a9be241ceb47359a603d010270ceabf37454282abac1b953776651.jpg`.

### 2. Move Beyond Descriptive Chronology
The simple passage of time is rarely a good explanatory variable. Chronology does not equal causality.

*   **Smuggle in Additional Variables:** Introduce other variables into the graphic design to provide causal explanation. 
*   **Use Dual Labels:** Add multiple scales or labels (e.g., distance and date, or phase and time) to enrich the context without cluttering the data.
*   **Decompose Data:** Break out time-series into seasonal fluctuations, trading-day cycles, and long-run trends to reveal underlying patterns.
*   **Before-After Designs:** Use before-and-after time-series to vividly demonstrate the impact of an event.

> **Example (Playfair's Balance of Trade):** Showing imports and exports as dual lines, shading the difference to illustrate the shifting balance—a clear visual arithmetic of profit and loss. See `../../images/3bac21bd586bec6f651f3a677718d7a57dd02de5b35cdd5196f3e03494f72044.jpg`.

### 3. Embrace Relational Graphics for Causal Explanation
To achieve graphical sophistication, advance beyond time-series and maps. Use relational graphics to link two or more variables, confronting theories of "X causes Y" with empirical evidence.

*   **Reject Simplistic Doctrines:** Do not subscribe to the beliefs that "statistical data are boring" or that "graphics are only for the unsophisticated reader." These doctrines lead to over-decorated, simplistic designs (chartjunk) and "big lies."
*   **Demand Graphical Intelligence:** Maintain the same standard of intelligence and sophistication for your graphics as you do for your prose. Relational graphics are explanatory and essential for competent analysis.

> **Reference:** For examples of multivariate displays, such as Voyager 2's radio emissions from Jupiter, see `../../images/18489170b86de71e6bd6d823d34341612526b6dd558c38ab2752b56beccb2ee9.jpg`.

## If/Then Troubleshooting Logic

*   **IF** the data consists of a very short, simple sequence of numbers with little variability, **THEN** remove the graphic and present the information in a table or as text.
*   **IF** the time-series simply shows a trend over time but fails to explain *why* the trend is occurring, **THEN** "smuggle" additional explanatory variables into the design (e.g., mapping events, seasonal adjustments, or related metric overlays).
*   **IF** you are tempted to animate or decorate a graphic because the data seems "boring," **THEN** stop. If the statistics are boring, you have the wrong numbers. Focus on finding better data rather than embellishing weak data.
*   **IF** your publication dictates that graphics must be instantly understandable at a glance, **THEN** resist the urge to dumb them down. Push for explanatory relational graphics that respect the reader's intelligence.

## Verification Checklists

**Time-Series Integrity & Depth:**
- [ ] Does the graphic contain a sufficiently large dataset to warrant a visual display rather than a table?
- [ ] Is the time scale naturally ordered and properly scaled?
- [ ] Have you moved beyond mere chronology by integrating causal or explanatory variables?
- [ ] Are small, non-comparative datasets relegated to text or tables?

**Relational & Sophistication Check:**
- [ ] Does the design link two or more variables (excluding time or geography) to test causal relationships?
- [ ] Is the graphic free from patronizing embellishments and chartjunk?
- [ ] Have all image paths been correctly formatted relative to the workflows directory (e.g., `../../images/img.png`)?
- [ ] Does the graphic match the sophistication and complexity of the accompanying prose?
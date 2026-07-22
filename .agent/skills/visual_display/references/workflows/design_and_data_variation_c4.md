# Workflow: Design and Data Variation

## Prerequisites & Context
When generating or evaluating statistical graphics, a core goal is **graphical integrity**—ensuring the visual representation accurately reflects the underlying numerical representation. This workflow provides actionable heuristics to avoid deceiving the viewer by confusing **design variation** with **data variation**. 

Use this workflow when:
- Designing time-series graphics, particularly those involving monetary values over time.
- Choosing how to represent one-dimensional data visually.
- Setting the context for statistical comparisons to answer the fundamental question: "Compared to what?"

> [!NOTE]
> For a deep dive into the historical origins of graphical integrity, the "Lie Factor", or additional theoretical context from Edward Tufte's work, use the `graphify_query` MCP tool with queries like "Tufte Design and Data Variation" or "Graphical Integrity".

## Comprehensive Guide & Best Practices

### 1. Show Data Variation, Not Design Variation
Each part of a graphic generates visual expectations. If a scale moves in regular intervals initially, the viewer expects it to continue uniformly. Changing the scale midway through a graphic (e.g., squishing years or expanding axes) creates an illusion of change where none exists.

- **Maintain Consistent Scales**: Ensure both horizontal (e.g., time) and vertical (e.g., value) scales remain perfectly uniform throughout the graphic. 
- **Avoid Multiplicative Distortion**: Do not shift two scales simultaneously, as it takes on multiplicative force and exaggerates the data exponentially.

> **Example of Design Variation vs. Data Variation:**
> Using an irregular scale can concoct a pseudo-decline. If the first seven increments on an axis are ten years long, but the final interval is four years long, a line graph will artificially "drop" at the end. 
> *See: `../../images/4cfbbc5ce0907880d2630c87a13873108c0079691f889eecc0dbae619542e6c7.jpg` (Irregular scale) vs `../../images/83af46c7ba149f3d32f3a910d1eaa0ddb4512756e85cf616e696776cf5ee1631.jpg` (Corrected scale)*

### 2. Deflate and Standardize Monetary Units
When displaying financial data over time, failing to adjust for inflation mixes up changes in the value of money with actual changes in the budget or price. 

- **Use Constant Dollars**: In time-series displays of money, deflated and standardized units of monetary measurement are nearly always better than nominal units.
- **Account for Population Growth**: When measuring government spending or broad metrics, adjust to "per capita" to reveal the true underlying trend rather than just parallel population growth.

> **Example:**
> A state budget might appear to be skyrocketing in nominal dollars, but when calculated in *constant dollars per capita*, the real spending might actually be flat or declining. 
> *See: `../../images/5bc6b8509293b2f85878937ece4a3143b0f44ac5021f78146fe5d634a28e29b4.jpg`*

### 3. Match Visual Dimensions to Data Dimensions
A common graphical fallacy is the "shrinking dollar" or "growing barrel" where one-dimensional data (e.g., the rate of inflation or the price of oil) is shown by varying the 2D area or 3D volume of an object.

- **1D Data = 1D Visual Measure**: The number of information-carrying (variable) dimensions depicted should not exceed the number of dimensions in the data.
- **Avoid Area/Volume Abstractions**: Changes in physical area on the surface of a graphic do not reliably produce appropriately proportional changes in perceived areas by the viewer. 

> **Example:**
> If the price of oil increases by 454%, displaying it as a 3D barrel that increases in volume by 27,000% yields a massive "Lie Factor". Use simple lines or bars for 1D data instead.
> *See: `../../images/543f84856d4d1399b77b6681eb37883e35328dace0790d33abb8e682b5d4c36f.jpg`*

### 4. Provide Sufficient Context
Data graphics must bear on the question at the heart of quantitative thinking: "Compared to what?" Graphics often lie by omission.

- **Do Not Quote Data Out of Context**: Always provide a baseline or a historical backdrop.
- **Show the "Before" and "After"**: A sudden drop in a single year means nothing without knowing the trajectory of the years preceding and following it.
- **Use Adjacent Comparisons**: Compare the primary subject (e.g., a state or a company) with its peers (e.g., neighboring states) to prove that an observed effect isn't just a broader systemic trend.

> **Example:**
> Showing a single year's drop in traffic fatalities after a speeding crackdown is meaningless without the prior years' baseline and without comparing it to neighboring states who did not implement a crackdown. 
> *See: `../../images/335ddd21c035fac1d8c96332b137d3e3c3782781454a6fbac97b09619021b42c.jpg`*

## If/Then Troubleshooting Logic

- **IF** a time-series curve suddenly drops or spikes at the very end of a graph, **THEN** check the X-axis intervals. Is the final interval representing a shorter timeframe than the rest? Adjust the scale to be uniform.
- **IF** an economic graph shows "skyrocketing" growth over a long period (e.g., decades), **THEN** verify if the data is in nominal or real (constant) units. Convert to constant, inflation-adjusted units to see the true trend.
- **IF** the graphic uses icons (like cars, coins, or barrels) that grow or shrink to represent data, **THEN** calculate the 1D percentage change of the data versus the 2D/3D percentage change of the icon. If they don't match, replace the icons with standard bars or points.
- **IF** a graphic highlights a single isolated data point or a tiny 2-point trend to prove a massive success/failure, **THEN** request the broader context. Ask "Compared to what?" and plot the adjacent historical data and peer groups.

## Verification Checklists

- [ ] Are the horizontal and vertical scales perfectly uniform across the entire graphic?
- [ ] Have all financial time-series data been adjusted for inflation (constant dollars)?
- [ ] If applicable, has broad demographic data been adjusted for population growth (per capita)?
- [ ] Does the visual dimension match the data dimension? (No 2D/3D objects for 1D data).
- [ ] Is there sufficient historical context to establish a baseline trend?
- [ ] Is there sufficient peer context to rule out broader systemic variables?
- [ ] Are all image paths properly rewritten relative to the workflows directory (e.g., `../../images/img.png`)?
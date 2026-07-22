## Part 14

> [BREADCRUMB_CTX: 《visual_display》 > Part 14]

The principle hasa great many consequences for graphical editing and design. The principlemakes good sense and generates reasonable graphical advice-for perhaps two-thirds ofall statistical graphics. For the others, theratio isill-defined or is just not appropriate. Mostimportant,however,is that other principles bearing on graphical design follow from theidea of maximizing the share of data-ink.

# Two Erasing Principles

The other side of increasing theproportion ofdata-ink is an erasing principle:

Erase non-data-ink, within reason.

Ink thatfails to depict statistical information doesnot havemuch interest to the viewer ofa graphic; in fact,sometimes such nondata-ink clutters up the data, as in thecase ofa thick mesh ofgrid lines. While it is true that this boring ink sometimes helps set the stage for the data action, itis surprising, aswe shall seein Chapter 7, how often thedata themselves can serve astheirown stage.

Redundant data-ink depicts the same number over and over. The labeled, shaded barofthe barchart, for example,

![](images/0f3fc5ee0360f0dd6d432617fef4588d45a81cb7717dacf442ddb535d9c57442.jpg)

unambiguously locatesthe altitude insix separate ways (any five of the six can be erased and the sixth will still indicate theheight): as the(1)heightof the left line, (2)height ofshading,(3) height ofright line,(4) position oftop horizontal line,(s) position (not content) ofnumber at bar's top,and (6) thenumber itself. Thatis more waysthan are needed. Gratuitous decoration and reinforcement ofthedata measures generate much redundant data-ink:

![](images/2c4075aab5c7a83065bd1378d35f5d0f1734996741c23bfeba497558aa6639c4.jpg)

Bilateral symmetry of data measures also creates redundancy, asinthe box plot,the open bar,and Chernoff faces:

![](images/c0db24de2908c49580240aefd30fbb49a922572f6c1349c039faf217dd0049de.jpg)

Half-faces carry thesame information asfull faces. Halves may be easier to sort (by matching the righthalf ofan unsorted face to the lefthalfofasorted face) than full faces. Orelse an asymmetrical full face can beused to report additional variables.1

Bilateral symmetry doubles the space consumed by the design in agraphic, without adding new information. The few studies done on the perception ofsymmetrical designs indicate that "when looking ata vase,for instance,a subject would examine one of its symmetric halves, glance at the other half and, seeing that it was identical, cease his explorations. The enjoyment of symmetry lies not with the physical properties of the figure. At least eye movements suggest anything but symmetry, balance,or rest."2

![](images/ee1cc45f80d1f3fa795657f629d40c3f61b89b88a69d879bb1e8af5b8fe39bfc.jpg)  
1Bernhard Fluryand HansRiedwyl, "Graphical Representation ofMultivariate Data byMeans of Asymmetrical Faces,JournaloftheAmerican Statistical Association, 76 (December 1981),757- 765.

Redundancy, upon occasion, has its uses: givinga contextand order to complexity, facilitating comparisons over various parts of the data,perhaps creating an aesthetic balance. Incyclical timeseries, for example, partsofthecycle should berepeated sothat the eye can track any part of the cycle without having to jump back to the beginning.Such redundancy possibly improvesMarey's $^ { 1 8 8 0 }$ train schedule. Those people leavingParis orLyon in the evening find thattheir trainsrun offtheright-hand edge of the chart, tobepicked up on theleft again:

![](images/baaa09be0ea90cd19f5943ffcfa97af01fb2c3c5043df093fd0d197b3a685e84.jpg)

Attaching an extra half cycle makes every train in the first 24 hours of the schedule a continuous line (as would mounting the original on a cylinder):

![](images/de9d31f9f210f60e116a3ff8cdf5865ad540ed8beeb0227614ba89f951d28acb.jpg)

And, similarly, instead of once around theworld in this display ofsurface ocean currents, oneand two-thirds timesaround is better:

![](images/a592b09f0edad9d8fa1d8b6457e2555df0096ef177b90037d3fdb26f51e745d5.jpg)  
KirkBryanand Michael D. Cox,"The Circulation ofthe World Ocean: A Numerical Study. Part 1, A Homogeneous Model,"Journal ofPhysical Ocean

Most data representations, however, are ofa single, uncomplicated number,and littlegraphical repetition isneeded. Unless redundancy hasa distinctly worthy purpose,the second erasing principleapplies:

Erase redundant data-ink, within reason.

# Application ofthe Principles in Editing and Redesign

Justas a good editor ofprose ruthlessly prunes out unnecessary words, SO a designer ofstatistical graphics should prune outink that fails topresent freshdata-information. Although nothing can replace a good graphical ideaapplied to an interesting set ofnumbers, editing and revision are as essential to sound graphical design work as they are to writing.T. S. Eliot emphasized the 'capital importance ofcriticism in thework ofcreation itself. Probably, indeed, the larger part ofthe labour ofan authorin composing hiswork iscritical labour; the labour of sifting,combining, constructing, expunging, correcting, testing: thisfrightful toil is asmuch critical as creative."3

Consider this display,which compares each long bar with the adjacent short bar to showthe viewer that, under thevarious experimental conditions, the long bar is longer:

![](images/cf2dbf2c0b6553f7a3b3f68f01cc77e4c0e5ce6b66ffc701caba28049aecc8a5.jpg)  
3T.S. Eliot, "The Function ofCriticism," in Selected Essays1917-1932 (New York, 1932),p.18.

Vigorous pruning improves the graphic immensely, while still retaining all thedata of the original. Itis remarkable that erasing alone can work such a transformation:

Lbub llbb L 山 H江

The horizontals indicate thepaired comparisons and would change if the experimental design changed-so they count as informationcarrying. All theasterisks areout since every paired comparison was statistically significant, a point that the caption can note. Here is themix ofnon-data-ink and redundant data-ink thatwaserased, about 65 percent of the original:

L L

Thedata graphical arithmetic looks like this- -theoriginal design equals the erased part plus the good part:

中 Lbb Lnll bbu 血 血 LiH H 8 Y 8 pres pestOs pretee poettoa postQs pretea pesttes

The next graphic, drawn by the distinguished science illustrator RogerHayward, shows the periodicity of properties ofchemical elements, exemplifiedbyatomic volume asa function ofatomic number. The data-inkratio is less than 0.6, lowered because the 76 data points and thereference curves are obscured by the63 dark grid marksarrayed overthe data plane like a precision marching band of 63 mosquitoes:

![](images/7690761807819410667c7243fdb871bae9482352352a0c3f19f6ca8a30396fc8.jpg)

The grid ticks compete with theessential information ofthe graphic, the curves tracing out theperiods and the empirical observations. The little grid marks and part of the framecan besafely erased, removed from the denominatorof thedata-ink ratio:

![](images/3e6609ae5fc8318fc069f03203ea88d7c78f09af92ba3691943fefd36e84b191.jpg)

The uncluttered display brings out another aspect of the data: several ofthe elementsdo not fit the smooth theoretical curves all thatwell. The data-inkratio hasincreased to about .9,with only the frame lines remaining as pure non-information:

![](images/0a493e0392649c15e8feec5b19e710af757d1915c2fbde5b1b70798c80f0052f.jpg)

The reference curvesprove essential fororganizing thedata to show the periodicity. Thecurves create a structure, giving an ordering, a hierarchy, to theflow ofinformation from the page:

![](images/1559c3af1b8a0a08dd169e3f733de7f77017a90649c5010e3c931a162d173e40.jpg)

Restoring thegrid fails to organize the data.The ticks aretoo powerful, and they also add a disconcerting visual vibration to the graphic. With theticks, the reference curves become all themore necessary, since the eye needs someguidance through the mazeof dotsand crosses:

![](images/17c9a8cf79bf81ef0c81fc417ab5c06008e3a277ad8667c64354347513662537.jpg)
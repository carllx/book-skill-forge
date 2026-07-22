## Part 18

> [BREADCRUMB_CTX: 《visual_display》 > Part 18]

![](images/0c9b5987d9a061ddf4bb5ebe1d4883dc2ca26fbcaa3b5cd0581b3d3f34d5831a.jpg)

Reflecting theone-dimensional projections from each scatter, the dashes encourage the eye to notice how each plot filters and translates thedata through thescatter from one adjacent plot to the next. Sometimes itisuseful to think ofeach bivariate scatter as the imperfect empirical representation ofan underlying curve that transforms onevariable into another. In therugplot, the sequence ofvariables can wander off asappropriate. Thequantitative history ofa single observation can be traced through a series ofone-and two-dimensional contexts.

# Conclusion

Thefirst part ofatheory ofdata graphics isin place. The idea,as described in the previous threechapters,is thatmost ofa graphic's ink should vary in response to datavariation. The theory has something tosayabouta greatvariety of graphics-workaday scientific charts,the unique drawings of Roger Hayward, the exemplars of graphical handbooks, newspaper displays, computer graphics, standard statistical graphics, and the recent inventions of Chernoffand Tukey.

Theobserved increases inefficiency, inhow much of the graphic's ink carries information, aresometimes quite large. In several cases, thedata-ink ratio increased from .1 or.2 to nearly 1.0. The transformed designs are less cluttered andcan beshrunk down more readily than theoriginals.

But,are the transformed designs better?

(1)They are necessarily betterwithin the principles of the theory, for more information per unit of space and per unit of ink is displayed. And thisis significant; indeed, thehistory ofdevices for communicatinginformation is written in terms of increases in efficiency ofcommunication and production.

（2) Graphics are almost always going to improve as they go through editing, revision, and testing against different design options. Theprinciples ofmaximizing data-ink and erasing generate graphical alternatives and also suggest a direction in which revisions should move.

(3) Then thereis the audience:will those looking at the new designs be confused? Some ofthe designs are self-explanatory, as in the case of the range-frame. The dot-dash-plot is more difficult, although it still shows all thestandard information found in the scatterplot. Nothing is lostto those puzzled by the frame of dashes, and something is gained by those who do understand. Moreover, it is a frequent mistake in thinking aboutstatistical graphics to underestimate theaudience. Instead, why not assume that if you understand it, most other readers will, too? Graphics should be as intelligentand sophisticated as theaccompanyingtext.

（4） Some of the new designs mayappear odd,but this is probably because we havenot seen them before. Theconventional designs for statistical graphics have beenviewed thousands of times by nearly every reader of this book; on theother hand, the rangeframe,thedot-dash-plot,the white grid, the quartile plot,the rugplot,and thehalf-face just afew times. With use, thenew designs will cometo look justas reasonable astheold.

Maximizing dataink (within reason) is buta single dimension of a complex and multivariate designtask. Theprinciple helps conduct experiments in graphical design. Someof those experiments will succeed. There remain, however, many other considerations in the design ofstatistical graphics-not only of efficiency, butalso ofcomplexity, structure, density,and even beauty.

# 7 Multifunctioning Graphical Elements

The sameink should often serve more than onegraphical purpose. A graphical element may carry datainformation and alsoperform a design function usually left to non-data-ink. Or it might show several different pieces ofdata. Such multifunctioninggraphical elements, ifdesigned with care and subtlety, can effectively display complex, multivariate data.1

Consider, for example, themultifunctioning blot of the blot map.It simultaneously locates the geographic unit on a twodimensional surface, describesthe shape of the geographic unit, and indicates thelevel ofthevariable displayed bycolor or intensity of shading. Thatis a great deal ofinformation for a small patch ofink-and the different pieces of information arenot confounded and mixed together.

In contrast, theconventional graphical frame performs only a modest design function,the separation ofthe grid and data measures from thelabels. And itis a placeto hang the grid ticks. With all thatink doing so little, itisa prime candidate formobilization as a double-functioning graphical element. Hence the range-frame, thequartile frame,and thedot-dash-plot.

The principle, then,is:

Mobilize everygraphical element, perhaps several times over, to show thedata.

The danger ofmultifunctioning elements is that they tend to generate graphical puzzles, with encodings that can onlybe broken by their inventor. Thus design techniques for enhancing graphical clarity in theface ofcomplexity must be developed along with multifunctioning elements.

# Data-Built Data Measures

The graphical element that actually locates or plots the datais the data measure. The bars ofa bar chart,thedotsofa scatterplot, the dots and dashes ofa dot-dash-plot, the blots ofa blot map are data measures. Theink ofthe data measure can itselfcarry data; for example, the dotsof the scatterplot can take on different shadings in response to a third variable.

Building data measures out ofthe data increases thequantitative detail and dimensionalityofa graphic. The stem-and-leaf plot constructs the distribution ofa variable with numbers themselves:

$0 | 9 = 9 0 0$ feet

97719630 69987766544422211009850 876655412099551426 9998844331929433361107 97666666554422210097731 898665441077761065 98855431100652108073 653322122937 377655421000493   
10 0984433165212   
11 4963201631   
12 45421164   
13 47830   
14 00   
15 676   
16 52   
17 92   
181 5 39730

Stem-and-leafdisplays: heightsof218volcanoes,unit 100feet.

19 $\mid 3 = 1 9 , 3 0 0$ feet

Theidea ofmaking every graphical element effective was behind the design of the stem-and-leaf plot.In presentinghis invention, John Tukey wrote: "If we are going tomake a mark,it may as well be ameaningful one. The simplest-and mostuseful -meaningful mark is a digit."2

Here, too, thedata form thedata measure. Note the bimodal distribution in the histogram ofcollege students arranged byheight.

![](images/ac06671a755d30cee7d28e9f263ee0386211f2dc19221f79d16a11a1f8f8b335.jpg)

A distinguished graphic thatbuilds data measures out ofdata was designed by Colonel Leonard P. Ayres for his statistical history of World WarI, a book with several notable graphics all doneby typewriter and rule. Constructing thedata measures outof each American division'sname （a numerical designation) turnswhat might havebeen a routine time-series into an elegant display. (Note that the cumulative design depends on the fact that none ofthe divisionsreturned before October 1918.) Thetriple-functioning data measure shows: (1) the number of divisions in Francefor each month,June 1917 to October 1918;(2) what particular divisions were in France ineach month; and(3）the duration ofeach division' presence in France.

Leonard P. Ayres, The Warwith Ger-many(Washington,D.C.,1919)，p.102.

3466848740 838313466846740   
4039888178369129 398881766 39   
36919976298790 36 88178636962970289878003056274285275532442621   
91   
9   
776 76   
29702288887880 297 29   
5   
90   
9289 92 92   
89 9988   
88 83   
7800303627428552736324142621 78 78   
030386274283527 30 808 80350   
3862742835 33 38   
6274885 62742852755324422621   
82 82   
785324142621 7352442621 77   
2626 422621 41422621 4422621 3241422621 8524422621 3532422621 5524422621   
1 1   
Jum Jul Aug Sep Oct Hov Dec Jan FebMar Apr May Jum Jul Aug Sep Oct   
1917 1918
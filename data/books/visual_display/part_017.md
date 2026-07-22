## Part 17

> [BREADCRUMB_CTX: 《visual_display》 > Part 17]

So far the principles of maximizing data-ink and erasing have helped to generatea series ofchoices in the process of graphical revision. Thisis an important result, but can the ideasreach beyond thedetails and particularities of editing? Isitpossible todo what a theory of graphics issupposed to do, thatis,to derivenew graphical forms? In this chapter theprinciples areapplied to many graphical designs, basicand advanced, including box plots, bar charts, histograms, and scatterplots. New designs result.

# Redesign ofthe BoxPlot

Mary Eleanor Spear's "rangebar”

![](images/d2384c84c9b15e2ca1338a2a21fa66b1d10ea686d7dff48a5dd20caea7a8c43d.jpg)

can bemostly erased without loss ofinformation:

The revised design, aquartileplot, shows the same five numbers. It is easy to drawby hand or computer and, most importantly, can replace theconventional scatterplot frame. The straightedge ned only be placed on the paper once to draw the quartile plot, compared to six separate placings for the box plot. An alternative is

but this design will notwork effectively to frame a scatterplot.   
Nor does it look very good.

Perhaps special emphasis should be given to themiddle halfof the distribution, however, asin the box plot. This can be doneby changing line weights

or, even better, by offsetting the middle half:

Thislatter design is thepreferred form of the quartile plot.It uses theink effectively and looks good.

In these revisions ofthe box plot, theprinciple of maximizing datu-ink has suggested a variety of designs, but the choice ofthe best overall arrangement naturally also rests on statistical and aesthetic criteria-in other words, the procedure is oneof reasonable data-ink maximizing.

The same logic applies to many similar designs,such asthis "parallel schematic plot." The original required 80 separate placings of the straightedge, 50 horizontals and 30verticals:

i

An erased version requires only 10 verticals to show the same information:

_」 川 imd

The large reduction in the amount of drawing is relevant for the use of such designs in informal, exploratory data analysis, where theresearch worker's time should be devoted to matters other than drawing lines.

# Redesign ofthe Bar Chart/Histogram

Hereis thestandard model barchart,with the design endorsed by the practices and the style sheets of many statistical and scientific publications:

.ll

Its architecture differs little from Playfair's original design:

![](images/ff1e4d1d9890130e45328f50aa255de8441ea58413683a4fa0b7ffb12ce24c66.jpg)  
TheUprightdivifionsare TenThousandPounds cach. TheBlack Linesare Exports theRibbedlinesImports bdeeActdecneoWlatr Nederup'ssSrand.Londen

The boxcan beerased:

n.l

And the vertical axis, except for the ticks:

Even part of the data measures can beerased, making a white grid, which showsthe coordinate lines more precisely than ticks alone:

15%   
10% lu.llull   
5%

The whitegrid eliminates the tick marks, since the numerical labels on thevertical aretied directly to the white lines:

15%   
10% lul   
5%

Although the intersection ofthe thicker bar with the thinner baselinecreates an attractive visual effect (but also the optical illusion of gray dots at the intersections), thebaseline can be erased since thebars define the end-point atthe bottom:

Ilu.l

Still, a thin baseline looks good:

tln.l

Erasingand data-ink maximizing have induced changes in the plain old bar chart.The techniques-no frame, no vertical axis, no ticks,and thewhite grid- apply to other designs:

![](images/3ab431236c0b258e94b304c1158952fab02a060fec98cbb1f9bfdbda64559165.jpg)  
Robert McGill,Jon W. Tukey,and Wayne A.Larsen, "Variations ofBox Plots, American Statistician,32 (1978), 12-16.

# Redesign ofthe Scatterplot

Consider thestandard bivariate scatterplot:

![](images/2a7102db77874b52d950c05ad49221db470852d7e3741897cc4433a19d849090.jpg)

A useful fact, brought to noticeby the maximization and erasing principles, is that the frame ofa graphic can become an effective data-communicating element simply by erasing part of it.The frame lines should extend only to themeasured limits of the data rather than, as is customary, to some arbitrarypoint like thenext round number markingoffthe gridand grid ticksoftheplot. That part ofthe frameexceeding the limitsofthe observed data is trimmed off:

![](images/84ed9d1dd3f647d23282433ef78ddb94d482704b454958764c0b72fdad8fd8a0.jpg)

The result, a range-frame, explicitly showsthe maximumand minimum ofboth variablesplotted (along with the range),information availableonlyby extrapolation and visual estimation in theconventional design. The data-ink ratio hasincreased: somenon-dataink hasbeen erased, and theremainder ofthe frame,now carrying information, has gone over to the side of data-ink.

![](images/21a1e34bd67e65f021dd631b9fc7dd3dfc67377409bfa31fa88cfc0c99ffae01.jpg)

Nothing but thetails ofthe frame need change:

![](images/4b692414342cf43bdb2ffe5701ab0367e88db9bd39ec6baacf1e3ea88ea2c1a8.jpg)

Arange-frame does not require any viewing or decoding instructions; itis not a graphical puzzle and most viewerscan easily tell what is going on. Since it is more informative aboutthedata in a clearand precise manner, therange-frame should replace the non-data-bearing framein many graphical applications.

Asmall shiftin the remaining ink turns each range-frame into a quartile plot:

![](images/8dc74cb04b29b959cd3dde546d79b6906b87862b3e1f5d2c84ad7184f3c894a6.jpg)

Erasing and editing has led to the display of ten extra numbers (the minimum, maximum, two quartiles, and themedian for both variables). The design is useful for analytical and exploratory data analysis, as well as for published graphics where summary characterizations ofthe marginal distributions haveinterest. The design is nearly always better thanthe conventionally framed scatterplot.

Range-frames can also present ranges along 4 single dimension. Herethehistorical highandlowareshowninthevertical frame. Thisis an excellent practiceand should be used widely in all sorts ofdisplays, both scientific and unscientific:

![](images/be4e8b678402265e8d06473ec91d0ffa2d396460bb6f55ab202be1cb0b76e290.jpg)

Finally, the entire framecan beturned into data by framing the bivariate scatter with themarginal distributionofeach variable. Thedot-dash-plot results.1

The dot-dash-plot combines the two fundamental graphical designs used in statistical analysis, themarginal frequency distribution and the bivariate distribution. Dot-dash-plots make routine what good data analysts doalready- plotting marginal and joint distributions together.

Anempirical cumulative distribution ofresiduals ona normal grid shows the outer 18 terms plus the3oth term,withall 6o points plotted in themarginal distribution:

![](images/5d6a2c235f249099f6dc1256c3804372878dca65503f30b1a50795c70cba3a32.jpg)  
1Theterminology followstradition, for scatterplots were oncecalled "dotdiagrams"-forexample, inR.A.Fisher's StatisticalMethodsfor Research Workers (Edinburgh, 1925).

![](images/7b2094e083d0459f8b3425f50cf5189c6929bda081d3f6f02f212743211f6bda.jpg)

Similarly, this data-rich graphic ofsignals from pulsars shows both marginal distributions:

![](images/7b475f37d96a200ecbfe2a596499be6f69f5a9f09e2c9f0e733d938bc21e740a.jpg)  
Narrowband spectra ofindividual subpulses. Each point of the intensity $I _ { \vartheta } ( t )$ （20号 plotted on the right is the sum of the distribution of intensities across the receiver bandwidth shown in the center. At thetopis plotted the spectrum averaged bverthes pulsp. In the limitofmany thousands ofpulses thiswould show the receiver

Timothy H. Hankinsand BarneyJ. Rickett, "Pulsar Signal Processing, 3 in Berni Alder, et al.,eds., Methods in ComputationalPhysics,Volume14:Radio Astronomy (NewYork, 1975),p.108.

The fringe of dashes in thedot-dash-plot can connect a series of bivariate scatters in arugplot (since it resembles a set of fringed rugs-and covers the statistical ground):
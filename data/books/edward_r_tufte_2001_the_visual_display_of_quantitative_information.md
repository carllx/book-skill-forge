Edward R.Tufte

# The Visual Display of Quantitative Information

SECOND EDITION

Copyright $\circledcirc$ 2001 by Edward RolfTufte PUBLISHED BY GRAPHICS PRESS LLC POST OFFICE Box 430, CHESHIRE, CONNECTICUT 06410

AllrightstoillustrationsandtextreservedbyEdwardRolfTufte. Thiswork may not becopied,eproduced,ortrstedin wholeorin part without writenpermissonofthepublisher, exceptforbriefexcerptsinconnectionwithreviewsor scholarlyanalysis. Usewith any form of information storage and retrieval,electronicadaptationorwhatever,computersoftware,orbysimlarordissmilarmethodsnow known ordeveloped in thefutureisalsostrictlyforbiddenwithout writtenpermisionofthepublisher. Anumberofillustrationsarereproduced by permission;thosecopyright-holders are credited onpage197.

# Contents

# PARTI GRAPHICAL PRACTICE

1 Graphical Excellence 13   
2 Graphical Integrity 53   
3 Sources of Graphical Integrity and Sophistication 79

# PART II THEORY OF DATA GRAPHICS

4 Data-Ink and Graphical Redesign 91   
5 Chartjunk: Vibrations, Grids, and Ducks 107   
6 Data-Ink Maximization and Graphical Design 123   
7 Multifunctioning Graphical Elements 139   
8 Data Density and Small Multiples 161   
9 Aesthetics and Technique in Data Graphical Design 177

Epilogue: Designs for the Display of Information 191

For my parents Edward E. Tufte and Virginia James Tufte

Tothe memory of John W. Tukey (1915-2000)

# Introduction to the Second Edition

Thisnew edition provides high-resolution colorreproductions of the many graphics ofWilliam Playfair,adds color to other images whereappropriate,and includesall the changes and corrections accumulated during the 17 printings of the first edition.

Thisbook beganin 1975when Dean Donald Stokes ofPrinceton's Woodrow Wilson School asked metoteach statistics to a dozen journalists who were visiting that year to learn some economics. Iannotated a collection of readings,with a long section on statistical graphics. The literature here was thin, too often grimly devoted to explaining use of the ruling pen and to promulgating graphic standards' indifferent to thenature of visual evidenceand quantitative reasoning. Soon wroteup some ideas. ThenJohn Tukey,the phenomenal Princeton statistician, suggested thatwe give a series of joint seminars. Since the mid-196os,Tukey had opened up the field, ashis brilliant technical contributionsmade itclear thatthestudyofstatistical graphics was intellectually respectable and not just about pie chartsand ruling pens.

After moving to Yale University,I finished the manuscript in 1982. Apublisherwas interested but planned to print only 2,000 copiesand to charge a very high price,contrary to my hopes for a widereadership. also sought to design the book so as to make it self-exemplifying-thatis,thephysicalobjectitselfwould reflect theintellectual principlesadvanced in the book. Publishersseemed appalled at the prospect that an author might govern design.

Consequently investigated self-publishing.This required a firstrate book designer, a lot of money (at least for a young professor), and a large garage. found HowardGrallawho haddesigned many museum catalogs with great care and craft. He was willing to work closely with thisdifficultauthor who was filledwith all sorts ofopinions about designand typography. We spent the summer in his studio laying out the book,page by page. We were able to integrate graphics right into the text,sometimes into themiddle ofa sentence, eliminating the usual separation oftext and imageone of the ideas Visual Display advocated. To finance the book I took out another mortgage on myhome. Thebank officer said this was the second most unusual loan that she had evermade; first placebelonged to aloan toa circus to buy an elephant!

![](images/ed45825cae6aa3b3d9e6d0c90fba8f6d0177805de5f43eae6fdd9adbffd9fc82.jpg)

# Introduction

Data graphics visually display measured quantities by means of the combined use of points, lines, a coordinate system, numbers, symbols, words, shading,and color.

Theuse ofabstract,non-representational pictures to show numbers isasurprisingly recent invention, perhaps becauseofthe diversity ofskills required-the visual-artistic, empirical-statistical,and mathematical. It was not until $1 7 5 0 - 1 8 0 0$ thatstatistical graphicslength and area to show quantity, time-series,scatterplots, and multivariate displays-were invented, long after such triumphs of mathematical ingenuity as logarithms, Cartesian coordinates, the calculus,and thebasics of probability theory.Theremarkable William Playfair (1759-1823) developed orimproved upon nearly all the fundamental graphical designs, seeking to replace conventional tables ofnumbers with thesystematic visual representations ofhis "linear arithmetic."

Modern data graphics can do much more thansimply substitute forsmall statistical tables. At their best,graphics areinstruments for reasoning about quantitative information. Often the most effectiveway to describe, explore,and summarize a set ofnumberseven avery large set-is to look atpictures of those numbers. Furthermore,ofall methods for analyzing and communicating statistical information, well-designed data graphics are usually the simplest and at the same time themost powerful.

The first part ofthis book reviews the graphical practice of the two centuries since Playfair. The readerwill, I hope, rejoice in the graphical glories shown in Chapter 1 and then condemn the lapses and lostopportunities exhibited in Chapter 2. Chapter 3, on graphical integrity and sophistication,seeks to account forthese differences in quality of graphical design.

The second part of the book provides a languagefor discussing graphicsand a practical theory of datagraphics. Applying to most visual displaysofquantitative information, the theory leads to changes and improvements in design, suggests why some graphics might be better than others, and generatesnew types of graphics. Theemphasis is on maximizing principles, empirical measures of graphical performance,and thesequential improvement of graphics through revision and editing. Insights into graphical design are to be gained, believe, from theoriesofwhat makes for excellence inart, architecture, and prose.

Thisisa book about thedesign of statistical graphics and, assuch, itis concerned both with design and with statistics. Butitis also abouthow tocommunicate information through the simultaneous presentation ofwords, numbers, and pictures. The design of statistical graphics is a universal matter-like mathematics-and is not tied to theunique features ofa particular language. The descriptive concepts (avocabulary for graphics) and the principlesadvanced apply to most designs. Ihaveat times provided evidence about the scope of these ideas,by showing how frequently a principle applies to （a random sample of) newsand scientific graphics.

Each year,the world over,somewhere between900 billion $\left( 9 \times 1 0 ^ { 1 1 } \right)$ and 2 trillion $\left( 2 \times 1 0 ^ { 1 2 } \right)$ images of statistical graphics are printed. The principles of this book apply to most of those graphics. Some of the suggested changes are small,butothers are substantial, with consequences for hundreds ofbillions ofprinted pages.

But Ihope also that thebook has consequences for the viewers and makers of those images- that they will never view or createstatistical graphics the same way again. That isin part because weare about to see, collected here, so manywonderful drawings, those ofPlayfair, ofMinard, ofMarey,and, nowadays, ofthe computer.

Most ofall, then, this book isa celebration ofdata graphics.

# Graphical Practice

# I Graphical Excellence

Excellence in statistical graphics consists ofcomplex ideas communicated with clarity, precision, and efficiency. Graphical displays should

show thedata induce theviewer to think aboutthe substancerather than about methodology, graphic design, the technology of graphic production, or something else   
avoid distorting what thedata have to say present many numbers in a small space make large data sets coherent encourage the eye to compare different pieces of data   
$\cdot$ reveal thedataat several levels ofdetail, from a broad overview to thefine structure servea reasonably clear purpose: description, exploration, tabulation, or decoration   
beclosely integrated with thestatistical and verbal descriptions ofadata set.

Graphicsreveal data. Indeed graphics can be more precise and revealing than conventional statistical computations. Consider Anscombe'squartet: all fourof these data setsare described by exactly thesame linearmodel （at leastuntil theresiduals areexamined).

II Y   
10.0 8.04 10.0 9.14 10.0 7.46 8.0 6.58 （2号 $\mathbf { N } = 1 1$ 8.0 6.95 8.0 8.14 8.0 6.77 8.0 5.76 mean of $\mathbf { X } ^ { \prime } s = 9 . 0$   
13.0 7.58 13.0 8.74 13.0 12.74 8.0 7.71 meanof $\Upsilon ^ { \prime } s = 7 . 5$ 9.0 8.81 9.0 8.77 9.0 7.11 8.0 8.84 equation ofregression line $\mathbf { Y } = 3 + 0 . 5 \mathbf { X }$   
11.0 8.33 11.0 9.26 11.0 7.81 8.0 8.47 standarderrorofestimateofslope $= 0 . 1 1 8$   
14.0 9.96 14.0 8.10 14.0 8.84 8.0 7.04 $t = 4 . 2 4$ 6.0 7.24 6.0 6.13 6.0 6.08 8.0 5.25 sum ofsquares $\mathbf { X } - \overline { { \mathbf { X } } } = 1 1 0 . 0$ 4.0 4.26 4.0 3.10 4.0 5.39 19.0 12.50 regression sum of squares $= 2 7 . 5 0$   
12.0 10.84 12.0 9.13 12.0 8.15 8.0 5.56 residual sum of squares of $\mathbf { Y } = 1 3 . 7 5$ （号   
70 4.82 7.0 7.26 7.0 6.42 8.0 7.91 correlation coefficient $= . 8 2$ 5.68 5.0 4.74 5.0 5.73 8.0 6.89 $\mathbf { r } ^ { 2 } = { \bf \nabla } \cdot { \bf { 6 7 } }$

And yet how they differ, as the graphical display of thedata makes vividly clear:

![](images/03fb79fb172a6cb57bb298891bf6fda93ca94ecae796fe23c4dd3db6b9b547a5.jpg)  
F.J. Anscombe, "Graphs in Statistical Analysis, American Statistician, 27 (February 1973), 17-21.

And likewise a graphic easily reveals point A,a wildshot observation thatwill dominate standard statistical calculations. Note that point A hidesin themarginal distribution but shows up as clearly exceptional in the bivariate scatter.

![](images/65aaa60b418f7f218eb62bb9a84d1c5e09e49478170ffbea1f5b668ba2ee5471.jpg)  
Stephen S. Brierand Stephen E. Fienberg,"Recent Econometric Modelling ofCrime andPunishment: Supportfor theDeterrenceHypothesis?"in Stephen E.Fienberg and AlbertJ. Reis,Jr.,eds., IndicatorsofCrime and Criminal Justice: Quantitative (Washington,D.C., 1980),p. 89.

Of course, statistical graphics, just likestatistical calculations, are only as good as what goes into them. An ill-specified or preposterousmodel orapuny data set cannot berescued bya graphic (or by calculation), no matter how cleveror fancy. Asilly theory means a silly graphic:

![](images/3f10216bccc830e20b7f14096b54ca3ba39132c49a9e987e8ceba895d0f2874a.jpg)  
A. New York stock prices (Barron'saverage) B. Solar Radiation, inverted, and C. London stock prices, all by months, 1929 (after Garcia-Mata and Shaffner)

Letus turn to thepractice of graphical excellence, the efficient communication of complex quantitative ideas. Excellence, nearly always of a multivariate sort,is illustrated here for fundamental graphical designs: data maps, time-series, space-time narrative designs,and relational graphics. These examples serveseveral purposes, providing a set ofhigh-quality graphics thatcan be discussed (and sometimes even redrawn) in constructing a theory of data graphics, helping to demonstratea descriptive terminology, and tellingin briefabout the history ofgraphical development. Most ofall, wewill beable to see just how good statistical graphics canbe.

# Data Maps

These six maps report theage-adjusted death rate from various types ofcancer for the 3,056 counties ofthe United States. Each map portrays some 21,000 numbers.1 Only apicturecan carry such a volume ofdata in such a small space. Furthermore,allthat data, thanks to the graphic, can be thought about in many different ways atmany differentlevelsofanalysis ranging from the contemplation of general overall patterns to thedetection ofvery finecounty-by-county detail. To take just a few examples, look at the

high death rates from cancer in the northeast partof the country and around theGreat Lakes   
low ratesin an east-west band across themiddle ofthe country higher ratesfor men than for women in the south,particularly Louisiana (cancers probably caused by occupational exposure, from working with asbestos in shipyards)   
unusual hot spots, including northern Minnesota and a few counties in Iowa and Nebraska along the Missouri River   
differences in types of cancer by region (for example, the high rates ofstomach cancer in the north-central part ofthe country -probably theresult of the consumption ofsmoked fishby Scandinavians)   
ratesin areas where you have lived.

The maps provide many leads into the causes-and avoidanceof cancer. For example, theauthors report:

In certain situations the unusual experience of a county warrants furtherinyestigation. For example, Salem County, New Jersey, leads thenation in bladder cancer mortality among white men. Weattribute this excessrisk tooccupational exposures, since about 25 percent of the employed persons in this county work in thechemical industry, particularly the manufacturing of organic chemicals, which may cause bladder tumors. Afterthe finding wascommunicated toNew Jersey health officials, a company in the areareported thatat least330 workers in a single plant had developed bladder cancer during the last 50 years. Itis urgent that surveys of cancer risk and programs in cancer control be initiated among workers and former workers in thisarea.2

1Each county'srate is located in two dimensions and,further atleast four numbers would benecessary to reconstruct the sizeand shape ofeach county. Thisyields $7 \times 3 , 0 5 6$ entries in a data matrixsufficient toreproducea map.

In highest decile, statistically significant

Significantly high,but notin highestdecile

In highest decile, butnot statistically significant

Not significantly different fromU.S.asawhole

Significantly lower than U.S.asa whole

三

2RobertHoover,ThomasJ.Mason, Frank W. McKay, andJoseph F.Fraumeni,Jr., "Cancer by County: New Resource for EtiologicClues, Science, 189 (September19, 1975), 1006.

![](images/1c5459de6f49d1105237ee14c41c1613146fa134c388caf9ef40765086040520.jpg)

![](images/992c211a6736853bb6dc85a28fbf0e1da3a3521a6a21250dad720e8241234ac7.jpg)

![](images/09f1d16df2951b543ce4f09d5e075f76dfac5f52e2bc7c8f3e0c85fef22f1225.jpg)

![](images/7ec6c583d5a43f7f1e05a450b1b5ab33b9bf7e59a9550f56081ea386d1f66e71.jpg)

![](images/b63b10c4ef02db9658d369822392b76a1dc0249ea9a67b43c2af7bc306c2d0ca.jpg)

![](images/9339f70ae41e44f06125a8201eeaf4c47cdb1587d6882ca815548a6ebeaf1bcb.jpg)

The maps repay careful study.Notice howquickly andnaturally ourattention has been directed toward exploring the substantive content ofthe datarather than toward questions of methodology and technique. Nonetheless the maps do have their flaws. They wrongly equate the visual importance of each county with its geographic area rather than with thenumber ofpeople living in the county (or the number of cancer deaths). Ourvisual impression of thedata is entangled with the circumstance of geographic boundaries, shapes,andareas-thechronic problemaflicting shadedin-area designs of such "blot maps or 'patch maps.

A further shortcoming, a defect ofdatarather than graphical composition, is that the maps are founded on asuspect data source, death certificate reports on the cause ofdeath. Thesereports fall under the influence of diagnostic fashions prevailing among doctorsand coroners in particular places and times, a troublesome adulterant ofthe evidence purporting to describe the already sometimes ambiguous matter of the exact bodily site of the primary cancer. Thus part of the regional clustering seen on the maps, as well as some ofthe hot spots,may reflect varying diagnostic customs and fads along with theactual differencesin cancer rates betweenareas.

Data maps have a curious history.Itwas not until the seventeenth century that the combination of cartographic and statistical skills required to construct thedata map came together, fully s,00o years afterthe first geographic maps were drawn on clay tablets. And many highly sophisticated geographic maps were produced centuries before the first map containing any statistical material was drawn.3 For example, a detailed map with a full grid was engraved during the eleventh century A.D. in China. TheYü Chi Thu (Map ofthe Tracks of Yü the Great) shown hereis described by Joseph Needham asthe

mostremarkable cartographic work of its age in any culture, carved in stone in $+ 1 1 3 7$ but probably dating from before $+ 1 1 0 0$ The scale of the grid is100 li to the.division. The coastal outline isrelatively firm and the precision ofthe network of river systems extraordinary. The size of the original, which is now in the PeiLin Museum at Sian, is about 3 feet square. Thename of the geographer is not known. Anyone who compares this map with thecontemporary productions of European religious cosmography cannot but beamazed at theextent to which Chinese geography was at thattime ahead of the West. There was nothing likeitin Europe till the Escorial MS. map ofabout $+ 1 5 5 0$

![](images/4d3889f0d7e8a72441341daa4011afcbcdd622c813e86b7ce5cf30d8da15563d.jpg)  
E. Chavannes,"LesDeux Plus Anciens Specimensdela CartographieChinoise, Bulletin de P EcoleFrangaise de l'Extreme Orient, 3 (1903), 1-35, CarteB.

# Ecceformulam vfum,atque

ftructuram TabularumPtolomxi,cumquibufdam locis,in quibus ftudiofus Geographix fe fatis exercere poteft.

![](images/a290851758534674ec689bcd0f08d23f100531642c8a1191aba423801a3dbce5.jpg)

The1546 edition ofCosmographia by Petrus Apianus contained examples ofmap design that show how very close European cartography by thattimehad come to achieving statistical graphicacy, even approaching the bivariate scatterplot. But, according to the historical record, no one had yet made thequantitativeabstraction of placing a measured quantity on the map's surface at the intersection of the two threads instead of the name ofa city,let alone the more difficult abstraction of replacing latitude and longitude with some other dimensions, such as time and money. Indeed, it was not until $^ { 1 7 8 6 }$ that thefirst economic time-series wasplotted.

One ofthe first data maps was Edmond Halley's 1686 chart showing trade winds and monsoons on a worldmap.5 Thedetailed section below shows thecartographic symbolization;with, as Halley wrote, 4 the sharp end ofeach little stroak pointing out that part ofthe Horizon, fromwhence the wind continually comes; and where thereare Monsoons therows ofstroaks run alternately backwardsand forwards,bywhich means they are thicker [denser] than elsewhere."

![](images/06b37b8ec1869d50f55e24e0d497c3d4d6d26a763dc30b2a4b5365161edc671d.jpg)  
5NormanJ. W. Thrower, "Edmond Halley asaThematic Geo-Cartographer, Annalsof the Association ofAmerican Geographers,59 (December 1969), 652-676.

![](images/5f0dc1929f515a0bfb4b61c6414d8146d95c92d747ded983dab897b644e1b750.jpg)  
Edmond Halley,“AnHistorical Account ofthe Trade Winds, and Monsoons, Observable in theSeas Between andNear theTropicks; Withan Attemptto Assign the Phisical Cause of SaidWinds," Philosophical Transactions, 183 (1686), 153-168.

An early and most worthy use ofa mapto chart patterns of disease wasthe famous dot map ofDr.John Snow, who plotted the location ofdeaths from cholera in central London for September $1 8 5 4$ Deaths were marked by dotsand, in addition,the area eleven waterpumps were located by crosses. Examining the scatter over the surface of the map, Snow observed thatcholera occurred almost entirely among thosewho lived near (and drank from) the Broad Street water pump. He had thehandle ofthe contaminated pump removed, ending the neighborhood epidemic which had taken more than 500 lives.6 The pump is located atthe center of the map,just to theright of the D inBROAD STREET. Of course the link between the pump and the disease might have been revealed by computation and analysis without graphics, with some good luck and hard work. But, here atleast,graphical analysis testifies aboutthedata far more efficiently than calculation.

Charles Joseph Minard gave quantity aswell as direction to the data measures located on the world map in hisportrayal ofthe $^ { 1 8 6 4 }$ exports ofFrench wine:

![](images/910d556717ff2882f8ff607d2e90d2698c1723a6fc664abbc9e2d825a44a8a08.jpg)  
6E.W. Gilbert, "Pioneer Maps ofHealth andDisease in England," Geographical Journal, 124(1958),172-183. Shown here isa redrawing ofJohn Snow’smap.For areproductionand detailedanalysisof the original map,see Edward Tufte, Visual Explanations: ImagesandQuantities,Evidence andNarrative(Cheshire,Connecticut, 1997),Chapter 2. Ideally,seeJohnSnow, OntheModeofCommunicationofCholera (London,1855).

![](images/60724af8ff42de987324922a0109321469164d27229ef53efe53e34ea0af08cc.jpg)  
Cpep osoed neeaerg aaae, sirs prar seesefsesreea pbrpoatp

Computerized cartography and modern photographic techniques haveincreased the density ofinformation some5,000-fold in the best of current data maps compared to Halley's pioneering effort. This map showsthe distribution of1.3 million galaxies (including some overlaps) in the northern galactic hemisphere. The map divides the sky into $\phantom { - } 1 , 0 2 4 \times 2 , 2 2 2$ rectangles. Thenumber ofgalaxiescounted ineach of the2,275,328 rectangles is represented by ten gray tones; the darkerthe tone,the greater the number of galaxies counted. Thenorth galactic pole is at thecenter.The sharp edge on theleft results from the earth blocking the view from the observatory.In thearea near the perimeter of the map, the viewis obscured by the interstellar dust of the galaxy in which we live (the Milky Way) as theline of sight passes through the fattened disk ofour galaxy.The curious texture oflocal clusters of galaxies seenin this truly new view oftheuniverse wasnot anticipated by students ofgalaxies,who had, ofcourse, microscopically examined millions of photographs of galaxies before seeing this macroscopic view. Although the clusters are clearly evident (and accounted forby a theory ofgalactic origins), the seeminglyrandom filaments may be happenstance. The producers of the map note the "strong temptation to conclude that the galaxies are arranged ina remarkable filamentary pattern on scales ofapproximately $\boldsymbol { \mathfrak { s } } ^ { \circ }$ to $1 5 ^ { \circ } { \mathrm { ~ } }$ butwe caution thatthisvisual impression may be misleading because the eye tends topick out linear patterns even in random noise. Indeed, roughly similar patterns areseen on mapsconstructed from simulated catalogs where no linear structure has been built in. ,7   
.

The most extensive data maps, such as the cancer atlasand the count of thegalaxies, placemillions ofbits ofinformation on a single page before oureyes. No other method for the display of statistical information isso powerful.

![](images/a492426b6f9733d20b85ca93a168e49e10fd472dd730ac02e7efb31dee89e7f7.jpg)

![](images/ddc838d32db571dacf66e1fd6af378dab485e2422f6fb596d6acd97a7bbeebb0.jpg)

# Time-Series

The time-series plot is themost frequently used form of graphic design.8 With one dimension marching along to theregularrhythm of seconds, minutes, hours,days, weeks,months,ears, centuries, or millennia, thenatural ordering ofthe time scale gives this design a strength and efficiency of interpretation found in no other graphic arrangement.

Thisreputed tenth- (or possibly eleventh-) century illustration ofthe inclinations of the planetary orbits asa function of time, apparently part ofa text for monastery schools, is the oldestknown example ofan attempt to show changing values graphically. It appears asa mysteriousand isolated wonder in the history ofdata graphics, since thenext extant graphic ofa plotted time-series shows up some 800years later. According to Funkhouser, the astronomical contentis confused and thereare difficulties in reconciling the graph and its accompanying text with theactual movements of the planets. Particularly disconcerting is the wavy path ascribed to the sun.9An erasure and correction ofa curve occur near themiddle of the graph.

$^ { 8 } \mathrm { A }$ random sampleof $^ { 4 , 0 0 0 }$ graphics drawnfrom $^ { 1 \varsigma }$ ofthe world'snewspapersand magazines published from 1974to1980 found that more than 75 percent ofall thegraphics published were time-series. Chapter 3reportsmore on this.

![](images/8babcf594ecf2d05c269781aeaf19779f6e9c0ff3e16aec8057458920426c3fe.jpg)  
9H. Gray Funkhouser, "ANote on aTenth Century Graph, Osiris,1 (January1936),260-262.

It was notuntil the late1700s thattime-series charts began to appear in scientific writings. This drawing ofJohann Heinrich Lambert, oneofa long series, shows the periodic variation in soil temperature in relation to the depth under the surface. Thegreater the depth, thegreater the time-lag in temperatureresponsiveness. Modern graphic designs showing time-series periodicities differ little from those ofLambert, although thedata bases are far larger.

![](images/d3d811ed8c4715e9cce35ba639018e5d67daed148f5335c32a41391cdb323110.jpg)  
J.H.Lambert, Pyrometrie (Berlin,1779).

This plot ofradio emissions fromJupiter is based on datacollected by Voyager 2 in itspass closeby theplanet in July 1979. Theradic intensity increases and decreases in a ten-hour cycle asJupiter rotates. Maximum intensity occurs when the Jovian north magnetic pole is tipped toward thespacecraft, indicating anorthern hemisphere source. A southern source was detected on July 7, as the spacecraft neared the equatorial plane. Thehorizontal scale shows thedistance ofthe spacecraft from the planet measured in terms of Jupiter radii (R).Note theuse ofdual labels on thehorizontal to indicate boththe dateand distance from Jupiter. The entire bottom panel also serves to label the horizontal scale, describing the changing orientation ofthe spacecraft relative to Jupiter as the planet is approached. Themultiple time-series enforce not only comparisons within each series over time (asdo all time-series plots) butalsocomparisons between thethree different sampled radio bands shown. This richly multivariate display is based on 453,600 instrumentsamples of eight bits each. The resulting 3.6million bits were reducedby peak and average processing to the 18,900 points actually plotted on the graphic.

![](images/18489170b86de71e6bd6d823d34341612526b6dd558c38ab2752b56beccb2ee9.jpg)  
D.A. Gurnett, W.S. Kurth,and F.L. Scarf,"PlasmaWave Observations Near Jupiter: Initial Results from Voyager 2," Science2o6(November23,1979), 987-991;and letter from Donald A. Gurnett to EdwardR.Tufte,June27, 1980.

Time-series displays are at their best for bigdata sets with real variability. Why waste thepower of data graphics on simplelinear changes,

![](images/4857adf066fb8642e6d9d95388af65455f26c04df62cf3083c80ac78dfdd1a97.jpg)

which can usually be better summarized in one or two numbers? Instead,graphics should bereserved forthe richer, more complex, more difficult statistical material. ThisNew York City weather summary for $1 9 8 0$ depicts $^ { 1 , 8 8 8 }$ numbers. Thedaily high and low temperatures are shown in relation to the long-run average. The path of the normal temperatures also provides aforecastof expected change over theyear; in themiddle of February,for instance, New York City residents canlook forward to warming attherate of about 1.5 degrees per week all theway to July, the yearly peak. This distinguished graphic successfully organizes a large collection ofnumbers, makes comparisons between different parts ofthe data,and tells astory.

![](images/077e543d53a9be241ceb47359a603d010270ceabf37454282abac1b953776651.jpg)  
NEWYORKCITY'SWEATHERFOR1980   
NewYork Times,January11,981,p.32.

A design with similarstrengths isMarey's graphical train schedule forParis to Lyon in the $1 8 8 0 s .$ Arrivals and departures from a station arelocated along the horizontal; length of stop ata station is indicated by the length of the horizontal line. The stations are separated in proportion to theiractual distance apart. The slope ofthe linereflects the speed ofthe train: the more nearly vertical the line,thefasterthetrain. The intersection of two lines locates the time and place that trains going in opposite directions pass each other.

![](images/4fe169d9a4eb7a5c3c15230a0d245bb2e21c94d14f7549ee80f8fc5e2be7ff6e.jpg)  
E.J.Marey, Lamethodegraphique (Paris, 1885),p.2o.Themethod isattributed totheFrench engineer,Ibry.

In 1981 a new express train from Paris to Lyon cut the trip to under three hours,compred to more thannine hourswhen Marey published the graphical train schedule. The path of themodern TGV (train a grande vitesse) is shown, overlaid on the schedule of 100years before:

![](images/42ad5a011955174b0f16fa1a72bb23eac6a3cc612b77652a632ac565c058b3e5.jpg)

The two great inventors ofmodern graphical designs wereJ.H. Lambert (1728-1777), a Swiss-German scientist and mathematician, and William Playfair (1759-1823), a Scottish political economist.10 The first known time-series using economic data waspublished in Playfair'sremarkable book, The Commercial andPolitical Atlas (London, 1786). Note the graphical arithmetic, which shows the shifting balance of trade by the difference between the import and export time-series. Playfair contrasted hisnew graphical method with the tabular presentation ofdata:

Information, thatis imperfectlyacquired, is generally as imperfectly retained; and a man who hascarefully investigated a printed table, finds, when done, thathe hasonly a very faint andpartial ideaofwhat hehas read;and thatlike a figure imprinted on sand, is soon totally erased and defaced. The amount ofmercantile transactions in money,and ofprofit or loss,are capable of being as easilyrepresented in drawing, as any part of space, or as theface ofa country; though, till now, it hasnot beenattempted. Upon that principle these Charts were made; and, while they give asimple and distinct idea, they are as near perfect accuracy asis any wayuseful. On inspecting any one ofthese Charts attentively, a sufficiently distinct impression will be made, to remain unimpaired fora considerable time, and theidea which does remain will be simple and complete, at once including the duration and the amount. [pages 3-4]

For Playfair,graphics werepreferable to tables because graphics showed the shape of the data in a comparative perspective. Timeseriesplots did this,and all but one of the 44charts in thefirst edition ofTheCommercial and Political Atlas were time-series. That one exception is the first known barchart, which Playfair invented because year-to-year data were missingand he needed a design to portray the one-year data thatwereavailable. Nonetheless hewas skeptical abouthis innovation:

![](images/2f3de3896bde527d7b26f91c7c60e939cc9ccda3fb8cb419b84ff3f29ba99ccb.jpg)  
CHART fall the IMPORTSand EXPORTS b and from ENGLAND From the year 1700 t 1782 b W.Playfair   
The Divisionsatthe Bottom,capref YEARS. & thaseon theRighthandMILIoNsoJPOUNDS JdheSode! PublichdartheActdirboAug.178s

This Chartis different from the others in principle, asit does not comprehend anyportion of time,and itis much inferior in utility to those that do; for though itgives the extent ofthe different branches oftrade, it does not compare thesame branch ofcommerce with itselfat different periods; nor does itimprint upon themind that distinct idea, in doing which, thechief advantage of Charts consists: foras it wants the dimension thatis formed by duration, there isno shape given to thequantities. [page 101]

Hewas right:small, noncomparative, highly labeled data sets usually belong in tables.

![](images/3bac21bd586bec6f651f3a677718d7a57dd02de5b35cdd5196f3e03494f72044.jpg)  
TheUprightdisiponsareTenThoufandPoundscach. TheBlackLinesareExportstheRibbedlinesImports. ndeddioJmyguy pos.Lm

The chart does show, atanyrate, the imports (cross-hatched lines)and exports (solid lines) toand from Scotland in $1 7 8 1$ for 17 countries, which are orderedbyvolume oftrade. Thehorizontal scale isat thetop,possibly to make it moreconvenient to see in plotting the points by hand. Zero values arenicely indicated both by the absenceof a barand by a "0." The horizontal scale mistakenly repeats "200." In nearly allhis charts, Playfairplaced the labels for the vertical scale on theright side of the page (suggesting that he plotted thedata points using his left hand).

Playfair's last book addressed thequestion whether theprice of wheathad increased relativeto wages. Inhis Letter onour agricultural distresses, theircausesandremedies;accompanied with tablesand copper-plate charts shewing and comparing theprices ofwheat, breadand labour,from 1565 to 1821, Playfair wrote:

You have before you,my Lords and Gentlemen, a chartof the prices of wheat for 25o years, made from official returns; on the same plate have traced a line representing, asnearly as I can, the wages ofgood mechanics,such as smiths, masons, and carpenters,in order to compare theproportion between themand theprice ofwheat at every different period. the main fact deserving ofconsideration is, thatneveratany former period waswheat so cheap, in proportion to mechanical labour, as itis at the present time. [pages29-31]

Here Playfair plotted three parallel time-series: prices, wages,and the reigns of British kings and queens.

![](images/84bc2a6793f827dc7e38c59faa704a13e096558b32956194063d82b35d35e2fd.jpg)

The history and genealogy ofroyalty was long graphical favorite. This superb construction of E.J. Marey brings together several sets of facts about English rulers into a time-series that conveys a sense ofthe march ofhistory. Marey $( 1 8 3 0 - 1 9 0 4 )$ also pioneered the development of graphical methods in humanand animal physiology, includingstudies ofhorses moving atdifferent paces, the movement ofa starfish turning itself over (read imagesfrom the bottom upwards),

![](images/0e674c650ef2d02915aca3bb7bf3de67847e0bafd0ea8e7e300ccadd6a5e4f83.jpg)  
E.J.Marey,LaMethode Graphique (Paris, 1885),p. 6.

![](images/79d7f5e6eaa683ec0ddc60f005b42a3ee9c34011d3bdb6d709d6ef9aef368001.jpg)  
E.J.Marey, Movement (London,1895). Beginningwith the tracks of the horse, thetime-seriesare from pages 191,224, 222,265, 60,and 61.

![](images/e0ded3ecd11c31679acb7bb372ca803d37f075d3d709d31e5d096f5d7401123c.jpg)

the undulations ofthe dorsal fin ofa descending sea-horse, 节节年年平半年年年 as well as the advance of the gecko.

d科

Marey's man in black velvet, photographed in stick-figure images, becamethe time-series forerunner ofMarcel Duchamp' Nude Descending a Staircase.

![](images/79b05766a2f26f44c56f5dfe4addd8d3c46f0f9699bc8602c462c921941c6696.jpg)

![](images/17733ed5d59c8edc57979fb04d8f37a28bbb100c1ddbd2d3e8443869968722ad.jpg)

Theproblem with time-series is that the simple passage oftime is notagood explanatory variable: descriptive chronology is not causal explanation.There are occasional exceptions,especiallywhen thereisa clear mechanism thatdrives theY-variable. This timeseries does testify about causality: the outgoing mail of theU.S. HouseofRepresentatives peaks every two years,just before the election day:

![](images/c092e42ba8057ea4594e64154d4e3cf7ccb697eab0eaefac2c36652ed428bc03.jpg)

The graphic is worth at least700words, thenumber used in a news report describing how incumbent representatives exploit their free mailing privileges to advance their re-election campaigns:

![](images/f6efffa9314850b4fe3e6464544f9135007266860499c19add9ffeac951a28cb.jpg)

Time-series plots can bemoved toward causal explanation by smuggling additional variables into thegraphicdesign.For example, this decomposition of economic data, arraying 1,296 numbers breaks outthe topseries into seasonal andtrading-day fluctuations (which dominate short-term changes) toreveal the long-run trend adjusted for inflation. (Notea significant defect in thedesign, however: the vertical grid conceals the height ofthe December peaks.) The next step would beto bringinadditional variables to explain thetransformed and improved seriesat the bottom.11

![](images/2c01fee191475d8300926f831a14bf3b0d7f2b3b3e8fedaf7d38e4c5b8336504.jpg)

11SeeWilliam S. Cleveland and IrmaJ. Terpenning, "Graphical Methodsfor Seasonal Adjustment, Journal of the American Statistical Association77 (March 1982),52-62.

Julius Shiskin, "Measuring Current Economic Fluctuations, Statistical Reporter (July1973), p.3.

Finally, a vivid design (with appropriate data)is the before-after time-series:

# A monopole?

![](images/f61d1c9da9e03fce98e8225d128782d6f24fb0bab4c320d29e48cf604ad6cfb9.jpg)  
M. Mitchell Waldrop, "In Search ofthe MagneticMonopole, Science (June4,1982), p.1087.

Cabrera's candidate monopole signal looms over a disturbancecaused bya liquidnitrogen transfer earlier in the day.Thejump in magneticfluxthrough thesuperconducting detector loop (orequivalently, thejump in the loop'ssupercurrent) isjust the rightmagnitude to bea monopole. Moreover,thecurrentremained stableformany hoursafterward.

And beforeandafterthecollapseofabridge on theRhone in 1840:

Pont de Bourg-StAndeol surle Rhone.

![](images/44f0f2062e8e91ea335b0c483533f98e90f0da9e895000d87b637729bab70641.jpg)  
Charles Joseph Minard, "Dela Chutedes Ponts dans les grandes Crues,"(October24，1856)，Figure3，inMinardCollection deses brochures (Paris, 1821-1869),held by the Bibliotheque de1'EcoleNationaledes PontsetChaussees,Paris.

# Narrative Graphics ofSpaceand Time

Anespecially effective device for enhancing the explanatory power oftime-series displaysis to addspatial dimensions to the design of thegraphic, so that thedata are moving over space (in two or three dimensions) aswell as over time. Three excellent space-time-story graphics illustrate here how multivariate complexity can be subtly integrated intographical architecture, integrated so gently and unobtrusively that viewers are hardly aware that they are looking intoa world of four or five dimensions. Occasionally graphics are bellgerently multivariate, advertising the techniquerather than thedata.But not these three.

Thefirst is theclassic ofCharlesJoseph Minard(1781-1870), the French engineer,whichshows the terrible fate ofNapoleon’s army inRussia. Described by E.J.Marey as seeming to defy the pen of thehistorian by its brutal eloquence,12 this combination of data map andtime-series,drawn in1869,portraysasequenceofdevastating losse suffered in Napoleon'sRussian campaign of1812.Beginning at left onthePolish-Russian bordernear theNiemenRiver,the thick tan flow-line shows the size of theGrand Army(422,000) asit invaded Russia in June $\ 1 8 1 2 .$ The width ofthis band indicates the size of the army at each place on the map.In September,the army reached Moscow,which wasby then sacked and deserted, with 100,000 men. The path ofNapoleon's retreat from Moscow is depicted by thedarker,lower band, which islinked toatemperature scaleand datesatthe bottom of thechart. It wasa bitterly cold winter,and many froze on the march out ofRussia. As the graphic shows,the crossing of the Berezina River was 3 disaster,and thearmyfinally struggled back into Poland with only 10,000 men remaining. Also shown are the movements of auxiliary troops, as they sought to protect the rear and the fankof the advancing army.Minard's graphic tellsa rich, coherent story with itsmultivariatedata,far more enlightening than just single number bouncing along over time.Six variablesare plotted: the size of thearmy,itslocation ona two-dimensional surface, direction of the army'smovement, and temperature on various dates during the retreat from Moscow. At upper right weseeMinard'sFrench original, whichwas printed as a two-color lithograph in the formofa small poster. Andat lower right,ourEnglish translation.

It may well bethe best statistical graphic ever drawn.

![](images/10baef635ac8bb58b0f7467fcfa95e2660f7504487a49d11ebdc5eccd73962ad.jpg)

![](images/477a5aa44ea3e08368b306dfbca201ff05376e28ec5732c410a97da18434dab5.jpg)

Thenext time-space graphic, drawn by a computer, displays thelevels of threeair pollutants located over a two-dimensional surface (six counties in southern California) at four times during the day. Nitrogen oxides (top row) areemitted bypower plants, refineries,and vehicles. Refineries along the coast and Kaiser Steel's Fontana plant produce the post-midnight peaks shown in thefirst panel; traffic and power plants (with their heavydaytimedemand) send levels up during the day. Carbon monoxide (second row) is low after midnight exceptout at the steel plant; morning traffic then begins to generate each day's ocean ofcarbon monoxide, with the greatest concentration at the convergence offive freeways in downtown Los Angeles. Reactive hydrocarbons (third row), like nitrogen oxides, come from refineries after midnightand then increasewith traffic during the day. Each of the 12 time-spacepollutant slices summarizes pollutants for 2,400 spatial locations (2,400 squares five kilometers on a side).Thus28,8oo pollutant readings are shown,except for thosemasked by peaks.

Theair pollution display is a small multiple.Thesame graphical design structure isrepeated foreach of the twelve slices or multiples.Small multiples are economical: once viewersunderstand the design of one slice, they have immediate access to thedata in all the other slices. Thus,as the eye moves from one slice to thenext, the constancy of the design allows the viewer to focuson changes in the data rather than on changes in graphical design.

LosAngeles Times,July 22,1979;based on work ofGregoryJ.McRae, California Institute ofTechnology.

![](images/14b985eaf7198f25a558f83399ef42c81697c78bc694829f2bd7bf18cc1913f2.jpg)

Our thirdexample of a space-time-story graphic ingeniously mixes space and timeon the horizontal axis. This design moves well beyond theconventional time-series becauseof its clever plotting field, with location relative to the ground surface on the vertical axis and time/space on the horizontal. The lifecycle of theJapanese beetle is shown.

L.Hugh Newman, Manand Insects (London, 1965),pp. 104-105.

![](images/7f6143aa236c747d2f9bc57543ccd4f8dbccea1dad5f478e2fac80a4ddb800be.jpg)

# More Abstract Designs: Relational Graphics

The invention of data graphics required replacing the latitudelongitude coordinates of the map with more abstract measures not based on geographical analogy.Moving from maps to statistical graphics was a big step, and thousands ofyears passed before this step was takenby Lambert, Playfair,and others in the eighteenth century. Evenso,analogies to the physical world served as the conceptual basis for early time-series. Playfairrepeatedly compared his charts to maps and, in thepreface to the first edition ofThe Commercialand Political Atlas,argued that hischarts corresponded to a physical realization ofthe data:

Suppose the money we pay in any oneyear for the expence ofthe Navy were in guineas,and that these guineas were laid down upon a large table in astraight line,and touching each other,and those paid next yearwere laid down in another straight line, and the same continued foranumber ofyears: these lines would be of different lengths, as there were fewer or moreguineas;and they would makea shape,the dimensions ofwhich would agree exactly with the amount ofthe sums; and thevalue ofa guinea would berepresented by the part of space which itcovered. The Charts are exactly this upon a small scale,and onedivision represents the breadth or value of ten thousand oran hundred thousand guineas as marked, with thesame exactness that a square inch upon a map may represent a square mile of country. And they, therefore,are a representation ofthereal money laiddown in different lines, asit was originally paid away. [pagesiii-iv]

Fifteen years laterin The Statistical Breviary,his most theoretical book about graphics, Playfair broke free of analogies to the physical world and drew graphics as designs-in-themselves.

One of four plates in The Statistical Breviary,this graphic is distinguished byits multivariate data, theuse ofarea to depict quantity,and thepie chart-in apparently the first application of these devices. The circle represents the area of each country; the lineon theleft, the population in millions read on the vertical scales;the lineon theright,therevenue (taxes) collected in millions of pounds sterling read also on the vertical scale;and the"dotted linesdrawn between the population and revenue, aremerely intended to connect together the lines belonging to the same country. The ascent

\*D\* THE   
STATISTICAL BREVIARY; SKEWINC, ON A PRINCIPLE ENTIRELY NEW, THE RESOURCES OF EVERY   
STATEAND KINGDOMINEUROPE; ILLUSTRATED WITS STAINEDCOPPER-PLATECHARTS, ALPRESENTING TNE   
PHYSICAL POWERSOF EACH DISTINCTNATION WITHEASE AND PERSPICUITY. By WILLIAM PLAYFAIR. To WKICK18 ADDED,   
ASIMILAR EXHIBITION OF THERULINGPOWERS OF HINDOOSTAN. LONDON: PdbyT.oC FleetStreer,   
F, PdVerC CAXPEKTEA dCo.B   
dPAARY, LelSt andT:sst HooD, dDit, Polry; sjsn's BLACK 1801.

![](images/1f37b7025809d4606ddf8931869c6cf36c472d6ee6fbb63605ced3b3f1d616ae.jpg)

ofthose lines being fromright toleft, orfrom left toright, shews whether in proportion toitspopulationthecountry is burdened with heavy taxes or otherwise" (pages $_ { 1 3 - 1 4 } )$ .The slope of the dotted lineisuninformative, since itisdependentonthediameter of the circle as well as the heightof the two verticals.However, the sign ofthe slope does make sense, taking Playfair to his familiar point about what he regarded asexcessivetaxation in Britain (sixth circle from the right, withthe slope running opposite to most countries).Playfair was enthusiastic about the multivariate arrangement becauseitfostered comparisons:

The author ofthis work applied the use of lines to matters of commerceand finance about fifteen years ago, with great success. Hismode was generally approved ofas not only facilitating, but rendering those studies more clear,andretained more easily by the memory. The present charts arein like mannerintended to aidstatistical studies, by shewing to the eye the sizes ofdifferent countries represented bysimilar forms, forwhere forms are not similar, theeye cannotcompare them easily nor accurately. From this circumstance it happens, that wehavea moreaccurate idea of the sizes ofthe planets, which arespheres, than ofthe nations of Europe which we see on themaps,all ofwhich are irregular forms in themselves aswell asunlike to each other. Size,Population,and Revenue, arethe three principal objects of attention upon the general scale of statistical studies, whether we are actuated by curiosity or interest; Ihave therefore represented these three objects in one view. [page 1s]

But here Playfair had a forerunner-and one who thought more clearly about theabstractproblems of graphical design than did Playfair, who lacked mathematical skills. A mostremarkable and explicit early theoretical statement advancing the general (nonanalogical) relational graphic wasmade byJ.H.Lambert in 1765, 35years before The Statistical Breviary:

Wehave in general two variable quantities, x,y,which will becollated with one another by observation, So that we can determine for each valueof $\mathbf { x }$ whichmay beconsidered as an abscissa, thecorresponding ordinatey. Were the experiments or observations completely accurate, these ordinates would give a number of points through which a straight orcurved line should be drawn. Butasthis is not SO, theline deviates to agreater or lesser extent from theobservational points. Itmust thereforebedrawn in such a way thatit comes as near as possible to its true position and goes, asit were, through the middle of the given points.13

Lambert drew agraphical derivation of the evaporation rate of water asa function of temperature, according to Tilling.The analysis beginswith two time-series: DEF,showing the decreasing height ofwater in a capillary tube as a functionof time,and ABC, the temperature. The slope ofthe curve DEFiS then taken (note the tangent DEG) ata number of places, yielding therateofevaporation:

To complete thegraphical calculus, themeasured rate isplotted against thecorresponding temperature in this relational graphic:

![](images/775fcefe0efcf78d24ca0ff624a16473388263ef2eec41b645677f47921eba8a.jpg)

![](images/3c760c35d95b98724f70e53e654ed4fcff5e808458c51a467b60816740ed80c4.jpg)  
J.H Lambert,"Essaid'hygrometrie ou surla mesure del'humidite," Memoires del'AcademieRoyaledes SciencesetBellesLettres . 1769(Berlin, 1771），plate 1, facing p.126; from Tilling'sarticle.

Thus, by the early 1800s,graphical design wasat last no longer dependent on direct analogy to the physical world thanks to the work ofLambert and Playfair. This meant,quite simply but quite profoundly, that any variable quantity could be placed in relationship to any other variable quantity, measured forthe same units ofobservation. Datagraphics, because they were relational and nottied to geographic or time coordinates, became relevant to all quantitative inquiry. Indeed, inmodern scientific literature, about 40 percent of published graphics have a relational form, with two or more variables (none of which are latitude, longitude, or time).This is no accident, since the relational graphic-inits barest form,the satterplot and itsvariants-is the greatest of all graphical designs. It links at least two variables, encouragingand even imploring the viewer to assess the possible causal relationship between the plotted variables. It confronts causal theories thatX causes Ywith empirical evidenceas to theactual relationship between Xand Y, as in the case of therelationship between lung cancer and smoking:

# CRUDE MALE DEATH RATE FOR LUNG CANCER IN 1950 AND PER CAPITA CONSUMPTION OF CIGARETTES IN 1930 IN VARIOUS COUNTRIES.

![](images/991bdeb5275ea58d95a6ae64d64ee0e58375a5a4bd2f4b7ac373c81a2f7ef4a2.jpg)  
Report ofthe Advisory Committee to the Surgeon General, Smokingand Health (Washington,D.C.,1964),p.176;bsed on R.Doll,"Etiology ofLung Cancer,” Advances in CancerResearch,3 (1955), 1-50.

These small-multiple relational graphs show unemploymentand inflation over timein "Phillips curve" plots for nine countries, demonstrating the collapse ofwhat was once thought to be an inverse relationship between thevariables.

![](images/3508a332599a7ec6850ce2e56e4946d974a7cc7257c8a290bb7d852d59dade90.jpg)  
Paul McCracken,et al., TowardsFull Employment and Price Stability(Paris, 1977),P. 106.   
Inflation and Unemployment Rates

Theory and measured observations diverge in the physical sciences, also. Here therelationship between temperature and the thermal conductivity of copper is assessed in a series ofmeasurements from different laboratories. The connected points are from a single publication, cited by an identification number. Thevery different answers reported in the published literature result mainly from impurities in the samples of copper. Note how effectively thegraphic organizes a vastamount of data,recording findings ofhundreds of studies on a single page and, atthe same time, enforcing comparisons ofthe varyingresults.

![](images/963fa060170ba660216a27120b160b687fe185a75bca162615485c2a0997afb0.jpg)

Finally, two relational designs ofadifferent sort-wherein the data points are themselves data. Here theeffect of two variables interactingis portrayed bythe faces on the plotting field:

![](images/0766ec25e353a45f75fa067d7be6a78f7f6e7efae5b310bcd20171e35427fef2.jpg)  
E.C.Zeeman,"Catastrophe Theory," Scientific American,234（April 1976),67; basedonKonradZ.Lorenz,King Solomon’sRing(NewYork,1952).

And similarly, the varying sizes of white pine seedlings after growing for one season in sand containing different amounts of calcium, in parts per million in nutrient-sand cultures:

![](images/33b174d2dca0299ee70b3e53bbf2b18b617265bbec12ede17844dcfab036bd7f.jpg)

# Principles of Graphical Excellence

Graphical excellence is thewell-designed presentation ofinteresting data-amatter ofsubstance,ofstatistics, and of design.

Graphical excellence consists ofcomplex ideas communicated with clarity, precision, and efficiency.

Graphical excellence is that which gives to theviewer the greatest number ofideas in the shortest timewith the leastinkin the smallest space.

![](images/d261585129cc054ecb3eadf7a75a2dd81f981f2d6cfaf5a123d944c4c1619201.jpg)

Graphical excellence isnearly always multivariate.   
And graphical excellence requires telling the truth about thedata.

As to the propriety and justness ofrepresenting sums of money, and time, byparts of space,tho'veryreadilyagreed to by most men,yet a few seem to apprehend thattheremaypossiblybe some deception in it, of which they arenot aware.

William Playfair, The CommercialandPolitical Atlas (London, 1786)

People said: "With thechart on the wall, withthefigurespublished, let's emulateandrouseour enthusiasm in production."

State Statistical Bureau ofthe People's Republic of China, Statistical Work in theNew China (Beijing, 1979)

Get it right or letit alone.   
The conclusion you jump to may be your own.

James Thurber, Further Fables for Our Time (NewYork, 1956)

# 2 Graphical Integrity

Formany people the first word thatcomesto mind when they think about statistical chartsis"lie." No doubt some graphics do distort the underlying data, making it hard forthe viewer to learn the truth. But data graphics areno different from words in this regard, forany meansofcommunication can beused to deceive. There is no reason to believe that graphics areespecially vulnerable to exploitation by liars; in fact,most ofus have pretty good graphical lie detectors that helpus seeright through frauds.

Muchof twentieth-century thinking about statistical graphics has been preoccupied with thequestion ofhow some amateurish chart might fool a naiveviewer. Other important issues,such as the use of graphics for serious data analysis, were largely ignored. Atthe core of the preoccupation with deceptive graphics wasthe assumption that data graphics were mainly devices for showing the obvious to the ignorant. It is hard to imagine any doctrine more likely to stifle intellectual progress in a field. The assumptionled down two fruitless paths in the graphically barren years from 1930 to 1970: First, that graphics had tobe“alive,” "communicatively dynamic, overdecorated and exaggerated (otherwiseallthedullards in the audience would fall asleep in theface ofthose boring statistics). Second, that themain task of graphical analysis wasto detectand denounce deception (the dullards could not protect themselves).

Then,in the late196os,John Tukey made statistical graphics respectable, putting an end to theview that-graphics were only for decorating a fewnumbers. For herewasa world-class data analyst spinning offhalf dozen new designs and, more importantly,using them effectively to explore complex data. Nota word about deception; no tortured attempts to construct more graphical standards" in a hopeless effort toend all distortions. Instead, graphics wereused asinstruments for reasoning about quantitative information. With this good example,graphical work has come to fourish.

Of course false graphics are still with us. Deception must always be confronted and demolished, even iflie detection isno longer at the forefront ofresearch. Graphical excellence beginswith telling thetruth about the data.

Hereare several graphics thatfail to tell the truth. First, thecase ofthe disappearing baseline in theannual report ofa company that would just as soon forget about 1970. Acareful look at the middle panel reveals a negative income in 1970, which is disguised by having the bars begin at the bottom at approximately minus \$4,200,000:

![](images/715a1ff37e1b2c059143c46653b1cc29574d871062c16b338cf13d9a72ac1749.jpg)

This pseudo-decline was created by comparing sixmonths' worth of payments in 1978 to a full year's worth in 1976 and 1977, with the lierepeated four times over.

![](images/fc6c74c87a4b9598d6dfe505290ce6589ae52a91906ba0b6d7047f8f20e8af1e.jpg)

And sometimes thefact that numbers have a magnitude aswell as an order is simply forgotten:

![](images/303edf5cea2883ef9f379ed0151bb089bb4a85b7cabd55b13c546e30710a0ca0.jpg)  
Pittsburgh Civic Commission, Report on ExpendituresoftheDepartmentofCharities (Pittsburgh, 1911),p. 7.

# What is Distortion in a Data Graphic?

Agraphic doesnot distort ifthe visual representation ofthedata is consistent with thenumerical representation. What then is the "visual representation" ofthe data? As physically measured on the surface of the graphic? Or the perceived visual effect? How do we know that thevisual image represents the underlying numbers?

One way to try to answer these questions isto conduct experimentson the visual perception of graphics-having people look at lines of varying length, circles of different areas, and then recording their assessments ofthe numerical quantities.

![](images/ef68eef4f52a9b858fb3634798f5700f84d1c03f969f9a115fe544c5df0a289e.jpg)

Such experiments have discovered very approximatepower laws relating the numerical measure to thereported perceived measure. For example, the perceived areaofa circle probably grows somewhat more slowly than theactual (physical, measured) area: thereported perceived area $\ c =$ (actual area)x,where $\mathbf { x } = . 8 \pm . 3$ a discouraging result. Different people see the sameareassomewhat differently; perceptions change with experience; and perceptions arecontext-dependent.2 Particularly disheartening is the securely established finding that thereported perception of something as clear and simple as line length depends on the contextand what other people have alreadysaid about thelines.3

Misperception and miscommunication are certainly not special to statistical graphics,

![](images/b0658ae16373cee9fdc807628f891cd261667edc9f630d1fdbf3aad170e7cacb.jpg)

but whatis a poor designer to do? A different graphic for each perceiver in each context? Or designs thatcorrect for the visual transformations of the average perceiver participating in theaverage psychological experiment?

One satisfactory answerto these questions isto useatable to show the numbers. Tablesusually outperform graphics in reporting on small data sets of 20 numbers orless. Thespecial power of graphics comes in the display of large data sets.

At any rate, given the perceptual difficulties, the best we can hope for is some uniformity ingraphics (ifnot in the perceivers) and some assurance that perceivers havea fair chance of getting the numbers right. Two principles lead toward these goals and, in consequence, enhancegraphical integrity:

Therepresentation ofnumbers, as physically measured on the surface of the graphic itself, should bedirectly proportional to thenumerical quantities represented.

Clear, detailed, and thorough labeling should be used to defeat graphical distortion and ambiguity. Write out explanations ofthe data on the graphic itself. Label important events inthedata.

2Theextensive literature is summarized in MichaelMacdonald-Ross,"How NumbersAreShown:A Review of Research on thePresentation ofQuantitativeData inTexts, 3 Audio-Visual Communication Review, 25 (1977),359- 409.In particular, H.J.Meihoefer finds greatvariability among perceivers; see “TheUtility of the Circleas an Effective CartographicSymbol,”Canadian Cartographer, 6 (1969), 105-117and"The Visual Perception ofthe Circle inThematicMaps:Experimental Results," ibid.,10 (1973),63-84.

# 3S.E. Asch, "Studies of Independence and Submission to Group Pressure. A Minority ofOne Against a Unanimous Majority,' PsychologicalMonographs (1956), 70.

Drawing by CEM; copyright 1961, TheNew Yorker.

Violations ofthe first principle constitute one form ofgraphic misrepresentation, measured by the

If theLie Factorisequal to one, then the graphic might be doing areasonable job of accurately representing the underlying numbers. Lie Factors greater than 1.05or less than.95 indicatesubstantial distortion, far beyond minorinaccuraciesin plotting. Thelogarithm of the Lie Factorcan be taken in order to compare overstating $( \log \mathrm { L F } > 0 )$ ） with understating $( \log \mathrm { L F } < 0 )$ 0 errors.In practice almostalldistortions involve overstating,and Lie Factorsof two to five are not uncommon.

Here is an extremeexample. A newspaper reported thatthe U.S. Congress and the Department of Transportation had seta series offuel economy standards to be met by automobile manufacturers, beginning with 18 milesper gallon in 1978 and moving in stepsup to 27.5 by 1985, an increase of53 percent:

$$
\frac { 2 7 . 5 - 1 8 . 0 } { 1 8 . 0 } \times 1 0 0 = 5 3 \%
$$

These standards and the dates for their attainment were shown:

This line,representing18miles per gallon in 1978, is 0.6inches long.

![](images/cfed799890403814c3d1e397fa7d09eddecda28358abe244587c10f82aa1cf30.jpg)

This line,representing 27.5 miles per gallon in $1 9 8 5 ,$ is 5.3inches long.

Themagnitude ofthe change from 1978 to $1 9 8 \xi$ is shown in the graph by therelative lengths ofthe two lines:

$$
\frac { 5 . 3 - 0 . 6 } { 0 . 6 } \times 1 0 0 = 7 8 3 \%
$$

Thus the numerical change of53 percent is presented by some lines that changed 783 percent, yielding

$$
{ \mathrm { L i e ~ F a c t o r } } = { \frac { 7 8 3 } { 5 3 } } = 1 4 . 8
$$

which is too big.

The display also has several peculiarities of perspective:

On most roads the future isin front ofus,toward the horizon, and the present is at our feet. This display reverses the convention SO as to exaggerate the severity of the mileage standards. Oddly enough, thedates on theleft remain a constant size on the page even as they move along with theroad toward the horizon. Thenumbers on the right, aswell as thewidth oftheroad itself, are shrinking because oftwo simultaneous effects: the change in the values portrayed and the change due to perspective. Viewers have no chance of separating the two.

Itis easy enough to decorate these data without lying:

![](images/5d8ee3a1878d8820c0446b49bac17248bbf25041c91561f243b83c2b0b573028.jpg)

The non-lying version, in addition,puts thedatain a context by comparing the new carstandards with the mileage achievedby the mix of cars actually on theroad. Also revealed is a side ofthe datadisguised and mispresented in the original display: the fuel economy standards require gradual improvement at start-up, followed by 3 doubled rate from 1980to 1983,and flattening out after that.

Sometimes decoration can help editorialize about thesubstance of the graphic. But itis wrong to distort thedata measures-the ink locating values ofnumbers-inorder tomake an editorial comment orfita decorative scheme. Itis also a sure sign of the Graphical Hack at work. Here are many decorations but no lies:

![](images/2ceaf007ece51d24e0e46846ccbd25dd662c1f9acf9b68d37f9323734f1f7ff9.jpg)

# Design and Data Variation

Each part of a graphic generates visual expectations about its other parts and, in the economy ofgraphical perception, these expectations often determine what the eye sees. Deception results from the incorrect extrapolation ofvisual expectations generated atone place on the graphic to other places.

A scalemoving in regular intervals, for example, is expected to continue itsmarch to the very end in aconsistent fashion, without the muddling or trickery ofnon-uniform changes. Here an irregularscale isused to concoct apseudo-decline. The first seven increments on the horizontal scale are tenyears long, masking the rightmost interval of four years. Consequently the conspicuous feature of the graphic is the apparent fall ofcurves at theright, particularly the declinein prizes won by people from the United States (the heavy, dark line) in the mostrecent period. This effect results solely from design variation. Itis a biglie, since in reality (and even in extrapolation, scaling up each end-point by 2.5 to take thefour years' worth of dataup to a comparable decade), theU.S. curve turned sharply upward in the post-1970 interval. A correction, with theactual data for1971-80, isat the right:

![](images/4cfbbc5ce0907880d2630c87a13873108c0079691f889eecc0dbae619542e6c7.jpg)  
Nobel Prizes Awarded in Science, for Selected Countries,1901-1974

![](images/83af46c7ba149f3d32f3a910d1eaa0ddb4512756e85cf616e696776cf5ee1631.jpg)  
Nobel Prizes Awarded in Science, for Selected Countries, 1901-1980

The confounding ofdesign variation withdata variation over the surface ofa graphic leads to ambiguityand deception,for theeye may mixup changesin the design with changes in the data.A steady canvas makes fora clearer picture. Theprincipleis, then:

Show data variation, not design variation.

Design variation corrupts this display:

![](images/ebc03a61a344c0370358349cf5425f2560adbbaea48bbd5d5298e6b33c90e457.jpg)  
TheNew York Times/Dec.19,1978

Five different vertical scales show the price:

During this time onevertical inch equals   
1973-1978 \$8.00   
January-March 1979 \$4.73   
April-June 1979 \$4.37   
July-September1979 \$4.16   
October-December 1979 \$3.92

And two different horizontal scales show the passage oftime:

![](images/5b3250fb187b85a2f15fc6e881211964701bc07ae9e8a030c4a00f7a332f37d4.jpg)

As thetwo scales shift simultaneously, thedistortion takes on multiplicative force. On theleft of the graph, a price of $\$ 10$ for oneyear is represented by 0.31 square inches; on the right side, by 4.69 square inches. Thus exactly the same quantity is $4 . 6 9 / 0 . 3 1$ $= 1 5 . 1$ times larger depending upon where it happens to fall on thesurface ofthe graphic. That is design variation.

New York Times, December 19,1978, P.D-7.

Design variation infected similargraphics in other publications. Here an increase of454 percent is depicted as an increase of $4 , 2 8 0$ percent, for a Lie Factor of9.4:

![](images/50101a1abebaa8279b4488e84a2c39e29c72ed2650f11ea3c02d80ba19cc719e.jpg)

And an increase of708 percent is shown as 6,700 percent, fora Lie Factor of9.5:

Time, April9, 1979,P.57.

![](images/7355425b46f0707a29101a78710b4ee675dfbff3538e086b3c6441a967976499.jpg)  
WashingtonPost, March28, 1979,p. A-18.

Al these accounts ofoil pricesmade a second error, by showing the price ofoil in inflated (current) dollars. The 1972 dollar was worth much more than the 1979 dollar. Thus in sweeping from left to right over thesurface of the graphic, thevertical scale in effect changes-design variation-because thevalue of money changes over theyears shown. Theonly way to think clearly about money over time is to makecomparisons using inflation-adjusted units ofmoney. Several distinguished graphic designers did express the price in real dollars-and theyalso avoided other sources ofdesign variation. The stars were Business Week, the Sunday Times (London),and The Economist.

![](images/11ae34f96949e0b1ff96b5a8def9abf076cbac24f7e46b4a9ed08fd1f0b718cb.jpg)

In the graphic we saw first, thetwo sources of design variation covered up anintriguing, non-obvious aspect of the data: in the four yearsprior to the1979-1980 increases, the real price of oil had declined. Busy with decoration, the graphic had missed the news.

![](images/98e2d19148bd164616bb70784b614071ae351ee53a77bb94af7b56f9c6e211a7.jpg)

![](images/4c88e7faffce05e9abaa3a487470a4f1b910030b52c8397517b4ac220ac8778a.jpg)

TheEconomist, December29,1979,p.41.

Sunday Times (London), December 16, 1979,P. 54.

Business Week,April9, 1979,P.99.

![](images/107ba89d86191c143fb683a9674e95f8f0d95404555ef357c9928e1c62c6fc35.jpg)

![](images/f754aa87fb3ad81b66797fd3756738567f90bca4b30e493624a491229747b766.jpg)  
TheDivisionsat theBottomare Years,&cthoseontheRight hand Money.

# The Case of Skyrocketing Government Spending

Probably the most frequently printed graphic, other than the daily weather map and stock-market trend line, is the display of government spending and debt over the years.These arrays nearly always create theimpression that spending and debt are rapidly increasing.

Asusual, Playfair was the first, publishing this finely designed graphic in $^ { 1 7 8 6 }$ Accompanied by his polemic against the "ruinous folly" ofthe British government policy offinancing its colonial wars through debt, itis surely the first skyrocketing government debt chart,beginningthenow 200-year history of such displays. Thisis one of the few Playfairs thatistaller than wide; less than one-tenth of allhis graphics (about 9o, drawn during 35years of work) are longer on the vertical. The tal shape here serves to emphasize the picture of rapid growth. The money figures are not adjusted for inflation.

But Playfairhad the integrity to showan alternative version a few pages later in The Commercial and Political Atlas.The interest on thenational debt was plotted ona broad horizontal scale, diminishing the skyrocketeffect. And, furthermore, "This is inreal and notinnominal millions' (page 129):

![](images/bb40ff46398d3a9e6e839039d050457dbe215959d3532398fcc7b8877931be31.jpg)  
Interest oftheNATIONAL DEBT from the Revolution.   
T'he Bottom line is Years,thoseon the RighthandMillions fPounds.

Although Playfair deflated money units over time in his work of $^ { 1 7 8 6 }$ thematter has proved difficult for many, eluding even modern scholars. This display helps its political point along by failing to discount for infation and population growth andby using a tall and thin shape (the area covered by the data is2.7 times taller than wide):

![](images/26922871ac3b29de6ddcac6da6cce26922d5bae6147384dad6462026dbd23143.jpg)  
Figure A3. The Growth of Government:Federal Spending in Selected Domestic Areas

Morris Fiorina, Congress: Keystone ofthe Washington Establishment (New Haven, 1977),P. 92.

Letus look, in detail, at anothergraphic on government spending:

![](images/3480cfe868c967f3bb816c022385edc0a5d981fb4bea95464f91316e2cad8b24.jpg)

Despite the appearance created bythehyperactivedesign,the state budget actually did not increase during the last nine years shown. To generate the thoroughly false impression ofasubstantial and continuous increase in spending, the chart deploys several visual and statistical tricks-all working in thesame direction, to exaggerate the growth in the budget. Thesegraphical gimmicks:

These three parallelepipeds have been placed on an optical planein front of theother eight, creating theimage that thenewer budgets tower over the older ones.

This cluster oftype emphasizes stretches out thelow value for 1967, encouragingtheimpression that recentyears have shot up from a stable base. Horizontal arrowsprovide similaremphasis.

This squeezed-down block oftype contributes to an image of small, squeezed-down budgets back in the good old days.

![](images/c6818bc31a6d5caf92816bdaada6c736fe933be992d9ee680855bf9b23d4354e.jpg)  
Arrows pointing straightup emphasize recent growth. Comparewith horizontal arrows atleft.

Leaving behind the distortion in the chartjunk heap at theleft yields a calmer view:

![](images/5cd06b5e032353b0f4d93f8e34f325ff46a43e6ebc2810489821731936fca0f8.jpg)

![](images/ce2fc7ef345818a482e5712119b55e6f14520a650487d63e57e8cc08f5db960b.jpg)

Two statistical lapses also bias the chart. First, during the years shown, thestate'spopulation increased by 1.7 million people, or 10percent. Part of the budget growth simplyparalleled population growth. Second, theperiod wasa timeof substantial inflation; those goods and services thatcost stateand local governments $\$ 1.00$ to purchase in 1967 cost $\$ 2.03$ in 1977. By not defating, the graphic mixes up changes in the value of money with changes in the budget.

Application ofarithmetic makes itpossible to takepopulation and inflation into account. Computing expenditures in constant (real) dollars per capita reveals a quite different-and farmore accurate-picture:

Percapita budget expenditures, in constant dollars

![](images/5bc6b8509293b2f85878937ece4a3143b0f44ac5021f78146fe5d634a28e29b4.jpg)

![](images/96309d3be771e481638e093612f84646fc1ff10b9169364baa5e8bff3884a672.jpg)

Thus,in terms ofreal spending per capita, thestate budget increased by about20 percent from 1967 to 1970and remained relatively constant from 1970 through 1976. And the 1977 budget representsasubstantial declinein expenditures. Thatis thereal news story of these data,and it wascompletely missed by the Graph of theMagical Parallelepipeds. Of course no small set of numbers is going to capture thecomplexities ofa large budget- but, atany rate,why tell lies?

The principle:

In time-series displays ofmoney, deflated and standardized units of monetary measurement are nearly alwaysbetter than nominal units.

# Visual Areaand Numerical Measure

Anotherway toconfuse datavariation with design variation isto use areas to show one-dimensional data:

![](images/bc1132e7ac1f2ec0248be20b967752b67fc26d97facb4911603a97cd569f5e1d.jpg)  
R. Satet,Les Graphiques (Paris,1932), p.12.

And here is theincredible shrinking doctor,with aLie Factor of 2.8, not counting the additional exaggeration from theoverlaid perspective and the incorrect horizontal spacing of the data:

# THE SHRINKING FAMILY DOCTOR In California

![](images/f1c43748c78176dfa2c05fa885b087fa97bfbe6dd4ad2b4d7636cf714ddd2d76.jpg)

Many published efforts using areas to show magnitudes make the elementary mistake of varying both dimensions simultaneously in response to changes in one-dimensional data.Typical is the shrinking dollar fallacy. To depict the rate ofinflation, graphs show currency shrinking on two dimensions,even though the valueofmoney is one-dimensional. Here is oneof hundreds of such charts:

![](images/543f84856d4d1399b77b6681eb37883e35328dace0790d33abb8e682b5d4c36f.jpg)

Ifthe area of thedollar isaccurately to reflect its purchasing power, then the $^ { 1 9 7 8 }$ dollarshould beabout twiceas big as that shown.

Thereare considerable ambiguities in howpeople perceive a twodimensional surfaceand then convert that perception into a onedimensional number. Changes in physical area on the surface ofa graphic do not reliably produce appropriately proportional changes in perceived areas. The problem is all the worse when the areas are tricked upinto three dimensions:

By surface area, theLieFactor for this graphic is 9.4. But, ifone takes the barrel metaphor seriouslyand assumes that the volume of the barrels represents the price change, then thevolume from 1973 to 1979 increases 27,000 percent compared to a data increase of 454percent, fora Lie Factor of59.4, which isa record.

Similarly, a three-dimensional representation puffing up one-dimensional data:

Conclusion: The use oftwo (or three) varying dimensions to show one-dimensional data isaweak and inefficient technique, capable of handling only very small data sets, often with errorin design and ambiguity in perception. These designs cause SO many problems that they should beavoided:

Thenumber ofinformation-carrying (variable) dimensions depicted should not exceed the number ofdimensions in thedata.

![](images/22fb5a51d924104607f9df978db409be0b079c669331c3a996395e4eb4afa104.jpg)  
New York Times,January27,1981, P.D-1.

![](images/1724474fda8d860676b82fe236a9c05e5dc488f9efaa56aa4a093aa0d4483d30.jpg)

# CASSE POSTALI DI RISPARMIO ITALIANE

Numero dei Libretti Libretto medio e Deposito totale al fine di ogni mese

![](images/9b6b264fff16f7d7f3abbc9314551c04b41265e962865b4191a709e18c15ea44.jpg)  
Antonio Gabaglio, Teoria Generale della Statistica (Milan, second edition, 1888).

This multivariate history of the Italian post office uses two dimensions in a way nearly consistent with this principle, with the number of postal savings booksissued and the average size of deposits multiplying up to total deposits at theend of eachmonth from $^ { 1 8 7 6 }$ to $1 8 8 1$

But Playfair's circles, an early use ofarea to showmagnitude, arenot consistent with theprinciple, since theone-dimensional data (city populations) arerepresented by anareal data measure:

![](images/79102b43d097293431d3eeb043e9adf220f2f689c64571779c7a50a517c5cbd3.jpg)  
Scientific American Reference Book (New York, 1909),p. 280.

Perhaps graphics that border on cartoons should be exempt from the principle. Wecertainly would not want to forgo the 4,340 pound chicken:

![](images/9d18035d8d7b128575376720c22270e06e9a89dd41a3b4a6da4a186b9628b4cf.jpg)

# Context is Essential for Graphical Integrity

To betruthful and revealing, data graphics must bearon the question at the heart of quantitative thinking: "Compared to what?"' The emaciated, data-thin design should always provoke suspicion, for graphics often lie by omission, leaving out data sufficient for comparisons. The principle:

Graphics must not quote data out ofcontext.

Nearlyall the important questions are left unanswered by this display:

![](images/091a1e3151200483aae85af8ff568a6b5e893924dd58c6ee56c92da62410e544.jpg)

A few more data points add immensely to the account:

![](images/71e0b0dd419983d399642bfc6f78dbda0b3b353e6de152528e9808da5055d390.jpg)

Imagine the very different interpretations other possible timepaths surrounding the1955-1956 change would have:

![](images/73f9343be0de22d3b30bb30e6595cd896d5babd90652b9d6977fe0a716c88759.jpg)

Comparisons with adjacent statesgive astill better context, revealing it was not only Connecticut that enjoyed decline in traffic fatalitiesin theyear ofthe crackdown on speeding:

![](images/335ddd21c035fac1d8c96332b137d3e3c3782781454a6fbac97b09619021b42c.jpg)

# Conclusion

Lying graphics cheapen the graphical arteverywhere. Since the lies often show up in newsreports, millions of images are printed When a chart on television lies, it lies tens ofmillions oftimes over; when aNew York Times chart lies,it lies 900,000 times over to agreatmany important and influential readers. The lies are told about themajor issues ofpublic policy-the government budget, medical care, prices, and fuel economy standards, for example. The lies are systematic and quite predictable, nearly always exaggerating therate ofrecent change.

Themain defense of the lying graphic is "Well, at leastit was approximately correct, wewere just trying to show the general direction of change. But many of the deceptive displays we sawin this chapter involved fifteenfold lies,too large to bedescribed asapproximately correct. And in several cases the graphics were not evenapproximately correct by the most laxof standards, since they falsified thereal news in thedata. Itis the special character ofnumbers that they have a magnitude aswell asan order; numbers measure quantity. Graphics can display the quantitative size of changes aswell as their direction. Thestandard of getting only the directionand not themagnitude right is the philosophy that informs the Pravda School ofOrdinal Graphics. There, every charthasacrystal clear direction coupled with fantasy magnitudes.

![](images/ede6adad7c7d0e0dbee355db7bbfcf8d9b705df53449831155582a218d6c4915.jpg)  
POCT nPOAyKIHN nPOMbIWneHHoCtH [1922r. $\ c =$ I.

A second defense of the lying graphic is that,although thedesign itself lies, theactual numbers are printed on thegraphic for those picky folkswho want to know the correct size of the effects displayed. Itis as if notlying in one place justified fifteenfold lies elsewhere. Few writerswould work undersuch a modeststandard ofintegrity, and graphic designers should not either.

Graphical integrity ismore likely to result if these six principles are followed:

The representation ofnumbers, as physically measured on the surface of the graphic itself, should be directly proportional to thenumerical quantities represented.

Clear, detailed, and thorough labeling should beused to defeat graphical distortion and ambiguity. Write out explanations of thedata on the graphic itself. Label importantevents in thedata.

Show data variation, not design variation.

In time-scries displays of money,deflated and standardized units of monetary measurement arenearly always better thannominal units.

Thenumber of information-carrying (variable) dimensions depicted should not exceed thenumber ofdimensions in the data.

Graphics must not quote data out ofcontext.

Why do artists draw graphics thatlie? Why do theworld's major newspapersand magazines publish them?1

Although bias and stereotyping are the origin ofmore thana fewgraphical distortions,theprimary causes ofinept graphical work are to be foundin theskills,attitudes,and organizational structure prevailing among those who design and editstatistical graphics.

# Lack ofQuantitative Skills of Professional Artists

Lurking behind the inept graphic is a lackof judgment aboutquantitative evidence. Nearly allthose who produce graphics formass publication are trained exclusively inthefine artsand havehad little experience with the analysis of data. Such experienceis essential for achieving precision and grace in the presence ofstatistics, but even textbooks ofgraphical design are silent on howto think aboutnumbers. Illustrators too often see their work as an exclusively artistic enterprise-the words "creative,' 77 "concept,' and "style' combineregularly in all possible permutations, a Big Think jargon for the small task of constructing a time-series a fewdata points long. Those who get ahead arethose who beautify data, nevermind statistical integrity.

# The Doctrine That Statistical Data Are Boring

Inept graphics also flourish becausemany graphic artists believe that statistics are boring and tedious. Itthen followsthat decorated graphics mustpep up,animate,and all too often exaggerate what evidence there isin thedata. For example:

Time'sfirst full-time chart specialist, anart-school graduate, says that in his work, "The challenge is to present statistics as avisual idearather than a tedious parade ofnumbers."2 The opening sentence ofthe chapter on statistical chartsin Jan White'sGraphic Idea Notebook: "Why arestatistics so boring?" Sample illustrations supposedly reveal "Dry statistics turned

1"It isdifficult toknowwhythesesame errorsare being repeated. InPlayfair's original work these kinds ofmistakes were notmade; moreover, these errors were notas widespread in the 1930sas theyare now. Perhaps thereason is an increasein the perceived need forgraphs . without a concomitant increase in trainingin their construction. Evidence gathered bythe committee ongraphics ofthe American Statistical Association indicatesthat formal trainingingraphic presentation has hada marked decline atalllevels of education over thelast fewdecades." HowardWainer,“MakingNewspaper Graphs Fit to Print," in PaulA.Kolers, etal., eds. Processing of VisibleLanguage2 (New York,1980）, P.139.

into symbolic graphics and "Plain statistics embellished or humanized with pictures."3

Afinebook on graphics, Herdeg' Graphis/Diagrams,isdescribed by its publisher: "Aninternational review demonstrating convincingly thatstatistical and diagrammatic graphics do not necessarily haveto be dull."4

The doctrine of boring data servespolitical ends, helping to advance certain interests over othersin bureaucraticstruggles for control ofapublication's resources. For ifthenumbersaredull dull dull,then an artist,indeed many artists, indeed an ArtDepartmentand an Art Director are required to animate the data, lest the eyes of the audience glaze over. Thus the doctrine encourages placing data graphics under control ofartists rather than in the hands of those who write thewords and know the substance. As the art bureaucracy grows, style replaces content. And theword people, having lost space in thepublication to data decorators, console themselves with thoughts that statistics arereally rather tedious anyway.

If the statistics are boring, then you've got the wrong numbers. Finding the right numbers requires as much specialized skillstatistical skill-and hard work as creating a beautiful design or covering a complex news story.

# The Doctrine That Graphics Are Only for the Unsophisticated Reader

Many believe thatgraphical displays should divertand entertain thosein theaudience who find thewords in the text too difficult. For example:

5Consumer Reports,45(July 1980),408.

Consumer Reports describes the design of their new consumer   
magazine for children: "For the firsttest issue, CU's profes  
sional staff produced an article about sugar thatwas longer on   
graphics than on information. Wehad feared children mightbe   
overwhelmed by too many facts."5   
An art director with overall responsibility for the design of   
some3,000 data graphics each year (yielding2.5billion printed   
images) said that graphics areintended moreto lure thereader's   
attention away from the advertising than to explain the news   
in any detail. “Unliketheadvertisements,”hesaid, "atleast   
we don't put naked womenin our graphics."6

A news director ata national television network said that graphics mustbe instantly understandable: "If you have to explain it, don't useit."7

7Interview with author,July 1980.

This kind of graphical thinkingleads to

![](images/5e7e8bc1536514a64222f6cb6b3f1420b9083ad72a7cdb6f07fa8e11f89a674e.jpg)

Mary Eleanor Spear, Charting Statistics (New York,1952）,p. 5, whoappropriately describes thisasan "unnecessary chart.'

# The Consequences

What E.B. White said ofwriting is also true of statistical graphics "No onecan write decently who is distrustful ofthe reader's intelligence, or whose attitude is patronizing."8 Contempt for graphics and their audience, along with the lack ofquantitative skills among illustrators,has deadly consequences forgraphical work: over-decorated and simplistic designs,tiny datasets,and big lies.

8InWilliamStrunk,Jr.,andE.B. White, TheElementsofStyle(NewYork,1959), P.70.

Like censorship, these constraints on graphical design lead to elliptical and eccentric communication. In seeking to avoid the subtletiesof the scatterplot, artists drew up theseconvoluted specimens, forcing bivariatedata into aunivariate design:

NewYork Times,June16,198o,p.A-18.

Allen D. Manvel, "Taxation and Economic Growth, Taxation withRepresentation Newsletter, 9 （June 1980),p.3.

COMPARATIVETAXLOADSANDECONOMICGROWTHRATES INTHEFIFTEENLARGESTOECDCOUNTRIES CheNewor Views on the Economy Influence CarterSupport 2EsA5 Percentage of Democratic otorssaying that thelrfinancinl situationis worse thana yearago Percentage Democratic ticprimary votewon by Carter Wis. N.H Calit. Ohio N.Y. Mass, N.J. N lmm mv0 Gw 173-157A h0st

Butbeyond reviewing afewexamples, let us look moresystematically atthelevel ofgraphical sophistication prevailing at different publications. In order to make comparisons among a variety of newspapers, magazines, scientific journals, and books, I have compiled a rough measure of graphical sophistication-the share ofapublication's graphics thatare relational. Such a design links two ormore variables butis not a time-series or a map. Relational graphicsare essential to competent statistical analysis since they confront statements about cause and effect withevidence, showing how onevariable affects another. The design idea is a simple one, although not quite as simple as the barchart, timeseries plot, or data map. Relational graphics have beenused since 1765and are printed billions oftimesand ways every year;and thereis evidence that twelve-year-old children understand the design.9

All these graphics count as sophisticated by our hardly demanding measure:10

産业别倆格指数（1965/1955） 180業160 建设業140 卸小壳晨 農林業業120 公共事業 業10080L 製造業1401601802002202402602801就業者当質純生産額（1965/1955）

%121086 地 日本  
经济成長率 4 ↑并リ。  
0設備投资比率

9Clara Francis Bamberger, "Interpretation ofGraphs atthe Elementary School Level," Catholic University of America Educational ResearchMonographs, 13 (May1942). Additional data from textbooks and standardized testsare presented shortly.

$^ { 1 0 } \mathrm { A }$ variety of measures of graphical intelligenceand complexity arepossible and another, data density,is discussed in Chapter8.

△CZECHOSLOVAKIA FRANCE OGERMANY GREECE ISRAEL UNITED STATES Prage-Munich Netanyaerro -Safed -NewHaven   
L Psychro Corte 1 Dimonraklion   
3- ltea   
100n Lu 2 Luunl 10,000 100.0001,000,000 Population

# Pace of City Life Found 2.8FeetperSecondFaster

ByBOYCE RENSBERGER The pace of life in big cities is faster than itisin small towns- about 2.8 feet per second faster, according to 8 study by a Princeton University psychologist and his wife, who is an anthropologist.

![](images/7b769c842807d9875d710bacaebfdb9259ad3b1fbbbc596412aff367f089b518.jpg)  
ThNew YorxTimes/Feb.29，176

By measuring how fast people walk along the main streets of municipalities of varyingsizes, theyhave confirmed what most people have sensed informally.The biggerthe city,the faster its inhabitants walk.

They found, for example, that on Flatbush Avenue in Brooklyn, people brisk only IOWe e cou quar amble along ind the people ofCorte, France (population 5,500, move at 3.3 feetper second

Thefrequency ofuse of relational designs was counted for randomly selected issues from 1974 to 1980 ofeach of $^ { 1 \varsigma }$ news publications. A total of about 4,ooo graphics were examined in sampled issues. Scaling up the observed data by the frequency and circulation of the publication indicates that the sample represents a population of250 to 300 billion printed graphical images.

New York Times, February 29,1976, p.46.

Isao Satoand Miyohei Shinohara,New Politicsand Economics (Tokyo,1974), P. 113; aJapanesehighschool textbook.

Table 1 shows theresults, ranking the 15 news publications by graphical sophistication. Seven of the papers, from Pravda to the Wall StreetJournal, produced no relational graphics among those sampled and usually limited themselves to time-series. Other papers published more advanced graphics: theJapanese Asahi (a masscirculation daily), Akahata ("Red Flag,' a Communist party paper thatappears,from the data,tohave employed a sophisticated and talented graphical designer in 1979), and Nihon Keizai (afinancial daily), aswell as Der Spiegel and The Economist. Although none reached the level ofsophistication found in displays of scientific data (a random sample of220 graphics from Science 1978-1980 had 42 percent ofrelational design), itis clearthat some graphical intelligence is possible in news work, at least in Japan and ata few European weeklies.

Table1 Graphical Sophistication, World Press,1974-1980   
![](images/99f53e0e306297dc7214887bef2594b5b405312f8074274b38b9f6305caee9e7.jpg)

Japanese graphical distinction is consistent with thatcountry's heavy use ofstatistical techniques in theworkplace and extensive quantitative training, even in the early years of school:

no nation ranks higher in its collective passion for statistics. InJapan,statisticsarethesubjectofaholiday, local andnational conventions, awards ceremonies and nationwidestatistical collection and graph-drawing contests. "Thisyear," said Yoshiharu Takahashi, a Government statistician, \`we had almost 30,000 entries. Actually, we had $^ { 2 9 , 8 3 6 }$ ”

Entries in the[children's] statistical graph contest were screened three times by judges, who gave first prize thisyear to the work offive 7-year-olds. Their graph creation, titled "Mom, playwith us more often," was theresult ofa survey of32 classmates on the frequency that mothers play with their offspring and the reasons given for not doing SO. Other children' workexamined the frequency of family phone usage and correlated the day'stemperature with cicadasinging.11

Note the relational design of thelast children's graphic mentioned.

Thefive U.S.publications examined rank toward the bottom of theworld list,along with Pravda and a few European papers. Note, inTable1, the complete dominance ofnon-relational designs at the lower-ranked newspapers and magazines. Thisis unfortunate because the relational graphic, unlike the simpler designs,isanexplanatorygraphic- surely anatural for news reporting and analysis.

The statistical graphics found in college and even high school textbooks are moresophisticated than those in news publications. Indeed,grade school children may experience agreater density of relational graphics than someone who reads only Business Week, the New York Times, Time,the Wall StreetJournal,and the Washington Post. Tables 2 and 3 record thegraphical sophistication of textbooks and of a variety of standardized educational tests. A comparison between these dataand Table 1 suggests thatmost news publications outside of Japan operate ata pre-adult level of intelligence ingraphical design.12

Table2 Graphical Sophistication, College and High School Textbooks   
![](images/85a458c8b041529d673bd49b33e38df7ed76049823de1fe47b2012e914ef4080.jpg)

Table3 Graphical Sophistication, Educational Tests   
![](images/d7623efc58a33504bda339710c9a3c38a0b106e1500d0d0674bce22e1ed9fca9.jpg)
\*Graphics collected in JamesR. Beniger, compiler, Selected Standardized TestItems thatMeasure Ability with Graphics (Washington, D.C.: Bureau ofSocial Science Research,1975).

And so,just as there isa double standard of integrity at a good many news publications-one for words, another for graphicsSo there is a double standard of sophistication. The statistical graphics arestupid; the prose is often serious and sometimes even demanding of expertise, as can be seen in these sentences from a single issue of theNew York Times:

Recycling petrodollars may postpone theday ofreckoning,but itseffects would soon become intolerable without a steady depreciation in theirpurchasing power. Floating rates ofexchange cannot restore evena semblanceof equilibrium.

Numerous facetsof the performance seem decidedly unfashionable ifnot downright eccentric:the square-toed instrumental phrasing and the frequent plodding temposin thearias,theRomanticized treatment ofthe chorales, the generous retards at everycadence, the often intrusively elaboratecontinuo improvisationsand an inconsistent attitude toward expression which ranges fromheavingMahlerian emphasestomechanical literalism.

The Court showsno sign ofretreating from its view thata stategovernment isprotected bysovereign immunityagainst court orders topayretroactive damages for past violations.

And Dr. Garth Graham, a medical director with Smithkline Corp., makers of Thorazine,noted thatneuroleptics produce no euphoria, andare therefore unlikelytobeabusedbypatients witha historyof drugoralcohol dependence. "They are,ifanything, dysphorogenic, Dr.Graham said.

# Conclusion

The conditions under which many data graphics are producedthelack ofsubstantive and quantitative skills of the illustrators, dislikeof quantitative evidence,and contempt for the intelligence oftheaudience- -guarantee graphic mediocrity. These conditions engender graphics that (1) lie; （2) employ only the simplest designs, often unstandardized time-series based on a small handful of data points;and (3)miss thereal news actually in the data.

It wastes thetremendous communicative power ofgraphics to use them merely to decorate a few numbers. Moreover, much of theworld these days is observed and assessed quantitatively- 1 -and well-designed graphicsare farmore effective than words in showing such observations.

How cangraphic mediocrity be remedied?

Surely there is something to besaid for rejecting onceand for all the doctrines that data graphics are for the unintelligent and that statisticsare boring. These doctrines blame the victims (the audience and thedata) rather than the perpetrators.

Graphical competence demands three quite different skills: the substantive, statistical, and artistic. Yetnow most graphical work, particularly atnews publications,is underthe direction ofbut a single expertise- 1 the artistic. Allowing artist-illustrators to control the design and content of statistical graphics is almost like allowing typographers to control the content,style, and editing of prose. Substantive and quantitative expertise must also participate in the design of data graphics, at least ifstatistical integrity andgraphical sophistication areto beachieved.

PART II

# Theory of Data Graphics

Everyone spoke of an information overload, but what there was in fact wasanon-information overload.

Richard Saul Wurman, What-If, Could-Be (Philadelphia, 1976)

4 Data-Ink and Graphical Redesign

Datagraphics should draw theviewer's attention to the sense and substance of the data,not to something else. The data graphical form should present the quantitative contents. Occasionally artfulness of design makes a graphic worthy of the Museum ofModern Art, but essentially statistical graphics are instruments to help people reason about quantitative information.

Playfair's very first charts devoted too much oftheir ink to graphical apparatus,with elaborategrid linesanddetailedlabels. This time-series, engraved in August $1 7 8 5$ 0 is from the early pages of The Commercial and Political Atlas:

![](images/6c72fdca5e2ad398bf389636743e0ec3e3c608cc518ba022804f61f688a9d798.jpg)  
CHART of IMPORTS and EXPORTS of ENGLAND to andfrom all NoRTHAMERICA From the Year 1790 to 1782 by W. Playfair   
The Bottom Line is divided into Years the right-handLine into HUNDRED THOUSAND POUNDS J.Ainslie Sculp: Pubjndas the.Actdirects 2oAug 1785.

Within a year Playfair had eliminated much ofthe non-data detail in favor of cleaner design that focused attention on the time-series itself. He then began working with a new engraver and was soon producing clearand elegant displays:

![](images/fc5ffcb391dc6daa7c2881d318a3f4b6f5debcf015ccc6a9e19683c4f770cf3e.jpg)  
The Bottom line is divided into Years, theRight hand line into L10,000 each. Publishedaothe ActdirersMay 1706, $\succcurlyeq$ W. Playfair Neelesapt 352Srad,L

This improvement ingraphical design illustrates the fundamental principle of good statistical graphics:

Above all else show the data.

The principleis the basis for a theory of data graphics.

# Data-Ink

A large share ofink on agraphic should present data-information, theink changing as thedata change. Data-ink is thenon-erasable core ofa graphic, thenon-redundant inkarranged in response to variation inthenumbers represented. Then,

data-ink Data-ink ratio $\mathbf { \tau } =$ total ink used to print the graphic $\mathbf { \tau } =$ proportion ofa graphic's ink devoted tothe non-redundant display ofdata-information $\mathbf { \lambda } = \mathbf { \lambda } _ { 1 . 0 }$ 1 proportion ofa graphic that can be erased without loss of data-information.

A few graphics useevery drop of their ink to convey measured quantities. Nothing can be erased without losing information in these continuous eight tracks of an electroencephalogram. Thedata change from background activity to a series of polyspike bursts. Note the scale inthe bottom block, lower right:

Most ofthe inkin this graphic is data-ink (the dots and labels on thediagonal), with perhaps 10-20 percent non-data-ink (thegrid ticks and the frame):

In this displaywith nearlyall its ink devoted to matters other than data, the grid sea overwhelms thenumbers (the faint points scattered about thediagonal):

![](images/01c449dc3a8fd8a886182e3e416d7dbfc42a367cdb92fbdfe22aa84447a7b589.jpg)  
John Tyler Bonner, Size andCycle: An Essay on the Structure ofBiology (Princeton, 1965), p. 17.

![](images/f92bbd79d5d164dab502355737f4d67a1d3918549b16f3c46d15c3e36635138b.jpg)

Another published version ofthe same data drove theshare of data-ink upto about 0.7,an improvement:

![](images/64a9a3a1d5b198dabb677485f53a604b8f6dcda6b31c55eb73d76f23344ee45a.jpg)  
Relationship of Actual Ratesof Registration to Predicted Rates(104cities 1960).

Buta third reprint publication of the same figure forgot to plot the pointsand simply retraced thegrid lines from theoriginal, including the excess strip of grid along the top and right margins. The resulting figure achieves a graphical absolute zero, anull dataink ratio:

![](images/a0ed7e1b7f2ce34bbb4ce2c034f8d7404187527b5c956d14940e9e917e875b7e.jpg)  
Figure19.1 Relationship of Actual Rates of Registration to Predicted Rates (104cities，1960)   
The threegraphics werepublished in, respectively,StanleyKelley,Jr.Richard E.Ayres,andWilliamG. Bowen, "Registration and Voting:Putting First ThingsFirst," American Political Science Review, 61 (1967), 371; thenreprinted inEdward R.Tufte, ed., The Quantitative Analysis ofSocial Problems (Reading, Mass.,1970)，p 267; andreprinted again in WilliamJ.Crottyedublic Opinion andPolitics: A Reader (New York, 1970),p. 364.

# Maximizing the Share ofData-ink

The larger the share ofa graphic's ink devoted to data,thebetter (other relevant matters being equal):

Maximize the data-ink ratio, within reason.

Every bit ofink on agraphic requires a reason. And nearly always thatreason shouldbe that theink presents new information.

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

The space opened up by erasing can be effectively used. Labels for theinitial elements of each period, an alkali, show the beginning ofeach cycle in theperiodic tableof elements-and in the graphic. Theunusual rare-earths are indicated. In addition, thelabel and numbers onthe vertical axis are turned to read fromleft toright rather than bottom to top,making the graphic slightly more accessible, a little more friendly:

![](images/ffebfcdfada82cb51c2ad7f062a781d4e1ce0d9081ae45c93bdc15834682dc0d.jpg)

# Conclusion

Five principles in the theory of data graphics produce substantial changes in graphical design. The principles apply to many graphics and yield a series of design options through cycles of graphical revision and editing.

Aboveall else show thedata.   
Maximize thedata-ink ratio. Erase non-data-ink. Erase redundant data-ink. Reviseand edit.

Theinterior decoration ofgraphics generates a lot ofink thatdoes nottell theviewer anything new. Thepurpose of decoration varies -to make thegraphic appear morescientific and precise, toenliven thedisplay,togive thedesigner anopportunity to exercise artistic skills.Regardless of its cause, itis allnon-data-ink orredundant data-ink, and itis often chartjunk. Graphical decoration, which prospers in technical publications aswell asincommercial and mediagraphics, comes cheaper than thehard workrequired to produce intriguing numbersand secure evidence.

Sometimes the decoration is thought toreflect theartist's fundamental designcontribution, capturing the essential spirit ofthe dataand so on. Thusprinciples ofartisticintegrityand creativity areinvoked todefend-even to advance-the cause of chartjunk. Thereare better waysto portray spirits and essences than to get themalltangled upwith statistical graphics.

Fortunately most chartjunk doesnot involve artistic considerations. Itis simply conventional graphical paraphernalia routinely added to every display that passes by:over-busy grid linesand excess ticks, redundantrepresentations ofthe simplest data,the debris ofcomputer plotting,and many ofthe devices generating design variation.

Likeweeds, many varieties ofchartjunk flourish. Here three widespread typesfound in scientificand technical research work arecatalogued-unintentional optical art, the dreaded grid, and the self-promoting graphical duck. Ahundred chartjunky examplesfromcommercial and mediagraphics have been forgone SO asto demonstrate therelevance of the critique to theprofessional scientific production ofdata graphics.

# Unintentional Optical Art

Contemporary optical art relies on moire effects,in which the design interactswith thephysiological tremor of theeye to producethe distractingappearanceofvibrationand movement.

![](images/fd84cb65af390ec9d75fdbedcc853e6460b17e8a2b83281d7663975b192ebd21.jpg)

The effect extends beyond theink of thedesign to the whole page. When exploited by the experts,such as Bridget Riley and Victor Vasarely, opart effects areundoubtedly eye-catching.

But statistical graphics are also often drawn upso asto shimmer. Thismoire vibration, probably the most common form ofgraphical clutter,isinevitably badartand bad datagraphics. The noise clouds theflowofinformationas theseexamplesfromtechnical and scientific publications illustrate:

![](images/7a422949c30015cc046f357ba687bd1650574b275b2911fd2ccb7442cd4cf8a0.jpg)  
Instituto deExpansao Commercial,Brasil: Graphicos Economicos-Estatisticas(RiodeJaneiro, 1929)，p. 15.

![](images/3067bfeea8eccf93ad2c90c2ff9b48c66ae0211009b2ab2e3cc78ef099c690bb.jpg)  
Figure2. SerialEchocardiographicAssessmentsoftheSeverity ofRegurgitationinthePulmonaryAutograftin31Patients. Thenumerical gradeswereassignedaccording lotheseverityofregurgitationas follows: 0，none;0.5,trivial；1.0to 1.5,mild;2.0, moderateand3.0，severe

On this page,what should have beensimple tablesare turned into bad graphicspublished inmajor scientific journals. Abovea duck moire withan unintentional Necker Illusion, as thetwo backplanes optically flip to the front. Some pyramids conceal others;and one variable (stacked depth ofthe stupid pyramids) has no label orscale. Below, we learnverylittle about data,butdodiscover thatmoiré vibrationmaywell beat a maximumforequallyspaced bars:

NicholasT.Kouchoukos,etal. "Replacement ofthe AorticRootwith aPulmonary Autograft in Childrenand YoungAdultswith Aortic-ValveDisease," TheNewEnglandJournalofMedicine,330 （January6,1994)，P.4

![](images/fdc5e2ff4c0e56d46d0b3149ac593c27760f87c0a8a4089da03b915fa5af6f44.jpg)  
JamesT.Kuznicki andN. Bruce McCutcheon, "Cross-Enhancementofthe SourTaste on Single HumanTaste Papillae,"JournalofExperimentalPsychology: General, 108 (1979), 76.   
EainM. Cornford and Marie E. Huot, "Glucose Transfer from Male to Female Schistosomes," Science,213 (September 11,1981）, 1270.

And, finally,from the style sheet once provided by theJournal ofthe American Statistical Association, agraphic described as “an example ofa figureprepared in theproper form":

![](images/406eb5672cc139af355d6929e75379a1d2022938e75777a65bf385ee74319130.jpg)

Thedisplay required 131 line-strokesand $^ { 1 5 }$ digitsto communicate itssimple information.Thevibrating lines arepoorly drawn, unevenly spaced, and misaligned withthevertical axis.

Vibrating chartjunk even frequents thegraphics ofmajor scientific journals:

![](images/fd7c2743187ac55e472b370f0aacc24897c71474188475f471a4d48b32a30e14.jpg)

Moire effects haveproliferated with computergraphics(in programs such asExcel).Such unfortunatepatterns were once generated bymeans of thin plastictransfer sheets; now the computer produces instantchartjunk. Shown hereare 3 fewof themany vibrating possibilities. Cross-hatching should bereplaced withtint screensofshadesofgray.Specificareas onagraphic should belabeled with words ratherthanencoded with hatching.

![](images/18a2f5d29d576f3888b54034e18b862c0af004e7af286e72d929ebed17b6c0c6.jpg)

This formofchartjunk isatwentieth-century innovation, and computer graphics aremultiplying it more than ever. Thehandbooks and textbooks ofstatistical graphics, alongwith user'smanuals for computer graphics programs, are filled upwith vibrating graphics, presented asexemplars ofdesign.Note thehigh

proportion of chartjunky graphics in themore recent publications. Computer graphics areparticularly active:

![](images/8f921c675f7d8ee6846968faccd1afa8a413840675542c3219a2d07424cd7775.jpg)

Canoptical arteffects ever produce a bettergraphic? Bertin exhorts:"Itisthedesigner' duty tomake themost of this variation; to obtain theresonance [ofmoiré vibration] without provoking an uncomfortable sensation: to firtwith ambiguity without succumbing to it."1 Butcan statistical graphics successfully "flirtwith ambiguity?Itis a cleveridea, but no good examples aretobe found. Thekeydifficulty remains: moire vibration is an undisciplinedambiguitywith anillusiveeyestrainingquality that contaminates the entiregraphic. Ithasno placein data graphical design.

# The Grid

Oneof the more sedategraphical elements,thegrid should usually be muted orcompletelysuppressed so thatits presence isonly implicit-lest it competewith thedata. Grids aremostly for the initial plotting of data at home or officerather than forputting into print. Dark grid linesare chartjunk. Theycarry no information,clutter up thegraphic, and generate graphic activity unrelated to data information. Thisgridcamouflagestheprofile ofthedatain theage-sex pyramid ofthe population ofFrance in 1967:

![](images/23ead8eb6aaa48044d7f1b027adc68db8b1d39a385db65e985e8c923a34da1ec.jpg)

A revision quiets thegrid and gives emphasis to the data:

![](images/c531be7cb5d0b19a57e7c3da4f2131eb59e937090acf2d9d29a921a0ea9d1006.jpg)  
Based on data in Institut National dela Statistique etdesEtudes Economiques, AnnuairestatistiquedelaFrance 1968 (Paris, 1968),Pp. 32-33； redrawn in Henry S. Shryock and Jacob S.Siegel, TheMethods andMaterialsofDemography (Washington，D.C.,1973）， vol.1,242.

(a) Military losses in World War1   
(b) Deficit 0 births during World War   
(c) MiltaryossesinWorldWar   
(d) Deficit of birthsduringWorld War Il   
(e) Riseof birthsdue to demobilizationafter World Warll

Thespace occupied by the doubledgrid linesconsumes 18percent ofthe area ofthis otherwise mostingenious design, a "multiwindowplot." Optical white dotsappear atthe intersections of thegrid lines.(Theplot shows the following: The large square contains $\mathbf { X } _ { \mathfrak { s } }$ $\mathbf { X } _ { \tau }$ scatterplots forthe indicated levels of $\mathbf { X } _ { \mathfrak { r } }$ and $\mathbf { X } _ { 3 }$ Themarginal plotson therightareconditioned on $\mathbf { X } _ { 3 }$ and the plotsat thetop on $\mathbf { X } _ { 1 }$ Theupper right corner showsthe unconditional $\mathbf { X } _ { 4 }$ $\mathbf { X } _ { 7 }$ scatter.) Redrawing eliminates the vibration:

PaulA.Tukey and John W. Tukey, "Data-DrivenView Selection; Agglomeration andSharpening, inVicBarnett, ed.,InterpretingMultivariateData(Chichester, England,1981),231-232.

![](images/b149c9efd5c21e32c7efde24b3508ff1bc8edfb7460cc62217bfc100aa967959.jpg)  
OF PARTICLE PHYSICS MOMENTUM DATA

Thegrid in the classic Marey train schedule isvery active:

![](images/f4d70a00811ee776411256efc7f389997c6768e1f7640d34130fc045e96e6601.jpg)

Thinning thegrid lines helps 4 littlebit:

![](images/0a3ceabcba456f4e40669a4b8597bc7c54bea8fefb16c39efca361f50665605b.jpg)

A better treatment, however, is a gray grid:

![](images/10143486c22fdf9b4a4b6d4189547e04bd8f9ebc8a01b5640da2dc42f5427abb.jpg)

When agraphic serves as a look-up table, thenagrid mayhelp in readingand interpolating. But even in this case thegrids should bemuted relative to the data. A gray grid works well and, with a delicate line,may promote more accurate data reconstruction thana dark grid.

Most ready-made graph paper comes with 3 darkly printed grid. The reverse (unprinted) side should beused, forthen the lines show through faintly and do not clutter thedata. If the paper is heavily gridded on both sides, throw it out.

# Self-Promoting Graphics: The Duck

When agraphic is taken overby decorative forms or computer debris, when thedata measures and structures become Design Elements, when the overall design purveys Graphical Style rather than quantitativeinformation, then that graphic may be called a duckin honor of theduck-form store,"Big Duck. 17 For this building the whole structureis itself decoration, justasin theduck data graphic. In Learning fromLas Vegas, RobertVenturi, Denise Scott

Brown,and Steven Izenour write about theducks ofmodern architecture-and their thoughts are relevantto the design ofdata graphics aswell:

When Modern architects righteously abandoned ornament on buildings, they unconsciously designed buildings that were ornament. In promoting Space and Articulation over symbolism and ornament, they distorted the whole building into a duck. They substituted forthe innocent and inexpensive practice ofapplied decoration on a conventional shed the rathercynical and expensive distortion of program and structure to promote a duck. Itis now time toreevaluate the once-horrifying statement ofJohn Ruskin that architecture is the decoration of construction, but we should append the warning of Pugin: It is all right to decorate construction but never construct decoration.2

![](images/35206b8f6b0779349fbcce41af6458586fcd58ac34814c1a645f4d8a640b866c.jpg)  
2RobertVenturi, Denise Scott Brown, and Steven Izenour, Learningfrom Las Vegas (Cambridge,revised edition, 1977),p. 163.Theinitial statementof the duckconcept is found onpp.87-103.

BigDuck, Flanders, New York;photograph by Edward Tufte,July2000.

The addition ofa fake perspective to the data structure clutters many graphics. This variety of chartjunk, now athigh fashion in the world of Boutique Data Graphics, abounds in corporate annual reports, the phony statistical studiespresented in advertisements, themass media,and the more muddled sorts of social science research.

A seriesof weird three-dimensional displays appearing in the magazine American Education in the 1970s delighted connoisseurs of the graphically preposterous. Here five colors report, almost by happenstance, only five pieces of data (since the division within each yearadds to 100 percent). This may well be the worst graphic ever to find itsway into print:

![](images/c06487b9ef8294aed789895e9b526f8cc3e1849fc8cf032a9892061d30d70616.jpg)

There are some superbly produced ducks:

![](images/bb54568811b956fd4ae44ffabe91f5fcbdbebad530280e3d4d455c5db9ea5e38.jpg)

Occasionally designers seem to seek creditmerely for possessing anew technology, rather than using it to make better designs. Computers and their affiliated apparatus can dopowerful things graphically, in part by turning out thehundreds of plots necessary for good dataanalysis. Butatleasta few computer graphics only evoke the response“Isn’t it remarkable that the computer can be programmed to drawlikethat?" instead of"My,what interesting data."

The symptoms of the We-Used-A-Computer-To-Build-A-Duck Syndrome appear in this display from a professional journal: the thin substance;the clotted,crinkly lettering allin upper-case sans serif; the pointlessly ordered cross-hatching; the labels written in computer abbreviations; the optical vibration-all thesethe by-products of the technology of graphic fabrication. The overly busy vertical scaling shows more percentage markers andlabels than thereareactual data points. Theobserved values ofthe percentages should be printed instead. Since the information consists ofa few numbers and a good many words, it is best to pass up the computerized graphicscapability thistime and tell the story with a table:

![](images/d4bf13a547ec6de425e9e85b46feedeadc27b5105450e19552f0adce12898aa8.jpg)  
ArthurH. Miller, EdieN. Goldenberg, and Lutz Erbring, "Type-Set Politics: Impactof Newspaperson Public Confidence," American Political Science Review,73 (1979), 67-84.

![](images/9d4204a17781cf197c6241a8d307ed4a18383aa553972df1310441456c5d9962.jpg)

# Conclusion

Chartjunk doesnot achieve the goals of its propagators. The overwhelming fact of data graphicsis that they stand or fall on their content, gracefully displayed. Graphics donot become attractive and interesting through the addition ofornamental hatching and false perspective to a few bars. Chartjunk can turn boresinto disasters, butit can never rescue a thin dataset.The best designs (for example,Minard onNapoleoninRussia,Marey's graphical train schedule, the cancer maps, the Timesweather history ofNew York City, the chronicle of the annual adventures of theJapanese beetle,thenew view of the galaxies) areintriguing andcuriosity-provoking, drawing the viewerinto thewonder ofthe data, sometimes by narrative power,sometimes by immense detail, and sometimes by elegant presentation ofsimple but interesting data. Butno information, no sense of discovery, no wonder, no substance isgenerated by chartjunk.

Forgo chartjunk, including moire vibration, the grid,and the duck.

Painting is special, separate, a matter of meditationand contemplation, for me, no physical action or social sport. Asmuch consciousness as possible. Clarity,comleessesseetse, no schmutz, no schmerz, no fauve schwarmerei. Perfection,passiveness, consonance, consummateness. No palpitations, no gesticulation, no grotesquerie. Spirituality, serenity, absoluteness, coherence. No automatism, no accident, no anxiety, no catharsis, no chance. Detachment, disinterestedness, thoughtfulness, transcendence. No humbugging, no button-holing, no exploitation, no mixing things up.

Ad Reinhardt, statement forthecatalogueof theexhibition, "TheNewDecade: 35 American Paintersand Sculptors,' Whitney Museum ofAmerican Art, NewYork,1955.

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

Encoding ofdatameasures can be farmore elaborate. The plotted points hereare Chernoff faces,which reduce well,mintaining legibility even with individual areas of.os square inches as shown.3The analystwould observe thestandard X-Y scatterplot and then turn to thewithin-scatter detail, seeking clusters of similar observations over the X-Y plane. Outlying faces and those inconsistent with others in the neighborhood-they are,of course, strangers -should be identified by observation number or name.

![](images/da143c436c4f69a2ee1e45bda634f0d73433c4d0119cb00aa61124ec1a59d09d.jpg)  
3Herman Chernoff, "The Use of Faces toRepresent Points in k-Dimensional SpaceGraphically,"Journal oftheAmerican Statistical Association 68 (June 1973), 361-368. Foranapplication of faceslocated overtwo dimensions, seeHoward Wainerand David Thissen,"Graphical Data Analysis,' Annual Review ofPsychology, 32 （1981）,191-241.

With cartoon facesand even numbers becoming data measures, we would appear to have reached the limit of graphical economy of presentation, imagination, and, let it be admitted, eccentricity.

Butlet Ls consider thisshaped poem, "Easter Wings”by George Herbert (1593-1633)，which uses space- thelength of each lineto depict quantity, all done 150 years beforePlayfair.4 Thelines double-function: the longer lines describe wealth, plenty, largesse, and rising to fight; shorter linestell of poverty and becoming \`most thinne"; and lines of intermediate length indicate transition and change (decaying, rising,combining, becoming):

# Easter-wings.

Ord, who createdst man in wealth and store,   
Though foolishly he lost the same,   
Decaying more and more,   
Till he became   
Most poore:   
With thee   
O let me rise   
As larks,harmoniously,   
And sing this day thy victories:   
Then shall thefall further theflight in me.   
My tender age in sorrow did beginne:   
And still with sicknessesand shame   
Thou didst So punish sinne,   
That I became   
Most thinne.   
With thee   
Let me combine   
And feel this day thy victorie:   
For, if I imp, my wing on thine,   
Afliction shall advance the flight in me.

And the typographical delight ofthe statistician W.J. Youden:

THE NORMAL LAW OF ERROR STANDS OUT IN THE EXPERIENCE OFMANKIND AS ONE OF THE BROADEST GENERALIZATIONS OF NATURAL PHILOSOPHY IT BERVEB AS THE GUIDING INSTRUMENT IN RESEARCHES IN THEPHYSICALAND SOCIALSCIENCES AND IN MEDICINE AGRICULTURE AND ENGINEERING 专 IT18 AN INDISPENSABLE TOOL FOR THE ANALYSIS AND THE INTERPRETATION OF THE BASIC DATA OBTAINED BY OBSERVATION AND EXPERIMENT

4For a remarkable OTSOG-liketour of the many typographical variant shapes of"Easter Wings' inits long publication history, see the essay "FIATfLUX, by "Random Cloud”inRandall McLeod, ed.,Crisis in Editing:TextsoftheEnglish Renaissance (New York, 1994), 61-172.

Finally, this graphical pun: the visual dataas thedata measure, asin the living histogram. Thechart shows how states once differed in their engineering standards for painting lane stripes on road pavement. Some states marked theroad laneswith short dashes and long gaps;others used only solid lines. Portrayed in the graphic is the actual physical pattern painted on the road, with $4 8 \ \mathrm { U } . 5$ states ordered by the length of the painted mark:

California   
Missouri   
Minnesota   
Alabama   
Arizona   
Colorado   
Florida   
Georgia   
Kentucky   
Louisiana   
Maine   
Massachusetts   
Misssippi   
Nebraska   
Nevada   
NewHampshire   
NewMexico   
NewYork   
North Carolina   
Oregon   
Pennsylvania   
Washington   
Delaware   
Iowa   
Wyoming   
Connecticut   
Vermont   
Wisconsin   
Rhode Island   
Kansas   
WestVirginia   
Idaho   
Michigan   
Arkansas   
North Dakota   
Maryland   
Montana   
Virginia   
South Carolina   
New Jersey   
Illinois   
Indiana   
Ohio   
Oklahoma   
South Dakota   
Tennessee   
Texas   
Utah

![](images/0d5f5e807843969d85f77bacc626444c67afe8cd94da55161599501acb37cd97.jpg)  
Redrawn fromA.R. Lauer, "Psychological Factors in EffectiveTraffic Control Devices,' TrafficQuarterly,5 (January 1951), 94.

# feet

# Data-Based Grids

Very occasionally thegrid can report directly on the data. This grid is formed by the location ofmeasurement instruments; the plain dots register a zero reading,in contrast with the white background where no readings were taken. Erasing the grid would erasemeasured data (ratheruneventful, to be sure). Such is not thecase for most grid dots, ticks,and lines.

![](images/78d6ad8b087e8629374b54486866db7b1d16f01c1dc89770d20df6027a067e52.jpg)  
K.V. Robertsand D. E. Potter, "Magnetohydrodynamic Calculations, in Berni Alder, etal., eds.,Methods in Computational Physics:Volume9,Plasma Physics (NewYork, 1970), P. 402.

Thearrangement ofdata in this table-graphicyields an internal grid, a rare example of data as grid:

![](images/63fbe85cfcc00bd024b3eb9baa105b78cac276336887c50d5cef07b91d8d0d60.jpg)  
Karl Pearson, TheLife, Letters andLaboursofFrancis Galton (Cambridge, 1930), vol.I-A,14.

Here thegrid is the element of interest, rather than the map.

![](images/b22eaebd45f6a7e67f5938cf256972d7cfd071dd627a723f5b7211976ace970f.jpg)  
LesterJ.Cappon, Barbara Bartz Petchenik,and John Hamilton Long,Atlasof EarlyAmerican History (Princeton,1976), P.58.

Thegrid that follows presents the data on the surface of the rock; on the sides, the grid isconventional. Thetwo displays compare theeffect ofreligion, taking into accountparty affiliation, on a person's vote forpresident in1956 and in 1960 (when a Catholic ran for president). Note thereis no reliable slope associated with religion in 1956, onceparty iscontrolled; in 1960, a systematic effect is found.Reading the slopes in the other direction shows the persistent effect of party in both elections:

PhilipE.Converse, "Religion and Politics:The196o Election," in Angus Campbell, PhilipE. Converse, Warren E.Miller,andDonaldE.Stokes, Elections andthePolitical Order (NewYork, 1966), 102-103.

![](images/c0a9e754b590511628aac3beb95060ebcee1dad10ac2d5c307821824b1e8798b.jpg)

Playfair tied thegrid to the data in his skyrocketing debt graphic. Although the implicit plotting coordinates are based on regular intervals, thevertical grid linesin the published version are irregularly spaced, keyed to significant events The data-based grid is a shrewd graphical device, serving rather than fighting with the data. It is a technique underused in contemporary graphical work.

![](images/10650658787476fd51a7f5bec62ace6611d60d1fd1387bba6213dc21bf2efe8a.jpg)

# Double-Functioning Labels

Data-based coordinate lines lead to data-based labels, as, for example, at the bottom of Playfair's debt graphic. Again, the issue is the same: why not use theink to show data? Beginningwith conventionally labeled frame

![](images/8fd19e353a105cf8f43e9e7aef90800a0be76c8b53818c21dc07234433bb10d7.jpg)

and erasing to therange-frame

![](images/c56e3c1eb3f858ddc5e296873e0b659b1bcce303a637a8589049edd47b01c065.jpg)

leaves those lonely ticksand numbers out on thetails, working to help the eye get a better reading on where the line of the rangeframe ends. But that job can be done better by investing thesame ink in data: rather than showing the minimum round number and the maximum round number at the ends ofthe frame, show theactual minimum and maximum realized in thedata:

![](images/56b79ec13bd33eccc4fa63d72cb30477376131312649c12c08b78f1331c87299.jpg)

With itsgreater precisionand two tick-marks less of non-dataink,the range-frame with range-labels is superior to the rangeframewith round number labels. Both improve on the standard, passive frame.

Numbersalso double-function when used both to name things (like an identification number) and to reflect an ordering. Inthis graphic (in which the circled numbersfail to double-function), each number identifies a particular study of the thermal conductivity of tungsten, ordered alphabetically by the last name ofthe first author. If that list were ordered by date of publication instead, then the codewould also indicatethetimeorder inwhich thevarious conductivity determinations were made. Thus"1" would indicate theearliest study,and so on-or,alternatively, "61c” would bethethird studypublished in 1961. Such information has interest, since we could see which of the early studies got the right answer. In addition, the movement of the studies toward the"correct’recommended values could be tracked. This extra information requiresno additional ink.

![](images/3d97f74557554525a11bf3946b50ebc1300cde955b6ea866fefc2ef705d46801.jpg)

In mostgraphics, the coordinate labels are far from thedata measures. Consequently the eye ofthe viewermust move back and forth between the path formed by thedataand thecoordinate positions arrayed along the margins of the graphic. Sometimes this eye-work can beeliminated entirelyby turning the coordinate labels into datameasures, another double-functioning maneuver. Take the example from the style sheet of the Journal ofthe American Statistical Association:

![](images/2e87be7de14df7490406f18203dddb9803bb42f60862162f0228ed9c83748813.jpg)

The grid increments ofthe X-axis are relocated upward to mark the path ofthedata:

.15   
.10   
.05 中   
.00 67891011 12 131415

And since theissue in this display is the probability ateach integer value, theround-number Y-scale isreplacedby exact values:

.177 0

The Y-scale nowresembles the dashes ofthe dot-dash-plot, with the vertical column of data-positioned numbers serving as the dashes to indicate themarginal distribution.

The method ofdata-based markers for the marginal distributions suggests a further enhancement of the dot-dash-plot:

![](images/492d882d69edffdc124319cc996b906c203fa25d37d07efe5e015c50fc5d0eec.jpg)

Now thenumbers in themargin eliminate thestandard frame and even arange-frame, replacethe coordinate ticks, show the marginal distribution ofboth variables, and record the exact values ofthe two measurements made on each unit ofobservation. This graphical arrangement performs better for smaller data sets (say 30 observations or less)and when afinelevel ofdetail isrequired.

Finally, a striking design with data-based labels:

![](images/325bb615869cbfb51be3b3f69dc2b3fa625a4e3001e293441c0da1268433702e.jpg)

# Puzzles and Hierarchy in Graphics

Thecomplexity ofmultifunctioning elements can sometimes turn data graphics into visual puzzles,crypto-graphical mysteries for theviewer to decode. A sure sign ofa puzzle isthat thegraphic must be interpreted through a verbal rather thana visual process.

For example,despiteitscleverand multifunctioning datameasure, formed by crossing two four-color grids, this isapuzzle graphic. Deployed here, in a feat of technological virtuosity,are 16shades of colorspread on 3,056 counties, a monument to a sophisticated computer graphics system.5 But itis surely agraphic experienced verbally, not visually. Over and over, the viewers must run little phrases through their minds, trying to maintain theright pattern ofwords to make sense out of thevisual montage: "Now let's see, purple represents counties wherethereare both high levels ofmale cardiovascular diseasemortality and11.6to $\scriptstyle 5 6 . 0$ percent ofthe households have more than 1.01 personsper room. What does thatmean anyway? And the yellow-green counties. By contrast, in anon-puzzle graphic, thetranslation ofvisual toverbal isquickly learned, automatic, and implicit -so that the visual imagefows right through the verbal decoder initially necessary tounderstand the graphic. As Paul Valéry wrote, "Seeing is forgetting the name ofthe thing one sees. ,7

![](images/b85dabcd84891dabd1e6516bb3065faadc2e8977ba3b06def2ab3b96ba75b5d9.jpg)  
5The technique is described in Vincent P. Barabba and AlvaL. Finkner, "The Utilization ofPrimary Printing Colors inDisplayingMorethanOneVariable, inBureau oftheCensus,TechnicalPaper No.43, GraphicalPresentationofStatistical Information (Washington,D.C.,1978), 14-21.The mapsareassessed inHoward Wainer andC.M. Francolini, "An Empirical Inquiry Concerning Human Understandingof Two-Variable Color Maps,' American Statistician, 34(1980）, 81-93.

Color often generates graphical puzzles. Despite ourexperiences with the spectrum in science textbooks and rainbows, themind's eye does not readily give a visual ordering to colors, except possibly for red to reflecthigherlevels than other colors, asin the hot spots of the cancer map. Attempts to give colors an order resultin those verbal decodersand themumbling oflittlemental phrasesagain-inded, even mnemonicphrases about the phrases required for graphical decoding:

Amethod ofcoloring ingenious in ideabut not very satisfactory in practice was used byL.L. Vauthier. It was called the mountain-to-the-sea method. White wasused for the representation ofthegreatest intensity ofthefact because it indicated the summit ofa mountain with itseternal snow, next came green representing the forests farther down the slopes,then yellow for the grain of theplains,and finally for theminimum the blue of the waters at sea level.

Because they do havea natural visual hierarchy, varying shades of gray show varying quantities better than color. Ten gray shades worked effectively in the galaxies map:

![](images/63b4b895a0ded0b76aa9fba3ab6ce0059f71dddea759b5565eb88098cfbf829c.jpg)  
${ } ^ { 6 } \mathrm { H } .$ Gray Funkhouser, "Historical Development of the Graphical RepresentationofStatistical Data, Osiris,3 (1937), 326, who cites E. Cheysson, "Lesmethodesdestatistique graphiqueal'Exposition universellede 1878,"Journal dela Societede Statistique deParis,19 (1878), 331.

The success of gray compared to the visually more spectacular color gives us a leadon how multifunctioning graphical elements can communicate complex information without turning into puzzles.The shades ofgray provide an easily comprehended order to thedata measures. Thisis the key. Central to maintaining clarity in the face of the complex are graphical methods that organizeand ordertheflowofgraphicalinformation presented to the eye.

How cangraphical architecture promote theordered, sequenced, hierarchical flow ofinformation from the graphic to themind's eye?How can the data-information bearranged so that the viewer isableto peel back layerafterlayerofdatafrom a graphic?

Multiple layersof information arecreated bymultiple viewing depths and multiple viewing angles.

Graphics can bedesigned to haveat leastthree viewing depths: (1) whatis seen from a distance,an overall structure usually aggregated froman underlying microstructure; (2) what is seen up close and in detail, the fine structure of the data; and (3) what is seen implicitly,underlying the graphic- that whichis behind the graphic. Look atall thedifferentlevelsofdetail created by this population density map of the United States, a glory of modern cartography prepared by the Bureau of the Census. Each dot, except in urban centers, represents soo people. Note the corridors connecting the major urban complexes; theeffects of landforms on the population distribution (the central valley of California, the valleys and ridges of Appalachia, and the clusters along rivers); and the small towns along the highways,linked likea string of pearls. The map arrays, in effect, some 400,000 points onits implicitgrid.

Different visual angles for different aspects ofthedata also organize graphical information. Each separate line of sight should remain unchanging (preferably horizontal or vertical) as the eye watches for data variation off thefat of the line of sight. For multivariatework,several clear lines can becreated. Recall Ayres' display of American divisions in France. Even with its complex, interwoven data, the graphic is not apuzzle. Three separate visual angles make theflow ofinformation coherent: theprofile ofthe horizon for the upward-moving time-series, thevertical forthe composition of thebar,and the horizontal foreach division's stay. Thus while every drop of ink serves three different data display functions,each ofthe three comes to the eye with itsown independence and integrity.

55324422621 755324422621 030362742835273632422621 55 5   
26 26 442521 442621 21226 3222621 282   
22 2 2   
111   
mJlAng Sep Oct Hov Ded Jn Pab MnT Apr Mny Jm Jul Ang Sop 0ot   
1917 1918

![](images/3126bc6d81b558fba1d03722e0e33497e31afe483d0ddb545272ca3365ba8d7f.jpg)

Current Receipts ofGovernment asa Percentage of Gross Domestic Product, 1970 and 1979

![](images/eed47d2a7d996ba9abfd0cd0a2d2478ba5c511d81f7beb55cbd3710d2ad2ecb8.jpg)

Similarly, this table-graphic organizes datafor viewing in several directions. The chart, whenread vertically,ranks 15 countries by government tax collections in 1970 and again in 1979,with the names spaced in proportion to the percentages. Across thecolumns, the paired comparisons show how the numbers changed over the years. The slopes are also compared by reading down the collection oflines, and lines ofunusual slope stand out from the overall upward pattern. Theinformation shown is both integrated and separated: integrated through itsconnected content, separated in that the eye followsseveral different and uncluttered pathsin looking over thedata:

丰

Such an analysis ofthe viewing architecture ofa graphic will help in creating and evaluating designs that organize complex information hierarchically.

Iwanttoreach that state of condensation ofsensations which constitutes apicture.

Henri Matisse

# 8 Data Density and Small Multiples

Our eyes can make a remarkable number of distinctions within a small area. With theuse of very light grid lines, itis easy to locate 625 points in one square inch or, equivalently, 100points in one square centimeter.

Or consider how an 8oby 80grid over asquareinch- -about 30   
by 30 over asquare centimeter-divides the space:1

With thehelp ofconsiderable redundancy and context, oureyes make fine distinctions of this sortallthe time. Measurementinstruments used in engineering,architectural, andmachine workare engraved with scales of20 increments to the centimeter andso to the inch. Orconsider thereading of fine print. The type in the U.S. Statistical Abstract is setat 12 lines pervertical inch, witheach line running at about23 characters per inch fora maximum density of276 characters per square inch. The actual density, given thewhite space, isin thiscase $^ { 1 8 5 }$ characters per square inch or 28 per square centimeter.

No. 1450. STEEL PRODUCTS-NET SHIPMENTS, BY MARKET CLASSES: 1960 TO 1978 [Inthousands of short tons. Comprisescarbon,alloy,andstainlesssteel."N.e.c."meansnot elsewhere elassified]   
![](images/15e5a30a1871e54a6ed056bab16614225766598a532b01bbdbd928643944080c.jpg)
1 Total ineludes nonclassifed shipmentsand,beginning1970 data include estimates for a relativelysmall number Ineludesrailways,apid transit systems,rilroadralls,trackwork,and equipment. ofcompanieswhichreport raw steel production but not shipments. Bolts,nuts,rts,d ews

![](images/d2438c9c3af15eec423b3c7424d22615ec5eee46ed6784c22a92dd4befe33c15.jpg)  
25,281 distinctions   
U.S. Bureau ofthe Census, Statistical AbstractoftheUnitedStates:1979 (Washington,D.C.,1979), P. 822.

$^ { 1 } \mathbf { A }$ square grid formed on each side by nparallel black andn-1parallel white lines contains $\scriptstyle \mathtt { n } ^ { 2 }$ intersections oftwo blacklines (corners ofsquares), $( n - 1 ) ^ { 2 }$ 号 intersections oftwo white lines (white squares),and $2 \mathrm { n } ( \mathrm { n } { - } 1 )$ intersections ofa black and white line (sides of squares), foratotal of $( 2 n - 1 ) ^ { 2 }$ line intersections or distinct locations.

Mapsroutinely present even finer detail. Acartographer writes that"the resolving power ofthe eyeenables itto differentiate to $0 . 1 \ \mathrm { m m }$ where provoked to do so. Clearly, therefore, conciseness is ofthe essenceand high resolution graphics are a common denominator ofcartography."2 Distinctions at0.1 mm mean 254per inch.

Howmany statistical graphics take advantage ofthe ability ofthe eyeto detect large amounts of information in small spaces? And howmuch information should graphics show?Let us beginby considering an empirical measure of graphical performance, the data density.

# Data Density in Graphical Practice

Thenumbers that go into agraphic can be organized into a data matrix ofobservations by variables. Taking into account the size of the graphic in relation to theamount ofdatadisplayed yields thedata density:

number of entries in data matrix data density ofa graphic $\ l =$ area ofdata graphic

Data matricesand data densities vary enormously in practice. At one extreme, this overwrought display (originally printed in five colors) presents a data matrix offour entries, the namesand thenumbers for the two barson theright. Theleft bar is merely the total ofthe other two. The graph covers26.5 square inches (171 square centimeters),resulting ina data density of.15numbers persquare inch (.02 numbers per square centimeter), which is thin indeed.

![](images/f7b486c1439c7683582b7b3b2ad8ac0fec214b923711ddbea1965a5fc64a60d8.jpg)

Theexemplar from theJASA style sheet comes in ata lightweight3.8 numbers per square inch (0.6numbers per square centimeter) and a small data matrix of32 entries:

![](images/b043d06e2b42f9a94b21dcb5f75fa3d68d19be9570042dcb3da8b1dde6c1db18.jpg)

In contrast, theNewYork weather history, in this reduced version, does verywell at $^ { 1 8 1 }$ numbers per square inch (28per square centimeter):

![](images/639c19430a7f35449d22cd878ef4a80d6c5febed33c842c73c67eb0348bf5702.jpg)

Anannual sunshine record reports about1,000 numbers per square inch (160 per square centimeter):

![](images/6334c4234a1fac93e580a02b48052881954d50140cb67374624dbaec8912a9a8.jpg)  
F.J.Monkhouse andH.R. Wilkinson, Maps andDiagrams(London, third edition, 1971),pp. 242-243.

Thevisual metaphorcorresponds appropriately to thedata if the image is reversed, So that the light areas are the times when the sun shines:

![](images/b65b73015403c897fc05ee2756a03a640cd9a1566f0929b7b615a2c1ba70b70e.jpg)

![](images/5aa3b41befc7e3b2e608098e4e447ecf45cfbca835fd44c3ea4049715eaeaf43.jpg)  
Graphique1973)，p.152.

Thismap (27 square inches, 175square centimeters) showsthe location and boundaries of30,000 communes ofFrance. Itwould requireat least 240,000 numbers torecreate thedata of the map (30,000 latitudes, 30,000 longitudes, and perhaps six numbers describing the shape of each commune). Thus thatdata density isnearly 9,000 numbers persquare inch, or1,400 numbers per square centimeter.

Thenew map ofthegalaxieslocates2,275,328 encoded rectangles ona two-dimensional surface of61 square inches (390square centimeters). Each rectangle represents three numbers (two by its location, one by its shading), yielding a data density of110,000 numbers persquare inch or17,000 numbers persquare centimeter. Thatis the current record.

![](images/a9f49070b5c755773574224f0afb5499edbe295aaec21180094ca12ba9941b48.jpg)

# Data Density and the Size of the Data Matrix: Publication Practices

Thetable shows the data density and the size of thedata matrix for graphics sampled from scientific and news publications. Atleast 20graphics fromeach publication wereexamined.

Thetable recordsan enormous diversity of graphical performances both within and between publications. Afewdata-rich designs appearinnearly every publication. The opportunity is therebut itis rarely exploited: the average published graphic israther thin, based on about 5o numbers shown at the rate of 10 per square inch. Among the world’s newspapers,the Wall StreetJournal, The Times (London), and Asahi publish data-rich graphics,with data densities equal to those of theJournal ofthe American Statistical Association. Mostof the American papers and magazines, along with Pravda, publish less data per graphic than the major papers ofother industrialized countries.

Data Density and Size ofData Matrix, Statistical Graphics inSelected Publications, Circa 1979-1980   
![](images/4de17fd7cb9ded1d188a16bd9be96f3fd11a5eca1ebb2880cd86e657460e68a0.jpg)

Very few statistical graphics achievethe information display rates found in maps. Highly detailed maps portray 100,000 to 150,000 bits per square inch. Forexample, the averageU.S. Geological Survey topographic quadrangle (measuring 17by 23 inches) is estimated to contain over100million bits ofinformation, or about25o,ooo per square inch (40,000 per square centimeter).3 Perhaps some day statistical graphics will perform as successfully as maps in carrying information.

# High-Information Graphics

Data graphics should oftenbebased on large rather than small data matricesand have a highrather than low data density. More information is betterthan less information, especially when the marginal costs of handling and interpreting additional information are low,as they are for most graphics. The simple things belong in tables or in the text;graphics can givea sense oflarge and complex data sets that cannot bemanaged in any other way. If thegraphic becomes overcrowded (although several thousand numbersrepresented may be just fine),a variety ofdata-reduction techniques-averaging, clustering,smoothing-can thinthe numbers out before plotting.4 Summary graphics can emerge from high-information displays,but there isnowhere togo ifwebegin with a low-information design.

Data-rich designs give a contextand credibility to statistical evidence. Low-information designs are suspect: whatis leftout, whatis hidden, why are we shown so litte?High-density graphics help us to compare parts ofthe data by displaying much information within theview of the eye: we look at onepage ata time and the more on the page, themore effectiveand comparative oureye can be.5 The principle, then,is:

Maximizedata densityand the size ofthedata matrix, within reason.

High-information graphics mustbedesigned with special care. As the volumeofdata increases, datameasures must shrink (smaller dots for scatters, thinner lines for busy time-series). Theclutter of chartjunk, non-data-ink, and redundant data-ink iseven more costly than usual in data-rich designs.

The way to increase data density other than by enlarging the data matrix is to reduce the area ofa graphic. The Shrink Principle has wide application:

Graphics can be shrunk way down.

Many data graphics can be reduced in area to half their currently published sizewith virtually no loss in legibility and information. For example, Bertin's crisp and elegant line allows the display of 17 small-scale graphics on a single page along with extensive text. Repeated application ofthe Shrink Principleleads to a powerful and effective graphical design,the small multiple.

![](images/eb4671b679e19f8e0c735f3d1e5fcfa796f03aa9cae47d6535e0fa9853978e06.jpg)

Jacques Bertin, Semiologie Graphique (Paris, second edition, 1973),p.214.

# PROBLEMES GRAPHIQUES POSES PAR LES CHRONIQUES

Untotal surdeux cases(sur deux ans) doitetre divisepardeux (1).   
Untotalpour SiX moisseramultiplie pardeux dans des cases annuelles. Courbestrop pointues, reduirel'echelle desQ; la sensibilite angulaire s'inscrit dans une zone moyenne autour de 70.   
Si la courbe n'est pas reductible (grandes el petitesvariations) employer les colonnes remplies(5).   
Courbes tropplates augmenterl'echelledesQ.

Variationstresfaiblesparrapportautotal. Celui-ci perd del'importance et le zero peut etre supprime, a condition que le lecteur voit sasuppression(9).Legraphiquepeutetre interprete comme uneacceleration sil'etudefine des variationsestnecessaire(echellelogarithmique (10)(v.p. 240).

Tresgrande amplitude entreles valeurs extremes.Il fautadmettre ：   
10) Soit de ne pas percevoir les plus petites variations.   
20 Soit de ne s'interesser qu'aux differences relatives(echellelogarithmique)sans connaitre la quantite absolue.   
30） Soit admettre des periodes differentes dansla composante ordonnee et les traiter a desechelles differentesau-dessus de T'echelle commune (12).

Cyclestres marques.

Sil'etudeporte surla comparaison desphases de chaque cycle, i est preferable de decomposer(13) de manierea superposer les cycles (14).Laconstructionpolairepeutetre employee. depreferencedansuneformespirale(I5)(nepas commencerparun troppetit cercle);pourspectaculaire quelle soit, elle est moins efficace que laconstructionorthogonale.

Courbesannuellesde pluie ou detemperature. Uncycle possede deux phases (17). pourquoi n'en offrir qu'une a la perception du spectateur？(16).

# Small Multiples

Small multiples resemble the frames ofa movie: aseries of graphics, showing the same combination ofvariables, indexed by changes in another variable. Twenty-three hours ofLos Angeles air pollution areorganized into this display, based on a computer generated video tape. Shown is the hourly average distribution of reactive hydrocarbon emissions. The design remains constant through all the frames, SO that attention is devoted entirely to shifts in thedata:

From video tape byGregoryJ.McRae, California Instituteof Technology. Themodel is described inG.J.McRae, W. R. Goodin, andJ.H. Seinfeld, "Development ofaSecond-Generation Mathematical Model for Urban Air Pollution. I. Model Formulation," Atmospheric Environment, 16 (1982), 679-696.

![](images/22d2ffb98661e71d02ad3fea86c4b0bd33e73831f9cb90cd63c323b9e8ed8dd8.jpg)

These grimsmall multiples show the distribution of occurrence ofthe cancermelanoma. The sites of269 primary melanomas are recorded, along with the distribution between menand women. Note thedata graphical arithmetic, similar to that ofthe multiwindow plot.

![](images/b65df1a3ef70f40a95a4675e3f22ac6ce9ff254a6c7b2fcff16ac9a3150ec14b.jpg)  
Abb.1. Verteilung von 269 primaren Melanomen auf Kopf undHals

![](images/ddf2e99d1683c8798c5556fb85aaa57b0190cc1c7f70ef5e449e9d68030d9bf0.jpg)  
Abb. 2 u.3. DifferenzierungderMelanomverteilung nach Geschlechtern

Arthur Wiskemann, "ZurMelanomentstehungdurch chronische Lichteinwirkung, DerHautarzt, 25 (1974), 21.

Theeffects of sampling errors areshown in these 12 distributions, each based ona sample of50 random normal deviates:

社金公会会室

These six distributions show the age composition of herring catches eachyear from 1908 to 1913. A tremendous number of herring were spawned in 1904,and thatclass began to dominate the 1908 catch as four-year-olds, then the 1909catch as five-year-olds, and SO on:

![](images/3427769c0403392460cbde44f0a356afb7b263ec9d83f647eb31e7d4a2a0ea59.jpg)  
EdmondA.Murphy,"One Cause? Many Causes?The Argument from the BimodalDistribution, Journal of   
Johan Hjort, "Fluctuations in theGreat Fisheries ofNorthern Europe, Rapports etProces-Verbaux,20 (1914),in Susan Schlee,The Edge of an UnfamiliarWorld (NewYork,1973）, P.226.   
JorgeJ.Yunis and Om Prakash, "The Origin ofMan:A Chromosomal PictorialLegacy,' Science, 215 (March19, 1982),1527.

Thisnext design compares a complex set ofdata: shown are the chromosomesof(fromleft to right) man, chimpanzee, gorilla, and orangutan. The similarities between humansand the great apes are to benoted.

![](images/994ae932c8fcc4a6be6a3e82dd337dd88a2d78c21bdd439ec08386cfcd1953d7.jpg)

And, finally, a visually similar small multiple, the Consumer Reportsfrequency-of-repairrecords forautomobiles built from 1976 to 1981. Thisis aparticularly ingenious mix oftableand graphic, portraying a complex setofcomparisons between manufacturers, types ofcars, year,and trouble spots.

Consumer Reports, 47 (April1982）, 199-207. Redrawn.

$0$ Muchbetterthanverage =Better than average O=Average 6 Worse than average Muchworse than average

ChevroletMalibu, ChevroletMonza4 Datsun210,B210 TroubleSpots Ford Granada6 Ford pickuptruck 62WD） Honda Accord   
Chevelle6,V6   
76 77 78 79 80 77 80 77 7980 81 76 7778 7980 81 7677787980 81 767778798081   
000000 T + 。 。 0 00. 电 Air-conditioning 000000 000000 O00000   
000000 0 清 8 00000 Body exterior(paint) .000 。 O00000 000OOO   
000000 。 O000 。 00000 Body exterior(rust) 000000 000000 .0000   
000000 福 0..0 000000 Body hardware 000000 O00000 O00000   
000000 福 .0 。 00000 Body integrity 000000 000000 000000   
000000 。 000o 。 O0000 Brakes 000000 000000 O00000   
@0000 。 O0000 Clutch 00o 000000 000000   
000000 00000 000000 Driveline 000000 000000 000000   
000000 00000 00000O Electricalsystem(chassis) O00oo0 。 O00000 000000   
000000 00●●. 000000 Engine cooling OO0000 000000 000.00   
O00000 0.00. 000000 Enginemechanical 000000 000000 00000   
00.000 0000 0000 。 Exhaust system 000000 000000 00.000   
000000 。0。 000000 Fuel system 000000 000000 O00000   
000000 0.000 00000O Ignitionsystem 000000 000000 OO0000   
000000 00000 000000 Suspension 000000 00.000 OOO000   
。 0000 000000 Transmission(manual) 000 00.000 000000   
000000 0000 000000 Transmission(automatic) 000000 0.0000 000000   
000000 0000OO TroubleIndex 000000 000000 00000O   
O0000 00o 。。 O0000 Cost Index 00000 00000 00000   
Mercedes-Benz300D PlymouthVolare Subaru(except4WD) Trouble Spots Toyota Corolla Volkswagen Rabbit Volvo240series   
5(diesel) (exceptTercel) (diesal)   
767778798081 767778798081 767778798081 767778798081 767778798081 767778798081   
00000 00O00 000000 Air-conditioning 000000 .0.0 0000.0   
O0000 00000 000000 Body exterior(paint) 000000 OO00o O00000   
O0000 H .00 0000 Body exterior [rust) 000000 O000 OO0000   
00000 00 0000O0 Body hardware 000000 00000 000000   
O000O 福 0 。 000OO Body integrity OO000O O0000 O0000O   
00000 8.:8 000000 Crutes 000000 00000 000000   
00000 00000 00000 。 000000 00000 000000   
Driveline   
00000 0 ..00 00000O Electricalsystem(chassis) OO0000 00000 000000   
00000 00000 0 O00o 。 Engine coaling O00000 O..00 O00000   
00000 00000 D 00000 Enginemechanical O00000 0000o 000000   
00000 O0000 OO000 。 Exhaust system 000000 0...0 0..000   
O0000 000000 Fuelsystem 0000OO 0000 。 000000   
O0000 O 00 000000 Ignitionsystem 000000 00000 OOO000   
O0000 0.00 000000 Suspension OO0000 00000 000000   
福 。 000000 Transmission(manual) 000000 00000 000000   
O0000 00000 000000 Transmission(automatic) 000000 000000   
OO0OO 。 .00 0000OO OO0000 00000 OOOOOO   
Trouble Index   
00000 00000 Cost Index OO000 0000 00000

# Conclusion

Well-designed small multiples are

inevitably comparative   
deftly multivariate   
shrunken, high-density graphics   
usually based on a large data matrix   
drawn almost entirely with data-ink   
efficient in interpretation   
often narrativein content,showing sifts in the relationship between variables as theindex variable changes (thereby revealing interaction or multiplicative effects).

Small multiplesreflect much ofthe theory of data graphics: For non-data-ink, lessis more. For data-ink, less isabore.6

![](images/4eb6902bc549b44940bd1f8b120f9875c8f89308a15f6ce873dfd71532d2d1d0.jpg)

# 9 Aesthetics and Technique in Data Graphical Design

Along with the amazing graphic ofthe French losses in the Russiar invasion, Minard includes a second “CarteFigurative. Itportrays Hannibal's fading elephant campaign in Spain, Gaul,and Northern Italy. Minard uses alighttransparentcolorforflow-lines,allowing the underlying type to show through.Thisrefined use of color to depict more information contrasts with the garish tonestoooften seenin modern graphics.

Whatmakes for such graphical elegance? Whataccounts for the quality ofMinard'sgraphics, ofthose ofPlayfairand Marey, and of some recent work,such as thenewview ofthe galaxies? Good design has two key elements:

Graphical elegance is often found in simplicity of design and complexity ofdata.

Visually attractive graphicsalso gather power from contentand interpretations beyond the immediate display of some numbers. The best graphicsare about theuseful and important, aboutlife and death, about the universe. Beautiful graphics do not traffic with the trivial.

Onrare occasions graphical architecture combineswith thedata content toyield a uniquely spectaculargraphic. Such performances canbedescribed and admired but there areno easy compositional principles onhow to create that onewonderful graphic in millions. As BarnettNewman once said, "Aesthetics is for theartist like ornithology is for thebirds."

What can be suggested, though,are some guides for enhancing the visual quality ofroutine, workaday designs. Attractive displays ofstatistical information

·haveaproperly chosen formatand design   
use words, numbers, and drawing together   
·reflecta balance, a proportion, a sense ofrelevant scale   
display an accessible complexity ofdetail   
often haveanarrative quality, a story to tell about thedata ·are drawn in a professional manner,with the technical details ofproduction donewith care   
avoid content-free decoration, including chartjunk.

# The Choice ofDesign: Sentences, Text-Tables, Tables, Semi-Graphics, and Graphics

The substantive content, extensiveness oflabels,and volume and ordering ofdata all help determine the choice ofmethod forthe display of quantitative materials. Thebasic structures for showing dataare the sentence, the table,and the graphic. Often two or three of these devices should be combined.

Theconventional sentence is a poorway to show more than two numbers because it preventscomparisonswithin the data. The linearly organized flow of words, folded over atarbitrary points (decided not by content butby the happenstance of column width), offers less than one effective dimension for organizing the data. Instead of:

Nearly 53, percent of the type A group did something or other compared to46percent ofBand slightlymorethan57percentofC

Arrange the type to facilitate comparisons, asin this text-table:

The three groups differed inhow   
they did something or other:   
Group A （号 $5 3 \%$   
Group B $4 6 \%$   
Group C 57%

There are nearly always better sequences thanalphabetical-for example, ordering by content orby data values:

Group B 46% Group A 53% Group C 57%

Tables are clearly the best way to show exactnumerical values, although theentries canalso bearranged insemi-graphical form. Tables are preferable to graphics for many small data sets.1 A tableisnearly always better than a dumb pie chart; the only worse design than a pie chart is several ofthem, for then the viewerisasked to compare quantities located in spatial disarray both within and between pies, asin thisheavily encoded example from anatlas. Given their low data-density and failure to order numbers along a visual dimension,piecharts should never beused.

![](images/a0b7486e94dd02432676ff3be480be300db2c23be67633f34b416df19fa642e3.jpg)  
Department of Surveys, Ministry of Labour,AtlasofIsrael (Jerusalem, 1956-),vol. 8,p. 8.

1Onthe design oftables, see A.S.C. Ehrenberg,"RudimentsofNumeracy, Journal oftheRoyal Statistical Society, A,140 (1977), 277-297.

# How DifferentGroups Votedfor President

Tablesalso work well when thedata presentation requiresmany localized comparisons. In this410-number tablethatI designed for theNew York Timesto show how different people voted in presidential elections in theUnited States,comparisons between the elections of1980and 1976 are read acrosseach line;within-election analysis is conducted by reading downward in theclusters ofthree to seven lines. The horizontal rules divide thedata into topical paragraphs; the rows are ordered so as totell an ordered story aboutthe elections. This type of elaborate table, a supertable, is likely to attractand intrigue readers through its organized, sequential detail and reference-like quality. One supertable is far better thana hundred little bar charts.

Based on12,782interviewswith voters at theirpollingplaces. Shownis how eachgroupdivided its vote for Presidentand, inparentheses, the percentage of the electorate belonging to each group.

![](images/763b9a2ff0a6bdaba3e89c62cba99fc52119264da3e721f8364ae13453f70eb2.jpg)
Source:1976and1980electiondaysurveysbyTheNewYorkTimes/CBSNewsPolland 1976electionday survey by NBCNews.

For sets of highly labeled numbers, a wordy data graphiccoming close to straight text-works well. Thistable of numbers is nicely organized intoa graphic:

Some Winners and Losers In the Forecasting Game Chase Econometrics: 7.4% CouncllofEconomic Wharton Econometric Advisors: +4.7% Forecssting Data Conference Resources .5% Aboutayearago,elghtforecasterswereaskedfor Board: thelrpredictionson some key economlcIndicatore. Nat ABSOC. D1 Businees Here's how the forecasts stack up agalnst the NaLAssoc.ofBuslnees Economists: 4.5% probable 1978 results(shown In the black panel). Economists: Wharton conometric I.B. Economice Forecasting: 5 Department: ongression Budget Deta Office Resources: Conferenc NaLAssoc.ofBusinees Congressional Budget Board: Economlsta: +6.2% Office: 6.3% E AN 中 I.B.M.Economics LB.M. Economics Wharton Econometric Councllof Economic Department: +4.1% Department: +5.9% Forecasting: +21% Advisers: 3 RealG.N.P. Industrial Production ChangeinConsumer CorporateProfits Unemployment Growth: 3.8% Growth: +5.8% Prices: +7.7% Growth: +13.3% Rate: Chese Conference B.M Economics Data Econometrics: +2.8% Board: spartment 69 Resources: +10.5% Dats Busines Economics osource Department +10.4% WhartonEcon Chase Econometrics: +6.5% E Chae Econometrics: ssourcee Chase Econometrics 5 Councll of Economic Forecasterearenotllsted Advisers: 5.9% in categorlesforwhich they didnotmakeaprediction. Wharton Econometric Forecasting: Aftertaxes A

# Making Complexity Accessible: Combining Words, Numbers,and Pictures

Explanations that give access to the richness ofthe datamake graphics more attractive to the viewer. Words and pictures are sometimes jurisdictional enemies, asartists feud with writers for scarce space. An unfortunate legacy of these craft-union differences is the artificial separation ofwords and pictures; a few style sheets even forbid printing ongraphics. What has gone wrong is thatthe techniques of production instead ofthe information conveyed have been given precedence.

Words and pictures belong together. Viewers need the help that words canprovide. Words on graphics are data-ink, making effective use of the space freed up by erasing redundant and nondata-ink. Itisnearly always helpful to write little messages on the plotting field to explain thedata,to label outliersand interesting data points, to write equations and sometimes tables on the graphic itself,and to integrate thecaption and legend into the design So that the eye is not required to dartbackand forth between textual material and the graphic. (The size of type on and around graphics can be quite small, since the phrases and sentences areusually not too long I and therefore the small type will not fatigue viewers the way it does in lengthy texts.)

Theprinciple ofdata/textintegrationis

Data graphics areparagraphs about dataand should betreated as such.

Words,graphics, and tables are differentmechanisms with buta single purpose-the presentation of information. Why should the fow ofinformation be broken upinto different places on the page becausethe information is packaged one way oranother? Sometimes itmay beuseful to have multiple story-lines or multiple levels of presentation, but that should bea deliberate design judgment, not something decided by conventional production requirements. Imagine if graphics were replaced by paragraphs ofwords and those paragraphs scattered over the pages out of sequence with the rest of the text-that is howgraphical and tabular information isnow treated in the layout of many published pages, particularly in scientific journals and professional books.

Tables and graphics should berun into the text whenever possible,avoiding the clumsy and divertingsegregation of "See Fig. 2,” (figures all too often located on theback of the adjacent page).3 Ifa display is discussed in various parts of the text,it might well beprinted afresh neareach referenceto it,perhaps in reduced size in later showings. Theprinciple of text/graphic/table integration also suggests that the same typeface beused fortextand graphic and, further, thatruled lines separating different types of information be avoided. AlbertBiderman notes thatillustrations were once well-integrated with text inscientific manuscripts,such as those ofNewton and Leonardo da Vinci,butthatstatistical graphics became segregated from textand table asprinting technology developed:

The evolution ofgraphic methods asanelement ofthe scientific enterprisehas been handicapped by theiradjunctive,segregated, and marginal position. The exigencies of typography that moved graphics to a segregated position in theprinted work havein the past contributed totheir intellectual segregation and marginality as well. Therewas a corresponding organizational segregation,with decisions on graphics often passing out of the hands of the original analyst and communicator into those of graphic specialists-the commercial artists and designers of graphic departments and audio-visual aids shops, for example, whose predilections and skillsare usually more thoseofcosmeticians and merchandisers than of scientific analysts and communicators.4

Page after page of Leonardo's manuscripts havea gentle but thorough integration of text and figure, a qualityrarely seen in modern work:

chevai le cose uedute cifene ranro miavre chi noche lemcmbva mairuogasiiara imosibile do tvfguare ome soccossaua du   
gliavto di bvaccio guak alla tua tauota dipinta sia,a,bdisostra H dal'ochio mezo Gvaccio allova tu wdvai per esfo spa cio tutte le cose d uder siporgiden rdla langhe dnns ovizonte di cento miglia intana confusa diminuttione cheno cheyuradglcarabg maxpena potva povve sipicclopunrodi penclloche yon sla maqgiove chogm gvan 'cdsamento bosto in dieai migaa didirantia Perche lmonti in langha digtania sidimostranopiu scun ndllacima   
Lana che mlla basa 一 c'acgnista gvadi di grossezca inogmgradode la sua basjea della sna distuna ccansachcfe cime demonn che biu sindam pin mstranala sna natu rale oscurita pev A che mdco sondimpe- dite dlalla   
gvosse LLa delavia mllaama che ndllay Covo basa onella ucimta che nella remottione,Pro   
nasiopds,vak,sono gvadi delbovia chesem  
pr snsotiylian'guantopins'inalzan af，f.h,k. ogdaeot

Finally, a caveat: the use of words and pictures together requires a special sensitivity to the purpose ofthe design-in particular, whether the graphic is primarily for communication and illustration ofasettled finding or, in contrast, for the exploration of a data set. Words on and around graphics are highly effectivesometimes all too effective-in telling viewers how to allocate their attention to thevarious parts ofthedata display.5Thus, for graphics in exploratory dataanalysis, words should tell the viewer how to read the design (if it is a technically complexarrangement and notwhat to read in terms of content.

# Accessible Complexity: The Friendly Data Graphic

An occasional data graphic displays such carein design that it is particularly accessible and open to the eye, as if the designer had theviewer in mind at every turn while constructing thegraphic. Thisisthefriendlydatagraphic.

There are many specific differences between friendly and unfriendly graphics:

![](images/56df89307ba5154e28b70d6919a77e782ea4a16f02a41876512f2533bcdfea95.jpg)

With regard to typography,Josef Albers writes:

Theconceptthat"thesimpler theform ofa letter the simpler reading ofbeginningconstructivism. It became something like a dogma, and is still followed by "modernistic' typographers. 5 Ophthalmology has disclosed that themore theletters aredifferentiated from each other, the easier is the reading. Without going into comparisons and details, it should berealized thatwords consisting ofonly capital letters present themost difficult reading-because of theirequal height, equal volume, and, with most, their equal width. When comparing serif letters with sans-serif, thelatter provide an uneasy reading.The fashionable preference for sans-serif in text shows neither historical nor practical competence.6

# Proportion and Scale: Line Weight and Lettering

Graphical elements look better together when their relativeproportions are in balance. Anintegrated quality, an appropriate visual linkage between the various elements,results. Thismusical score ofKarlheinz Stockhausen exhibits such a visual balance:

![](images/4bae1a822163bc4425be1c3b84f4104e20c4ef196266287aacaff8ed2fa15929.jpg)  
Karlheinz Stockhausen, Texte,vol.2 (Cologne, 1964),p. 82, from the score of "Zyklus fiir einen Schlagzeuger."

In contrast, this next design is heavy handed, with nearly every element out ofbalance: the clotted ink, the poor style of lettering, the puffed-up display of a small data set,the coarse texture ofthe entiregraphic, and themismatch between drawing and surrounding text:

![](images/ff54fbc332c651fd11179a1ab06661b45c548484eb5fdd20e565f99af9331060.jpg)  
Figure4.SeatsandVotesin1968.

Lines in datagraphics should be thin. One reason eighteenthand nineteenth-century graphics look so good is that they were engraved on copper plates, with a characteristic hair-thin line, The drafting pens of twentieth-century mechanical drawing thickened linework, making it clumsy and unattractive.

An effective aesthetic device is the orthogonal intersection of linesofdifferent weights:

二1 Y

Nearly every intersection ofthe linesin this design (based ona painting by Burgoyne Diller) involves lines of differing weights, andit makes a difference, for the painting's character is diluted with lines ofconstant width:

二 1  
1

Poster for the exhibition "Mondrianand Neo-Plasticism in America," YaleUniversity Art Gallery, October18to December2,1979.The originalpainting was donein 1941 byDiller; see Nancy J.Troy, MondrianandNeo-Plasticism in America (NewHaven,1979),p.28.

Likewise, data graphicscan be enhanced by the perpendicular intersections oflinesof differing weights. The heavier line should bea data measure. Ina time-series, forexample:

-1

The contrast in lineweight represents contrast in meaning. The greater meaning isgiven to thegreater line weight; thus the data line should receive greater weight than the connecting verticals. The logic here is a restatement, in different language, ofthe principle ofdata-ink maximization.

# Proportion and Scale: The Shape of Graphics

Graphics should tend toward the horizontal, greater in length than height:

![](images/f3a55ee1f13274678eb44db4ccb36717f1a74249ccbed606aad95e8454362987.jpg)  
greater length

Several lines of reasoning favor horizontal over vertical displays. First, analogy to the horizon. Our eye isnaturally practiced in detecting deviations from the horizon, and graphic design should take advantage of this fact. Horizontally stretched time-series aremore accessible to the eye:

![](images/714aaa76b0813e83c708cd1682751975f97f6e6bf5541c610491e95383dae27e.jpg)

The analogy to the horizon also suggests thata shaded, high contrast displaymight occasionally bebetter than the floating snake. The shading should be calm, without moire effects.

![](images/0210554d0dcdca3d39797b87d94c61c58e91899bee323b283dac65af400e122b.jpg)

Second, ease of labeling. Itis easier to write and toread words that read from left to right on a horizontally stretched plottingfield:

![](images/f738eee270e24709e4903820aef5447f7b80bf7a8dd47caddf982c967099f272.jpg)

Third, emphasis on causal influence. Manygraphicsplot,inessence, and a longer horizontal helps to elaborate the workings ofthe causal variable in more detail.

![](images/356e41afff6694c66e5712a11fd8443baca930cb652724868c4a444749707c2f.jpg)

Fourth, Tukey's counsel.

Most diagnostic plots involve either a more orless definite dependence that bobblesaround a lot, orapoint spatter. Such plotsare rather more often bettermadewider than tall. Widerthan-tall shapes usually make it easier for the eye to follow from left to right.

Perhaps the most general guidance we can offeris that smoothly-changing curves canstand being taller than wide, buta wiggly curve needs to bewider than tall. .7

And, finally, Playfair's example. Ofthe 89graphics in sixdifferent booksby William Playfair, most (92percent) are wider than tall. Several of the exceptions are his skyrocketing government debtdisplays. This plot shows thedimensions ofeach ofthose 89graphics:

![](images/01bb148612da69fca3657d3e35c6c04067b3391eaf75d7340a9bc61208b9025e.jpg)

If graphics should tend toward the horizontal rather than thevertical, then how much so? A venerable (fifth-century B.c.) but dubious ruleof aesthetic proportion is the Golden Section, a"divine division' ofaline.8 A length is divided such thatthe smaller is to the greater part as the greater is to the whole:

$$
\frac { a } { b } = \frac { b } { a + b }
$$

Solving thequadratic when $\mathsf { a } = \mathsf { 1 }$ yields ${ \mathfrak { b } } = { \frac { { \sqrt { 5 } } + 1 } { 2 } } = 1 . 6 1 8 \cdots$

In turn the Golden Rectangle is

![](images/1342fc28ddd8ed12328252077e64fdb8388407e9c5b9c86fa59473270fc31678.jpg)

The nice geometry ofthe Golden Rectangle is not unique; Birkhoff points out thatat least five other rectangles (including the square) have one simple mathematical property oranother for which aesthetic claims might be made:9

![](images/8609d78f42a406385e114d70628182f2118916819ed61eaef11edaf5ad660631.jpg)

Playfair favored proportions between 1.4and 1.8in about twothirds ofhis published graphics, with most ofthe exceptions moving more toward the horizontal than the golden prescription:

8Thecombination ofgeometryand mysticism surroundingthe Golden Rectangle can beseen in Miloutine Borissavlievitch, The Golden Number andthe ScientificAestheticsofArchitecture(New York,19s8）and Tons Brunes, The Secrets ofAncient Geometry (Copenhagen, 1967), vols. 1and 2.

9George D. Birkhoff, Aesthetic Measure (Cambridge, 1933),pP. 27-30.

![](images/68203dddb86ffeaa6dfe0b438fa672a4da495b0d9c3bf23d9b3405984c6c225c.jpg)

Visual preferences forrectangular proportions have been studied by psychologists since $1 8 6 0$ but, even given theimplausible assumption thatsuch studies are relevant to graphic design, thefindings are hardly decisive. A mild preference for proportions near to the Golden Rectangle is found among those taking partin the experiments, but thepreferred height/length ratios also vary a great deal, ranging between

And, asis nearly always the case inexperiments in graphical perception, viewer responses were found tobehighly contextdependent.10

The conclusions:

![](images/6a8416a5eaef4b51d7780da3578c4eee9f18a3964fcd54437f3ff8568ed442ec.jpg)  
10Ihaverelied onLeonard Zusne, Visual PerceptionofForm (New York,1970), ch. 10,forasummary ofthe immense literature.

Ifthe nature ofthe data suggests the shape of the graphic, follow that suggestion.   
Otherwise, move toward horizontal graphics about 50percent wider than tall:

![](images/301efd6f1045901ae597fe583e9ed2e717a5ed7533118bd1602bd7a1c68df52a.jpg)

# Epilogue: Designs for the Display of Information

Design is choice. The theory ofthe visual display ofquantitative information consists of principles that generate design options and that guide choices among options. The principles should notbe applied rigidlyor in a peevish spirit; they arenot logicallyor mathematically certain; and itis betterto violate any principle than to place graceless or inelegant marks onpaper. Most principles of design should be greeted with some skepticism,for word authority can dominate our vision,and we may come to see only through thelenses ofword authority rather thanwith our own eyes.

Whatis to be sought in designs for thedisplay ofinformation is the clear portrayal of complexity. Not the complication ofthe simple;rather the task ofthe designer is to givevisual access to the subtle and the difficult-that is,

therevelation ofthe complex.

![](images/9e2346ccd873618e68e22c42cf06d9a51535b2eb32ee5b2fb346930b4306840c.jpg)

aesthetics, graphical 177-191   
airpollution 42,170   
Akahata(“RedFlag") 83   
Albers,Josef 183   
Alder, Berni 134，145   
American Education 118   
American Political Science Review 167   
Annuaire Statistique delaFrance 167   
Anscombe,F.J. 14   
Anscombe's quartet 13-14   
area and quantity 69-73   
Arkin, Herbert 112   
Asahi 83,167,168   
Asch,S.E. 56   
astronomical graphics 26-29,154， 166   
Ayres,Leonard P. 141,155   
Ayres, Richard E. 95   
Bamburger, Clara Francis 82   
Bancroft, T.A. 53,140   
barchart 96-97,126-128,129   
Barabba, VincentP. 153   
Barnett,Vic 114,168   
before-aftertime-series 39   
Beniger,JamesR. 20,86   
Bertin,Jacques 112, 166, 169,178   
Bickmore, D.P. 162   
Biderman, AlbertD. 181   
'BigDuck' 116,117   
bilateralsymmetry 97   
Biochemistry 110   
BiochimicaetBiophysicaActa 110   
Birkhoff, GeorgeD. 189   
blot maps 20,139   
Blot,William J. 16   
Bonner,John Tyler 94   
boringstatistics 79-80, 87   
Borissavlievitch, Miloutine 189   
Boutique Data Graphics 118   
Bowen, William G. 95   
boxplot 97, 123,129   
Brier, Stephen S. 14   
Brinton, Willard C. 112   
Brown,Denise Scott 116-117   
Brunes, Tons 189   
Bryan,Kirk 99   
Business Week 63,83,167   
calculus 9   
calculus, graphical 46   
California WaterAtlas 119   
Campbell, Angus 147   
Campbell, Donald T. 75   
cancer 16-20, 47,171   
cancer maps 16-20,121   
Cappon,LesterJ. 146   
cars, frequency ofrepair 174   
Cartesian coordinates 9   
causeandeffect 37,47,82,187   
CEM 56   
chartjunk 107-121   
Chavannes,E. 21   
chemical elements 102-105   
Chernoff faces 97,142   
Chernoff, Herman 136，142   
Cheysson,E. 154   
chicken，4,340-pound 73   
cholera map 24   
chromosomes 172-173   
Cleveland, William S. 38,168   
color 153-154,183   
color-deficient viewers 183   
Colton, Raymond R. 112   
computer graphics 26-27,29,42,   
116,120-121，136,153， 170   
Connecticut speeding 74-75   
constant dollars 65-68   
Consumer Reports 80,174   
context 74-75   
Converse, PhilipE. 147   
copper, conductivityof 49   
Cornford, Eain M. 109   
Cosmographia 22   
county maps 16-20,153   
Cox,Michael D. 99   
Crotty,William J. 95   
Curti, Merle 85   
Dahl, Robert A. 85   
Dakin, Edwin F. 15   
Daniel, Cuthbert 133   
data-based grid 148   
data-based labels 149-152   
data-built data-measures 139-144   
data density 161-169   
data-ink 91-105   
data-ink maximization 96-105,   
123-137, 175, 186,187   
data-inkratio 93-96   
datamaps 16-27   
datamatrix 167-169   
data measures 139-144   
data/text integration 180-182   
datavariation 60-61   
Davis,John C. 162   
DayMines, Inc, 54   
decoder, visual 153-154   
deflatingmoney 65-68   
Der Spiegel 83   
designvariation 60-63   
Dewey, Edward R. 15   
DieZeit 83   
Diller,Burgoyne 185   
distortion, graphical 55-59   
dogs 50   
Doll,R. 47,82   
dollars,constant 65-68   
dot-dash-plot 133,136,139， 152   
double-functioning labels 149-152   
Duchamp,Marcel 36   
ducks 116-121   
'Easter Wings' 143   
economic data 15，32-34,38，54-55，   
61-68,70,91-92, 108,126,148,152,   
158,161, 180   
TheEconomist 63,83,167   
educational tests, graphics 86   
Ehrenberg,A.S.C. 178   
election graphics 147,179   
electroencephalogram 93   
elegance, graphical 177   
Eliot,T. 100   
encodings 178,183   
erasing principles 96-100,136   
Erbring,Lutz 120   
excellence, graphical 13-51   
Fienberg,Stephen E. 14   
'Fig.' 181   
Finkner, AlvaL. 153   
Fiorina,Morris 66   
Fisher,R.A. 133   
Flanigan, William H. 85   
Flury,Bernhard 97   
Fortune 167   
Francolini, C.M. 153   
Frankfurter Allgemeine 83   
Fraumeni,JosephF. 16   
French communes 166   
French wine map 25-26   
friendly datagraphics 183   
fuel economygraphic 57-59   
Funkhouser, H. Gray 20,28,154   
Gabaglio, Antonio 72   
galaxiesmap 26-27,154,166   
gecko 36   
Geological Survey maps 168   
Gilbert, E.W. 24   
Goldenberg, EdieN. 120   
Goodin, W. R. 170   
Gould,John D. 182   
government spending 64-68,158   
grade school graphics 86   
Graph ofMagical Parallelepipeds 68   
Graphical Hack 59   
gray grid 116   
gray shades 154   
grids 112-116   
grids, data-based 145-148   
grids,gray 110   
grids，white 127-129,136   
Groth,EdwardJ. 26   
Gurnett,DonaldA. 29   
half-face 97, 136   
Halley,Edmond 23   
Hankins,TimothyH. 134   
Hannibal'scampaign 176-177   
Hayward,Roger 102,136   
Herbert,George 143   
Herdeg,Walter 80, 152   
herring catches 172   
hierarchy ingraphics 153-159   
high-information graphics 168-169   
Hilgard,Ernest 85   
histogram 126-128   
histogram, living 140   
Hjort,Johan 172   
Ho, C.Y. 49, 150   
Hoover,Robert 16   
horizon,analogy to 186-187   
horse paces 34-35   
House of Representatives 37   
Huot,MarieE. 109   
identification numbers 149-150   
Israel,Atlas of 178   
Italian post office 72   
Izenour,Steven 117   
Japan,graphics in university entrance   
exams 86   
Japanese beetle 43,121   
Japanese graphics $8 2 - 8 4$   
JASA style sheet 110,150-151,164   
Joiner,BrianL. 140   
JournaloftheAmerican Chemical   
Society 110   
JournalofAmericanMedicalAssociation   
167   
JournaloftheAmerican Statistical   
Association 110,150-151,164,   
167-168   
JournalofBiologicalChemistry 110   
JournalofChemical Physics 110   
JournaloftheRoyal Statistical Society 16,   
Jupitergraphic 29   
Kahrl,WilliamL. 119   
Kelley, Stanley 95   
Kolers, Paul A. 79   
Kooi, Kenneth 93   
Kouchoukos,Nicholas 109   
Kuznicki,JamesT. 100,109   
labels on graphics 180-182, 183,187   
Lambert,JohannHeinrich 29,32,   
45-46   
Lancet 110   
lane stripes 144   
Larsen, Wayne A. 129   
Lauer,A. R. 144   
LawSchool Admission Test,   
graphics 86   
Learning from Las Vegas 116-117   
Leonardo da Vinci 181-182   
lessisa bore 175   
lessismore 175   
lettering 184   
LieFactor 57   
lies,defense of 76-77   
Liley,P.E. 49,150   
lineweight 185   
living histogram 140   
Long, John Hamilton 146   
Los Angelessmog 42,170   
Los Angeles Times 42, 69   
lung cancer 16-20,47   
lying graphics 76-77   
Macdonald-Ross,Michael 56   
MacGregor,A. J. 112   
magnetic monopole 39   
mail,HouseofRepresentatives 37   
Malcolm, AndrewH. 84   
Manvel, AllenD. 81   
map,blot 20, 139   
map,cancer 16-20   
map,cholera 24   
map,data 16-27   
map, Frenchwine 25-26   
map, galaxies 26-27, 154, 166   
map,Israel 178   
map,patch 20   
map, thematic 16-27   
map, Yu ChiThu 20-21   
Marey,E.J. 31,34-36,40,115-116,121   
Mason, ThomasJ. 16   
Masterton,William 8s   
Matisse,Henri 160   
maximizing data-density 168   
maximizing data-ink 96-105,123-137,   
175, 186,187   
McClenaghan,William 85

McCracken,Paul 48 McCullagh,Michael J. 162 McCutcheon,N. Bruce 100,109 McGill,Robert 129 McKay,Frank W. 16 McRae, GregoryJ. 42, 170 Meihoefer,H.J. 56 melanoma 171 Mies van der Rohe, Ludwig 175 Miller,ArthurH. 120 Miller,Warren E. 147 Minard,CharlesJoseph 24-25,39, 40-41,51, 121,176-177 Mitchell,H.L. 50 moirevibration 107-112 LeMonde 83,167 Mondrian,Piet 185 Monkhouse, F.J. 112,165 Monty,Richard A. 168,182 Moore,Carol 152 Moscow,Napoleon'scampaign 40-41 121,176-177 mountain-to-the-sea 154 multifunctioning elements 139-159 multiple viewing angles 154-155 multiple viewing depths 154-155 multiwindow plots 114,171 Murphy,EdmondA. 172 MuseumofModernArt 91 Napoleon'smarch 40-41,51,121, 176-177 narrative graphics 40-43 National Science Foundation 60 Nature 110,167 Needham,Joseph 20 NewEnglandJournalofMedicine 110, 167 Newman,Barnett 177 Newman, L.Hugh 43 Newsweek 167 Newton, Isaac 181 New York City weather 30,121,164 New York Times 30, 54, 57,61,66,71, 76,80-83,86, 121, 164, 167,179,180 NihonKeizai 83 non-data-ink 96,107 NudeDescendingaStaircase 36 ocean currents 99 oil prices 61-63 optical art 107-108 ontical dots 114

orthogonal lines 185-186   
outliers 142   
Puaaavt Aaa Pvv   
patch maps 20   
Pauling, Linus 85, 102   
Pearson,Karl 145   
Peebles,P.JamesE. 26   
periodicity of elements 102-105   
perpendicular lines 185-186   
Petchenik, BarbaraBartz 146   
Phillipscurve 48   
pie chart 178   
Pittsburgh Civic Commission 55   
Playfair,William 9,32-34,43-45，52   
64-65, 73,91-92,126, 148,188-189   
population density map 155-157   
Potter,D.E. 145   
Powell, R. W. 49, 150   
Prakash,Om 172   
Pravda 83,167   
Pravda School of Ordinal Graphics 7   
presidential votegraphics 147, 179   
press,graphical sophistication （2 $8 2 - 8 4$ （20号   
ProcedngsoftheNationalAcademyof   
Sciences,U.S.A. 110   
Psychological Bulletin 167   
psychological experiments 55-56   
Pugin 117   
puzzle graphics 153   
quartile plot 124，136,139   
range-frame 130,136, 139, 149, 152   
redundant data-ink 96-100   
Reinhardt,Ad 122   
Reiss, AlbertJ. 14   
relational graphics 43-50   
Rhone bridge 39   
Rickett,BarneyJ. 134   
Riedwyl,Hans 97   
Riley,Bridget 108   
road stripes 144   
Roberts,K.V. 145   
Robinson, ArthurH. 20,40   
Robyn,DorothyL. 20   
Rogers, Anna C. 112   
Ross,H.Laurence 75   
royalty,genealogy 34-35   
rugplot 135, 136   
Ruskin,John 117   
sampling error 172   
Sampson,Roy J. 85   
Samuelson.Paul 85   
sans serif 183   
SAS/GRAPH 112   
Satet,K. 09,112   
Sato,Isao 82,85   
Scarf,F.L. 29   
scatterplot 130-135   
Schlee,Susan 172   
Schmid, Calvin F. 112   
Schmid,Stanton E. 112   
Science 39,83,109,110,167,173   
Science Indicators, 1974 60   
ScientificAmerican 50,73,167   
sea-horse 36   
Seinfeld,J.H. 170   
Seldner,Michael 26   
semi-graphics 178-180   
Senders,John W. 168, 182   
Shahn,Ben 177   
shape, graphical 186-190   
Shinohara, Miyohei 82,85   
Shiskin,Julius 38   
Shrink Principle 169   
Shryock,Henry S. 113   
Siebers,B.H. 26   
Siegel,Jacob S. 113   
Silverstein,Louis 80   
Slowinski,Emil 85   
small multiple 42,48,170-175   
smog 42, 170   
Snow, Dr.John 24   
Social Indicators,1973 163   
sophistication,graphical 82-86   
Spear,Mary Eleanor 81,112,123   
starfish 36   
StatisticalAbstractoftheUnitedStates   
161,167   
stem-and-leafplot 140   
Stockhausen,Kreinz 184   
stock prices 15   
Stokes,Donald E. 147   
strangers 142   
Strunk, William 81   
Sunday Times (London) 63   
sunshine,British 165   
supertable 179   
Swift,Jonathan 106   
Sypher,Wylie 139   
table-graphic 145,158-159   
tables 56,178-180   
Tanur,Judith 85   
television graphics 76,81   
Tell-A-Graf 112   
Terpenning,IrmaJ. 38   
textbooks $8 4 - 8 5$ 2号   
textbooks, statistical graphics 112   
text-tables 178-180   
Thissen, David 142   
Thomas, Edward Llewellyn 168   
Thomas,LaVerne 85   
Thompson, MorrisM. 168   
Thrower,NormanJ.W. 23   
Thurber,James 52   
tick marks 127-129,149   
Tilling, Laura 32,45-46   
Time 62,71,79, 83   
TheTimes (London) 83,167   
time-series 28-39   
time-series,before-after 39   
Todd,Lewis Paul 85   
train schedule 31,98, 115-116,121   
Troy,Nancy J. 185   
Tufte, Edward R. 29,53,75,95,184   
Tukey,John W. 53,114,123,125,   
129,136,140, 168,188   
Tukey, PaulA. 114,168   
tungsten, conductivityof 150   
typography 178-183   
Valery, Paul 153   
Vasarely, Victor 108   
Vauthier,L.L. 154   
Venturi, Robert 117,139,175   
viewing architecture 159   
Wainer, Howard 79,142,153   
Waldrop,M.Mitchell 39   
WallStreetJournal 83,167-168   
Washington Post 62,70,83   
White, E.B. 81   
whitegrid 127-129, 136   
White, Jan 79-80   
white pines 50   
Wilk, Martin B. 53   
Wilkinson,H.R. 112,165   
Wilson,James Q. 85   
Wiskenmann, Arthur 171   
WorldWarIgraphic 141   
Wurman, Richard Saul 90   
Yajima,Yokichi 85   
Youden,W.J. 143   
Yu ChiThumap 20-21   
Yunis,JorgeJ. 172   
Zeeman,E.C. 50   
Zingale,Nancy H. 85   
Zusne,Leonard 97,190

The following illustrations arereprintedbypermission: CHAPTER 1.Anscombe'squartet $\mathfrak { O }$ 1973American Statistical Association. Map ofthegalaxies, P.JamesE.Peebles, Princeton University. Radio emissions ofJupiter, Donald A. Gurnett, $\circledcirc$ 1979 American Association fortheAdvancement of Science. New York City weather history $\circledcirc$ 1981 TheNew York TimesCompany. Text on franked mail $\circledcirc$ 1975 TheNew York TimesCompany Magneticmonopole $\circledcirc$ 1982American Association fortheAdvancement ofScience. Bridgeon Rhone, Bibliotheque del'Ecole Nationale desPonts etChausses.LosAngeles smog,byBob Allen $\circledcirc$ 1979TheLosAngeles Times,based on data from GregoryJ. McCrae, California InstituteofTechnology.Japanesebeetle $\circledcirc$ 1965 Aldus Books, London. Phillips curve, Organisation forEconomic Cooperation and Development,Paris. Dogs $\circledcirc$ 1976 Scientific American, Inc. CHAPTER 2.Payments to travel agents $\circledcirc$ 1978 TheNew York Times Company. Drawing byCEM $\circledcirc$ 1961 The New Yorker Magazine, Inc.Fuel economy standards $\circledcirc$ 1978The New York Times Company.OPEC oil prices $\circledcirc$ 1978 TheNew York Times Company. Oil prices $\circledcirc$ 1979 Time,Inc. Oil prices $\circledcirc$ 1979 The Washington Post.Real price of oil, Business Week, $\circledcirc$ 1979McGraw-Hill, Inc. Real price of oil $\circledcirc$ 1979The Sunday Times,London. Realprice ofoil $\circledcirc$ 1979 The Economist. Growth ofgovernment $\circledcirc$ 1977 Yale University Press, New York budget $\circledcirc$ 1976 TheNew York Times Company.Shrinkingdoctor, by Bob Allen and Pete Bentevoja, $\circledcirc$ 1979 TheLos AngelesTimes. Shrinkingdollar $\circledcirc$ 1978The Washington Post. Picture ofoil derricks $\circledcirc$ 1981 TheNew York TimesCompany. CHAPTER 3.Views on economy $\circledcirc$ 1980TheNewYorkTimesCompany.Pace of city life $\circledcirc$ 1976 TheNew York Times Company. CHAPTER $4 .$ Electroencephalogram $\circledcirc$ 1971 Harper &Row. Generation time $\circledcirc$ 1965 Princeton University Press. Registration rates $\circledcirc$ 1967 American Political Science Association. Registration rates $\circledcirc$ 1970 Addison

Wesley Publishing Company. Registration rates $\circledcirc$ 1970Holt, Rinehartand Winston. Ocean currents, Kirk Bryan,Princeton University andthe American Meteorological Society. Barchart, taste experiment, James T. Kuznicki, Proctor&Gamble Company. RogerHayward drawing ofperiodic properties ofelements, Linus Pauling. CHAPTER 5.Vertical bars,glucose transfer, Eain M. Cornford, $\circledcirc$ 1981 American Association for theAdvancementof Science.Multiwindowplot,Paul A.Tukey.BigDuck,PeterBlake. Californiacrops,State ofCalifornia, Office of Planning and Research Newspaper content $\circledcirc$ 1979 AmericanPolitical Science Association. CHAPTER 6.Parallel schematic plot $\circledcirc$ 1977 Addison-Wesley Publishing Company. Boxplot variation $\circledcirc$ 1978 American Statistical Association. Pulsar signals $\circledcirc$ 1975Academic Press. Empirical cumulativedistribution $\circledcirc$ 1976John Wiley. CHAPTER 7. Stem-and-leaf plot $\circledcirc$ 1972The Iowa State University Press. Living histogram, BrianJoiner.Magnetohydrodynamics $\circledcirc$ 1970 AcademicPress. $1 7 8 3$ 2号 map $\circledcirc$ 1976Princeton University Press.1956 and1960 elections $\circledcirc$ （号 1966John Wiley. CHAPTER 8.French communes $\circledcirc$ 1973 Mouton and Gauthier-Villars. Bertinsmallmultiple $\circledcirc$ 1973 Moutonand Gauthier-Villars. Melanoma $\circledcirc$ 1972Springer-Verlag.Normal distributions $\textcircled { \odot } 1 9 6 4$ Pergamon Press,Ltd. Chromosomes,JorgeJ. Yunis, $\circledcirc$ 1982American Association for theAdvancementof Science. Automobilefrequencyofrepair $\circledcirc$ 1982 Consumers Union of theUnited States, Inc. CHAPTER 9.How different groups voted for president $\circledcirc$ 1980TheNew York Times Company.Forecasting $\circledcirc$ 1979TheNew York TimesCompany.Leonardo daVinci drawing, facsimile $\circledcirc$ 1956Princeton University Press.Musical score,KarlheinzStockhausen, $\textcircled { \odot } 1 9 6 4$ VerlagM.DuMontSchauberg. Seats-votes graph $\circledcirc$ 1973 American Political Science Association. PosterillustrationbasedonBurgoyneDiller,GeometricalComposition in Black,Red,and White,Yale UniversityArtGallery, Collection Societe Anonyme.

# Acknowledgments, Second Edition

In preparing this new edition,Iamgrateful to Michael Arsenault, Michael and Winifred Bixler, Nicholas Cox,Inge Druckrey, Howard Gralla, Graham Larkin, MaryBeth Uryga,Carolyn Williams, and to GHP.

Thewonderful staff of Graphics Press continues with their very special care: Kate Atkinson, Karen Bass,Cynthia Bill, Donna Karosi, ElaineMorse, Kathy Orlando, Peter Taylor,and Carolyn Williams.

January 2001 Cheshire, Connecticut

# Acknowledgments

Iam indebted to many fortheir adviceandassistancewith this book.

For leave and research support during several academic years, the Center for Advanced Study in theBehavioral Sciences, the John Simon Guggenheim Foundation,the Woodrow Wilson School ofPrinceton University, and Yale University.

For providing access to their superb collections, the Bibliotheque Nationaleand the Bibliotheque de 1'Ecole Nationale des Ponts et Chaussees in Paris,and, atYale University,the Historical Medical Library and the Beinecke RareBook and Manuscript Library.

For helping me appreciate the practicalities in the production of statistical graphics, several members of the art department atthe New York Times and my students in Graphic Design and in the Department of Statistics at Yale.

For assistance in establishing Graphics Press, Peter B. Cooper, Earle E.Jacobs,Jr., and Trudy Putsche.

For design and artwork, Howard I. Gralla and Minoru Niijima.

For theirhelpand hospitality in Paris during mywork on the Minard drawings, Michel Balinski,JeanDubout, AndreJammes, and Claudine Kleb.

For providing examples and for suggesting improvements in the manuscript,James Beniger, Inge Druckrey, Timothy Gregoire, Joanna Hitchcock,Joseph LaPalombara, Kathryn Scholle, Stephen Stigler, Howard Wainer,and Ellen Woodbury.

For their reviews of the manuscript and fortheir inspiration and encouragement through all the years of this enterprise, Frederick Mosteller andJohn W. Tukey.

June 1982 Cheshire, Connecticut
## Part 2

> [BREADCRUMB_CTX: 《visual_display》 > Part 2]

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
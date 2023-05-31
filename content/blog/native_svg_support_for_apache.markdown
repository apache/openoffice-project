layout: post
title: Native SVG support for Apache OpenOffice 3.4 (Incubating)
layout: post
date: '2012-01-19T11:02:42+00:00'
permalink: native_svg_support_for_apache

<p>Apache OpenOffice 3.4 supports embedding SVG graphics using a newly created native SVG interpreter implementation. I want to talk about the advantages and some internals of this solution and the necessary changes done.<br /></p> 
  <p>One reason to do this was IP clearance. It allowed removal of six GPL/LGPL libraries, namely 
librsvg, libcroco, libgsf, gdk-pixbuf, glib, and pango gettext. These 
were used as an external pixel-based renderer. The new SVG uses an own internal 
interpreter in a new library and some new UNO API services. IP clearance was no interesting task to do, but it leaded to effects like here with SVG; the install sets get smaller (less libraries to deliver), the app needs less libraries (startup, memory, runtime) and the internal handling of SVG vector data is completely vector-graphic oriented.<br /> <br />There were also ODF-compatible File Format adaptions needed, more concrete the in ODF already contained and described multi-image support. In ODF, the original SVG is now embedded to the 'Pictures' folder inside the ODF file as one 
would expect from such a feature and can be easily extracted (unzip the ODF file and there you are). There is also a Png file 
written as replacement image. The draw:frame is now multi-image 
capable (as the spec allows). In the case of a SVG it writes a good 
quality Png and the original SVG as draw:image elements. Since older 
(and other) office versions are only capable of loading a single (and 
thus the first) image, the Png is written first. This allows file 
exchange with other and older offices without breaking backward compatibility and/or ODF file exchange. At load time, multi-image support 
will choose the best quality graphic available for further work, e.g. 
preferring vector format over pixel format, pixel format with 
alpha over non-alpha and lossless formats over those with 
losing info (you get the idea). Other ODF implementations (e.g. a 
viewer) may just use the pixel graphic available. Multi-image support is 
independent from SVG in principle and will work with all image file 
formats. This is implemented for the Drawinglayer graphic object (used 
in Draw/Impress/Calc) and the Writer graphic object (used in Writer).
<br /> <br />SVG is no longer interpreted each time it needs to be 
rendered (unavoidable by an external renderer), but only once transformed to a 
sequence of primitives (UNO API graphic atoms). That sequence is then used for all outputs, 
transformed to the graphic object's form and viewport. The 
sequence itself is completely view-independent. Internally, it is reused 
and thus it makes no difference if you have your SVG graphic added once 
or multiple times to your document. This is also true for saving, so always only one copy of your added SVG will be written (the same is true for the replacement 
Png image). Both, the sequence of primitives and the replacement 
image, are created using new UNO API services. One is capable of 
converting an io::XInputStream with SVG content to a sequence of primitives, the other is 
able to convert every sequence of primitives to a rendering::XBitmap 
with given DPI and discrete sizes (pixels, with automatic resolution 
reduction to a given maximum square pixel count to be on the safe side). This will be useful 
for other purposes, too, since it creates a fully alpha-capable 
representation of anything in primitive format to use as e.g. sprite.
<br /> <br />For all graphic processing the created vector graphic in form 
of a sequence of primitives is used. This means that you will get best 
quality in all zoom situations and all resolutions. This is also true 
for all exports, e.g. printing or PDF export which also uses the vector 
format. With an external renderer, it is unavoidable to use bitmaps with 
discrete solution in those cases, looking bad when zooming and needing more space in most cases as vector data. There is one caveat since not all 
program paths already use primitives; some will use the internal MetaFile 
format in-between (One more reason for more reworks to primitive usages 
in the future).
<br /> <br />I implemented most SVG features from SVG 1.1, but not yet 
using animations or interactions (but possible in the future due to an 
own interpreter, impossible with an external SVG renderer). It supports 
all geometric SVG forms. It supports SVG gradients (using a new primitive 
for this which will be reused when we add SVG gradients to 
SdrObjects one day), these have a resolution-dependent low-level format 
to not waste runtime on low resolutions. It supports masks, clipPath, markers, linked content, embedded graphics or SVG (intern, extern, 
base64), SVG use nodes, text, text on curve and patterns. It does not yet 
support filters, color profiles, embedded scripts, interactions and 
linking. These can be added when needed, most of them will need to 
implement new primitive types (e.g. filtering) which would be useful for the future
anyways.
Especially interesting is the possibility to later add SVG animation import to GraphicObjects for Impress.<br /> <br />Some side effects: I had to fix cropping (unified with new primitive) which 
works now also for mirrored graphics (never worked) and quite some other 
stuff. We are prepared for SVG gradients as possible future feature (we 
can already render them now). You can work with an added SVG as with a normal GraphicObject; crop it, break it (to SdrObjects, currently limited to the 
transfer over the old MetaFile format, though). You can convert an 
inserted Tux to 3D, you can bend the SVG in vector quality in Draw. It 
is possible to directly export the original SVG again by selecting the 
object and using 'Save as Picture...' from the context menu. You can add text, line style, fill 
style, pretty much the same as most other graphic objects. You can add 
shadow which casts shadow for the SVG graphic itself as expected (also not possible with an 
external renderer).
<br /> <br />This is a bigger change, but most stuff is isolated in the 
two mentioned services. There will be errors (I'm too long a programmer 
to deny that :-)), but I tried to be as careful as possible. I already got some help from other community members and fixed some reported bugs (kudos to all testers and bug writers), but to find 
the rest, your help is appreciated. Please feel free to play around with any 
SVG you can find in current AOO 3.4 builds and report problems early in the <a href="https://issues.apache.org/ooo/">Apache bugtracker</a>!
 </p> 
  <p><a href="http://eric.bachard.org/news/index.php?post/2011/12/03/In-progress-%3A-native-support-of-the-SVG-graphic-format-in-Apache-OpenOffice.org">Here</a> is another blog entry about an early version of this feature.<br />And <a href="https://cwiki.apache.org/confluence/display/OOOUSERS/AOO+3.4+Unofficial+Developer+Snapshots">here</a> are some developer snapshots of AOO 3.4 when you want to check it out. Be aware that these are AOO 3.4 Unofficial Developer Snapshots; these are intended to be used for early testing by other community volunteers.
  They have no release quality and should not be installed in a 
production environment.  Developer snapshots can be unstable and are 
expected to have bugs.  </p> 
  <p>Regards,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Armin<br /></p>

title: 'Merging Lotus Symphony:  Allegro moderato'
layout: post
date: '2013-01-21T16:40:35+00:00'
permalink: merging_lotus_symphony_allegro_moderato

<br /> 
  <div align="center"> 
    <p><a href="https://www.flickr.com/photos/nlireland/7057077503/" title="April 8, 1926 by National Library of Ireland on The Commons, on Flickr"><img width="500" height="383" src="https://farm6.staticflickr.com/5345/7057077503_9062b4a532.jpg" alt="April 8, 1926" /></a></p> 
  </div> 
  <p> </p> 
  <p> </p> 
  <p> </p> 
  <h2>The house lights flash; Please take your seats.&nbsp; The symphony is about to begin.<br /></h2> 
  <p><a href="http://www.openoffice.org/">Apache OpenOffice</a> will soon have some new features and other 
improvements, courtesy of IBM and their <a href="http://www-03.ibm.com/software/lotus/symphony/home.nsf/home">Lotus Symphony</a>&nbsp;effort.&nbsp; Interoperability, performance, accessibility improvements, as well as exciting new user interface elements are in the works.&nbsp; Read on to 
learn how the Apache OpenOffice volunteer community is doing this, and how this will benefit users of OpenOffice as well as developers who build upon OpenOffice. <br /></p> 
  <h2>Movement I:&nbsp; The Contribution.<br /></h2> 
  <p>IBM Lotus Symphony is an IBM licensed derivative of OpenOffice, offered at no charge, which <a href="http://wiki.openoffice.org/wiki/Symphony_contribution">IBM enhanced</a> for their customer and corporate use.&nbsp;&nbsp; Symphony was developed with OpenOffice.org technology, essentially a fork of OpenOffice.&nbsp; Last May IBM decided to end that fork and combine their development effort with the Apache OpenOffice project.&nbsp; IBM contributed the source code for Symphony to Apache, via a <a href="http://www.apache.org/licenses/cla-corporate.txt">Software Grant Agreement</a> (SGA).&nbsp;&nbsp; (An SGA is an agreement by which a code base developed outside of Apache is contributed to Apache under specified licensing terms.)&nbsp; Since the areas that IBM improved Symphony are also areas of interest for OpenOffice users, and for 3rd party products based on OpenOffice, the Apache OpenOffice project was glad to receive this contribution.</p> 
  <p>Once the Symphony contribution was received and checked into the Apache OpenOffice version control, the discussion to determine the best way to use this new code.&nbsp; The two primary options discussed on our mailing list were:</p> 
  <ol> 
    <li>Make the Symphony code the new base for Apache OpenOffice.&nbsp; Then merge back into Symphony the code improvements that had been made in Apache OpenOffice 3.4.<br /></li> 
    <li>Continue with the existing Apache OpenOffice 3.4 as the base and merge features from Symphony into that code.</li> 
  </ol> 
  <p>There were good arguments for either approach, and we had a spirited discussion.&nbsp;&nbsp; The main points were:<br /></p> 
  <ul> 
    <li>Using Symphony as the new base would have required careful review of that code base, and months of additional work to bring it up to Apache IP requirements.&nbsp; Essentially we would need to redo much of the work we had already done with the OpenOffice code that Oracle had contributed via their SGA.&nbsp; This would have been more disruptive to other, non-IBM, OpenOffice developers, but would have brought the distinguishing Symphony features to a release faster.</li> 
    <li>Merging Symphony features into OpenOffice would be less disruptive, but would be a slower path to integrating Symphony features, and would require more attention from IBM, since they know the Symphony code best.<br /></li> 
  </ul> 
  <p>In the end the consensus was to go with the 2nd option, merging Symphony code into OpenOffice.&nbsp;&nbsp; This brings the Symphony code, feature by feature, bug fix by bug fix, into OpenOffice, where it is integrated, tested, reviewed, etc., in smaller chunks, as it works its way toward release.&nbsp; Doing it this way is less flashy.&nbsp; There is no 'big bang integration&quot; where everything happens at once.&nbsp; But that was the point, to avoid the disruptions of a radical change in the code base.<br /></p> 
  <p>Work on the &quot;slow merge&quot; has been ongoing since last summer, in parallel with work on Apache OpenOffice 3.4.1.&nbsp; Our use of <a href="http://subversion.apache.org/">Apache Subversion</a> facilitated this kind of parallel development, where one group focused on the 3.4.1 release in a &quot;branch&quot;, another group of developers started to bring Symphony enhancements into the &quot;trunk&quot;.<br /></p> 
  <p> </p> 
  <p> </p> 
  <h2>Movement II:&nbsp; Many Bug Fixes<br /></h2> 
  <p>Expect to see a lot of bug fixes in Apache OpenOffice 4.0, especially in the area of Microsoft interoperability.&nbsp; The Symphony team reviewed their IBM bug reports from Symphony and pulled out the most important ones that were already fixed in Symphony.&nbsp; They then tested Apache OpenOffice, to see which of these bugs still existed in OpenOffice.&nbsp; For the ones that still were in OpenOffice, they merged in the fix from Symphony.&nbsp; This was a very efficient approach to a targeted merge and led to many fixes, include the following so far (and we're still months away from release):<br /></p> 
  <ul> 
    <li>
To open a sample file contains chart with large data source can lead to AOO crash</li> 
    <li>
Application crashed if undo paste text from shape</li> 
    <li>
Impress crashed when play screen show with sample file</li> 
    <li>
Crash if undo redo creating data pilot from imported data</li> 
    <li>
Application crash if insert sample file to section</li> 
    <li>
Application crashed if undo/redo covert nest table to text</li> 
    <li>
Undo redo insert file cause application crashed</li> 
    <li>User-defined format code is lost with a cell which value is TRUE or FALSE when importing xls file</li> 
    <li>
Loading performance for xls file with row banded style is bad</li> 
    <li>
Macro doesn't work if click &quot;Undo&quot; button</li> 
    <li>
Chart data lost if the source data refers to a range name which is defined as a reference formula</li> 
    <li>
Sample file's table border is missing</li> 
    <li>
Page number in footer display incorrectly</li> 
    <li>
Text is overlapped by the drawing object when open the .doc file</li> 
    <li>
&quot;Fit shape to text&quot; property not work after opening ppt by AOO</li> 
    <li>
It costs too much memory to open a large spreadsheet file containing pivot tables</li> 
    <li>
Numbering will lose when saving or opening a ppt file</li> 
    <li>
Color of underline display wrongly</li> 
    <li>
Grid size for snake wipe transition too fine</li> 
    <li>
Bookmark value changed when opening the doc file</li> 
    <li>
Repeat count of animations ignored.</li> 
    <li>
Fill color animations run too fast</li> 
    <li>
Table changes to multiple shapes after saved in AOO</li> 
    <li>
after save the sample file with page border and shadow to doc, the shadow depth and color changed</li> 
    <li>
The graphic's spacing is not correct when open the .doc file</li> 
    <li>
The graphic's border size and spacing is not correct when open the .doc file</li> 
    <li>
Animation color is not exported correctly to PPT.</li> 
    <li>
Number range variable filed shows in AOO</li> 
    <li>
import of Microsoft Word document: indent of certain paragraphs in list is wrong</li> 
    <li>
the text properties from table style are lost for table in the docx file</li> 
    <li>
the background color from table style are lost for table in the docx file</li> 
    <li>
Page number in footer alignment changed after saved</li> 
    <li>
Shape Gradient MS2003 import/export Enhancement</li> 
    <li>
Connector line does not show correctly in grouped object</li> 
    <li>
characters at the beginning of each lines in shape are lost when loading the sample ppt in AOO</li> 
    <li>
disable antialiased lines for background hatches</li> 
    <li>
Cell text direction changed after saved as doc file</li> 
    <li>
Time format is different than MS Office</li> 
    <li>
the text in textbox display partially when opening .ppt file</li> 
    <li>
After doc file saved by AOO, one more section is created</li> 
    <li>
Doc file saved by AOO, section size changed</li> 
    <li>
the text in the table turn to black from white when opening the pptx file</li> 
    <li>
the background of the file create from template 'blue_floral.otp' changed after save as the ppt or pot file</li> 
    <li>
Filter is not shown in merged cell</li> 
    <li>
Need press &quot;ESC&quot; key twice to exist chart edit mode</li> 
    <li>
Cannot modify the second document even if close range picker in first document</li> 
    <li>
Pie chart height becomes greater when open Excel file</li> 
    <li>
Ellipse shape display too large in MS Office after save odp file to ppt format file</li> 
    <li>
Formula GETPIVOTDATA returns #REF! value</li> 
    <li>
The Emphasis or Exit or Motion Path effect can not play if there is an Entrance effect after it.</li> 
    <li>
Picture missing when saving ODP file</li> 
    <li>
Number displays different from MS with the same format code</li> 
    <li>
TOC should not be updated if load doc in Writer</li> 
    <li>
Placeholder in ppt file created by MS 2007 is lost if load in Impress</li> 
    <li>
Text outside quotation cannot be paste in cell</li> 
    <li>Cannot open sample file</li> 
    <li>
Application crashed if undo add caption to drawing object</li> 
    <li>
Underline &quot;_&quot; can not work with &quot;;&quot; in format code, the semicolon will always be regarded as separator</li> 
    <li>
Last argument of formula should not be removed</li> 
    <li>
Removing chart in odt file, it causes a crash.</li> 
    <li>
Graphic in header and footer can not be displayed correctly</li> 
    <li>
Crash when redo split the pasted table</li> 
    <li>
Number formatting are changed after save and reopen it again.</li> 
    <li>
Import .pptx file into OO3.4, the vertical text direction of the table will be lost.</li> 
    <li>
Shape border and fill color lost if open the ppt doc via AOO</li> 
    <li>
Shape shadow position changed incorrect if open the ppt doc via AOO</li> 
    <li>
Fontwork alignment changes after saving to another ppt with AOO</li> 
    <li>
The graphic background in left table display incorrectly when using AOO open the sample .ppt file</li> 
    <li>
Vertical text direction in table cell change to horizontal after saving to another .ppt by AOO</li> 
    <li>
The vertical text alignment of the placeholder is wrong while opening the ppt file in AOO</li> 
    <li>
all drawing objects lost aftering saving to another ppt by AOO</li> 
    <li>
Line transparency value is lost after saving as another ppt by AOO</li> 
    <li>
Graphic bullet is incorrect in the .ppt doc which saved via AOO</li> 
    <li>
The bullet in outline area lost after opening by AOO</li> 
    <li>
Some shapes in master page lose after save to another ppt by AOO</li> 
    <li>
The position of connector change after save to another ppt by AOO</li> 
    <li>
Froze when saving the doc file to another one.</li> 
    <li>
TOC jumping function lost if save document by AOO</li> 
    <li>
star and symbol shape in ppt changed after opening by AOO</li> 
    <li>
Transparency setting of Fill color lost in cell comments.</li> 
    <li>
animation flash once doesn't work after save the ppt by aoo</li> 
    <li>
exit animation changed after save as ppt file to another ppt</li> 
    <li>
Page number lost if save template to doc format</li> 
    <li>
Some numbering format not support</li> 
    <li>
Additional dot appear after the numbering.</li> 
    <li>
Apply Envelope page style cause application crash</li> 
    <li>
Crash after delete column(s) from chart's source table, and then adjusted table size</li> 
    <li>
[Crash]When press &quot;Ctrl+Shift+Backspace&quot; in table cell &quot;A1&quot; ,Undo,crash</li> 
    <li>
Font size increased if saved by AOO</li> 
    <li>
Hyperlink font size increased if saved to .doc file</li> 
    <li>
Function &quot;Case sensitive&quot; in &quot;Special Filter&quot; dialog can not work.</li> 
    <li>
Shape shadow lost if load .doc file in AOO</li> 
    <li>
Macro button lost if save template to .doc file</li> 
    <li>
Teardrop shape can not show correct in pptx sample file</li> 
    <li>
Bullet color is lost when open pptx sample file</li> 
    <li>
Arrow shape changed is save doc file by AOO</li> 
    <li>
Outline level in sample file lost</li> 
    <li>
the .doc page number is incorrect when opened in aoo 3.4</li> 
    <li>
[BiDi]The order of Hebraic string are changed after save as new .doc</li> 
    <li>
Alphabetical and roman numerals became digital numbering</li> 
    <li>
Text font spacing in comments doesn't expand/condense by the expected value</li> 
    <li>
The left-style columns display with the same width when opening with AOO</li> 
    <li>
MS Word that has Table that with Text wrap around the table can not be shown correctly</li> 
    <li>
MS's Macro button symbol can't correct display in aoo 3.4</li> 
    <li>
][BIDI]The position and direction of Right bracket is incorrect in Arabic locale</li> 
    <li>
Paragraph indent and spacing between bullets and text are inconsistent with MS Word</li> 
    <li>
the content display mess when open the sample in AOO3.4</li> 
    <li>
WMF graphic size changed too small to see if saved by AOO</li> 
    <li>
The text box style display incorrectly when open the sample in AOO3.4</li> 
    <li>
Vertical letters in &quot;VerticalText&quot; fontwork get horizontal when opening .ppt file</li> 
    <li>
Table rows get higher when opening a .docx file with AOO 3.4</li> 
    <li>
Column header can not be displayed correctly in AOO3.4 after open the xls file.</li> 
    <li>
font size of Fontwork changes from 96 to 36 after save as new .doc file</li> 
    <li>
Text anchor in subtitle text box is changed from Top to Center when open a pot template in AOO3.4</li> 
    <li>
Can't pop up protect password dialog when attempt to unprotect sheet with password for xls file in AOO.</li> 
    <li>
Can't open by MS Office correctly when save sample file contain line with text to ppt format file</li> 
    <li>
Position of drawing obj incorrect when opening .doc in aoo 3.4 if the text direction of the whole document is vertical</li> 
    <li>
paragraph&gt;pagination&gt; <wbr />Window/Orphan control setting lost after save the .doc file by aoo 3.4</li> 
    <li>
The title text is Align left in sample file, while in MS Office, it is aligned right.</li> 
    <li>
he table border got lost when open the .ppt file in AOO</li> 
    <li>
The title text is not Italic in Studio design template like that in MS Office.</li> 
    <li>
sequence number is not displayed when open docx</li> 
    <li>
Failed to open sample file but no any feedback to user</li> 
    <li>
&lt;Shape&gt;&lt;Extrusion&gt;The Extrusion direction of shape can't be saved correctly</li> 
    <li>
arrow change size and position in MS after save odp to ppt format</li> 
    <li>
Trendline of two Data Series can't be displayed but after edit it the trendline will be shown correctly</li> 
    <li>
the bullet color display incorrectly in AOO3.4</li> 
    <li>
the subtitle area of ppt file display incorrectly in AOO3.4</li> 
    <li>
Can not open the sample ppt file which contain vb controls in the slide master.</li> 
    <li>
The line indent change after save once by AOO</li> 
    <li>
the right brace shape cannot display after save the sample .odt file to .doc file then reopen in aoo</li> 
    <li>
One shape's border cannot be displayed completely</li> 
    <li>
Text and fill color in a table are lost while opening a ppt file</li> 
    <li>
Text in a text box can not be displayed correctly</li> 
    <li>
a pic in the .doc file cannot display in Aoo 3.4</li> 
    <li>
The numbering in table cell changes to bullets when saved in AOO</li> 
    <li>
Item lists are incorrectly imported by Symphony.</li> 
    <li>
Picture is lost when opening sample PPT file</li> 
    <li>
Import file created by MS Excel, if there is blank item selected in Page filed of Pivot Table, the selection will be lost.</li> 
    <li>
one column is lost if opened in AOO</li> 
    <li>
[Crash]When save the file as ppt, AOO crashes</li> 
    <li>
PPT Import:Word Art becomes larger</li> 
    <li>
Arrow style of line changes after save the sample file to a new .ppt file.</li> 
    <li>
AOO crash if a connector which connected to PPT table</li> 
    <li>
The .xlsx sample file is opened with modified state</li> 
    <li>
Under Handout view mode, Header&amp;Footer displays inconsistent with the one presented in MS PowerPoint</li> 
    <li>Images lose macro association when open Excel file in AOO.</li> 
    <li>
TOC lost if saved by AOO</li> 
    <li>
PPT Import:Cell background color in table gets lost while opening a ppt file with AOO</li> 
    <li>
PPT Export: Diagram bullet can not be displayed correctly after saved as *.ppt in AOO</li> 
    <li>
page number in header lost when we save the .doc file as another in web layout</li> 
    <li>
Picture shadow lost after saved by AOO</li> 
    <li>
Form controls cannot be saved into .ppt file in AOO3.4</li> 
    <li>
text alignment changed from left to center when importing the docx</li> 
    <li>
The position of Shape (connectors) in slide is incorrect after save once by AOO3.4.</li> 
    <li>
The image OLE's icon doesn't display correctly in Aoo3.4</li> 
    <li>
Formula field lost</li> 
    <li>
the shape 3D property effect in MS PPT can't be load correctly.</li> 
    <li>
Some field is not shown</li> 
    <li>
White block( on Mac and Black block on Windows) appears if click somewhere else in presentation</li> 
    <li>
Presentation crashed if exit screen show</li> 
    <li>
Writer crash after modify properties of new Frame</li> 
    <li>
Calc crashes when Redo refreshing data</li> 
    <li>
Create summary slide in .odp file which has expanded blank slides in,there is a crash.</li> 
    <li>
Calc crashed if paste unsupported formula from MS Excel</li> 
    <li>
Worksheet.Change event works not correctly</li> 
    <li>
Application.Run could not work correctly</li> 
  </ul> 
  <p> </p> 
  <p> </p> 
  <p> </p> 
  <p>&nbsp;On our wiki you can see a <a href="http://wiki.openoffice.org/wiki/Documentation/Fidelity_Improvement_Since_AOO341">visual &quot;before &amp; after&quot;</a> look and some of these fixes.<br /></p> 
  <h2>Movement III:&nbsp; New Features</h2> 
  <p>
  Of course, a long list of bug fixes is impressive, but what about new features?&nbsp;&nbsp; Symphony brings those as well.&nbsp; A large one is a user interface addition of a &quot;Task Pane&quot;.&nbsp; Since a Task Pane is continuously available, it can greatly improve productivity with some repetitive operations.&nbsp; Symphony had one version of this feature, but we're not just doing a literal copy of that UI, since grafting a UI of one application onto another is rarely successful.&nbsp; So we're reviewing several <a href="http://wiki.openoffice.org/wiki/AOO_UX_Design_Exploration_-_Task_Pane_Content_Panel_-_User_Interface_Design_Proposals">variations on a Task Pane design</a>, which you can see on our wiki.&nbsp; Coding for this feature is ongoing in a branch.<br /></p> 
  <p>Symphony had a nice collection of clipart and themes, and we're bringing those into OpenOffice. <br /></p> 
  <p>IAccesible2 is an interface used by &quot;assistive technologies&quot; (screen readers, etc.) to help persons with disabilities use desktop applications.&nbsp; We're bringing the IAccesible2 support from Symphony into OpenOffice.&nbsp;&nbsp; Coding for this feature is also ongoing in a branch.</p> 
  <p> <br /></p> 
  <h2>Movement IV:&nbsp; più allegro, anyone?<br /></h2>That's a summary of what Symphony is bringing to Apache OpenOffice 4.0 and beyond.&nbsp; Users of OpenOffice will benefit from these enhancements, of course.&nbsp; But so will other products, based on Apache OpenOffice, as they build their solutions on top of Apache OpenOffice, or selectively copy functionality from our releases.&nbsp; <br /> 
  <p>When exactly will Apache OpenOffice 4.0 be released?&nbsp; We don't have a date set yet, but we think it will be before mid-year.&nbsp; As a volunteer-led open source project we rely on our volunteers to set the direction and pace of the work.&nbsp; We welcome help in any of these areas, from developers of course, but also from associated project functions, like QA, design, documentation, translation, marketing, etc.&nbsp; If you are interested in volunteering with the Apache OpenOffice project, please read our &quot;<a href="http://openoffice.apache.org/get-involved.html">Getting Involved</a>&quot; page. With your help we can go even faster!<br /></p> 
  <p><br /></p> 
  <p> </p> 
  <p><br /></p>

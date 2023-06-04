title: 'The Sidebar: New And Improved'
layout: post
date: '2013-06-04T06:49:57+00:00'
permalink: the_sidebar_new_and_improved

<p> Usually the phrase &quot;new <i>and</i> improved&quot; does not make much sense because something either is new <i>or</i> did already exist and was improved upon.&nbsp; For the sidebar the situation is a little different.&nbsp; The core implementation is new but the content, the panels, did already exist.&nbsp; The concept, but not the name, of a sidebar has existed for many years both in Apache OpenOffice (and OpenOffice.org before that) and in IBM Lotus Symphony.&nbsp; In OpenOffice.org it was named &quot;task pane&quot; and was used primarily in Impress to give access to backgrounds, layouts, and shape and slide animations.&nbsp; Symphony renamed this to &quot;property panel&quot;, extended it to all applications and covered even more frequently used tasks.</p> 
  <p align="center"><a href="https://blogs.apache.org/OOo/mediaresource/e18c8858-4a7d-4e26-bf21-093bf64b3e44"><img width="344" height="217" src="https://blogs.apache.org/OOo/mediaresource/e18c8858-4a7d-4e26-bf21-093bf64b3e44" alt="Screenshot of Impress with sidebar." /></a><br /> </p> 
  <h3>So, what did you improve?</h3> 
  <p>The sidebar panels come from three different sources and have been improved in the migration process:<br /> </p> 
  <ul> 
    <li>The property panels that let you for example change the size of text or the color of shapes have all been migrated from Symphony.&nbsp; In the process we have cleaned up the code, made some improvements and fixed many bugs.&nbsp; While the property panels work really well, their implementation could profit from more cleanup.&nbsp; Removing duplicated code could reduce their code size and their complexity considerably.&nbsp; The one new property panel for inserting shapes into draw documents has roughly one tenth the number of code lines of the text property panel and still has about the same number of controls.<br /></li> 
    <li>The Impress panels come from OpenOffice.&nbsp; They allow you for example to control animations of slides and shapes.&nbsp; The new framework of the sidebar made big cleanups of their implementations possible.&nbsp; They are not view shells anymore; they are now regular controls.&nbsp; If you don't know what a view shell is, good for you.</li> 
    <li>The third group consists of non-modal dialogs like the Navigator, the Gallery, or the <i>Styles and Formatting</i> dialog.&nbsp; Only small changes were necessary to plug them into the sidebar.<br /></li> 
  </ul> 
  <h3>And what is new?</h3> 
  <p>The core implementation of the sidebar and the framework provided for panel developers is completely new.&nbsp; The sidebar looks similar to the Symphony property panel but shares no code with it.&nbsp; One important new feature is that the sidebar is easily configurable via the, well, configuration.&nbsp; Another one is that extensions can now add new decks and panels that can freely mix with existing decks and panels.&nbsp; More on that later.</p> 
  <h2>What exactly is &quot;the sidebar&quot;? 
  </h2> 
  <p>The sidebar is a window at the right side of the edit view of Writer, Calc, Impress and Draw.&nbsp; It provides access to frequently used tasks when editing documents. The content in the sidebar is organized into decks and panels.&nbsp; Decks are containers of panels, one or more of them.&nbsp; In very few cases there may not yet be a panel available for the current task. You can switch between decks by clicking on buttons in the tab bar at the right side of the sidebar. A menu allows you to hide decks that you don't need.<br /><br />The deck that is open by default is the &quot;Properties&quot; deck.&nbsp; Its set of panels is context sensitive and varies depending on what you are currently doing.&nbsp; For example, if you are editing text in Writer then the &quot;Text&quot; panel allows you to change the font, text attributes, text and background color.&nbsp; The &quot;Paragraph&quot; panel has controls for changing bullet style, text alignment and various indents.&nbsp; The &quot;Page&quot; panel lets you change page size and orientation.&nbsp; It is collapsed by default.&nbsp; That means that you can only see its title bar.&nbsp; One click on it and you can see the panel.&nbsp; This avoids cluttering the user interface with panels that are only used occasionally while at the same time making them easily accessible for when they are used.</p> 
  <p align="center"><a href="https://blogs.apache.org/OOo/mediaresource/0f541205-06c7-4e1b-bf06-31f1a8f008b1"><img width="431" height="362" align="middle" src="https://blogs.apache.org/OOo/mediaresource/0f541205-06c7-4e1b-bf06-31f1a8f008b1" alt="The different parts of the sidebar" /></a></p> 
  <h2>Why do you call it sidebar and not...?</h2> 
  <p>The Symphony name &quot;property 
panel&quot; did not work for us because the sidebar contains more than just 
information about document properties.<br /></p> 
  <p>The OpenOffice.org name
 &quot;task pane&quot; came from the never realized idea of making OpenOffice.org 
more task oriented.&nbsp; For example for the creation of form letters this 
could have been an adapted version of the mail merge wizard that would 
have displayed the general workflow and given access to templates, 
address books and so on.&nbsp; This idea proved to be too difficult to 
realize.<br /><br />The name &quot;sidebar&quot; is generic enough to host very 
different content such as document properties, clip art, navigator or 
third party extensions.&nbsp; At the same time it is descriptive enough to be
 remembered easily.&nbsp; Should you ever turn off the sidebar by accident 
then you will have no problem finding the menu entry for the &quot;bar&quot; at 
the &quot;side&quot; of the edit view and turn it back on.<br /></p> 
  <h2>Why add the sidebar now, why at all?</h2>Up to now, we, the OpenOffice community (developers, UXers, testers), were busy getting the project going at our new home in the Apache community.&nbsp; After that came two releases and then graduation.<br /> 
  <p><br />Only after that did we finally have the time to tackle the major task of combining the sidebars of OpenOffice and Symphony.<br /><br />Many users have asked us in the past to add a Symphony-like sidebar to OpenOffice.&nbsp; The feedback in the Apache community regarding the sidebar in the coming release is very positive.&nbsp; Even downstream has started to integrate our implementation.&nbsp; Some of the benefits of the sidebar are:<br /></p> 
  <p> </p> 
  <ul> 
    <li>As in toolbars you have the most important functions for the current task available on a single click.&nbsp; Unlike the toolbars it does that in a single place while some toolbars are docked above the edit view, some are docked below, and still others are displayed floating in front of it.</li> 
    <li>The position on the right side takes advantage of the form factor of most modern screens that have much more space in the horizontal direction than in the vertical.</li> 
    <li>The sidebar provides more space to its panels than the tool bar areas provide to tool bars.&nbsp; Therefore panels can display more information better.</li> 
    <li>The sidebar has a constant size (unless you decide to change that size).&nbsp; Context changes lead to different panels being displayed but do not change the size of the sidebar or the edit view.&nbsp; Dock a context sensitive tool bar and you will know how annoying such size changes can be.<br /></li> 
  </ul> 
  <h2>What about extensions?</h2> 
  <p> </p> 
  <p>A little known feature of OpenOffice is that extensions can provide panels for the task panel (now called sidebar).&nbsp; These extensions are still supported.&nbsp; But now there is a better way to do this.<br /><br />You can add a panel that is implemented in any language supported by the UNO API and display this panel in a deck of your choice or even in the properties panel.&nbsp; The panel can react to context changes such as different selections.&nbsp; But it does not have to.&nbsp; You want a panel that is only displayed when editing tables in Writer documents? No problem.&nbsp; You want to analyze a Calc document and display the result in real-time and always visible?&nbsp; That is possible. Or you can display the current time or weather.</p> 
  <p>Here is an example:&nbsp; an extension adds a deck (see the clock icon in the tab bar) and a panel that shows the current time.<br /></p> 
  <p align="center"><a href="https://blogs.apache.org/OOo/mediaresource/6e289a7f-8ee2-46bd-9981-31f0c127e942"><img width="119" height="223" align="middle" alt="Clock added to sidebar by extension." src="https://blogs.apache.org/OOo/mediaresource/6e289a7f-8ee2-46bd-9981-31f0c127e942" /></a><br /></p> 
  <h2>We need your input</h2>The toolbars and dialogs such as gallery and navigator are not yet scheduled to be disabled by default or even to be removed.&nbsp; Not because we don't think that the sidebar works.&nbsp; It does.<br /> 
  <p>The reason for keeping these established user interface elements is to let you become familiar with the sidebar in your own time.&nbsp; We hope that you will use the toolbars and dialogs less and less.<br /></p> 
  <p>Apache OpenOffice is an open source project.&nbsp; You can help by telling us what you don't like and what you miss. Share your ideas about how to make the sidebar better. Write a comment in the comment section below or subscribe to our <a href="http://openoffice.apache.org/mailing-lists.html#development-mailing-list-public" title="Apache OpenOffice development mailing list">development mailing list</a> if you are willing to invest a little more time.&nbsp; And Apache also accepts <a title="how to make a donation" href="http://www.apache.org/foundation/contributing.html">donation</a><a href="http://www.apache.org/foundation/contributing.html" title="how to make a donation">s</a> (not project specific).<br /> </p>

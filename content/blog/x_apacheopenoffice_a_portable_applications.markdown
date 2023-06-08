title: 'X-ApacheOpenOffice: A Portable Applications Version of Apache OpenOffice from winPenPack'

layout: post
date: '2013-04-04T12:12:08+00:00'
permalink: x_apacheopenoffice_a_portable_applications

<p>We receive many questions from users looking for a portable version of Apache OpenOffice.&nbsp; &quot;Portable Applications&quot;<span lang="en"><span></span></span> are software applications designed or adapted to run from portable storage, like a USB memory stick, without requiring an installation.&nbsp; Such applications allow you to bring your applications, settings and documents with you.&nbsp; One popular portable version of OpenOffice is &quot;<a href="http://www.winpenpack.com/en/download.php?view.1341">X-ApacheOpenOffice</a>&quot;, from the <a href="http://www.winpenpack.com">winPenPack</a> open source project. &nbsp; We interviewed the founder of winPenPack, <span class="il">Danilo</span>
 Leggieri, and his team to learn more. </p> 
  <p> </p> 
  <p align="center"><br /><img src="../images/blog/x_apacheopenoffice_a_portable_applications_winPenPack.png" /></p> 
  <p align="left"> </p> 
  <p><br /></p> 
  <h3>What is winPenPack? &nbsp;How did the project start? &nbsp; How many people work on the project?
</h3> 
  <p> </p> 
  <p> </p> 
  <div class="gmail_quote"> 
    <div class="im"> 
      <div> </div> 
    </div> 
    <div> 
      <p>Well, it is really difficult to describe in a few words what this project 
is for us, because since from the first moment has begun to be part of our 
own life...&nbsp; Briefly we can say that winPenPack is an Italian open source
 project that deals with portable software, both natively portable <i>and portabilized</i> by means of X-Launcher, our portable program launcher. These
 apps can be grouped into suites or can be used also as standalone 
portable programs, adapting with end users preferences.<br /></p> 
      <p>winPenPack philosophy is well summarized by our (very restrictive) definition of 
&quot;portable software&quot;: a portable program can't simply be a &quot;no-install&quot; 
program, but must also be able to save its settings into his own folder 
(or a user-definable folder), does not write settings or leave other data in user folders (i.e. into 
c:\Users\TheUserName\AppData\<wbr />Roaming\ or c:\Documents and 
Settings\TheUserName) or into the registry, must be able to run from a 
USB pen drive and can perform path normalizations moving around different 
PCs (where the pen drive could be installed with different drive letters).
 Obviously, all of these programs can be executed also from hard 
drives, greatly simplifying recovery operations of all programs (and 
their preferred configurations) when reinstalling the operating system.<br /><br />Our
 project started in November 2005 by a brilliant intuition of <span class="il">Danilo</span>
 Leggieri (AKA Danix, the founder of the project). <span class="il">Danilo</span> and a couple 
of &quot;web friends&quot; expanded the project and the community grew very 
quickly. Since that date, we have issued about 20 new releases and hundreds
 of Open Source portable applications. Actually, the project is well 
known in Italy and is growing also abroad. winPenPack is hosted on 
SourceForge and all the collections are regularly distributed also in 
bundles with some IT magazines. The community of users has grown over 
the years and has actively contributed to the growth of the whole project. 
<a href="http://www.winpenpack.com">The site</a> currently hosts various projects created and suggested also by forum members, and is also used for bug reporting and users 
suggestions.<br /><br />Currently, the project involves 6 officially active 
people and a lot of contributors (translators, testers, and so on). All 
of them are spending their time completely for free, working on the 
project out of pure passion. Each member of the staff has a different 
job in &quot;normal life&quot;, not necessarily connected to the world of computer
 and information technology.<br /><br /></p> 
      <h3>How do you make a winPenPack application? &nbsp;What kinds of things do you need to do to make a desktop application portable?
</h3> 
    </div> 
    <div><br />The core of all our portabilizations is X-Launcher, the winPenPack 
program launcher. A program portabilized by X-Launcher is called an &quot;X-Program&quot;. The folder structure of any X-Program always contains a \Bin 
folder (the program folder) and a \User folder (the settings folder), plus
 other optional folders, such as \Documents or \Downloads (depending on the 
nature of the portabilized program). At the root of this structure there
 is X-ProgramName.exe (the launcher of &quot;ProgramName&quot; program) and 
X-ProgramName.ini (the text file that contains all the settings and 
instructions for X-ProgramName.exe to make portable the portabilized 
program). Due to its nature, the .ini file can be easily edited with any
 text editor, simplifying the creation, the testing and the fine-tuning of 
the portabilization. The various sections of the X-ProgramName.ini file 
allow us to define the X-Launcher behavior towards the registry or the 
user folders or to perform other actions. We can easily copy or move 
registry keys or files or folders back and forth beween the USB pen drive
 and the PC hard drive,&nbsp; leaving the host PC
 in the exactly same state it was before we executed it on our 
X-Program.&nbsp; So X-Launcher allows us to recreate the environment in which a 
program works correctly (registry keys, user folders, etc.), but, after 
the program execution completes, it leaves the PC &quot;clean&quot;, because when closing the 
program all these keys (or files) are moved back into the \User folder 
of the portabilized program folders structure, ready to recreate the 
environment at the next execution.<br /><br />The process of portabilization of a
 program passes through various steps. First of all, someone (a team 
member or a forum user) signals an interesting program. We test its 
portability through <a href="http://sourceforge.net/projects/regshot/">RegShot</a>, which helps us understand if the program 
uses the registry or the user folders for saving its settings or for 
other purposes.&nbsp; If, after our tests, the program turns out to be 
natively 100% portable, it is added to the &quot;Portable Software&quot; section 
of our Download area. If the program is not fully portable, we check 
whether it is possible to make it portable through X-Launcher. This 
phase reuses all the information gathered during portability tests to 
determine which features of X-Launcher should be enabled to portabilize
 the program.&nbsp; This is the most important step, that requires all the 
portabilization skills of our developers, and often makes the difference
 between being able to consider a program portabilizable or not. The 
last step is the packaging of the X-Program and its distribution through
 our &quot;X-Software&quot; Download area. Sometimes even 100% portable programs 
can receive some benefit from X-Launcher (for example, backups of 
configurations, paths normalization, use in conjunction with external 
libraries like Java), so we create also X-Programs of that kind.<br /><br /> 
      <h3>Did you run into any special challenges when making the portable version of Apache OpenOffice (X-ApacheOpenOffice)? &nbsp;Are there any changes we could make in the OpenOffice to make portable versions more powerful?
</h3> 
    </div> 
    <div> 
      <p><br />For developing X-ApacheOpenOffice Portable we were able to put into 
practice our previous knowledge acquired in past years with early 
versions of OpenOffice. This background helped us a lot for speeding up 
the development of X-AOO Portable. </p> 
      <p>The more relevant features added to Apache OpenOffice for building the completely portable X-ApacheOpenOffice Portable are:<br /></p> 
      <ol> 
        <li>Path normalization: all paths of recent files that are saved into X-AOO Portable folder structure have been normalized</li> 
        <li>&quot;System&quot; folders: the \Documents and \Backups X-ApacheOpenOffice 
Portable subfolders have been set as &quot;system&quot; folders, also moving the 
main folder</li> 
        <li>Disabled quickstart.exe: quickstart.exe has been 
disabled to prevent the soffice.exe process from remaining active in the traybar
after closing the program, or when the user tries to disconnect
 the USB pen drive from the PC</li> 
        <li><a href="http://www.winpenpack.com/en/page.php?39">JavaGet</a> integration: the 
integration of JavaGet functions into the launcher allows X-AOO to work
 with or without a Java installation present on the host PC</li> 
      </ol> 
      <p><br />We
 haven't had particular challenges to develop our portable version (just 
some extra-time due to the download of all language versions to be 
merged into one single X-Program). However, the fact that Apache 
OpenOffice recognizes automatically the OS language has simplified our 
work, allowing us to have a single launcher. For the future we would 
like very much also a monolithic multi-language setup of Apache 
OpenOffice to be used as a base for our portable X-ApacheOpenOffice 
Portable.<br /><br /></p> 
      <h3>When I think of portable applications I think mainly of putting apps on USB keys. &nbsp;But are you seeing any other interesting uses, like people running their apps from the cloud, DropBox, etc.?</h3> 
    </div> 
    <div><br />Portable programs aren't simply &quot;apps to be run from USB keys&quot;. 
Portable programs allow the users to carry in their pockets all their 
preferred applications, with all their preferred settings, to be run anywhere they find a Windows PC with a free USB port. That's it. We 
could even say that the portable programs were the forerunners of the 
cloud: your programs, everywhere...&nbsp; At this moment, we see cloud apps 
more oriented to mobile devices (that are &quot;portable&quot; by definition). 
Windows programs need an operating system in which to be executed. If we 
would be able to run Windows portable programs from the cloud, the only 
thing that we would do without would be exactly our USB pen drive...&nbsp; <br /><br /> 
      <h3>Where can readers go to learn more about winPenPack or to help with the project?
</h3> 
    </div> 
  </div><br />Of course on <a href="http://www.winpenpack.com">our site</a>! We have a <a href="http://www.winpenpack.com/en/page.php?10">&quot;Documentation</a>&quot; section that with 
considerable efforts we have translated almost entirely in English, in 
order to help as many users as possible. We have also 
an <a href="http://www.winpenpack.com/en/e107_plugins/forum/forum_viewforum.php?24">English forum</a> where we answer all users' questions and discuss any 
other aspect of programs portabilization. You all are welcome to visit 
us and donate to the project to allow us to continue to develop even 
more exciting portabilizations! <br /><br /><br />

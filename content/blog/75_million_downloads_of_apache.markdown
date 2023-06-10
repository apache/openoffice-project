title: 75 Million Downloads of Apache OpenOffice
layout: post
date: '2013-10-30T19:02:24+00:00'
permalink: 75_million_downloads_of_apache

We are pleased to report that yesterday, October 29th, someone downloaded the <b>75,000,000th </b>copy of&nbsp; Apache OpenOffice™. &nbsp; The 75 million downloads have occurred in the less than 18th months since the first release of Apache OpenOffice on May 8th, 2012.&nbsp; 
  
  
  
  
  
  
  
  
  <p>Apache OpenOffice (formerly called OpenOffice.org) is the leading free and open source office application suite for Windows, Mac and Linux.&nbsp; <br /></p> 
  <p>Although we're all very busy now with working on our next major release, Apache OpenOffice 4.1, it is worth taking a few minutes to explore some of the trends that can be discerned from our download data.&nbsp; The information we have gathered, relative to desktop OS versions, 64-bit Linux use, etc.,&nbsp; may be of special interest to other open source projects to consider in their 
planning. <br /></p> 
  <p> </p> 
  <p>First a scatter plot of daily download numbers, with a 7-day moving average overlay.&nbsp; Each of our releases is marked by a vertical line.&nbsp; You can clearly see the increase in interest since the release of Apache OpenOffice 4.0.<br /></p> 
  <p><br /></p> 
  <p><br /></p> 
  <p align="center"> <img src="../images/blog/75_million_downloads_of_apache_day.png" alt="daily-downloads.png" /></p> 
  <p> </p> 
  <p align="left"> </p><br /> 
  <p> </p> 
  <p align="left"> </p>We are able to break down these trends along several other dimensions.&nbsp; One is by country, looking at where the download request came from.&nbsp; This information is gleaned from the IP address of the machine making the request.&nbsp; Since each IP address is part of an assigned block of addresses, and blocks are assigned geographically, we can create a table of downloads by country, territory, etc.&nbsp; We show the <a href="http://www.openoffice.org/stats/countries.html">full table</a> on our website, of all 238 countries, territories, etc., but here are the top 10: 
  
  
  
  
  
  
  
  <p> </p> 
  <p> </p> 
  <p align="center"> </p> 
  <p> </p> 
  <table border="1" align="center"> 
    <tbody> 
      <tr> 
        <td align="right">#1</td> 
        <td>United States</td> 
        <td align="right">14,148,707</td> 
      </tr> 
      <tr> 
        <td align="right">#2</td> 
        <td>France</td> 
        <td align="right">9,622,464</td> 
      </tr> 
      <tr> 
        <td align="right">#3</td> 
        <td>Germany</td> 
        <td align="center">7,363,242</td> 
      </tr> 
      <tr> 
        <td align="right">#4</td> 
        <td>Italy</td> 
        <td align="right">6,239,913</td> 
      </tr> 
      <tr> 
        <td align="right">#5</td> 
        <td>Japan</td> 
        <td align="right">3,944,256</td> 
      </tr> 
      <tr> 
        <td align="right">#6</td> 
        <td>United Kingdom</td> 
        <td align="right">3,316,827</td> 
      </tr> 
      <tr> 
        <td align="right">#7</td> 
        <td>Spain</td> 
        <td align="right">2,756,638</td> 
      </tr> 
      <tr> 
        <td align="right">#8</td> 
        <td>Russia</td> 
        <td align="right">2,693,113</td> 
      </tr> 
      <tr> 
        <td align="right">#9</td> 
        <td>Canada</td> 
        <td align="right">2,177,430</td> 
      </tr> 
      <tr> 
        <td align="right">#10</td> 
        <td>Poland<br /></td> 
        <td align="right">1,569,020</td> 
      </tr> 
    </tbody> 
  </table> 
  <p> </p> 
  <p> </p> 
  <p> </p> 
  <p>Another approach is to look at which localized versions of Apache OpenOffice were downloaded.&nbsp; We can see these trends in the following dot chart:</p> 
  <p> </p> 
  <p> </p> 
  <p align="center"><img src="../images/blog/75_million_downloads_of_apache_languages.png" alt="languages.png" /></p> 
  <p>We can also look at the trend over time of downloads by operating system.&nbsp;&nbsp; (Note the log-scale on the Y-axis.)&nbsp; OpenOffice is a mainstream open source desktop application, so the OS distribution reflects overall desktop operating system market shares:<br /></p> 
  <p align="center"><img src="../images/blog/75_million_downloads_of_apache_os-downloads_64-bit.png" alt="os-downloads.png" /></p> 
  <p>Since we have Linux versions of OpenOffice packed as RPMs (e.g., for RedHat) as well as DEBs (e.g., for Ubuntu), we can look for trends in the ratio of requests for these two packaging formats over time:<br /></p> 
  <p align="center"> <img alt="packaging.png" src="../images/blog/75_million_downloads_of_apache_packaging.png" /></p> 
  <p> </p> 
  <p>Also, we have 32-bit and 64-bit Linux downloads, and we see a gradual increase in demand over time for the 64-bit version, now reaching 50%.&nbsp; (The drop in July-September is not fully explained, but may have been an error in our download page that was not recommending 64-bit downloads appropriately.)<br /></p> 
  <p align="center"> <img src="../images/blog/75_million_downloads_of_apache_64-bit.png" alt="64-bit.png" /></p> 
  <p> </p> 
  <p>Although we don't have detailed download data for different Windows versions (we have a single download for all Windows users) we do have information from website visitors (nearly 7 million visitors per month) that tells a similar story.&nbsp; Windows 7 remains the most popular Windows version for our users, accounting for over half of Windows visitors.&nbsp; Windows XP ties with Windows 8 for second place, though Windows XP usage is declining quickly.<br /></p> 
  <p> </p> 
  <p align="center"><img alt="windows-version.png" src="../images/blog/75_million_downloads_of_apache_windows.png" /></p> 
  <p>Looking at the similar data for web browsers, we see the rise in Chrome users among our website visitors:<br /></p> 
  <p align="center"><img src="../images/blog/75_million_downloads_of_apache_browsers.png" alt="browsers.png" /></p> 
  <p> </p><br /> 
  <p> </p> 
  <p>The above charts were made in <a href="http://www.r-project.org/">R</a>, using data from <a href="http://sourceforge.net/p/forge/documentation/Download%20Stats%20API/">SourceForge's REST API</a> and from Google Analytics.&nbsp;&nbsp; The processing of the SourceForge data was automated via a <a href="https://svn.apache.org/repos/asf/openoffice/devtools/aoo-stats/detail-by-day.py">custom Python script</a>.<br /></p> 
  <p> </p> 
  <p align="center"><br /></p> 
  <p> </p> 
  <p> </p> 
  <p><br /> </p>

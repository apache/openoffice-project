layout: post
title: 'Apache OpenOffice: One Year, 50 Million Downloads'
layout: post
date: '2013-05-15T17:19:19+00:00'
permalink: apache_openoffice_one_year_50

<p>We are pleased to note that yesterday we reached the <b>50 million download mark</b> for Apache OpenOffice 3.4. &nbsp; This milestone occurred within a few days of the first anniversary of the release of Apache OpenOffice 3.4., on May 8th, 2012.&nbsp; <br /></p> 
  <p>Apache OpenOffice (formerly called OpenOffice.org) is the leading free and open source office application suite for Windows, Mac and Linux.&nbsp; Version 1.0 of OpenOffice was released 11 years ago, in May 2002.<br /></p> 
  <p>Although we're all very busy now with the testing of our next major release, Apache OpenOffice 4.0, it is worth taking a few minutes to explore some of the trends that can be discerned from our download data over the past year.&nbsp; The information we have gathered, relative to desktop OS versions, 64-bit Linux use, screen aspect ratios, etc.,&nbsp; may be of special interest to other open source projects to consider in their 
planning. <br /></p> 
  <p> </p> 
  <p>First a scatter plot of daily download numbers, with a 7-day moving average overlay.&nbsp; Noticeable on the chart is the peak in June 2012, when we enabled the upgrade notifications for OpenOffice.org 3.3.0 users, and the peak in September when Apache OpenOffice 3.4.1 was released.&nbsp; There is also a noticeable summer lull and big drop around the end-of-year holidays.<br /></p> 
  <p><br /></p> 
  <p><br /></p> 
  <p align="center"> <img src="https://blogs.apache.org/OOo/mediaresource/a75fe8ac-6a4d-4bb0-8e55-d02fbbfa9601" alt="daily-downloads.png" /></p> 
  <p> </p> 
  <p align="left"> </p> 
  <p>The following histogram shows the distribution of download counts.&nbsp; The average daily download count is 134,900,&nbsp; with a peak day of 197,500.&nbsp; On average we see around a million downloads every 7.4 days.&nbsp; Since a typical download size is 
130MB, this amounts to an average of around 17 TB per day of downloads, 
ably handled by SourceForge and their distribution network. <br /></p> 
  <p> </p> 
  <p> </p> 
  <p align="center"><img src="https://blogs.apache.org/OOo/mediaresource/d21b73ef-9d0e-4a57-be4f-648552ab1182" alt="histogram.png" /></p> 
  <p> </p> 
  <p align="left"> </p> 
  <p>&nbsp;One final way to look at the daily counts (shown here in unit of 1000 downloads) is to decompose it into the sum of a smooth trend, a periodic weekly trend, and residual random noise:<br /></p> 
  <p> </p> 
  <p> </p> 
  <p align="center"><img src="https://blogs.apache.org/OOo/mediaresource/2d9ef56a-0d28-44fe-88b7-d26556c55193" alt="decomposition.png" /></p> 
  <p align="left"> </p> 
  <p>We are able to break down these trends along several other dimensions.&nbsp; One is by country, looking at where the download request came from.&nbsp; This information is gleaned from the IP address of the machine making the request.&nbsp; Since each IP address is part of an assigned block of addresses, and blocks are assigned geographically, we can create a table of downloads by country, territory, etc.&nbsp; We show the <a href="http://www.openoffice.org/stats/countries.html">full table</a> our the website, of all 237 countries, territories, etc., but here are the top 10:</p> 
  <p> </p> 
  <p> </p> 
  <p align="center"> </p> 
  <p> </p> 
  <table border="1" align="center"> 
    <tbody> 
      <tr> 
        <td align="right">#1</td> 
        <td>United States</td> 
        <td align="right">9,782,293</td> 
      </tr> 
      <tr> 
        <td align="right">#2</td> 
        <td>France</td> 
        <td align="right">6,738,682</td> 
      </tr> 
      <tr> 
        <td align="right">#3</td> 
        <td>Germany</td> 
        <td align="center">4,947,255</td> 
      </tr> 
      <tr> 
        <td align="right">#4</td> 
        <td>Italy</td> 
        <td align="right">4,484,601</td> 
      </tr> 
      <tr> 
        <td align="right">#5</td> 
        <td>Japan</td> 
        <td align="right">2,742,292</td> 
      </tr> 
      <tr> 
        <td align="right">#6</td> 
        <td>United Kingdom</td> 
        <td align="right">2,214,791</td> 
      </tr> 
      <tr> 
        <td align="right">#7</td> 
        <td>Spain</td> 
        <td align="right">1,925,193</td> 
      </tr> 
      <tr> 
        <td align="right">#8</td> 
        <td>Russia</td> 
        <td align="right">1,830,316</td> 
      </tr> 
      <tr> 
        <td align="right">#9</td> 
        <td>Canada</td> 
        <td align="right">1,527,682</td> 
      </tr> 
      <tr> 
        <td align="right">#10</td> 
        <td>Netherlands</td> 
        <td align="right">833,691</td> 
      </tr> 
    </tbody> 
  </table> 
  <p> </p> 
  <p> </p> 
  <p> </p> 
  <p>Another approach is to look at which localized versions of Apache OpenOffice were downloaded.&nbsp; We can see these trends in the following dot chart:</p> 
  <p> </p> 
  <p> </p> 
  <p align="center"><img src="https://blogs.apache.org/OOo/mediaresource/0a472c36-6a5a-43f2-b8b5-3aeb80581ae7" alt="languages.png" /></p> 
  <p>We can also look at the trend over time of downloads by operating system.&nbsp;&nbsp; OpenOffice is a mainstream open source desktop application, so the OS distribution reflects overall desktop operating system market shares, and with a slight growth in Windows at the expense of Mac:<br /></p> 
  <p align="center"><img src="https://blogs.apache.org/OOo/mediaresource/690f6d03-d666-4003-b1b2-8e44331e2511" alt="os-downloads.png" /></p> 
  <p>Since we have Linux versions of OpenOffice packed as RPMs (e.g., for RedHat) as well as DEBs (e.g., for Ubuntu), we can look for trends in the ratio of requests for these two packaging formats over time:<br /></p> 
  <p align="center"> <img alt="packaging.png" src="https://blogs.apache.org/OOo/mediaresource/d014552a-6517-489a-a5c4-bebff546640f" /></p> 
  <p> </p> 
  <p>Also, we have 32-bit and 64-bit Linux downloads, and we see a gradual increase in demand over time for the 64-bit version, though the 32-bit version still dominates.&nbsp; (The drop in July-September is not fully explained, but may have been an error in our download page that was not recommending 64-bit downloads appropriately.)<br /></p> 
  <p align="center"> <img src="https://blogs.apache.org/OOo/mediaresource/5f86ed31-5b4a-450c-94e3-15afc18834a8" alt="64-bit.png" /></p> 
  <p> </p> 
  <p>Although we don't have detailed download data for different Windows versions (we have a single download for all Windows users) we do have information from website visitors (nearly 7 million visitors per month) that tells a similar story.&nbsp; Windows 7 remains the most popular Windows version for our users, accounting for over half of Windows visitors.&nbsp; Windows XP is in second place, though declining.&nbsp; At the end of the year Windows 8 overtook Vista for 3rd place, and continues to rise.<br /></p> 
  <p> </p> 
  <p align="center"><img alt="windows-version.png" src="https://blogs.apache.org/OOo/mediaresource/4c0faac4-4190-49fd-a33b-5d3b55e7a12b" /></p> 
  <p>Looking at the similar data for web browsers, we see the rise in Chrome users among our website visitors:<br /></p> 
  <p align="center"><img src="https://blogs.apache.org/OOo/mediaresource/f688dc39-bbd6-48c8-aafc-9b525a7b70e5" alt="browsers.png" /></p> 
  <p> </p> 
  <p>Information from website visitors also tells us their screen resolution.&nbsp; There is a huge diversity of screen resolutions, but the general trend is a gradual increase in HD 16:9 resolutions and away from the older 1280x800 and 1024x768 modes.&nbsp; If you average it all out and look at the average aspect ratio, you see a slow, but steady trend toward increased aspect ratios (wider screen monitors):</p> 
  <p> </p> 
  <p align="center"> <img alt="aspect-ratio.png" src="https://blogs.apache.org/OOo/mediaresource/550a68f3-e70f-4fe7-a050-1bc230a3cd15" /></p> 
  <p> </p> 
  <p>The above charts were made in <a href="http://www.r-project.org/">R</a>, using data from <a href="http://sourceforge.net/p/forge/documentation/Download%20Stats%20API/">SourceForge's REST API</a> and from Google Analytics.&nbsp;&nbsp; The processing of the SourceForge data was automated via a <a href="https://svn.apache.org/repos/asf/openoffice/devtools/aoo-stats/detail-by-day.py">custom Python script</a>.<br /></p> 
  <p> </p> 
  <p align="center"><br /></p> 
  <p> </p> 
  <p> </p> 
  <p><br /> </p>

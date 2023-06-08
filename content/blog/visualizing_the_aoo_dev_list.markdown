title: Visualizing the AOO Dev List
layout: post
date: '2013-04-17T13:54:24+00:00'
permalink: visualizing_the_aoo_dev_list

<div align="center"> <a href="https://blogs.apache.org/OOo/mediaresource/c4168894-6de7-4ebc-b500-cdc97eb487f2"><img src="https://blogs.apache.org/OOo/mediaresource/db630374-272e-419b-ad76-956a2dbef2b1" alt="Dev list graph" /></a> </div> 
  <h3>&nbsp;What am I looking at?<br /></h3> 
  <p>The above image illustrates the social network of posts and responses to the Apache OpenOffice project's main development mailing list, from when it started in May 2011 until the end of March 2013 when this data was collected.&nbsp; (Click on the image to view a larger version)&nbsp; <br /></p> 
  <p>Each circle represents a person posting to the mailing list.&nbsp; The arcs represent responses to posts, i.e., they are drawn from the person posting to the person to whose post they are replying.&nbsp; The weight of each line is proportionate to the number of times person X responded to person Y.&nbsp; So darker lines portray more frequent communication pathways.&nbsp; The size of each circle is proportionate to the poster's <a href="http://en.wikipedia.org/wiki/Betweenness#Eigenvector_centrality">eigenvector centrality</a>, a theoretical measure of influence within the graph.&nbsp; The colors represent modularity classes, based a calculation that determines the most tightly-connected portions of the overall graph.&nbsp; These can represent real-world structures within the community.&nbsp; </p> 
  <p>Overall the graph has 1077 nodes (persons) and 8181 arcs (response emails).&nbsp; On average each person responded to 7.6 other persons, and made 27.1 total responses. </p> 
  <p>Now some interpretation.&nbsp; This is not the the &quot;hub and spokes&quot; or tree pattern of a 
command/control or hierarchical organization, but a complex organism, 
with project participants contributing at various levels of engagement.&nbsp; The larger circles in the center, connected with many and darker lines, are the core project participants (at least on the development list).&nbsp; The very small circles at the periphery of the graph are those who posted a single question, received a response were never heard of again.&nbsp; They typically received one or two response posts, but did not really engage further. And in the middle we see additional rich structure of conversation patterns.&nbsp; The modularity classes, represented by colors here, appear to segment the list participants into what I'll call &quot;programmers&quot;, &quot;marketing&quot; and &quot;support&quot;, though these labels are imperfect.</p> 
  <p>It is difficult to ascribe too much meaning to these email response patterns.&nbsp; Some mailing lists have been the topic of research before.&nbsp; In Q&amp;A forums, where nearly 100% of the initial posts are questions, and responses are all answers, it is interesting to look at the response patterns as an indication of expertise.&nbsp; See <a href="http://wwwconference.org/www2008/papers/pdf/p665-adamic.pdf">Adamic, et al.</a>, for a good example.&nbsp; We might apply a similar analysis to the support forums.&nbsp; But with the Dev list, an initial post might be a question, but it is often a report, or a proposal or just information sharing.&nbsp; And responses are not always expert answers or answers at all.&nbsp; Some responses are expressing approval or disapproval, or asking questions of their own.&nbsp; All these factors make this quite complex.<br /></p> 
  <h3>How I made the graph<br /></h3> 
  <p><br /></p> 
  <p> </p> 
  <ol> 
    <li>I started with the <a href="http://mail-archives.apache.org/mod_mbox/openoffice-dev/">list archives</a>, downloaded the mbox files extracted the response graph to a text file, with a custom python script, using the python &quot;mailbox&quot; package.</li> 
    <li>Then I manually cleaned up the data, coalescing multiple mail accounts used by some members.</li> 
    <li>I used the open source graph visualization package &quot;<a href="https://gephi.org/">Gephi</a>&quot; to process the data and draw the graph (layout via the <a href="http://wiki.gephi.org/index.php/Fruchterman-Reingold">Fruchterman-Reingold</a> algorithm) and export it to a PNG file.<br /></li> 
  </ol> 
  <p> </p> 
  <p><br /></p>

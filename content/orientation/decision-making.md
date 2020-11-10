Title:     Decision Making
Notice:    Licensed to the Apache Software Foundation (ASF) under one
           or more contributor license agreements.  See the NOTICE file
           distributed with this work for additional information
           regarding copyright ownership.  The ASF licenses this file
           to you under the Apache License, Version 2.0 (the
           "License"); you may not use this file except in compliance
           with the License.  You may obtain a copy of the License at
           .
             http://www.apache.org/licenses/LICENSE-2.0
           .
           Unless required by applicable law or agreed to in writing,
           software distributed under the License is distributed on an
           "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
           KIND, either express or implied.  See the License for the
           specific language governing permissions and limitations
           under the License.

In this Orientation Module you will learn about Decision Making within the project. As with the previous Level 1 Module, if you have prior experience with an open source software project, especially one at Apache, then much of this material will already be familiar to you.

In the previous Module we read about collaboration on the mailings lists, how to do it efficiently and how to avoid the most common pitfalls. We use the mailing lists for many things, for asking questions, for sharing information or the like. But one of the most important uses of the mailing list is for decision making. It is important to understand how decisions are made in an Apache community. Here are a few general principles that you should keep in mind:

  1. Commit-Then-Review (CTR) and Review-Then-Commit (RTC).

	The two primary ways of managing product changes go by the names Commit-Then-Review (CTR) and Review-Then-Commit (RTC). For most cases we operate in a CTR mode, meaning that our [Committers](https://www.apache.org/foundation/how-it-works.html#committers) are able to check in changes as they desire, with no advance approval or review.

	We trust our Committers to do the right thing. By default Committers don't ask permission before acting. They avoid unnecessary discussion and email traffic. This is not because they are anti-social. This is because they realize that in a project of this size it is impossible to discuss every small change in advance. Discussing too much is both 
	unnecessary and unproductive. We have a "time machine" called Subversion that allows us to undo any changes to the product or website. So if a Committer believes that a change would be uncontroversial, and the change is reversible, then the default approach is to go ahead make the change.

	Terms that you might need to know related to the above are: [JFDI](https://www.urbandictionary.com/define.php?term=JFDI) and ["assuming lazy consensus"](https://www.apache.org/foundation/glossary.html#LazyConsensus).

  2. When is RTC, Review-Then-Commit Used?

	There are times where CTR is not appropriate and RTC is used. This happens, for example, at the end of a release cycle, when we want to carefully review changes made to the product, in order to control the final quality before the release. When we're in RTC mode, no changes are made to the code unless first discussed and approved on the mailing list.

	Other situations when RTC is used instead of CTR might include:

	1. A Committer is unsure of the technical merits of what they want to do. They want
	an extra pair of eyes to review the proposal point out weaknesses, alternatives, etc.

	2. A change is a job for more than one person or requires coordination across several
	subgroups within the project.

	3. A change to one of our websites that impacts terms and conditions, license,
	copyright, branding, etc. So not a technical change, but a substantive change to
	content in these areas. These require PMC review.

	4. A technical change that breaks backwards compatibility of the product.

	5. Changes that break things. Sometimes this is unavoidable. But it should be
	proposed and coordinated like #2 above.

	6. Changes that cannot easily be reversed. Code changes and most website changes are
	in SVN and can be reverted. But some changes, like administrative bulk actions in
	BZ, cannot be easily undone.

	7. Public statements in behalf of the project, e.g., some blog posts and
	announcements, press releases, etc.

	In all of the above cases, a Proposal detailing the change is sent to the development
	list.

  3. Proposals

	The convention is to send all proposals in their own new thread. (Don't hide a proposal 10 posts deep in an existing thread). Put "[PROPOSAL]" in the subject line or make it obvious that you are making a proposal.

	Because the Volunteers are spread out all across the globe, in various time zones, and many have day jobs or other commitments, the convention is to wait *at least* 72 hours for feedback on a proposal.

	In cases where the proposer wants to act on their proposal, if there are no objections, they should state this in the proposal. For example, "If there are no objections voiced within 72 hours, I'll go ahead and make these changes". This is called "stating lazy consensus". You can read more about lazy consensus [here](https://openoffice.apache.org/docs/governance/lazyConsensus.html).

  4. Voting, Consensus, and Vetoes

	1. In Apache projects it is common to use a shorthand way of responding to proposals, where +1 indicates approval, 0 indicates indifference and -1 indicates disapproval.

	2. In most cases proposals are decided by consensus, based on community discussions. Only in rare cases, and in a small number of pre-defined administrative questions, do we resort to a formal counting of votes. The places where we require voting are: voting to release, voting in a new Committer or PMC Member, Voting in a new PMC Chair. That's it. Generally speaking, voting on any other topic is avoided in favor of consensus building. With voting there are winners and losers. With consensus everyone wins.

	3. Another aspect of decision making in an Apache project is the "veto". Every Committer has the ability to "veto" a change, for technical reasons, provided he explains the technical reasons for the veto, describes an alternative approach, and offers to help implement the alternative approach. Vetos are quite rare.

	4. There is one disorder of community decision making that is common enough to warrant a colorful name: [bikeshedding](http://bikeshed.com/). Follow the link and read more about this topic.

  5. To apply the above skills, be sure you are subscribed to the project's [main mailing list](https://openoffice.apache.org/mailing-lists.html#development-mailing-list-public). Keep your eye out for terms like "proposal", "lazy consensus", "vote" or "veto" and see how they are used in practice. Compare actual practice to the above descriptions. No, we're not perfect. But we work best and have the most fun when we follow the above guidelines. And so will you when you apply then in your own list communications!

Congratulations, you have completed this Module!

If you have any questions or feedback on this module, please send a note to [recruitment@openoffice.apache.org](mailto:recruitment@openoffice.apache.org?subject=Comments on Decision Making Module).

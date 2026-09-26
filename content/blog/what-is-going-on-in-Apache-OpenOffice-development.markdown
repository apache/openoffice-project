title: What is going on in Apache OpenOffice development?
layout: post
date: '2026-09-26T20:00:00+00:00'
permalink: what-is-going-on-in-Apache-OpenOffice-development

<p>
  <b>A new release is in preparation: Apache OpenOffice 4.1.17</b>
</p>
<p>
  We are preparing Apache OpenOffice 4.1.17, a maintenance release carrying important fixes backported from current development. The release branch 4.1.x remains the version we recommend to our users today.
</p>
<p>
  <b>What comes after that?</b>
</p>
<p>
  The work that has landed in the development branch are no longer the kind of changes that fit into a point release. We are changing the platforms we build for, the compilers we build with, and part of the runtime we ship. The next logical version would be 4.2.0 but that would undersell our work and – more importantly – would mislead our users about what they are installing.
</p>
<p>
  We have therefore retired the planned 4.2.0 and are heading directing towards Apache OpenOffice 5.
</p>
<p>
  <b>What will be new?</b>
</p>
<p>
  <b>The biggest changes</b>
</p>
<p>
  <ul>
    <li>Support for Windows 64-bit. The full suite now builds and runs as a native Windows 64-bit application, rather than the 32-bit binary we have shipped since the beginning.</li>
    <li>Support for macOS on Apple Silicon. Apache OpenOffice builds and runs as a native macOS arm64 application instead of going through Apple's Rosetta emulation.</li>
  </ul>
</p>
<p>
  Still under discussion is the support for Windows 32-bit binaries in general, the Windows 7 platform (please note: Microsoft has already stopped its support for older Windows versions: Windows 7 on January 14th, 2020, Windows 8.1 on January 10th, 2023 and even Windows 10 on October 14th, 2025) and older macOS releases with Intel architecture. No final decision has been already made. We are still looking for solutions that let us keep them but we will not know what is realistic until more of the work has settled. We can say more when the picture becomes clearer. If a particular older system matters to you, please tell us on the development mailing list as this is the place to say so.
</p>
<p>
  <b>Further changes you will see (only some extractions)</b>
</p>
<p>
  <ul>
    <li>Code signing and notarization on macOS, so that the application and the disk image install without the warnings from the Apple Gatekeeper like in recent versions for macOS.</li>
    <li>Bundled Python will be updated to the newer supported versions (currently 3.11), which put the scripting provider and the macros that rely on it back on a supported interpreter.</li>
    <li>OpenSSL 3 for TLS, encryption and digital signatures.</li>
  </ul>
</p>
<p>
  <b>More changes behind the scenes (only some extractions)</b>
</p>
<p>
  <ul>
    <li>Support for modern compilers. Windows builds now with the use a current Microsoft Visual C++ tool set instead of Visual Studio 2008, and macOS builds with current Xcode and clang. This sounds like normal housekeeping; But actually these are changes that unblock many, many other things on this list.</li>
    <li>New C++ / UNO bridges for Windows x86-64 and for macOS arm64, including the exception-handling routine each ABI needs. This is the piece that makes the two new platforms possible at all.</li>
    <li>A long tail of build and dependency work — static library handling, install-name rewriting, ICU, libxml2/libxslt, NSS and the rest — the kind of thing nobody notices until it stops everyone from building at all.</li>
  </ul>
</p>
<p>
  Since January 2025 that adds up to more than 850 changes from 15 contributors on the branch for version 5.
</p>
<p>
  <b>Furthermore, a short story from our engine room: Apache OpenOffice x AI</b>
</p>
<p>
  AI coding agents have been a real help to us, in particular on the build-system and porting work described above. Chasing a linker flag through four layers of makefiles, working out precisely where two ABIs differ, porting a bridge instruction by instruction: this is exactly the work that has historically kept new contributors away from Apache OpenOffice, because it is slow, unrewarding, and depends on a great deal of context that nobody ever wrote down. It turns out agents are good at it, and the people using them here are getting through that work at a pace we have not seen in years. We mention this because it changes the answer to a question we are often asked. If you have wanted to contribute to Apache OpenOffice and were put off by the size of the codebase or the age of the build system, the barrier is now genuinely lower than it was a year ago. Just come and talk to us.
</p>
<p>
  <b>Help wanted</b>
</p>
<p>
  Anyone can contribute to Apache OpenOffice. We need developers, but we equally need testers, translators, documentation writers, and people willing to help out on the user forums.
</p>
<p>
  <ul>
    <li>How to get involved: https://openoffice.apache.org/get-involved.html</li>
    <li>Mailing lists: https://openoffice.apache.org/mailing-lists.html</li>
    <li>Source code: https://github.com/apache/openoffice</li>
  </ul>
</p>

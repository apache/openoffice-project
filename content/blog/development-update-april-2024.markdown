title: Development Update - April 2024
layout: post
date: '2024-04-02T00:00:00+00:00'
permalink: development-update-april-2024

The Apache OpenOffice development is proceeding at a steady pace.

The ["trunk" branch](https://github.com/apache/openoffice/tree/trunk) has seen quite some important edits in the last few months. But because not all these changes are considered "mature enough" for the public, we will try to give you an overview in this blog post.

The most visible changes for users are the following:

- Enhanced compatibility with OOXML encryption, allowing to read encrypted files prepared with other Office Suites.
- Vector graphics can now be copied and pasted between OpenOffice and other applications in the [SVG format](https://en.wikipedia.org/wiki/SVG), that will help make prettier documents and increase interoperability between applications.
- various fixes in documentation, help files and interface, making the overall interface smoother and more pleasant to use.

But developers also work on what is "under the hood". The trunk branch has seen:

- OpenSSL upgrade: this will improve security, encryption and digital signatures;
- fix of compilation errors under the latest Linux distributions, helping contributors build and test OpenOffice on their systems;
- various spelling fixes in the source code and documentation (because developers must understand what they are reading!);
- other sparse code fixes and cleanups, allowing developers to focus on more interesting things.

Anyone can contribute to Apache OpenOffice! Start [reading here](https://openoffice.apache.org/get-involved.html) if you are interested to help the project.


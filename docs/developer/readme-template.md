<!--Meta
category:系统开发
title:README 模板
DO NOT Delete Meta Above -->


# Introduction

This `README.md` template is based on project [open-source-project-template](https://github.com/cfpb/open-source-project-template) and is been modified to suit deepin's needs, in order to make all the projects in deepin have clean and consistent guidelines for the new comers.


# Rules

- Format in [markdown syntax](https://help.github.com/articles/github-flavored-markdown/).
- Keep one or more space lines between sections.
- 'deepin' is the official trademark which must be **in all lower case**, and following legacy combinations are deprecated
    - deepin OS
    - linux deepin
    - deepin linux
- You can cap the first letter of 'deepin' as 'Deepin' **if and only if** the usage is compliant with English practice.


----

# Project Title

**Description**:  Put a meaningful, short, plain-language description of what
this project is trying to accomplish and why it matters.
Describe the problem(s) this project solves.
Describe how this software can improve the lives of its audience.

Other things to include:

  - **Technology stack**: Indicate the technological nature of the software, including primary programming language(s) and whether the software is intended as standalone or as a module in a framework or other ecosystem.
  - **Status**:  Alpha, Beta, 1.1, etc. It's OK to write a sentence, too. The goal is to let interested people know where this project is at. This is also a good place to link to the [CHANGELOG](CHANGELOG.md).
  - **Links to production or demo instances**
  - Describe what sets this apart from related-projects. Linking to another doc or page is OK if this can't be expressed in a sentence or two.

**Screenshot**: If the software has visual components, place a screenshot after the description.


## Dependencies

Describe any dependencies that must be installed for this software to work.

The dependencies in this section must be described in **distro independent way** (upstream project name or name in pkg-config), instead of package name in specific distro (gtk+-3.0 instead of libgtk-3-0, which is a package name in Debian).

If versions of dependencies make things difference, you must also point it out. eg. gtk+-3.0 >= 3.16.0

### Build Dependencies

Describe any dependencies that must be installed before you build this project from source code. eg. gtk-doc is used to generate documents at build-time, but not been used at deploy-time or runtime.

### Runtime Dependencies

Describe any dependencies that must be installed to let this project runs properly. eg. 

## Installation

Detailed *instructions* on how to install, configure, and get the project running.
This should be frequently tested to ensure reliability. Alternatively, link to
a separate [INSTALL](INSTALL.md) document.

This section must be further divided into sub-sections for specific distors like, how to install build-time dependencies in Debian with apt-get, how to generate packages with debuild, how to install generated packages with dpkg/apt-get.

## Configuration (Optional)

If the software is configurable, describe it in detail, either here or in other documentation to which you link.

## Usage (Optional)

Show users how to use the software.
Be specific.
Use appropriate formatting when showing code snippets.

## How to test the software (Optional)

If the software includes automated tests, detail how to run those tests.

## Getting help

Instruct users how to get help with this software; this might include links to an issue tracker, wiki, mailing list, etc.

**Example**

If you have questions, concerns, bug reports, etc, please file an issue in this repository's Issue Tracker.

## Getting involved

This section should detail why people should get involved and describe key areas you are
currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building
important pieces, etc.

General instructions on _how_ to contribute should be stated with a link to [CONTRIBUTING](CONTRIBUTING.md).


----

## Open source licensing info
1. [TERMS](TERMS.md)
2. [LICENSE](LICENSE)
3. [CFPB Source Code Policy](https://github.com/cfpb/source-code-policy/)


----

## Credits and references (Optional)

1. Projects that inspired you
2. Related projects
3. Books, papers, talks, or other sources that have meaningful impact or influence on this project

<!--Meta
category:系统开发
title:README 模板
DO NOT Delete Meta Above -->


# Introduction

This `README.md` template is based on project [open-source-project-template](https://github.com/cfpb/open-source-project-template) and is been modified to suit deepin's needs, in order to make all the projects in deepin have clean and consistent guidelines for the new comers.

This template is consist of three parts

0. [Rules](#rules) everyone must obey
0. [Template](#project-title) itself and writing guideline
0. [Example](#deepin-terminal)


# Rules

- Keep content up to date.
- Format in [markdown syntax](https://help.github.com/articles/github-flavored-markdown/).
- Keep one or more empty lines between sections.
- 'deepin' (all lowercase letters) is the official trademark which must be used whenever you could, but, you can cap the first letter of 'deepin' as 'Deepin' **if and only if** the usage is compliant with English practice.
- Following legacy combinations are deprecated and should no longer be used
    - deepin OS
    - deepin 操作系统
    - 深度系统
    - linuxdeepin
    - linux deepin
    - deepin linux
    - deepin linux 系统


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
Most of deepin's projects are licensed under either of two licenses

* [GPLv3](http://www.gnu.org/licenses/gpl-3.0.txt)
* [CC-BY-SA 4.0](http://creativecommons.org/licenses/by-sa/4.0/legalcode.txt)

Please download a copy, name it LICENSE, put it in your project, and declare the license in this section.

----

## Credits and references (Optional)

1. Projects that inspired you
2. Related projects
3. Books, papers, talks, or other sources that have meaningful impact or influence on this project

----

# Deepin Terminal

**Description**: This is the default terminal emulator in deepin, simple, lightweight yet beautiful.

Deepin terminal is based on python-vte and with many patchs for advanced features, such as, search, adjust opacity in real-time etc.


## Dependencies

### Build Dependencies
- python

### Runtime Dependencies
- python
- deepin-ui >=1+git201209101328
- deepin-gsettings
- python-vte
- expect
- hicolor-icon-theme
- xdotool

## Installation

### Debian 8.0 (jessie)

Install prerequisites
```
$ sudo apt-get install build-essential \
                       python-vt \
                       hicolor-icon-theme \
                       ...
```

Build
```
$ make
```

If you have isolated testing build environment (say a docker container), you can install it directly
```
$ sudo make install
```

Or, generate package files and install deepin terminal with it
```
$ debuild -uc -us ...
$ sudo dpkg -i ../deepin-terminal-*deb
```

## Usage

Run deepin terminal with the command below
```
$ deepin-terminal &
```

Below is keymap list for deepin-terminal:

| Function                 | Keymap                |
|--------------------------|-----------------------|
| Copy                     | **Ctrl** + **C**      |
| Paste                    | **Ctrl** + **V**      |
| Select word              | Double click          |
| Open URL                 | **Ctrl** + LeftButton |
| Split vertically         | **Ctrl** + **H**      |
| Split horizontally       | **Ctrl** + **h**      |
|                                                  |
| Close current window     | **Ctrl** + **W**      |
| Close other windows      | **Ctrl** + **Q**      |
| Scrol up                 | **Alt**  + **,**      |
| Scroll down              | **Alt**  + **.**      |
|                                                  |
| Focus up terminal        | **Alt**  + **k**      |
| Focus down terminal      | **Alt**  + **j**      |
| Focus left terminal      | **Alt**  + **h**      |
| Focus right terminal     | **Alt**  + **l**      |
|                                                  |
| Zoom out                 | **Ctrl** + **=**      |
| Zoom in                  | **Ctrl** + **-**      |
| Revert default size      | **Ctrl** + **0**      |
|                                                  |
| New workspace            | **Ctrl** + **/**      |
| Close workspace          | **Ctrl** + **:**      |
| Switch preview workspace | **Ctrl** + **,**      |
| Switch next workspace    | **Ctrl** + **.**      |
|                                                  |
| Search forward           | **Ctrl** + **'**      |
| Search backward          | **Ctrl** + **"**      |
|                                                  |
| Fullscreen               | **F11**               |
| Help                     | **Ctrl** + **?**      |
| Show remote login window | **Ctrl** + **9**      |
| Show sub-process window  | **Ctrl** + **8**      |

## Getting help

Any usage issues can ask for help via

* [Gitter](https://gitter.im/orgs/linuxdeepin/rooms)
* [IRC channel](https://webchat.freenode.net/?channels=deepin)
* [Forum](https://bbs.deepin.org)
* [WiKi](http://wiki.deepin.org/)

## Getting involved

We encourage you to report issues and contribute changes

* [Contirubtion guide for
users](http://wiki.deepin.org/index.php?title=Contribution_Guidelines_for_Users)
* [Contribution guide for developers](http://wiki.deepin.org/index.php?title=Contribution_Guidelines_for_Developers).

## License

deepin terminal is licensed under [GPLv3](LICENSE).

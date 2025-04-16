<p align="center"><h1 align="center">AJAX-VIDEO-TRANSCODER</h1></p>
<p align="center">
	<a href="https://itmo.ru/"><img src="https://raw.githubusercontent.com/aimclub/open-source-ops/43bb283758b43d75ec1df0a6bb4ae3eb20066323/badges/ITMO_badge.svg"></a>
	<img src="https://img.shields.io/github/license/DRMPN/ajax-video-transcoder?style=default&logo=opensourceinitiative&logoColor=white&color=blue" alt="license">
	<a href="https://github.com/ITMO-NSS-team/Open-Source-Advisor"><img src="https://img.shields.io/badge/improved%20by-OSA-blue"></a>
</p>
<p align="center">Built with the tools and technologies:</p>
<p align="center">
	<img src="https://img.shields.io/badge/Flask-000000.svg?style=default&logo=Flask&logoColor=white"alt="Flask">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=default&logo=HTML5&logoColor=white"alt="HTML5">
	<img src="https://img.shields.io/badge/Selenium-43B02A.svg?style=default&logo=Selenium&logoColor=white"alt="Selenium">
	<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white"alt="Docker">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white"alt="Python">
</p>
<br>


---
## Overview

<overview>
ajax-video-transcoder is a web application that automates the assessment of submissions, likely in educational or competitive settings. It provides a platform for users to submit work and receive automated feedback on its correctness, simplifying the judging process and delivering results efficiently.
</overview>

---


## Table of contents

- [Core features](#core-features)
- [Installation](#installation)
- [Examples](#examples)
- [Documentation](#documentation)
- [Getting started](#getting-started)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [Citation](#citation)

---

## Core features

<corefeatures>

1. **Automated Assessment**: Web app for automated evaluation and feedback of submissions.
2. **Video Transcoding**: Handles video file submissions, like the included `small.webm`.
3. **Dockerized Deployment**: Uses Docker & Compose for consistent environments & easy deployment.
4. **Flask Web Application**: Built with Flask framework providing request routing & processing.
5. **Testing and Automation**: Includes testbot functionality for automated interaction/verification.

</corefeatures>

---


## Installation

Install ajax-video-transcoder using one of the following methods:

**Build from source:**

1. Clone the ajax-video-transcoder repository:
```sh
❯ git clone https://github.com/DRMPN/ajax-video-transcoder
```

2. Navigate to the project directory:
```sh
❯ cd ajax-video-transcoder
```

3. Install the project dependencies:


**Using `pip`** &nbsp;
[<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ pip install -r requirements.txt
```


**Using `docker`** &nbsp;
[<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker build -t DRMPN/ajax-video-transcoder .
```



---


## Examples

Examples of how this should work and how it should be used are available in [Not found any examples](https://github.com/DRMPN/ajax-video-transcoder/tree/master/).

---



## Getting started

### Usage

Run ajax-video-transcoder using the following command:
 
 **Using `pip`** &nbsp;
[<img align="center" src="https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white" />](https://pypi.org/project/pip/)

```sh
❯ python {entrypoint}
```


**Using `docker`** &nbsp;
[<img align="center" src="https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white" />](https://www.docker.com/)

```sh
❯ docker run -it {image_name}
```


---


## Contributing


- **[Report Issues](https://github.com/DRMPN/ajax-video-transcoder/issues )**: Submit bugs found or log feature requests for the ajax-video-transcoder project.


---


## License

This project is protected under the Not found any License. For more details, refer to the [LICENSE](https://github.com/DRMPN/ajax-video-transcoder/blob/master/) file.

---


## Acknowledgments

- List any resources, contributors, inspiration, etc. here.

---


## Citation

If you use this software, please cite it as below.

### APA format:

    DRMPN (2023). ajax-video-transcoder repository [Computer software]. https://github.com/DRMPN/ajax-video-transcoder

### BibTeX format:

    @misc{ajax-video-transcoder,

        author = {DRMPN},

        title = {ajax-video-transcoder repository},

        year = {2023},

        publisher = {github.com},

        journal = {github.com repository},

        howpublished = {\url{https://github.com/DRMPN/ajax-video-transcoder.git}},

        url = {https://github.com/DRMPN/ajax-video-transcoder.git}

    }

---

# ajax-video-transcoder

---

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

---

## Overview

ajax-video-transcoder is a web application that allows users to securely convert WebM videos to MP4. It provides a user-friendly interface for uploading files, monitoring progress, and downloading the converted video, all while requiring account authentication.

---

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Contributing](#contributing)
- [Citation](#citation)

---
## Core features

1. **Video Transcoding**: The core functionality of the application is to convert video files from WebM format to MP4 format using FFmpeg.
2. **User Authentication**: The application includes user registration and login features, securing access to the transcoding functionality. It uses password hashing for security.
3. **File Upload**: Users can upload WebM video files through a web interface for transcoding.
4. **File Download**: Once transcoding is complete, users can download the converted MP4 video files.
5. **Secure File Handling**: Uses secure filename handling with `secure_filename` from Werkzeug to prevent potential security vulnerabilities during file uploads.

---

## Installation

Install ajax-video-transcoder using one of the following methods:

**Build from source:**

1. Clone the ajax-video-transcoder repository:
```sh
git clone https://github.com/DRMPN/ajax-video-transcoder
```

2. Navigate to the project directory:
```sh
cd ajax-video-transcoder
```

3. Install the project dependencies:

```sh
pip install -r requirements.txt
```
## Getting Started

This web application provides a UI for converting .webm videos to .mp4. The README includes screenshots of the login form and file processing interface:

![UI login form](login-form.jpg)

![UI example](file-processing.jpg)

Currenty, no specific examples or instructions on running/integrating the project are provided beyond these UI previews.

---

## Contributing

- **[Report Issues](https://github.com/DRMPN/ajax-video-transcoder/issues)**: Submit bugs found or log feature requests for the project.

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

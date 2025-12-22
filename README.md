# ajax-video-transcoder

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

## Overview

A secure web application that enables users to convert WebM videos to MP4 format with a seamless, interactive interface. It offers user authentication, real-time processing feedback, and smooth file upload and download capabilities, ensuring a reliable and user-friendly transcoding experience for authorized users.

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

## Core features

1. **User Authentication**: The application provides secure user authentication with login and registration functionality. Users must register with a unique username and password, and log in to access the video transcoding features, ensuring that only authorized users can use the service.
2. **WebM to MP4 Video Transcoding**: Core functionality of the application is converting WebM video files to MP4 format using FFmpeg. The conversion is performed server-side with specific encoding settings, including frame rate adjustment to 24fps and proper timestamp generation.
3. **AJAX-Based File Upload**: The application uses AJAX to handle file uploads asynchronously, allowing users to upload WebM files without reloading the page. This provides a smoother user experience and enables dynamic status updates during processing.
4. **File Upload and Download Interface**: Provides a user-friendly web interface for uploading WebM files and downloading the converted MP4 files. The UI includes dedicated sections for upload and download, with appropriate form controls and feedback mechanisms.
5. **Server-Side Validation and Error Handling**: Implements server-side validation for file types, ensuring only WebM files are accepted. The application also captures and displays FFmpeg errors, providing meaningful feedback to users when transcoding fails.
6. **Session Management**: Uses Flask-Session to manage user sessions securely with filesystem-based storage. Sessions are cleared on logout and configured to prevent caching, enhancing the security of user data and authentication state.

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

## Contributing

- **[Report Issues](https://github.com/DRMPN/ajax-video-transcoder/issues)**: Submit bugs found or log feature requests for the project.

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
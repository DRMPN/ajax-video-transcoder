# ajax-video-transcoder

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

## Overview

A secure and user-friendly web platform that enables authorized users to convert WebM videos to MP4 format with ease. It offers a seamless experience through real-time processing feedback, intuitive upload and download capabilities, and robust authentication, ensuring reliable video transcoding for individual users.

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

## Core features

1. **User Authentication**: The application provides secure user registration and login functionality, requiring users to create an account and log in before accessing transcoding features. Passwords are securely hashed using industry-standard methods to protect user credentials and ensure only authorized access.
2. **WebM to MP4 Video Transcoding**: The core functionality enables server-side conversion of WebM video files to MP4 format using FFmpeg. The transcoding process applies specific encoding settings such as setting the frame rate to 24fps and generating proper timestamps to ensure high-quality output.
3. **AJAX-Based File Upload**: The application uses AJAX to support asynchronous file uploads, allowing users to submit WebM files without page reloads. This provides a seamless user experience with real-time feedback during both upload and processing stages.
4. **File Upload and Download Interface**: A user-friendly web interface enables users to upload WebM files and download the resulting MP4 files after transcoding. The interface includes intuitive form controls, status messages, and direct download links for efficient workflow management.
5. **Server-Side Validation and Error Handling**: The application performs strict server-side validation to accept only WebM files for transcoding. It captures and displays FFmpeg errors in a user-friendly manner, providing clear feedback when conversion fails due to file issues or encoding problems.
6. **Session Management**: User sessions are securely managed using Flask-Session with filesystem-based storage. Sessions are cleared upon logout and configured to prevent browser caching, enhancing security by protecting user authentication state and sensitive data.

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

DRMPN (2023). ajax-video-transcoder repository [Computer software]. https://github.com/DRMPN/ajax-video-transcoder

@misc{ajax-video-transcoder,
 author = {DRMPN},
 title = {ajax-video-transcoder repository},
 year = {2023},
 publisher = {github.com},
 journal = {github.com repository},
 howpublished = {\url{https://github.com/DRMPN/ajax-video-transcoder.git}},
 url = {https://github.com/DRMPN/ajax-video-transcoder.git}
}
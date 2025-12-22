# ajax-video-transcoder

[![OSA-improved](https://img.shields.io/badge/improved%20by-OSA-yellow)](https://github.com/aimclub/OSA)

## Overview

A secure and user-friendly web application that allows authorized users to convert WebM videos to MP4 format with a seamless interface, real-time feedback, and reliable file handling, ensuring a smooth and efficient transcoding experience.

## Table of Contents

- [Core features](#core-features)
- [Installation](#installation)
- [Contributing](#contributing)
- [Citation](#citation)

## Core features

1. **User Authentication**: The application provides secure user authentication with registration and login functionality. Users must create a unique account and log in to access the transcoding features, ensuring that only authorized individuals can use the service. Passwords are securely hashed using industry-standard methods.
2. **WebM to MP4 Video Transcoding**: The core functionality of the application is converting WebM video files to MP4 format using FFmpeg on the server side. The transcoding process includes specific encoding settings such as adjusting the frame rate to 24fps and generating proper timestamps to ensure high-quality output.
3. **AJAX-Based File Upload**: The application uses AJAX to enable asynchronous file uploads, allowing users to submit WebM files without refreshing the page. This provides a seamless and responsive user experience with real-time feedback during the upload and processing stages.
4. **File Upload and Download Interface**: A user-friendly web interface allows users to upload WebM files and download the resulting MP4 files after transcoding. The interface includes clear form controls, status messages, and direct download links for a smooth workflow.
5. **Server-Side Validation and Error Handling**: The application performs server-side validation to ensure only WebM files are accepted for transcoding. It captures and displays FFmpeg errors in a user-friendly way, providing meaningful feedback when the conversion process fails due to file issues or encoding errors.
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
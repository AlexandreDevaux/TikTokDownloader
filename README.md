<a name="readme-top"></a>
<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/AlexandreDevaux/TikTokDownloader">
    <img src="images/logo.jpg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-TikTok-Video-Downloader</h3>
  <h4 align="center">Working in November 2022</h4>

  <p align="center">
    An awesome command line tool to download tiktok videos!
    <br />
    <br />
    <a href="https://github.com/AlexandreDevaux/TikTokDownloader">View Demo</a>
    ·
    <a href="https://github.com/AlexandreDevaux/TikTokDownloader/issues">Report Bug</a>
    ·
    <a href="https://github.com/AlexandreDevaux/TikTokDownloader/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [![Python][Python.org]][Python-url]
* [![Selenium][Selenium.dev]][Selenium-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

* Python 3.8 or higher
* Chrome v^107
* pip

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AlexandreDevaux/TikTokDownloader.git
   ```
2. Change directory
   ```sh
   cd TikTokDownloader
   ```
3. Install requirements
   ```sh
    pip install -r requirements.txt --user
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE EXAMPLES -->
## Usage

### Download all videos from a user
```
python tiktok.py -u "alexandredevauxtiktok"
```

### Download a specific video
```
python tiktok.py -v "https://www.tiktok.com/@alexandredevauxtiktok/video/7010000000000000000"
```

## Options

```
  -h, --help            show this help message and exit
  
  -u, --user            user to download videos from
  
  -v, --videoUrl        url of the video to download
  
  -o, --output          name convention of the ouput, for example : `-o video` will name the videos `video_1.mp4, video_2.mp4, ..., default is `video`
  
  --destination, -d     destination folder, default is '.' (current folder)
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Alexandre Devaux - [@TikTok](https://www.tiktok.com/@alexandredevauxtiktok) - alexandre@wikicompany.com

Project Link: [https://github.com/AlexandreDevaux/TikTokDownloader](https://github.com/AlexandreDevaux/TikTokDownloader)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/AlexandreDevaux/TikTokDownloader.svg?style=for-the-badge
[contributors-url]: https://github.com/AlexandreDevaux/TikTokDownloader/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/AlexandreDevaux/TikTokDownloader.svg?style=for-the-badge
[forks-url]: https://github.com/AlexandreDevaux/TikTokDownloader/network/members
[stars-shield]: https://img.shields.io/github/stars/AlexandreDevaux/TikTokDownloader.svg?style=for-the-badge
[stars-url]: https://github.com/AlexandreDevaux/TikTokDownloader/stargazers
[issues-shield]: https://img.shields.io/github/issues/AlexandreDevaux/TikTokDownloader.svg?style=for-the-badge
[issues-url]: https://github.com/AlexandreDevaux/TikTokDownloader/issues
[license-shield]: https://img.shields.io/github/license/AlexandreDevaux/TikTokDownloader.svg?style=for-the-badge
[license-url]: https://github.com/AlexandreDevaux/TikTokDownloader/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/alexandre-devaux-engineer/
[Python.org]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Selenium.dev]: https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white
[Selenium-url]: https://www.selenium.dev/
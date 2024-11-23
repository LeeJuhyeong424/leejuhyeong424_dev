---
title: "GitHub Blog 시리즈 3: GitHub Desktop 설치 및 주요 기능 이해하기"
date: 2024-11-06 00:00:00 +0900 
categories: 
    [
        블로그 제작,
        개발 도구 사용법
    ]
tags: 
    [
        GitHub Desktop,
        GUI 도구,
        Git 사용법,
        Git vs CLI,
        저장소 복제,
        커밋 및 푸시,
        브랜치 관리,
        Git 연동,
        개발 협업 도구
    ]
excerpt: "이 글에서는 GitHub Desktop의 설치 방법과 기본 설정 과정을 안내하고, 주요 기능인 저장소 복제, 커밋, 푸시 및 브랜치 관리를 설명합니다. Git 명령어와의 비교를 통해 GitHub Desktop의 장점과 사용 편의성을 알아보고, Git 사용이 익숙하지 않은 사용자도 쉽게 접근할 수 있는 방법을 소개합니다."
image:
    path: /assets/img/thumbnails/GitHub-Emblem.png
    lqip: data:image/webp;base64,UklGRnIAAABXRUJQVlA4TGUAAAAvD8ABEAAIwv+5gwg3tm0dz6t++49Tmb1tDMQeRHo7pW2ny8QSNKWVvyJgkiABSDwpAJTAWoRVT0FLXt1Y29SKU9pd3J0X4q6sYeZubqXp4unn5cAiw64HGKQYafhx1IJcvGygAQA=
---
## GitHub Desktop 소개
**GitHub Desktop**은 Git 사용을 위한 **그래픽 사용자 인터페이스(GUI) 도구**로, GitHub에서 제공하는 프로젝트 관리와 협업을 보다 간편하게 수행할 수 있도록 합니다. **CLI(Command Line Interface)**에서 Git 명령어를 직접 입력하는 대신, 클릭만으로 작업을 처리할 수 있어 Git 사용에 익숙하지 않거나 CLI 사용이 어려운 사용자에게 특히 유용한 도구입니다.

---
## 설치 방법
### 1. GitHub Desktop 다운로드
![다운로드1](/assets/img/posts/github-blog-series-3/1.png)
먼저 [GitHub Desktop 공식 웹사이트](https://github.com/apps/desktop)에 접속하여 **Download now** 버튼을 클릭합니다.
![다운로드2](/assets/img/posts/github-blog-series-3/2.png)
**Download for Windows (64bit)** 버튼을 눌러 GitHub Desktop을 다운로드합니다.
### 2. 설치 실행
GitHub Desktop 설치 파일은 다운로드 후 별도의 **설치 과정 없이 바로 실행**됩니다. 프로그램은 자동으로 설치 및 실행되며, 추가적인 설정 없이 바로 사용할 수 있습니다. 따라서 파일을 다운로드한 후 곧바로 실행하시면 됩니다.

---
## 기본 설정 및 로그인
GitHub Desktop을 설치한 후, 이전 게시물에서 생성한 **[GitHub 계정](https://leejuhyeong424.github.io/posts/github-blog-series-1/#github-%EA%B3%84%EC%A0%95-%EC%83%9D%EC%84%B1)**으로 로그인합니다.  
이 과정을 통해 GitHub와 GitHub Desktop 간에 저장소를 동기화할 수 있습니다.
![다운로드2](/assets/img/posts/github-blog-series-3/3.png)
**Sign in to GitHub.com**을 클릭하여 계정 로그인 창을 엽니다.
![다운로드2](/assets/img/posts/github-blog-series-3/4.png)
이전 게시물에서 생성한 **[GitHub 계정](https://leejuhyeong424.github.io/posts/github-blog-series-1/#github-%EA%B3%84%EC%A0%95-%EC%83%9D%EC%84%B1)**으로 로그인합니다.  
![다운로드2](/assets/img/posts/github-blog-series-3/5.png)
**Continue**를 눌러 다음 단계로 진행합니다.
![다운로드2](/assets/img/posts/github-blog-series-3/6.png)
**Authorize desktop**을 클릭하여 권한을 부여합니다.
![다운로드2](/assets/img/posts/github-blog-series-3/7.png)
**열기**를 선택하여 GitHub Desktop과 연동을 완료합니다.
![다운로드2](/assets/img/posts/github-blog-series-3/8.png)
**Finish**버튼을 눌러 설정을 완료합니다.  

이 과정을 통해 GitHub와 GitHub Desktop 간에 저장소를 동기화할 수 있습니다.

---
## 주요 기능 및 사용법
### 저장소 복제(Cloning)
GitHub Desktop을 사용하여 GitHub에 있는 저장소를 로컬 컴퓨터로 쉽게 복제할 수 있습니다. **"Clone a Repository"** 버튼을 클릭하고, 복제할 저장소의 URL을 입력하거나 GitHub 계정에서 원하는 저장소를 선택하면 됩니다. 이를 통해 로컬 환경에서 직접 코드 작업을 진행할 수 있습니다.
### 변경 사항 커밋(Commit)
로컬 파일을 수정한 후, GitHub Desktop을 사용하여 변경 사항을 쉽게 확인하고 **커밋**할 수 있습니다. 변경된 파일을 선택하고 설명 메시지를 작성한 후, **"Commit to main"** 버튼을 클릭하여 변경 사항을 저장합니다. 커밋은 코드의 현재 상태를 기록하는 중요한 스냅샷이므로, 각 변경 사항에 대해 명확하고 구체적인 설명을 남기는 것이 좋습니다.
### 푸시 및 풀(Push & Pull)
- **Push**: 로컬의 변경 사항을 GitHub 원격 저장소에 반영하는 작업입니다. **"Push origin"** 버튼을 사용하여 커밋된 변경 사항을 원격 저장소에 업로드할 수 있습니다.  


- **Pull**: 원격 저장소에 추가된 변경 사항을 로컬로 가져오는 작업입니다. **"Fetch origin"** 또는 **"Pull origin"** 버튼을 클릭하여 원격 저장소의 최신 변경 사항을 로컬 저장소에 반영할 수 있습니다. 이를 통해 팀원 간의 변경 사항을 최신 상태로 유지할 수 있습니다.
### 브랜치 관리(Branch Management)
새로운 기능을 개발하거나 버그를 수정하기 위해 **브랜치(Branch)**를 사용하여 독립적으로 작업할 수 있습니다. **"New Branch"** 버튼을 클릭하여 새로운 브랜치를 생성하고, 필요한 경우 다른 브랜치로 전환하여 작업을 병행할 수 있습니다. 작업이 완료되면 **Merge** 기능을 사용해 변경 사항을 메인 브랜치에 병합합니다. 브랜치를 활용하면 팀 작업 간 충돌을 줄이고, 각각의 작업을 효율적으로 관리할 수 있습니다.

---
## Git 명령어와의 비교
**GitHub Desktop**은 Git을 더 직관적이고 시각적으로 사용할 수 있는 **그래픽 사용자 인터페이스(GUI)**입니다. **CLI(Command Line Interface)**에서 사용되는 Git 명령어 대신, 클릭만으로 작업을 수행할 수 있어 사용자 친화적이며 간편합니다.

- **CLI 환경의 Git**은 강력하고 세부적인 제어가 가능하지만, **명령어** 입력이 필요한 만큼 숙련도를 요합니다. 

- 반면, **GitHub Desktop**은 **브랜치 관리, 커밋, 푸시**와 같은 주요 Git 작업을 GUI 환경에서 쉽게 처리할 수 있어 Git에 익숙하지 않은 사용자에게 적합합니다. 


**GitHub Desktop**은 시각적인 정보 제공 덕분에 여러 작업의 변경 사항을 쉽게 파악할 수 있고, Git 명령어의 사용을 최소화하여 **작업의 복잡성을 줄이는 장점**이 있습니다. 하지만 고급 기능이나 복잡한 명령어 조합을 사용하는 경우에는 **CLI Git**이 더 유리합니다.

---
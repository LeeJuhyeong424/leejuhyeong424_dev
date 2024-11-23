---
title: "GitHub Blog 시리즈 2: Git의 기본 개념과 주요 기능 이해하기"
date: 2024-11-04 00:00:00 +0900 
categories: 
    [
        블로그 제작,
        개발 도구 사용법
    ]
tags: 
    [
        Git 설치,
        Git 기본 명령어,
        버전 관리,
        개발 환경 설정,
        Git 튜토리얼
    ]
excerpt: "이 글에서는 Git의 기본 개념과 주요 기능을 소개하고, Git 설치 방법 및 기본 명령어 사용법을 단계별로 안내합니다. 또한, Git을 활용하여 소스 코드의 변경 이력을 관리하고 협업을 효과적으로 진행하는 방법을 다룹니다."
image:
    path: /assets/img/thumbnails/Git-Logo.png
    lqip: data:image/webp;base64,UklGRiABAABXRUJQVlA4TBMBAAAvD8ABEL/hoI0kR/KEy0yeP7MH0DTYNpKkqPvIvjg+88/uLYZhGElSosYlFfLPDV5dRwBAVNm2+eXaRPs0QiO1RiM827wLAH4LLBO/FSJMsgoioRUSsAmmpBZYshJiAoQbvOE+jQFufhSEUdzquyhUzb37fOtSrzq58q11uy0+eZxTw0Qk7OhHRH5z4cRwFUt4av+zkFBUxJBgoFuLbvFfQ35RgP++x9kMcBhJtmnts23b/P8/5B/b/UFE9F9sQrDKIUD5ffEnY8QMUM2/neDHPs9q7Ht26bUBYWSKtuxKw9Ws+WeFEZi+xVkYrnp8+gVKJMLkdPo92uKeANOROYe3VWQ9SRhT9ISYQgIUZESJoZgAAAA=
---
## Git의 기본 개념
**Git**은 **분산 버전 관리 시스템**으로, 소프트웨어 개발 프로젝트에서 **소스 코드의 변경 이력을 관리**하고,  
여러 개발자가 동시에 작업할 수 있도록 돕습니다. Git을 사용하면 코드의 변경 사항을 기록하여,  
오류 발생 시 **이전 버전으로 쉽게 되돌아갈 수 있습니다.**

Git의 주요 개념은 다음과 같습니다:  
- **저장소(Repository):** 코드와 관련 파일이 저장되는 공간으로, 모든 변경 이력을 관리합니다.
- **커밋(Commit):** 코드의 특정 상태를 기록하는 스냅샷으로, 변경 사항을 저장소에 반영합니다.
- **브랜치(Branch):** 독립적인 작업 공간으로, 여러 기능을 병행하여 개발할 수 있습니다.
- **병합(Merge):** 서로 다른 브랜치를 통합하여 작업 결과를 반영합니다.
- **클론(Clone):** 원격 저장소를 복사하여 로컬에서 작업할 수 있게 하는 기능입니다.

**Git**은 이러한 기능들을 통해 팀원 간 협업을 용이하게 하고, 코드의 안정성과 추적 가능성을 높입니다.  
특히 **GitHub**와 같은 플랫폼과 함께 사용하면 원격 저장소에서의 협업을 더욱 쉽게 진행할 수 있습니다.

---
## Git을 사용하는 이유
Git을 사용하면 프로젝트의 모든 변경 사항을 기록하고, 다양한 버전을 비교하고 병합 작업을 간단하게  
수행할 수 있습니다. 또한, 팀원들과 동시에 여러 기능을 독립적으로 개발할 수 있어 협업에 큰 장점을 제공합니다.

---
## Git 설치 방법
![페이지 접속](/assets/img/posts/github-blog-series-2/1.png)
먼저 [Git 페이지](https://git-scm.com/)에 접속하여 **Download for Windows** 버튼을 클릭합니다.  
![페이지 접속2](/assets/img/posts/github-blog-series-2/2.png)
**64-bit Git for Windows Setup**를 눌러 설치파일을 다운로드 합니다.
![설치이미지1](/assets/img/posts/github-blog-series-2/3.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지2](/assets/img/posts/github-blog-series-2/4.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지3](/assets/img/posts/github-blog-series-2/5.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지4](/assets/img/posts/github-blog-series-2/6.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지5](/assets/img/posts/github-blog-series-2/7.png)
기본 편집기를 사용해도 되지만, **VSCode**를 주로 사용하신다면 `Use Visual Studio Code as Git's default editor` 옵션을 선택하는 것이 좋습니다. 이를 통해 Git에서 편집 작업을 할 때 VSCode가 자동으로 열리게 됩니다.  
만약 아직 VSCode가 설치되어 있지 않다면, [Visual Studio Code 공식 사이트](https://code.visualstudio.com/)에 접속하여 설치를 진행해 주세요.  
이를 통해 더 편리하게 Git과 통합하여 사용할 수 있습니다.
![설치이미지6](/assets/img/posts/github-blog-series-2/8.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지7](/assets/img/posts/github-blog-series-2/9.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지8](/assets/img/posts/github-blog-series-2/10.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지9](/assets/img/posts/github-blog-series-2/11.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지10](/assets/img/posts/github-blog-series-2/12.png)
기본값을 선택해도 되지만, **PowerShell** 화면이 더 편하신 경우에는 `Use Windows' default console window` 옵션을 선택하는 것이 좋습니다. 이렇게 하면 Git Bash 대신 Windows의 기본 콘솔인 PowerShell을 사용할 수 있게 됩니다.  
이 설정은 Git 명령을 수행할 때 더 익숙한 환경을 제공해 작업을 편리하게 진행할 수 있도록 도와줍니다.
![설치이미지11](/assets/img/posts/github-blog-series-2/13.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지12](/assets/img/posts/github-blog-series-2/14.png)
**Next** 버튼을 클릭하여 다음 단계로 진행하세요.
![설치이미지13](/assets/img/posts/github-blog-series-2/15.png)
"Next" 버튼을 클릭한 후, 설정이 완료되면 **Install** 버튼을 눌러 설치를 시작하세요.
![설치이미지14](/assets/img/posts/github-blog-series-2/16.png)
**Launch Git Bash** 옵션을 선택하고, **View Release Notes** 옵션은 해제한 후 Finish 버튼을 눌러 설치를 마무리하세요.
![설치이미지15](/assets/img/posts/github-blog-series-2/17.png)
```bash
git --version
```
위 명령어를 입력하여 설치가 정상적으로 완료되었는지 확인합니다.  
다음으로 사용자 이름과 이메일을 설정합니다. 이 정보는 커밋 시 기록되는 사용자 정보로 사용됩니다.
```bash
git config --global user.name "Your Name"
git config --global user.email "youremail@example.com"

```

---
## Git의 기본 명령어 사용법
이 명령어들은 Git을 사용하면서 가장 기본적이고 자주 사용되는 기능들입니다.
- **git init:** 새로운 Git 저장소를 초기화합니다.
- **git clone [URL]:** 원격 저장소를 로컬로 복사해옵니다.
- **git add [파일명]:** 파일을 스테이지 영역에 추가합니다.
- **git commit -m "메시지":** 변경 사항을 커밋하고 메시지를 추가합니다.
- **git status:** 현재 저장소의 상태를 확인합니다.
- **git push:** 로컬 커밋을 원격 저장소로 업로드합니다.
- **git pull:** 원격 저장소에서 최신 변경 사항을 가져옵니다.
- **git branch:** 브랜치를 확인하거나 생성합니다.
- **git checkout [브랜치명]:** 브랜치를 전환합니다.
- **git merge [브랜치명]:** 다른 브랜치의 변경 사항을 병합합니다.  
이 명령어들을 통해 Git을 사용한 코드 관리 및 협업을 효과적으로 할 수 있습니다.  
각 명령어의 사용법에 익숙해지면 Git 활용이 더욱 수월해질 것입니다.

---

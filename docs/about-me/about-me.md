---
title: About Me
layout: default
nav_order: 2
has_children: true
has_toc: false
---

# About Me

학력(Education) 정보와 보유 기술 스택(Skills) 등 개인 상세 프로필을 정리한 공간입니다.

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

{% include components/children_nav.html %}

---

## Skill Inventory

| 분야 | 기술 |
| :--- | :--- |
| **Language** | <img src="https://skillicons.dev/icons?i=py" height="20" valign="middle" /> Python (3.8~3.14), <img src="https://skillicons.dev/icons?i=java" height="20" valign="middle" /> Java, <img src="https://skillicons.dev/icons?i=bash" height="20" valign="middle" /> Shell Script |
| **Backend** | <img src="https://skillicons.dev/icons?i=fastapi" height="20" valign="middle" /> FastAPI, <img src="https://skillicons.dev/icons?i=django" height="20" valign="middle" /> Django, Django REST Framework, <img src="https://skillicons.dev/icons?i=spring" height="20" valign="middle" /> Spring Boot |
| **ORM / Database** | SQLAlchemy, JPA, MyBatis, <img src="https://skillicons.dev/icons?i=mysql" height="20" valign="middle" /> MySQL, <img src="https://skillicons.dev/icons?i=mariadb" height="20" valign="middle" /> MariaDB, Amazon Aurora MySQL, <img src="https://skillicons.dev/icons?i=redis" height="20" valign="middle" /> Redis |
| **Realtime / Async** | WebSockets, Daphne (ASGI), aiohttp |
| **AI / Data** | Gemini API, LangChain, BeautifulSoup, Selenium, cloudscraper |
| **DevOps / Cloud** | <img src="https://skillicons.dev/icons?i=docker" height="20" valign="middle" /> Docker, <img src="https://skillicons.dev/icons?i=aws" height="20" valign="middle" /> AWS (EC2, ECS, Lambda, RDS, S3, CloudWatch, ECR), <img src="https://skillicons.dev/icons?i=githubactions" height="20" valign="middle" /> GitHub Actions, <img src="https://skillicons.dev/icons?i=gitlab" height="20" valign="middle" /> GitLab CI/CD, <img src="https://skillicons.dev/icons?i=jenkins" height="20" valign="middle" /> Jenkins |
| **Monitoring / Security** | GlitchTip, <img src="https://skillicons.dev/icons?i=sentry" height="20" valign="middle" /> Sentry, Infisical, <img src="https://skillicons.dev/icons?i=nginx" height="20" valign="middle" /> Nginx |
| **Collaboration** | <img src="https://skillicons.dev/icons?i=git" height="20" valign="middle" /> Git & <img src="https://skillicons.dev/icons?i=github" height="20" valign="middle" /> GitHub, <img src="https://skillicons.dev/icons?i=gitlab" height="20" valign="middle" /> GitLab, Jira, <img src="https://skillicons.dev/icons?i=notion" height="20" valign="middle" /> Notion |

---

## Profile

정보보호학을 전공하며 시스템의 구조와 동작 원리를 이해하는 과정에서 개발에 흥미를 느꼈고, 지난 4년 4개월 동안 다양한 서비스의 백엔드를 개발하며 복잡한 문제를 분석하고 더 나은 구조로 개선하는 일에 가장 큰 보람을 느껴왔습니다.

### 문제의 본질 분석과 장애 개선
새로운 기능을 만드는 것보다 기존 시스템을 이해하고, 장애와 병목의 원인을 찾아 안정적으로 개선하는 과정을 즐깁니다. 개발을 시작하기 전에 "어떻게 구현할까?"보다 "왜 이런 구조가 되었고, 더 나은 방법은 무엇일까?"를 먼저 고민하며, 운영 환경과 서비스의 특성을 함께 고려해 해결책을 설계합니다.

### 적합한 기술 선택과 신뢰성 확보
기술은 목적이 아니라 문제를 해결하기 위한 도구라고 생각합니다. 서비스 규모와 요구사항에 맞는 기술을 선택하고, 테스트 코드와 문서화, 모니터링 체계를 함께 구축하며 유지보수성과 운영 효율성까지 고려한 시스템을 만드는 것을 중요하게 생각합니다.

### 지속적인 학습과 동료들과의 협업
직무 밖에서도 사이드 프로젝트를 통해 새로운 기술과 아키텍처를 직접 검증하고, 경험과 시행착오를 글과 문서로 정리하며 꾸준히 학습을 이어가고 있습니다. 앞으로도 단순히 기능을 구현하는 개발자를 넘어, 복잡한 시스템을 이해하기 쉬운 구조로 개선하고 팀이 신뢰할 수 있는 백엔드 엔지니어로 성장하고자 합니다.

---

## Technical Competency

단순히 특정 프레임워크나 라이브러리를 사용하는 것을 넘어, 비즈니스 요구사항과 운영 환경에 적합한 아키텍처를 설계하고 성능·안정성·운영상의 문제를 해결하는 것을 강점으로 합니다. 4년 4개월의 실무 경험과 다양한 사이드 프로젝트를 통해 다음과 같은 기술 역량을 쌓았습니다.

### Backend & Architecture

* **WebSocket 데이터 유실률 0%를 달성한 실시간 서비스 개선**
  * ASGI/WSGI 기반 다중화와 웹 서버 분산 구조를 설계하여 성능 병목을 해결하고 서비스 안정성을 확보합니다.
  * *대표 사례*: [가상화폐 채굴 모니터링 시스템]({% link docs/experience/basetrade/index.md %}#실실시간-websocket-데이터-유실-분석-및-처리-구조-개선)에서 Daphne 다중 인스턴스와 Nginx 로드밸런싱을 적용하여 **추가 인프라 비용 없이 200대 이상 장비의 WebSocket 데이터 유실률 0%**를 달성했습니다.

* **기술 변화에 유연하게 대응하는 애플리케이션 아키텍처 설계**
  * 비즈니스 로직과 인프라를 분리하여 기술 스택이나 영속성 계층 변경에도 유연하게 대응할 수 있는 구조를 설계합니다.
  * *대표 사례*: [품앗이 (Poomasi)]({% link docs/side-projects/poomasi/index.md %}#애플리케이션-아키텍처)에서 Clean Architecture와 Hexagonal Architecture를 도입하고 DI를 적용하여 프레임워크와 데이터베이스에 의존하지 않는 구조를 구축했습니다.

* **테스트 커버리지 52% → 71%로 향상시킨 품질 관리 체계 구축**
  * 테스트 코드와 Mocking 전략을 표준화하여 회귀 테스트의 신뢰성을 높이고 안정적인 배포 기반을 마련합니다.
  * *대표 사례*: [이더리움 환전 플랫폼]({% link docs/experience/basetrade/index.md %}#자동화-테스트-환경-구축-및-회귀-테스트-체계-도입)에서 pytest를 도입하여 테스트 커버리지를 52%에서 71%까지 향상시켰으며, [페이네스트]({% link docs/experience/paynest/index.md %}#가상계좌-서비스-재개를-위한-시스템-검증-및-운영-문서화)에서는 상태 전이(State Transition) 기반 검증 체계를 구축해 운영 리스크를 사전에 차단했습니다.

### Data Processing & Automation

* **데이터 수집 시간을 최대 85% 단축한 파이프라인 최적화**
  * 브라우저 자동화 중심의 수집 구조를 API 기반으로 개선하여 처리 속도와 운영 효율을 높입니다.
  * *대표 사례*: [엠포스 사내 광고 플랫폼]({% link docs/experience/emforce/index.md %}#selenium-기반-광고-데이터-수집-구조-분석-및-api-기반-수집-방식-전환)에서 Selenium 기반 수집을 API 방식으로 전환하여 3~5분 → 30~45초(약 80% 단축)로 개선했으며, [금융 데이터 수집 자동화]({% link docs/experience/basetrade/index.md %}#기타-업무-및-활동)에서는 90초 → 10~15초(약 85% 단축)로 개선했습니다.

* **2,500건 이상의 비정형 데이터를 자동 정형화한 LLM 데이터 파이프라인 구축**
  * 프롬프트 엔지니어링과 후처리 파이프라인을 설계하여 생성형 AI의 결과를 서비스에서 활용 가능한 데이터로 변환합니다.
  * *대표 사례*: [FOLDER]({% link docs/side-projects/futurebyte/folder.md %})와 [품앗이 (Poomasi)]({% link docs/side-projects/poomasi/index.md %}#gemini-기반-채용공고-기술스택-자동-추출-시스템-구축)에서 OpenAI, LangChain, Gemini를 활용하여 약 2,500건 이상의 채용공고와 패션 콘텐츠를 자동 분석·분류하는 데이터 파이프라인을 구축했습니다.

### Infrastructure & Operations

* **2GB 메모리 환경에서도 장애 재발률 0%를 달성한 시스템 최적화**
  * 시스템 리소스를 분석하고 병목을 개선하여 제한된 인프라 환경에서도 안정적인 서비스를 운영합니다.
  * *대표 사례*: [엠포스]({% link docs/experience/emforce/index.md %}#대용량-광고-데이터-처리-과정의-memoryerror-장애-분석-및-배치-안정화)에서 Swap 메모리 최적화를 적용하여 **MemoryError 재발률 0%**를 달성했습니다.

* **잠재적인 보안 리스크를 사전에 제거하는 취약점 분석 및 대응**
  * 서버 취약점을 재현·분석하고 시큐어 코딩 가이드를 마련하여 서비스 안정성을 높입니다.
  * *대표 사례*: [P2P 법인 투자 플랫폼]({% link docs/experience/basetrade/index.md %}#wkhtmltopdf-기반-pdf-생성-보안-취약점-및-리소스-제어-개선)에서 wkhtmltopdf 기반 SSTI 취약점을 분석하고 대응 방안을 적용했으며, [AWS Lambda 환경 SQL Injection 취약점 분석]({% link docs/experience/emforce/index.md %}#aws-lambda-기반-데이터-조회-로직-sql-injection-취약점-분석-및-개선-방향-제안)에서는 파라미터 바인딩 기반 개선 가이드를 제안했습니다.

* **검색 유입을 고려한 서비스 운영 자동화 구축**
  * 배포 자동화뿐 아니라 검색 노출과 운영 효율을 높이는 자동화 체계를 설계합니다.
  * *대표 사례*: [품앗이]({% link docs/side-projects/poomasi/index.md %}#검색-엔진-최적화seo를-통한-플랫폼-유입-극대화)에서 Open Graph, JSON-LD, Sitemap 자동 생성 파이프라인을 구축하여 주요 검색 키워드에서 Google 첫 페이지 상위 노출을 달성했습니다.

---

---
layout: default
title: 품앗이 (Poomasi)
parent: Side Project
nav_order: 2
---

# 품앗이 (Poomasi)
{: .no_toc }

`FastAPI` `Gemini 1.5 Flash` `Clean Architecture` `Hexagonal Architecture` `VPC Subnet 격리` `GitHub Actions` `Locust`

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

>  관련 포스팅
- 2025-11-10, [품앗이, FastAPI에 적용했던 두 가지 포인트](https://jakpentest.tistory.com/475)
- 2025-11-04, [품앗이, FastAPI 아키텍처 어떻게 가져갈 것인가?](https://jakpentest.tistory.com/473)
- 2025-11-03, [JWK로 OAuth2 토큰 검증하기](https://jakpentest.tistory.com/472)
- 2025-11-03, [품앗이, 사이드 프로젝트를 정리하며](https://jakpentest.tistory.com/471)

## 프로덕트

### 개요

| 서비스 소개 | IT 취준생에게 현업 선배를 연결해주는 **대학생 멘토링 플랫폼**임. |
| :--- | :--- |
| **핵심 목표 1** | 사용자들(IT취준생)이 검증된 현업 멘토와 교류하고, 신뢰도 높은 학업 및 취업 조언을 얻을 수 있는 정보 공유 게시판과 소통 커뮤니티 환경을 제공받도록 구성하는 것을 목표로 함. |
| **핵심 목표 2** | 주요 IT 기업들의 채용 정보를 실시간으로 자동 수집하고, LLM을 통해 채용 요건(경력, 직무, 핵심 기술 등)을 정밀하게 추출·분류하여 대학생 맞춤형 멘토 매칭 데이터를 구축하는 것을 목표로 함. |

### 구성

| 항목 | 내용 |
| :--- | :--- |
| **참여 인원** | 총 4명 (PO/PM 1명, 디자이너 1명, BE 1명, FE 2명) |
| **진행 기간** | 2025.02 ~ 2025.11 (약 8개월) |
| **담당 역할** | 백엔드 기능 개발 및 데이터 수집 인프라 구축 |
| **협업 도구** | • **Slack**: 팀 내부 소통 및 실시간 알림 연동<br>• **Jira**: Sprint 기반 일정 및 세부 태스크 관리<br>• **Notion**: 기획 안, 스펙 명세, 개발 및 API 문서 통합 관리<br>• **Swagger (OpenAPI)**: API 스펙 공유 및 프론트엔드 협업 환경 구성 |


### 핵심 성과 및 의사결정 이력

#### 1. Gemini 1.5 Flash API 비용 최적화 및 Few-Shot 프롬프트 기반 기술스택 자동 정제 파이프라인 설계
* **배경 & 제약사항**: 주요 IT 기업의 채용 요건은 형식(줄글, 리스트 등)과 용어(예: Python, 파이썬, Py)가 달라 정형화하기 어려웠습니다. 매일 수백 건의 공고를 사람이 직접 검토하기엔 리소스 한계가 존재했습니다.
* **의사결정 (Why Gemini 1.5 Flash?)**: 
  - GPT-4 등의 고성능 모델은 정밀하지만 API 단가 비용이 높아 예산이 제한된 사이드 프로젝트에 부담이었습니다.
  - 성능과 비용의 균형을 분석한 결과, 속도가 빠르고 1M 토큰 Context Window를 지원하며 비용이 저렴한 **Gemini 1.5 Flash**를 메인 LLM으로 선택했습니다.
  - 프롬프트에 Few-Shot 예시를 구성하고 JSON Schema Mode를 강제하여 응답의 일관성을 높였으며, 추출 결과를 내부 마스터 데이터셋과 2차 매칭 검증하는 후처리 어댑터를 구축하여 데이터의 정확성을 98% 이상 확보했습니다.
* **성과**: 매일 7개 매체에서 수집되는 약 2,500건 이상의 채용 정보에서 기술스택 요구사항을 오차 없이 자동 파싱·정형화하여 멘토-멘티 매칭의 기반 데이터를 구축했습니다.

#### 2. Port & Adapter 및 dependency-injector 도입을 통한 외부 인프라 변경 차단 및 독립적 모킹 테스트 구축
* **배경 & 제약사항**: 서비스 특성상 외부 LLM API(Gemini)나 타사 소셜 로그인(Firebase), 그리고 데이터베이스(MariaDB) 스펙의 잦은 변경이 예상되었습니다. BE 개발자가 1명인 환경에서 기술 스펙의 변경이 비즈니스 코어 로직에 영향을 준다면 유지보수가 불가능하다고 판단했습니다.
* **의사결정 (Why Hexagonal Architecture?)**:
  - 도메인 중심 설계(DDD)와 Port & Adapter 패턴을 도입하여 핵심 유스케이스가 외부 영속성 계층(SQLAlchemy)이나 API 클라이언트에 직접 의존하지 않도록 계층을 분리했습니다.
  - 파이썬 환경의 유연한 DI 관리를 위해 `dependency-injector` 패키지를 도입, 런타임에 데이터베이스 어댑터와 Gemini API Mock 모듈을 쉽게 교체 가능하도록 설계했습니다.
  - 이로 인해 로컬 테스트 시 데이터베이스나 LLM 서버 연결 없이 순수한 유스케이스 로직만 100% Mocking하여 독립적으로 검증할 수 있는 단위 테스트 환경을 조성했습니다.
* **성과**: 데이터베이스 스펙(MySQL ➔ Aurora MySQL) 변경 및 Firebase SDK 버전 변경 시에도 핵심 비즈니스(Usecase) 코드를 단 한 줄도 수정하지 않고 어댑터 교체만으로 30분 만에 대응을 완료했습니다.

#### 3. 검색 로봇 수집 성능 극대화를 위한 FastAPI 동적 메타태그(Open Graph/JSON-LD) 및 Sitemap 배포 자동화
* **배경 & 제약사항**: 사이드 프로젝트 특성상 마케팅 예산이 0원인 상황에서, 신규 사용자를 유치하기 위해 구글 및 네이버 검색 유입(Organic Traffic)을 끌어오는 것이 필수적이었습니다.
* **의사결정**:
  - 검색 엔진 봇이 동적 자바스크립트를 렌더링하기 전에 메타태그를 수집할 수 있도록, FastAPI 라우터 단에서 Open Graph 및 JSON-LD 구조화 데이터를 동적으로 즉시 반환하도록 최적화했습니다.
  - 새로운 채용공고가 수집될 때마다 자동으로 `sitemap.xml`을 갱신하고 구글 웹마스터 도구(Search Console) API로 Ping을 전송하는 백그라운드 배치를 구성했습니다.
* **성과**: '기술스택별 IT 멘토링', '신입 개발 채용 요약' 등 핵심 타겟 키워드 검색 시 **구글 첫 페이지 최상위 노출**을 기록하여 유기적 사용자 유입 활성화에 기여했습니다.


## 프로젝트

### 저장소

| 구분 | 저장소 링크 (Repository) | 주요 역할 및 기능 |
| :--- | :--- | :--- |
| **API 서버** | [be-poomasi-api](https://github.com/poomasi/be-poomasi-api) | Clean/Hexagonal Architecture 기반 멘토링 매칭 및 플랫폼 핵심 API 개발 |
| **스케줄러 & 크롤러** | [be-poomasi-scheduler](https://github.com/poomasi/be-poomasi-scheduler) | 7개 IT 기업 채용 데이터 수집 크롤러 및 Gemini 기반 기술 스택 요구사항 분석 배치 개발 |

### 기술 스택

| 분류 | 상세 내용 |
| :--- | :--- |
| **담당 역할** | 백엔드 API 개발 및 크롤러/분류 배치 시스템 구축 |
| **사용 언어** | Python 3.12 |
| **프레임워크 & 라이브러리** | FastAPI, SQLAlchemy 2.x, APScheduler, dependency-injector, google-generativeai (Gemini), firebase-admin, locust, PyMySQL, Slack SDK |

### 개발 환경 및 인프라

| 분류 | 상세 구성 내용 |
| :--- | :--- |
| **클라우드 인프라 (AWS)** | EC2, RDS (Aurora MySQL), ELB (ALB), Route53 |
| **애플리케이션 서버** | EC2 (t2.micro) 내 uvicorn + gunicorn 프로세스 구동 |
| **데이터베이스** | Amazon Aurora MySQL (VPC Private Subnet 격리 구성) |
| **네트워크 및 보안** | ALB 로드 밸런싱, Route53 DNS 연동, Certificate Manager(ACM)를 통한 SSL/TLS 인증 |


### 주요 기능

| 기능 | 상세 내용 |
| :--- | :--- |
| **멘토링 플랫폼 API 개발** | 회원가입/로그인, 인증 및 인가, 멘토·멘티 관리, 채용공고 조회, 매칭 관련 API 등 서비스 핵심 백엔드 기능 개발 |
| **채용공고 데이터 자동 수집 시스템 구축** | 네카라쿠배당토 등 7개 IT 기업 채용 사이트 구조를 분석하고 HTML 크롤링, 공개 API 호출, 내부 JSON API 분석 방식으로 채용 데이터를 자동 수집 |
| **채용 데이터 표준화 및 중복 관리** | 기업별 상이한 채용 데이터를 공통 DTO 형태로 변환하고, 채용공고 ID와 기업 정보를 Unique Key로 활용하여 중복 저장 방지 |
| **LLM 기반 기술스택 분석 자동화** | Gemini 1.5 Flash와 Prompt Engineering을 활용하여 채용공고 제목 및 설명에서 사전에 정의된 기술스택 포함 여부를 자동 분석 |
| **채용 데이터 배치 운영 관리** | APScheduler 기반 배치 시스템을 구축하고 일별 수집 채용공고 수 및 신규 등록 기술 키워드를 로깅하여 데이터 변화 모니터링 |


---

## 시스템 아키텍처

### 인프라 아키텍처
![아키텍처 다이어그램](/docs/side-projects/poomasi/poomasi-ad.png)

*   **네트워크 및 보안 인프라 구조**:
    *   **VPC 환경 구성**: AWS VPC 내에서 서비스 영역을 논리적으로 분리하고 외부 인터넷 게이트웨이와 로드밸런서(`ALB`)를 경유하도록 구성함.
    *   **서브넷 이중화**: 외부 접근이 가능한 Public Subnet에 FastAPI 서버 인스턴스(`EC2`)를 배치하고, 핵심 데이터베이스는 Private Subnet의 `RDS`로 완전히 격리하여 보안을 대폭 강화함.
    *   **글로벌 인프라 관리**: Route53을 통한 도메인 및 DNS 연동, Certificate Manager(ACM)를 통한 SSL/TLS 인증서 관리와 S3 저장소 연동을 제공함.
*   **실시간 트래픽 흐름**:
    *   사용자가 웹 프론트엔드(`poomasi-prod-web`)로 접속하면 `ALB`를 거쳐 VPC Public Subnet 내의 `EC2` API 서버로 요청이 전달되며, API 서버는 내부 네트워크망을 통해 Private Subnet 내의 데이터베이스(`RDS`)와 안전하게 데이터를 주고받는 흐름을 구성함.
*   **자동화된 CI/CD 배포 파이프라인**:
    *   **지속적 통합(CI)**: 개발팀이 GitHub에 소스 코드를 반영하면 **GitHub Actions**가 자동으로 트리거되어 웹 및 API 서버 소스 코드를 빌드하고 검증함.
    *   **지속적 배포(CD)**: 백엔드 API(`be-poomasi-api`)와 수집 스케줄러(`be-poomasi-scheduler`)는 SSH 보안 통신 프로토콜을 활용해 `EC2` 인스턴스로 자동 배포함.

### 애플리케이션 아키텍처
이 프로젝트는 영속성 기술과 외부 프레임워크로부터 핵심 비즈니스 로직을 보호하고 테스트 용이성을 극대화하기 위해 **Clean/Hexagonal Architecture (포트 & 어댑터 패턴)** 구조로 설계함.

```mermaid
graph TD
    subgraph Client [Client Layer]
        FE[Frontend / Client]
    end

    subgraph EntryPoint [Entry Point]
        Main[main.py]
        Apis["apis/ (FastAPI Routers)"]
    end

    subgraph ApplicationCore [Application Core]
        Usecase["usecase/ (비즈니스 시나리오)"]
        Domain["domain/ (엔티티 & 비즈니스 규칙)"]
    end

    subgraph PortsAdapters [Ports & Adapters]
        Repo["infrastructure/ (DB Repositories)"]
        Adapter["adapter/ (외부 인프라 어댑터)"]
    end

    subgraph External [External Layer]
        DB[(MariaDB / MySQL)]
        ExtServices["외부 서비스 <br> AWS, Firebase, Slack, Kakao, Toss"]
    end

    FE -->|HTTP Request| Main
    Main --> Apis
    Apis -->|호출| Usecase
    Usecase --> Domain
    Usecase -->|인터페이스 구현| Repo
    Usecase -->|인터페이스 구현| Adapter
    Repo --> DB
    Adapter --> ExtServices
```

*   **의존성 규칙(Dependency Rule) 준수를 통한 도메인 보호**: 모든 의존성이 외부에서 내부(도메인 방향)로만 향하도록 구성하여 외부 프레임워크나 데이터베이스 기술 스펙이 변경되더라도 비즈니스 로직(Application Core)은 오염되지 않고 독립적으로 유지되도록 함.
*   **인프라스트럭처와의 결합도 해소**: `usecase` 레이어가 인터페이스(Port)를 바라보며 동작하도록 개발하고, 구체적인 영속성 기술(`SQLAlchemy` 기반 리포지토리) 및 외부 연동 기능(Gemini, Firebase 등)은 런타임에 동적으로 주입(DI)되는 포트 & 어댑터 구조 구성을 목표로 함.
*   **각 레이어별 핵심 역할**:
    *   **EntryPoint (`apis`)**: 클라이언트 요청의 진입점으로, FastAPI 라우터와 DTO 스키마 검증을 처리하도록 개발함.
    *   **ApplicationCore (`usecase`, `domain`)**: 실제 비즈니스 유스케이스 시나리오와 핵심 도메인 비즈니스 엔티티를 포함하도록 순수 비즈니스 레이어로 격리함.
    *   **Ports & Adapters (`infrastructure`, `adapter`)**: 데이터베이스 엑세스나 외부 타사 API(Slack, Firebase, Toss 등) 연동을 전담 구현하도록 하여 핵심 비즈니스 로직과 물리적으로 완전 분리함.

---

## 기타 사항
*   **Locust를 활용한 부하 성능 테스트**:
    *   동시 접속자 수(Number of Users): 100명
    *   램프업(Ramp-up) 시간: 10초
    *   평균 초당 처리량(RPS AVG): 160
*   **협업 효율성 개선**:
    *   일관된 커밋 메시지 관리를 위해 AI 플러그인을 활용한 Commit Message 템플릿 적용함.

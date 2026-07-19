---
layout: default
title: FutureByte
parent: Side Project
nav_order: 1
has_children: true
permalink: /docs/side-projects/futurebyte
---

# FutureByte
{: .no_toc }

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 사이드 프로젝트 개요

| 항목 | 내용 |
| :--- | :--- |
| **목적** | 다양한 서비스 아이디어 검증 및 실제 서비스 출시를 목표로 기획, 디자인, 개발 전 과정을 경험하기 위한 사이드 프로젝트 |
| **참여 인원** | 총 6명 (PO/PM 1명, 서비스 기획 1명, 디자이너 1명, BE 1명, FEs 2명) |
| **진행 기간** | 2023.10 ~ 2024.07 (약 8개월) |
| **담당 역할** | 백엔드 API 개발 및 인프라 구축·유지보수 수행 |

## 프로젝트 목록 및 상세 내용

FutureByte 팀에서 진행한 3개의 서비스 빌드 프로젝트 및 활동 상세 내역입니다.

---

### [Petting (반려견 성격유형검사 서비스)](/docs/side-projects/futurebyte/petting) (2024.04 ~ 2024.07)

반려견의 성향을 기반으로 적합한 친구를 매칭하고, 견주들이 반려 경험과 정보를 공유할 수 있는 커뮤니티 및 소통 플랫폼입니다.

* **담당 역할**: 백엔드 API 개발 및 AWS 인프라 유지보수 수행
* **기술 스택**: Python 3.10, FastAPI, SQLAlchemy, MySQL, dependency-injector, AWS (EC2, S3, RDS), Docker
* **핵심 활동 및 성과**:
  * **SQLAlchemy Classical Mapping 아키텍처 설계**: `map_imperatively()` API를 통해 데이터 모델과 비즈니스 엔티티를 단방향 격리하여 외부 프레임워크나 DB 결합이 없는 순수 도메인 단위 테스트 환경 구축.
  * **도메인 이벤트(Domain Event) 아키텍처 도입**: 미디어 업로드 로직과 리워드 지급 보상 로직 간의 물리적 결합도를 EventHandler 버스 설계로 제거하여 신뢰성 및 확장성 향상.
  * **위치 기반 서비스 및 외부 API 연동**: Kakao Local API를 IoC 컨테이너를 통해 어댑터로 연동하여 유저 주소 검증 및 경위도 공간 좌표 추출을 자동화하고, 거리순 주변 반려견 탐색 기능 구현.

---

### [Oh-Manager (신인 배우의 오디션 중계 플랫폼)](/docs/side-projects/futurebyte/oh-manager) (2024.02 ~ 2024.04)

기획사 소속이 없는 무소속 신인 및 지망생 배우들에게 공정하고 안전한 오디션 매칭과 중계 기회를 제공하는 매칭 플랫폼입니다.

* **담당 역할**: 백엔드 API 개발 및 오디션 매칭 코어 비즈니스 도메인 설계 수행
* **기술 스택**: Python 3.x, FastAPI, SQLAlchemy, MySQL, Docker, Slack SDK, Dependency Injector
* **핵심 활동 및 성과**:
  * **커스텀 트랜잭션 라우터 자체 구현**: FastAPI의 내부 라우팅을 확장한 커스텀 `TransactionRoute`를 구현하여 HTTP 요청 단위로 트랜잭션 수명 주기를 데코레이터 단에서 일괄 관리. 비즈니스 서비스 레이어에서 영속성 세션 관련 코드를 완전히 배제함으로써 코드 순수성과 가독성 대폭 향상.
  * **의존성 주입 기반 클린/DDD 아키텍처**: `dataclasses` 엔티티로 핵심 규칙을 격리하고, `Dependency Injector` DI 컨테이너 및 `patch_ioc`를 설계하여 런타임에 동적으로 인프라 어댑터를 주입하도록 구성. 외부 라이브러리나 DB 종류에 영향받지 않는 독립적인 기능 테스트 구조 구축.

---

### [FOLDER (패션 서치 커뮤니티)](/docs/side-projects/futurebyte/folder) (2023.10 ~ 2024.02)

분산된 다수 온라인 패션 매체들의 최신 콘텐츠 트렌드 데이터를 자동으로 수집하여 통합 탐색 및 정보 교환을 돕는 커뮤니티 플랫폼입니다.

* **담당 역할**: 분산형 패션 콘텐츠 크롤링 및 자동화 수집 파이프라인 구축
* **기술 스택**: Python 3.x, FastAPI, SQLAlchemy, aiomysql, aiohttp, BeautifulSoup4, Langchain, OpenAI API, APScheduler, Docker
* **핵심 활동 및 성과**:
  * **어댑터 기반 계층형 수집 아키텍처 설계**: 어댑터 패턴(Adapter Pattern)을 수집(API) 계층과 정제(Pipe) 단계에 적용하여 철저히 격리. 신규 매체 추가에 따른 기존 수집 로직의 수정 범위를 최소화하고 연동 리드 타임 단축.
  * **방화벽 우회 및 비동기 파이프라인 최적화**: `cloudscraper` 및 `fake-useragent`로 봇 방화벽 탐지를 우회하고, `aiohttp` 및 `aiomysql`을 도입해 수집 및 DB 적재 파이프라인을 전면 비동기로 전환하여 대용량 데이터 처리 속도를 대폭 개선.
  * **LLM 데이터 정제 및 테스트 안정성 확보**: OpenAI GPT 모델과 Langchain을 연계하여 수집한 원문 본문의 정제 요약 및 키워드/태그 동적 분류 작업을 자동화. `Dependency Injector`를 활용한 격리 모의 테스트 설계 및 Slack Webhook 장애 모니터링 연동.

---
title: Home
layout: home
nav_order: 1
description: "성능 최적화와 안정적인 아키텍처 설계에 몰입하는 4년 차 백엔드 개발자 Jako의 포트폴리오입니다."
permalink: /
---

# Intro

<div class="intro-hero">
  <p class="hero-title">성능 최적화와 안정적인 아키텍처 설계에 몰입하는 4년 차 백엔드 개발자, Jako입니다.</p>
  <div class="hero-key-strengths">
    <ul>
      <li><strong>구현 전에 도메인 격리와 아키텍처 구조를 먼저 고민합니다.</strong></li>
      <li><strong>성능 저하와 장애의 원인을 로그와 데이터를 통해 정확히 분석하고 해결합니다.</strong></li>
      <li><strong>사이드 프로젝트를 통해 새로운 기술을 지속적으로 검증하고 실무에 도입합니다.</strong></li>
      <li><strong>정보보호 전공 지식을 바탕으로 잠재적인 보안 위협을 선제적으로 통제합니다.</strong></li>
    </ul>
  </div>
  <div class="intro-meta-grid">
    <div class="meta-item">💼 <strong>총 경력</strong>: 4년 4개월 (백엔드 엔지니어)</div>
    <div class="meta-item">🛠️ <strong>핵심 분야</strong>: 아키텍처 설계, 성능 최적화, 보안 리스크 예방</div>
    <div class="meta-item">🔗 <strong>채널</strong>: <a href="https://github.com/jak010" target="_blank">GitHub</a> · <a href="https://jakpentest.tistory.com/" target="_blank">Tech Blog</a></div>
  </div>
</div>

정보보호학 전공을 기반으로 시스템 코어의 동작 원리를 명확하게 파악하며 개발을 시작했습니다. 
단순히 동작하는 기능 개발에 그치지 않고, 비즈니스 코어 규칙과 인프라/세부 기술 스펙을 깔끔하게 격리하여 **지속 가능하고 변경에 유연한 구조**를 설계하는 일을 즐깁니다. 
또한 시스템 리소스 제약과 대량 수집 병목 등 운영 환경의 한계 상황에서 발생하는 까다로운 문제를 로그와 명확한 수치 데이터를 근거로 집요하게 추적하여 개선해 온 실무적 경험을 갖고 있습니다.

---

## About Me

### Core Competency

#### 1. 성능 최적화 및 문제 해결 (Performance & Optimization)
* **실시간 WebSocket 분산 수집**: 서버 증설 예산이 제한된 상황에서 Daphne 4개 인스턴스 다중화와 Nginx reverse proxy 분산 처리를 자체 구현하여 **추가 인프라 비용 없이 WebSocket 데이터 유실률 0%**를 달성했습니다. ([베이스트레이드 Daphne 다중화 이력]({% link docs/experience/basetrade/index.md %}#1-daphne-다중화-및-nginx-reverse-proxy를-통한-websocket-수집-유실률-0-달성))
* **수집 파이프라인 최적화**: Selenium 브라우저 자동화의 병목을 분석하여 **Keycloak OAuth2 인증 토큰 직접 API 발급 방식**으로 전환해, 데이터 수집 소요 시간을 **3~5분에서 30~45초로 약 80% 단축**했습니다. ([엠포스 API 수집 전환 이력]({% link docs/experience/emforce/index.md %}#2-selenium-기반-수집-구조의-api-기반-전환-및-최적화))
* **제한된 서버 리소스(RAM 2GB) OOM 장애 해결**: 2GB RAM의 소형 EC2 서버 환경에서 OOM `MemoryError` 발생 시, 인프라 업그레이드 없이 Swap 메모리 확장 및 Pandas 데이터프레임의 인플레이스(in-place) 메모리 연산 튜닝을 통해 **장애 재발률 0%**로 배치 작업을 안정화시켰습니다. ([엠포스 메모리 최적화 이력]({% link docs/experience/emforce/index.md %}#1-대용량-광고-데이터-처리-과정의-memoryerror-장애-분석-및-배치-안정화))
* **방화벽 우회 및 비동기 I/O 수집 최적화**: Cloudflare 방화벽 우회(`cloudscraper`/`fake-useragent`) 및 `aiohttp` / `aiomysql`을 도입하여 대용량 매체 데이터 파싱 및 DB 적재 파이프라인을 완전 비동기로 전환해 초당 처리 성능을 극대화했습니다. ([FOLDER 비동기 크롤러 이력]({% link docs/side-projects/futurebyte/folder.md %}#2-cloudflare-방화벽-우회-및-비동기-파이프라인-최적화))

#### 2. 유연한 애플리케이션 아키텍처 설계 (Flexible Architecture Design)
* **Clean/Hexagonal Architecture 기반 도메인 보호**: FastAPI, MariaDB 및 외부 LLM API(Gemini) 등의 기술 스펙 변화가 비즈니스 코어 규칙에 미치는 영향을 제어하기 위해 **Clean/Hexagonal Architecture** 및 **포트 & 어댑터 패턴**을 적극적으로 설계하고 검증했습니다. ([품앗이 아키텍처 검증 이력]({% link docs/side-projects/poomasi/index.md %}#2-clean--hexagonal-architecture-도입을-통한-도메인-보호))
* **SQLAlchemy Classical Mapping을 통한 도메인 독립성 극대화**: 데이터베이스 테이블 매핑 라이브러리(SQLAlchemy)의 결합도를 차단하기 위해 **Classical Mapping (`map_imperatively()`)**을 도입하여, DB 기술 스펙에 의존하지 않는 순수 도메인 단위 테스트 환경을 조성했습니다. ([Petting 도메인 격리 이력]({% link docs/side-projects/futurebyte/petting.md %}#1-sqlalchemy-classical-mapping-아키텍처-설계))
* **의존성 주입(DI) 컨테이너 및 커스텀 트랜잭션 라우팅**: `dependency-injector` 및 IoC 구조를 도입하여 런타임 구현체를 유연하게 주입받았고, FastAPI 라우팅을 확장한 커스텀 `TransactionRoute`를 직접 구현해 라우터 계층에서 세션 관리를 자동화했습니다. ([Oh-Manager DI 설계 이력]({% link docs/side-projects/futurebyte/oh-manager.md %}#2-의존성-주입di-기반-클린ddd-아키텍처-설계))
* **가상계좌 결제 및 정산 연동 라이프사이클 복구**: 중단되었던 Dozn API 가상계좌 결제/정산 연동 테스트망 규격을 역분석하고, 격리된 가상계좌 결제 테스트 환경을 복원해 잠재적 장애 리스크를 최소화했습니다. ([페이네스트 가상계좌 복구 이력]({% link docs/experience/paynest/index.md %}#1-중단된-가상계좌-결제-서비스-분석-및-재개-검증-환경-구축))

#### 3. 안정성 및 보안 제어 (Stability & Security Engineering)
* **AWS Lambda 기반 SQL Injection 취약점 분석 및 가이드 제안**: pymysql 환경에서 사용자 입력이 결합된 동적 쿼리의 Time-based SQL Injection 취약점을 진단 및 분석하고, 파라미터 바인딩 적용 가이드를 작성하여 사내 보안 가이드에 반영했습니다. ([엠포스 SQL Injection 분석 이력]({% link docs/experience/emforce/index.md %}#3-aws-lambda-기반-보안-취약점-진단-및-파라미터-바인딩-가이드-수립))
* **SSTI 취약점 예방 및 리소스 제어**: HTML 렌더러(wkhtmltopdf) 결합 시 발생할 수 있는 SSTI(Server-Side Template Injection) 공격 경로를 차단하고, 리소스 부하 예방을 위한 텍스트 크기(25,000자) 및 메모리 제한 설정을 구축했습니다. ([베이스트레이드 보안 설계 이력]({% link docs/experience/basetrade/index.md %}#2-p2p-법인-투자-플랫폼-개발-및-wkhtmltopdf-보안ssti-강화))
* **단일 인증 및 JWT 세션 자동 갱신**: 다양한 소셜 로그인을 통합 처리하는 OAuth 흐름을 단일 구조로 통합하고, Redis/JWT 기반의 Token rotation 방식을 직접 구축하여 동시성 오류 및 토큰 탈취 위협을 예방했습니다. ([팟팟 인증 설계 이력]({% link docs/side-projects/podpod/index.md %}#3-통합-소셜-인증-및-jwt-토큰-갱신-메커니즘-설계))
* **VPC Subnet 분리를 통한 데이터베이스 격리**: 퍼블릭 서브넷(WAS)과 프라이빗 서브넷(DB) 간의 엄격한 포트 제한 및 인바운드 보안 그룹 규칙 설정을 통해 외부 직접 접속을 완전히 차단하는 보안 아키텍처를 설계했습니다. ([품앗이 VPC 설계 이력]({% link docs/side-projects/poomasi/index.md %}#3-aws-vpc-이중화-및-rds-인프라-격리))

---

## Work Experience

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-time">2025.07 ~ 2025.12</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/paynest/index.md %}">페이네스트</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (계약직, 6개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>금융 결제망 분석 및 검증 환경 구축</strong>: 중단되었던 Dozn API 가상계좌 결제 서비스의 레거시 규격과 전체 데이터 라이프사이클을 분석하여 경남은행 연동망 테스트 결제 환경 복구</li>
          <li><strong>트랜잭션 검증 및 운영 표준화</strong>: 가상계좌 발급부터 대사 정산까지 시나리오별 결제 상태 전이를 검증하고 기능 규격서 및 운영 가이드를 현행화하여 시스템 안정성 확보</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2024.12 ~ 2025.06</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/emforce/index.md %}">엠포스</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (정규직, 7개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>데이터 수집 파이프라인 최적화</strong>: Selenium 브라우저 자동화 수집 방식을 Keycloak 인증 분석 기반의 HTTP API 수집으로 전환하여 수집 시간을 <strong>3~5분에서 30~45초로 약 80% 단축</strong>하고 오버헤드 제거</li>
          <li><strong>메모리 장애 분석 및 배치 안정화</strong>: 대용량 광고 데이터 병합 중 발생한 <code>MemoryError</code> 분석 후, 무중단 Swap 메모리 확장을 도입하여 서비스 중단 없이 배치 실행 안정성 확보</li>
          <li><strong>보안 취약점 진단 및 가이드 제안</strong>: AWS Lambda 환경의 데이터 조회 로직에서 Time-based SQL Injection 취약성을 검증하고, 파라미터 바인딩 적용 가이드를 보고서 형태로 도출해 사내 보안 수준 제고</li>
          <li><strong>Custom Test Runner 구축</strong>: Django 기본 테스트 러너(Test Runner)를 확장하여 테스트 메서드의 docstring을 터미널에 한글 설명으로 출력하게 함으로써 테스트 결과 가독성 향상</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2020.12 ~ 2023.10</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/basetrade/index.md %}">베이스트레이드</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (정규직, 2년 11개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>WebSocket 데이터 유실률 0% 달성</strong>: GPU 장비의 WebSocket 데이터 수집 누락 분석 후, Daphne 인스턴스 다중화(1개 → 4개) 및 Nginx 분산 처리를 통해 <strong>추가 인프라 비용 없이 데이터 유실률 0%</strong> 달성</li>
          <li><strong>P2P 법인 투자 플랫폼 구축 및 보안 강화</strong>: 핵심 금융/예치금 API 개발을 주도하여 <strong>누적 매출 20억 원 달성</strong>에 기여하고, wkhtmltopdf 기반 PDF 생성 시 발생할 수 있는 SSTI 취약점 차단 및 리소스 제어 (25,000자 제한) 정책 수립</li>
          <li><strong>금융 데이터 파이프라인 및 수집 자동화</strong>: EventBridge + Lambda 기반 수집 배치를 구축하고, Selenium UI 수집 방식을 HTTP Request 기반으로 리팩토링하여 데이터 수집 소요 시간을 <strong>90초에서 10~15초로 약 85% 단축</strong></li>
          <li><strong>테스트 환경 표준화</strong>: pytest 도입 및 모킹(Mocking) 표준 가이드를 정립하여 사내 테스트 커버리지를 <strong>52% → 71%로 향상</strong>시키고 Custom Test Runner 개발을 통해 개발 생산성 증대</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2020.09 ~ 2020.12</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/soulsoft/index.md %}">소울소프트</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">보안 취약점 진단 인턴 (4개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>주요 정보통신기반시설 보안 취약점 진단</strong>: 공공기관 기술적 취약점 분석·평가 가이드를 기반으로 Linux/Windows 서버의 보안 설정 점검 및 취약 항목 개선 방안 수립</li>
          <li><strong>헬스케어 빅데이터 수집 및 전처리 자동화</strong>: BeautifulSoup과 Selenium을 활용한 동적 웹 크롤러를 개발하여 헬스케어 분석에 활용 가능한 게시글/댓글 데이터셋 구축 자동화</li>
        </ul>
      </div>
    </div>
  </div>
</div>

---

## Side Projects

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-time">2025.12 ~ 진행중</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/side-projects/podpod/index.md %}">팟팟 (PodPod)</a> <span class="timeline-tag tag-side">Side Project</span></div>
      <div class="timeline-role">백엔드 개발자 (개인 BE 개발)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>모바일 앱 양대 스토어 출시</strong>: 기획, 디자인, 모바일(iOS/Android) 개발팀과 협업하여 구글 플레이스토어 및 애플 앱스토어에 앱을 성공적으로 런칭하고 실제 사용자 서비스 단계까지 프로젝트 완수</li>
          <li><strong>의존성 격리 및 Clean/Hexagonal 아키텍처 도입</strong>: 외부 프레임워크(FastAPI) 및 ORM(SQLAlchemy) 기술 스펙 변경이 비즈니스 도메인에 영향을 주지 않도록 레이어를 물리적으로 격리하고 테스트 용이성 극대화</li>
          <li><strong>통합 소셜 인증 및 JWT 세션 관리</strong>: 구글, 애플, 카카오, 네이버 등 다중 소셜 로그인 수단을 단일 인증 세션 API로 통합 설계하고 보안성이 확보된 JWT 토큰 발급 및 재발급 흐름 구축</li>
          <li><strong>동행 팟 매칭 및 실시간 소통 기능</strong>: 콘서트 동행 메이트 선발(신청서 승인/거절) 프로세스, 실시간 채팅 메시징 처리 및 메이트 신뢰도 자가 진단 평가 시스템 구현</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2025.02 ~ 2025.11</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/side-projects/poomasi/index.md %}">품앗이 (Poomasi)</a> <span class="timeline-tag tag-side">Side Project</span></div>
      <div class="timeline-role">백엔드 개발자 (품앗이 팀, 8개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>데이터 수집 및 정제 자동화</strong>: 7개 IT 기업의 채용 데이터를 파싱·표준화하고, Gemini 1.5 Flash와 프롬프트 엔지니어링을 결합해 요구 기술 스택을 자동 분석 및 추출하는 파이프라인 구축</li>
          <li><strong>Clean/Hexagonal Architecture 설계</strong>: Port & Adapter 패턴을 도입하고 `dependency-injector`를 적용하여 데이터베이스, 외부 API 등의 세부 기술과 비즈니스 로직을 격리함으로써 유지보수성 극대화</li>
          <li><strong>보안 및 인프라 이중화 설계</strong>: VPC Subnet 이중화를 통해 WAS 서버는 Public 영역에, 데이터베이스(RDS)는 Private 영역에 배치함으로써 외부 직접 접근을 격리하고 보안성 강화</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2024.04 ~ 2024.07</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/side-projects/futurebyte/petting.md %}">Petting</a> <span class="timeline-tag tag-side">Side Project</span></div>
      <div class="timeline-role">백엔드 개발자 (FutureByte 팀, 2개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>Classical Mapping 아키텍처 설계</strong>: SQLAlchemy `map_imperatively()` API를 통해 데이터 모델과 비즈니스 엔티티를 물리적으로 완전 격리(DIP)하여 도메인 독립성 극대화</li>
          <li><strong>공간 데이터 및 외부 API 연동</strong>: Kakao Local API를 IoC 컨테이너를 통해 어댑터로 통합하고 유저 주소 검증 및 경위도 좌표 데이터 정제 자동화</li>
          <li><strong>도메인 이벤트(Domain Event) 도입</strong>: 미디어 업로드 성공 이벤트를 비동기 전파하여 회원 자산 리워드 로직과의 결합도를 완전히 제거</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2024.02 ~ 2024.04</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/side-projects/futurebyte/oh-manager.md %}">Oh-Manager</a> <span class="timeline-tag tag-side">Side Project</span></div>
      <div class="timeline-role">백엔드 개발자 (FutureByte 팀, 2개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>트랜잭션 라우터 자체 구현</strong>: FastAPI의 라우팅 기능을 확장한 `TransactionRoute` 데코레이터를 구현해 라우터 계층에서 세션 롤백/커밋 관리를 자동화하고 도메인 로직 순수성 확보</li>
          <li><strong>의존성 주입 구조 설계</strong>: `Dependency Injector` DI 컨테이너와 `patch_ioc`를 적용하여 데이터베이스 및 AWS 인프라 의존성을 동적 주입함으로써 결합도 최소화</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2023.10 ~ 2024.02</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/side-projects/futurebyte/folder.md %}">FOLDER</a> <span class="timeline-tag tag-side">Side Project</span></div>
      <div class="timeline-role">백엔드 개발자 (FutureByte 팀, 4개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>방화벽 우회 및 비동기 수집 파이프라인</strong>: 10개 매체 대상 `cloudscraper`/`fake-useragent`로 Cloudflare 방화벽을 우회하고 `aiohttp`/`aiomysql`로 수집 속도와 대량 적재 최적화</li>
          <li><strong>LLM 데이터 정제 자동화</strong>: `Langchain` 및 `OpenAI API`를 정제 파이프라인에 도입해 본문 요약 및 키워드 분류 작업 자동화</li>
        </ul>
      </div>
    </div>
  </div>
</div>
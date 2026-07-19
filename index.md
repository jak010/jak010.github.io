---
title: Home
layout: home
nav_order: 1
description: "서비스 운영 과정에서 발생하는 성능, 안정성, 보안 문제를 분석하고 개선하는 백엔드 개발자의 포트폴리오입니다."
permalink: /
---
# Intro

4년 4개월간 다양한 서비스 환경에서 백엔드 개발과 데이터 처리 업무를 수행하며, 안정적인 서비스 운영과 지속적인 개선을 경험해 온 백엔드 개발자입니다. 단순히 기능 구현에 그치지 않고, 서비스가 운영되는 과정에서 발생하는 성능 저하와 장애 원인을 코드와 데이터 흐름 관점에서 분석하고 개선하는 데 관심을 가지고 있습니다.

특히 반복적인 데이터 수집 및 처리 과정에서 발생하는 비효율을 찾아 개선하는 경험을 쌓아왔습니다. 데이터 처리 흐름을 분석해 병목 구간을 찾아내고, 불필요한 외부 통신 구조를 개선하여 전체 처리 시간을 기존 대비 약 80%~85% 개선하는 등 서비스 응답성과 운영 효율성을 높였습니다.

또한 제한된 시스템 환경에서 안정적인 서비스를 운영하기 위해 서버 자원 활용 방식과 애플리케이션 구조를 지속적으로 개선해 왔습니다. 트래픽 처리 흐름을 분석하고 데이터 처리 구조를 개선하여 추가 인프라 비용 없이 데이터 처리 안정성을 확보했으며, 대량 데이터 처리 과정에서 발생하는 메모리 문제와 장애 원인을 분석해 서비스 운영 안정성을 높였습니다. 결제 및 외부 시스템 연동 과정에서도 발생 가능한 오류 상황을 점검하고 검증 절차를 개선하여 안정적인 서비스 운영에 기여했습니다.

저는 장기적으로 유지보수하기 좋은 코드를 만드는 것을 중요하게 생각합니다. 요구사항 변화에 유연하게 대응할 수 있도록 역할과 책임을 분리하고, 비즈니스 로직과 기술 구현을 적절히 분리하는 구조를 고민해 왔습니다. 또한 개발 과정에서 발생할 수 있는 보안 취약점과 운영 리스크를 사전에 고려하며, 안정성과 확장성을 함께 갖춘 서비스를 만드는 백엔드 개발자를 지향합니다.

---
## 🛠️ Skill Inventory (기술 스택)

| 분류 | 기술 스택 |
| :--- | :--- |
| **Language** | Python, Java |
| **Framework & Library** | Django, Django REST Framework (DRF), FastAPI, Spring Boot, Pytest, Daphne, Django Channels, JPA, MyBatis |
| **Database** | MySQL, MariaDB, Redis |
| **DevOps & Infra** | AWS (EC2, ECS, Lambda, EventBridge, Route53, S3, RDS, ELB, App Runner, Secrets Manager, ECR, API Gateway, CodeCommit, Parameter Store, CloudWatch), Docker, Nginx, Akamai, Fortinet, Juniper |


## ⏳ Experience Timeline

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
          <li><strong>트랜잭션 검증 및 운영 표준화</strong>: 가상계좌 발급, 입금 통지, 결제 완료, 정산 배치 등 시나리오별 결제 상태 전이를 검증하고 기능 규격서 및 운영 가이드를 현행화하여 시스템 안정성 확보</li>
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
          <li><strong>보안 및 인프라 IaC 구축</strong>: VPC Subnet 이중화를 통한 RDS 격리로 보안을 강화하고, Terraform을 활용해 전체 AWS 인프라 리소스를 선언적 코드로 형상 관리 및 자동 배포 환경 구축</li>
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

  <div class="timeline-item">
    <div class="timeline-time">2020.12 ~ 2023.10</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/basetrade/index.md %}">베이스트레이드</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (정규직, 2년 11개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>WebSocket 데이터 유실 개선</strong>: GPU 장비의 WebSocket 데이터 수집 누락 분석 후, Daphne 인스턴스 다중화(1개 → 4개) 및 Nginx 분산 처리를 통해 <strong>추가 인프라 비용 없이 데이터 유실률 0%</strong> 달성</li>
          <li><strong>P2P 법인 투자 플랫폼 구축 및 보안 강화</strong>: 핵심 금융/예치금 API 개발을 주도하여 **누적 매출 20억 원 달성**에 기여하고, wkhtmltopdf 기반 PDF 생성 시 발생할 수 있는 SSTI 취약점 차단 및 리소스 제어 (25,000자 제한) 정책 수립</li>
          <li><strong>금융 데이터 파이프라인 및 수집 자동화</strong>: EventBridge + Lambda 기반 수집 배치를 구축하고, Selenium UI 수집 방식을 HTTP Request 기반으로 리팩토링하여 데이터 수집 소요 시간을 **90초에서 10~15초로 약 85% 단축**</li>
          <li><strong>테스트 환경 표준화</strong>: pytest 도입 및 모킹(Mocking) 표준 가이드를 정립하여 사내 테스트 커버리지를 **52% → 71%로 향상**시키고 Custom Test Runner 개발을 통해 개발 생산성 증대</li>
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
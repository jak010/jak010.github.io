---
title: Home
layout: home
nav_order: 1
description: "서비스 운영 과정에서 발생하는 성능, 안정성, 보안 문제를 분석하고 개선하는 백엔드 개발자의 포트폴리오입니다."
permalink: /
---
# Intro

- `BLOG`: https://jakpentest.tistory.com/

정보보호학을 전공하며 시스템의 동작 원리를 이해하는 것에서 개발을 시작했고, 지난 4년 4개월 동안 다양한 서비스의 백엔드를 개발하며 문제를 분석하고 개선하는 과정에서 가장 큰 보람을 느껴왔습니다.

새로운 기능을 구현하는 것만큼이나 기존 시스템을 이해하고 병목과 장애의 원인을 찾아 더 안정적이고 유지보수하기 쉬운 구조로 개선하는 일을 즐깁니다. 그래서 개발을 할 때도 "어떻게 구현할까?"보다 "왜 이런 구조가 되었을까?"를 먼저 고민하는 편입니다.

기술을 선택할 때는 유행이나 최신 기술보다 서비스의 규모와 운영 환경에 적합한 선택을 중요하게 생각합니다. 테스트 코드, 문서화, 모니터링과 같은 보이지 않는 영역도 결국 서비스의 안정성과 팀의 생산성을 결정하는 중요한 요소라고 믿으며 꾸준히 개선해 왔습니다.

직무 외에도 사이드 프로젝트를 통해 새로운 기술과 아키텍처를 직접 검증하고, 개발 과정에서 얻은 경험과 시행착오를 문서와 글로 정리하며 배움을 지속적으로 축적하고 있습니다. 앞으로도 복잡한 문제를 단순하고 이해하기 쉬운 구조로 해결하며, 함께 일하는 사람들이 신뢰할 수 있는 백엔드 엔지니어가 되고자 합니다.

---

## Experience Timeline

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-time">2025.12 ~ 진행중</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/side-projects/podpod/index.md %}">팟팟 (PodPod)</a> <span class="timeline-tag tag-side">Side Project</span></div>
      <div class="timeline-role">백엔드 개발자 (개인 BE 개발, 2025.12 ~ 진행중)</div>
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
          <li><strong>WebSocket 데이터 유실률 0% 달성</strong>: GPU 장비의 WebSocket 데이터 수집 누락 분석 후, Daphne 인스턴스 다중화(1개 → 4개) 및 Nginx 분산 처리를 통해 <strong>추가 인프라 비용 없이 데이터 유실률 0%</strong> 달성</li>
          <li><strong>P2P 법인 투자 플랫폼 구축 및 보안 강화</strong>: 핵심 금융/예치금 API 개발을 주도하여 <strong>누적 매출 20억 원 달성</strong>에 기여하고, wkhtmltopdf 기반 PDF 생성 시 발생할 수 있는 SSTI 취약점 차단 및 리소스 제어 (25,000자 제한) 정책 수립</li>
          <li><strong>금융 데이터 파이프라인 및 수집 자동화</strong>: EventBridge + Lambda 기반 수집 배치를 구축하고, Selenium UI 수집 방식을 HTTP Request 기반으로 리팩토링하여 데이터 수집 소요 시간을 **90초에서 10~15초로 약 85% 단축**</li>
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
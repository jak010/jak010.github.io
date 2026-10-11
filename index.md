---
title: Home
layout: home
nav_order: 1
description: "성능 최적화와 안정적인 아키텍처 설계에 몰입하는 4년 차 백엔드 개발자 Jako의 포트폴리오입니다."
permalink: /
---

# 포트폴리오

## About Me

**총 경력:** 4년 4개월 · 백엔드 엔지니어  
**핵심 분야:** 아키텍처 설계 · 성능 최적화 · 안정성 · 보안  
**채널:** <a href="https://github.com/jak010" target="_blank">GitHub</a> · <a href="https://jakpentest.tistory.com/" target="_blank">Tech Blog</a>

문제가 생기면 먼저 원인을 확인하고, 주어진 환경에서 해결할 방법을 찾습니다.

4년 4개월 동안 백엔드 시스템을 개발하며 성능 저하, 메모리 부족, 데이터 수집 병목처럼 운영 환경에서 발생하는 문제를 직접 해결해왔습니다. RAM 2GB의 소형 서버에서 OOM으로 배치 작업이 중단되었을 때는 메모리 사용량과 데이터 처리 방식을 분석하고, Swap 확장과 메모리 연산 개선을 통해 배치 작업을 안정화했습니다. 데이터 수집 과정에서는 브라우저 자동화의 병목을 찾아 인증 방식을 API 통신으로 전환했고, 처리 시간을 3~5분에서 30~45초로 약 80% 단축했습니다.

문제를 한 번 해결하는 것에 그치지 않고, 같은 문제가 반복되지 않도록 구조까지 살펴보는 편입니다. 서버 증설이 어려운 상황에서는 인스턴스 다중화와 분산 처리를 직접 구현해 **데이터 유실률 0%**를 달성했고, 비즈니스 로직이 특정 기술에 묶이지 않도록 도메인과 인프라의 결합도를 낮추는 아키텍처도 설계하고 검증했습니다.

새로운 기술이나 구조를 그대로 적용하기보다 실제 환경에서 직접 검증하고, 그 과정에서 얻은 결과를 다시 개선에 활용합니다. 기능이 동작하는 것에서 끝나지 않고, 왜 문제가 발생했는지 이해하고 다시 문제가 생기지 않는 방향을 고민하는 백엔드 개발자입니다.

---

## Tech Blog

개발을 하면서 생긴 궁금증을 그냥 지나치지 않고, 직접 찾아보고 만들어보며 기록하고 있습니다.

업무에서 사용하는 기술뿐만 아니라 새롭게 등장하는 개발 도구나 기술에도 관심을 가지고, 필요하면 작은 프로젝트를 만들어 직접 사용해보거나 기존 방식과 비교해보기도 합니다.

그 과정에서 얻은 경험과 시행착오를 기술 블로그에 꾸준히 기록하고 있습니다.

<!-- BLOG-POST-LIST:START -->
- [Apache를 웹 서버로 쓰는 WSGI의 Python Sub Intepreter 이슈](https://jakpentest.tistory.com/498) (2026.10.09)
- [한빛미디어 - 나는리뷰어다2026, AI 시대의 엔지니어링 전략](https://jakpentest.tistory.com/496) (2026.08.27)
- [3. AI 가지고 놀기 - PoorMan의 AI Remote Control](https://jakpentest.tistory.com/494) (2026.08.12)
<!-- BLOG-POST-LIST:END -->

### 🔥 인기 포스트 (최근 30일)
<!-- POPULAR-POSTS:START -->
- 🥇 [환경변수 관리 도구인 Infisical 에 대한 노트](https://jakpentest.tistory.com/483) (최근 30일 조회수: 146회)
- 🥈 [마비노기 패킷 송수신 데이터 관찰기](https://jakpentest.tistory.com/411) (최근 30일 조회수: 51회)
- 🥉 [Commit Message 자동화하기, 근데 AI를 곁들인](https://jakpentest.tistory.com/456) (최근 30일 조회수: 44회)
<!-- POPULAR-POSTS:END -->

---

## Work Experience

<div class="timeline">
  <div class="timeline-item">
    <div class="timeline-time">2025.07 ~ 2025.12</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/paynest/index.md %}">P사</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (계약직, 6개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>기존 결제망 동작 검증 환경 구성</strong>: 운영 중단된 가상계좌 결제 서비스의 라이프사이클을 파악하기 위해, 외부 API 연동망을 활용한 검증 환경을 구성하여 실제 운영 데이터 오염 없이 전체 결제 흐름을 테스트함</li>
          <li><strong>복잡한 상태 흐름 분석 및 구조화</strong>: 기존 시스템의 파편화된 결제 상태값과 트랜잭션 로그를 추적하여 FSM(유한 상태 기계) 형태로 구조화하고 운영 가이드로 문서화함으로써 시스템 유지보수성을 높임</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2024.12 ~ 2025.06</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/emforce/index.md %}">E사</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (정규직, 7개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>데이터 수집 로직 개선</strong>: 기존 브라우저 자동화(Selenium) 수집 방식의 네트워크 요청을 분석하여 API 통신 방식으로 전환함으로써 수집 시간을 **약 80%** 단축(**3~5분** → **30~45초**)</li>
          <li><strong>배치 작업 메모리 최적화</strong>: **2GB** RAM 환경에서 발생하던 OOM(MemoryError) 원인을 분석하고, Swap 확장 및 데이터 연산 최적화를 적용하여 배치 중단 문제 해결</li>
          <li><strong>SQL Injection 취약점 분석 및 보안 가이드 작성</strong>: AWS Lambda 환경에서 사용자 입력값이 쿼리에 결합되는 구조를 검증하고, 파라미터 바인딩을 적용하여 안전한 SQL 작성 기준 마련</li>
          <li><strong>개발 환경 개선</strong>: Django Custom Test Runner를 활용하여 테스트 결과 출력 시 한글 설명이 표시되도록 개선해 오류 파악 편의성 향상</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2020.12 ~ 2023.10</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/basetrade/index.md %}">B사</a> <span class="timeline-tag tag-company">Company</span></div>
      <div class="timeline-role">백엔드 개발자 (정규직, 2년 11개월)</div>
      <div class="timeline-desc">
        <ul>
          <li><strong>WebSocket 데이터 수집 병목 개선</strong>: 단일 프로세스에서 처리하던 데이터 수집 로직의 누락 원인을 분석하고, 서버 인스턴스를 다중화하여 인프라 증설 없이 수집 안정성을 개선함</li>
          <li><strong>금융 거래 정합성 및 보안 조치</strong>: 동시성 처리를 위해 비관적 락을 적용하여 트랜잭션 무결성을 확보하고, PDF 보고서 생성 시 발생할 수 있는 템플릿 인젝션(SSTI) 및 자원 고갈 문제를 사전 방지</li>
          <li><strong>데이터 수집 파이프라인 최적화</strong>: 매일 반복되는 금융 데이터 수집을 자동화하고, 기존 브라우저 자동화 방식의 병목을 API 통신으로 변경하여 수집 시간을 **약 90초**에서 **10~15초**로 단축</li>
          <li><strong>테스트 환경 도입</strong>: 기능 배포 시 발생하던 불안정성을 줄이기 위해 pytest를 도입하고, 외부 연동망을 모킹(Mocking)하여 테스트 커버리지를 **52%**에서 **71%**로 향상</li>
        </ul>
      </div>
    </div>
  </div>

  <div class="timeline-item">
    <div class="timeline-time">2020.09 ~ 2020.12</div>
    <div class="timeline-badge"></div>
    <div class="timeline-content">
      <div class="timeline-title"><a href="{% link docs/experience/soulsoft/index.md %}">S사</a> <span class="timeline-tag tag-company">Company</span></div>
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
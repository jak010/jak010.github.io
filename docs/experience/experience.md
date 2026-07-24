---
title: Experience
layout: default
nav_order: 3
has_children: true
has_toc: false
---

# Experience

회사에서의 경력과 수행했던 주요 업무 및 프로젝트를 정리한 내용입니다. (총 경력: **4년 4개월**)

---

<div class="overview-list">
  <!-- 페이네스트 -->
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <h3 class="overview-card-title">페이네스트 <span class="timeline-tag tag-company">Company</span></h3>
        <div class="overview-card-meta">백엔드 개발자 (계약직) | 2025.07 ~ 2025.12 (6개월)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>회사 소개:</strong> 핀테크 및 전자금융 서비스를 제공하는 기업으로, 선불전자지급수단 발행·관리업 및 PG 라이선스를 기반으로 대표 서비스인 네스트페이(NestPay)를 운영합니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> Java, Spring Boot, JPA, MyBatis, Dozn API, GitLab CI/CD, On-premise
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>중단된 가상계좌 결제 서비스 복구</strong>: 중단되었던 Dozn API 가상계좌 결제/정산 연동 테스트망 규격을 분석하여 경남은행 연동망 테스트 결제 환경 복구 및 서비스 재개 검증 완료</li>
          <li><strong>결제 상태 검증 및 가이드 현행화</strong>: 가상계좌 발급부터 대사 정산까지 시나리오별 결제 상태 전이를 검증하고 기능 규격서 및 운영 가이드를 복구하여 시스템 안정성 확보</li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/experience/paynest/index.md %}" class="btn-detail">상세 업무 이력 보기 ➔</a>
    </div>
  </div>

  <!-- 엠포스 -->
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <h3 class="overview-card-title">엠포스 <span class="timeline-tag tag-company">Company</span></h3>
        <div class="overview-card-meta">백엔드 개발자 (정규직) | 2024.12 ~ 2025.06 (7개월)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>회사 소개:</strong> 빅데이터 기반의 디지털 마케팅 솔루션을 제공하는 국내 1세대 디지털 IMC 전문 기업으로, 검색광고, 디스플레이 광고, 소셜 마케팅 등 종합 디지털 광고 서비스를 제공합니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> Python, Django, DRF, Pytest, AWS (EC2, ECR, Lambda, EventBridge, RDS)
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>데이터 수집 파이프라인 최적화 (수집 속도 80% 단축)</strong>: 기존 Selenium 기반 브라우저 자동화 방식의 병목을 분석하여 Keycloak 인증 분석 기반의 HTTP API 직접 호출 방식으로 전환하여 수집 시간을 <strong>3~5분에서 30~45초로 단축</strong></li>
          <li><strong>대용량 데이터 병합 배치 메모리 장애 개선 (장애 재발률 0%)</strong>: 광고 데이터 병합 중 발생한 OOM `MemoryError`를 분석하여 서버 무중단 Swap 메모리 확장을 도입하여 배치 안정성 확보</li>
          <li><strong>서버 취약점 검증 및 보안 제안</strong>: AWS Lambda 기반 API의 Time-based SQL Injection 취약성을 검증하고, 파라미터 바인딩 적용 가이드를 기술 보고서 형태로 작성하여 사내 보안 수준 제고</li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/experience/emforce/index.md %}" class="btn-detail">상세 업무 이력 보기 ➔</a>
    </div>
  </div>

  <!-- 베이스트레이드 -->
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <h3 class="overview-card-title">베이스트레이드 <span class="timeline-tag tag-company">Company</span></h3>
        <div class="overview-card-meta">백엔드 개발자 (정규직) | 2020.12 ~ 2023.10 (2년 11개월)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>회사 소개:</strong> 모바일 애플리케이션 및 웹 기반 소프트웨어 개발을 비롯해, 시스템 고도화 및 운영·유지보수 서비스를 제공하는 IT 전문 기업입니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> Python, FastAPI, Django, Daphne (ASGI), Docker, Nginx, Redis, AWS (EC2, ECS, Lambda, RDS)
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>추가 인프라 비용 없이 WebSocket 데이터 유실률 0% 달성</strong>: 250대 이상 GPU 장비의 WebSocket 수집 병목 원인을 분석하고, Daphne 인스턴스 다중화 및 Nginx 로드밸런싱 분산 처리를 자체 구현하여 안정성 확보</li>
          <li><strong>P2P 법인 투자 플랫폼 런칭</strong>: 법인 투자 프로세스 및 보고서 생성 자동화 API 개발을 주도하여 <strong>누적 매출 20억 원</strong> 달성에 기여하고, wkhtmltopdf 기반 PDF 생성 시 발생 가능한 SSTI 취약점 차단</li>
          <li><strong>테스트 환경 표준화 (커버리지 52% ➔ 71%)</strong>: pytest 및 Mocking 표준 가이드를 수립하여 개발 생산성을 향상시키고 코드 신뢰성 확보</li>
          <li><strong>금융 데이터 수집 자동화 최적화 (수집 속도 85% 단축)</strong>: EventBridge + Lambda 기반 배치 환경을 구축하고, Selenium UI 수집 방식을 HTTP Request 기반으로 전환하여 수집 소요 시간을 <strong>90초에서 10~15초로 단축</strong></li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/experience/basetrade/index.md %}" class="btn-detail">상세 업무 이력 보기 ➔</a>
    </div>
  </div>

  <!-- 소울소프트 -->
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <h3 class="overview-card-title">소울소프트 <span class="timeline-tag tag-company">Company</span></h3>
        <div class="overview-card-meta">보안 취약점 진단 인턴 | 2020.09 ~ 2020.12 (4개월)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>회사 소개:</strong> 정보보안 취약점 진단 및 컨설팅과 디지털 헬스케어 서비스를 제공하는 IT 기업입니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> Shell Script, Python, BeautifulSoup, Selenium
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>인프라 보안 취약점 진단</strong>: 공공기관 기술적 취약점 분석·평가 가이드를 기반으로 Linux/Windows 서버의 보안 설정 점검 및 취약 항목 개선 방안 수립</li>
          <li><strong>헬스케어 빅데이터 수집 및 전처리 자동화</strong>: BeautifulSoup과 Selenium을 활용한 동적 웹 크롤러를 개발하여 데이터셋 구축 파이프라인 자동화</li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/experience/soulsoft/index.md %}" class="btn-detail">상세 업무 이력 보기 ➔</a>
    </div>
  </div>
</div>

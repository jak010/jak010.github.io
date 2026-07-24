---
layout: default
title: Side Project
nav_order: 4
has_children: true
permalink: /docs/side-projects
---

# Side Project

팀 단위로 진행한 사이드 프로젝트로, 새로운 기술 스택을 도입하고 검증하는 과정에서 기술 역량을 확장하기 위해 수행한 프로젝트입니다.

## 목차
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 1. 팟팟 (PodPod) - 모바일 스토어 출시 및 Clean/Hexagonal 아키텍처 의존성 격리

<div class="overview-list">
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <div class="overview-card-meta">백엔드 개발자 | 2025.12 ~ 진행중 | PO 1, 기획 1, 디자인 1, BE 1, 마케팅 1 (총 5명)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>프로젝트 소개:</strong> 콘서트나 페스티벌 등 오프라인 문화 예술 행사에 동행할 메이트를 매칭하고 소통하는 모바일 서비스입니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> FastAPI, SQLAlchemy, PostgreSQL, Clean/Hexagonal Architecture, JWT, Pytest, GitHub Actions
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>모바일 앱 양대 스토어 공식 출시 및 운영</strong>: 크로스 플랫폼 환경에서 모바일 및 기획팀과 긴밀하게 협업하여 Google Play Store 및 Apple App Store에 앱을 성공적으로 런칭하고 서비스 운영 완료</li>
          <li><strong>의존성 격리 아키텍처 도입</strong>: 외부 프레임워크(FastAPI) 및 ORM(SQLAlchemy)의 버전 업그레이드나 세부 사양 변경이 도메인 영역에 미치는 전파를 차단하기 위해 계층형 아키텍처를 물리적으로 설계하고 테스트 용이성 극대화</li>
          <li><strong>인증 구조 단일화</strong>: 구글, 애플, 카카오, 네이버 등 다중 소셜 로그인 수단을 단일 인증 세션 API로 통일하고 보안성이 확보된 JWT 세션 발급/재발급 흐름 구현</li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/side-projects/podpod/index.md %}" class="btn-detail">상세 프로젝트 이력 보기 ➔</a>
    </div>
  </div>
</div>

---

## 2. 품앗이 (Poomasi) - Gemini LLM 기반 데이터 정제 및 검색 엔진(SEO) 최적화

<div class="overview-list">
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <div class="overview-card-meta">백엔드 개발자 | 2025.02 ~ 2025.11 (8개월) | PO/PM 1, 디자인 1, BE 1, FE 2 (총 4명)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>프로젝트 소개:</strong> IT 취준생에게 현업 선배 멘토를 연결해 주고, 채용공고 분석 데이터를 매칭하여 최적의 취업 가이드를 제공하는 플랫폼입니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> FastAPI, Gemini 1.5 Flash, dependency-injector, AWS (EC2, Aurora MySQL), GitHub Actions, SEO 최적화
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>Gemini 1.5 Flash 기반 기술 요구스택 추출 자동화</strong>: 7개 IT 기업 채용 데이터 수집 파이프라인을 구축하고, 프롬프트 엔지니어링을 적용하여 채용 요건에서 핵심 기술스택을 자동 정밀 추출하는 데이터 정제 파이프라인 개발 (2,500건 이상 처리)</li>
          <li><strong>Clean/Hexagonal Architecture 설계</strong>: Port & Adapter 패턴과 `dependency-injector`를 적용하여 데이터베이스, 외부 API 등의 물리 세부 구현과 비즈니스 로직을 격리하여 대규모 확장성 확보</li>
          <li><strong>SEO 파이프라인 구축을 통한 구글 첫 페이지 노출</strong>: Open Graph, JSON-LD 스키마 마크업 동적 반환 및 Sitemap 자동 생성을 통해 유기적 검색 유입을 극대화하여 핵심 키워드 구글 최상위 노출 달성</li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/side-projects/poomasi/index.md %}" class="btn-detail">상세 프로젝트 이력 보기 ➔</a>
    </div>
  </div>
</div>

---

## 3. FutureByte - Classical Mapping 설계 및 대용량 비동기 수집 파이프라인 구축

<div class="overview-list">
  <div class="overview-card">
    <div class="overview-card-header">
      <div class="overview-card-title-group">
        <div class="overview-card-meta">백엔드 개발자 | 2023.10 ~ 2024.07 (9개월) | PO/PM 1, 기획 1, 디자인 1, BE 1, FE 2 (총 6명)</div>
      </div>
    </div>
    <div class="overview-card-body">
      <div class="overview-card-section">
        <strong>프로젝트 소개:</strong> 펫 매칭(Petting), 오디션 중계(Oh-Manager), 패션 정보 크롤러(FOLDER) 등 시장 검증형 프로덕트를 연속 개발한 사이드 프로젝트 팀입니다.
      </div>
      <div class="overview-card-section">
        <strong>주요 기술:</strong> FastAPI, Django, SQLAlchemy (map_imperatively), Daphne (ASGI), cloudscraper, OpenAI API
      </div>
      <div class="overview-card-section">
        <strong>핵심 도전 & 문제 해결:</strong>
        <ul class="overview-card-highlights">
          <li><strong>Petting (반려견 성격유형 매칭)</strong>: SQLAlchemy `map_imperatively()` API를 활용해 데이터 모델과 도메인 엔티티를 완전히 격리(DIP)하는 Classical Mapping 설계 및 카카오 로컬 좌표계 기반 반려견 탐색 구현</li>
          <li><strong>Oh-Manager (신인 배우 오디션 중계)</strong>: FastAPI의 라우팅 기능을 확장한 `TransactionRoute` 데코레이터를 직접 개발하여 라우터 레벨에서 데이터베이스 세션 롤백/커밋 관리를 자동화하고 도메인 로직 순수성 확보</li>
          <li><strong>FOLDER (패션 정보 수집 크롤러)</strong>: cloudscraper와 fake-useragent를 활용해 Cloudflare 방화벽을 우회하고, aiohttp/aiomysql 비동기 IO 연동으로 다중 패션 매체 데이터 수집 속도 극대화</li>
        </ul>
      </div>
    </div>
    <div class="overview-card-footer">
      <a href="{% link docs/side-projects/futurebyte/index.md %}" class="btn-detail">상세 프로젝트 이력 보기 ➔</a>
    </div>
  </div>
</div>

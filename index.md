---
title: Home
layout: home
nav_order: 1
description: "서비스 운영 과정에서 발생하는 성능, 안정성, 보안 문제를 분석하고 개선하는 백엔드 개발자의 포트폴리오입니다."
permalink: /
---
# PortPolio

4년 4개월간 다양한 비즈니스 환경에서 Python(FastAPI, Django)과 Java(Spring Boot) 기반 백엔드 시스템을 개발하고 운영해 온 백엔드 엔지니어입니다.
단순히 주어지는 기능을 구현하는 데 그치지 않고, 시스템의 내부 동작 원리와 인프라 자원의 효율성을 파악하여 실질적인 비즈니스 성능과 안전성을 향상하는 데 집중해 왔습니다.

그동안 다음과 같은 핵심 성과를 중심으로 비즈니스에 기여해 왔습니다.
*   **금융 및 외부 API 연동 안정화**: 가상계좌 결제/정산 프로세스의 Dozn API 규격을 분석하여 단절된 테스트망을 복구하고 네트워크 접근 정책(Akamai, Fortinet)을 조율했으며, P2P 투자 플랫폼 구축을 주도하여 **누적 매출액 20억 원** 달성에 기여했습니다.
*   **대용량 데이터 수집 및 인프라 효율성 극대화**: **추가 인프라 비용 증설 없이** Daphne(ASGI) 인스턴스를 **1개에서 4개로 다중화**하여 WebSocket 실시간 유실률 **0%**를 달성했습니다. 또한 Selenium 방식의 수집 병목을 API 호출 구조로 전환하여 데이터 수집 소요 시간을 **3~5분에서 30~45초로 약 80~85% 단축**했으며, 환율 수집 프로세스 성능도 **90초에서 10~15초로 약 85% 단축**시켰습니다.
*   **웹 어플리케이션 보안 결함 진단 및 보완**: 데이터 조회 로직의 SQL Injection 취약성을 **5초 지연(PoC)** 방식으로 검증하여 파라미터 바인딩을 적용했으며, PDF 생성 시 **25,000자 글자수 제한** 및 입력값 이스케이프 정책을 도입하여 웹 서버 자원 고갈 및 SSTI 유출 위협을 차단했습니다.
*   **테스트 환경 표준화 및 개발 생산성 개선**: 수동 검증 위주의 조직에 최초로 `pytest` 프레임워크와 Mocking 가이드를 수립하여 테스트 커버리지를 **52%에서 71%로 약 19%p 상향**하였으며, 테스트 결과의 한글 docstring이 콘솔에 직접 출력되도록 Custom Test Runner를 개발하여 디버깅 가시성을 개선했습니다.


---

## 🛠️ Skill Inventory (기술 스택)

| 분류 | 기술 스택 |
| :--- | :--- |
| **Language** | Python, Java |
| **Framework & Library** | Django, Django REST Framework (DRF), FastAPI, Spring Boot, Pytest, Daphne, Django Channels, JPA, MyBatis |
| **Database** | MySQL, MariaDB, Redis |
| **DevOps & Infra** | AWS (EC2, ECS, Lambda, EventBridge, Route53, S3, RDS, ELB, App Runner, Secrets Manager, ECR, API Gateway, CodeCommit, Parameter Store, CloudWatch), Docker, Nginx, Akamai, Fortinet, Juniper |
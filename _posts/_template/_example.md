---
title: test, 2025.07.14
excerpt: test
categories:
  - Side Project
tags:
  - Side-Project
permalink: /categories/side-projects/
toc: true
toc_sticky: true
date: 2020-05-21
last_modified_at: 2021-10-09
---


# CHAPTER 3 :  클래스 설계  

> 단계 : 실전  
> 제목 : 클래스 설계, 모든 것과 연결되는 설계 기반  
> 내용 : 이 책 전체의 기반이 되는 클래스와 객체 지향 설계의 기초를 다룹니다.  

**P.22**
- 클래스 기반이란 "데이터"와 "그 데이터를 조작하는 논리"를 클래스라는 기본 단위로 묶어서 정의해가며, 프로그램을 작성하는 방법입니다. 
- 이 장에서는 객체 지향 설계의 기본이라고 할 수 있는 클래스 설계의 기본을 설명합니다. 객체 지향 프로그래밍에서 클래스보다 작은 단위로는 조건 분기와 메서드 등이 있습니다.
	- 클래스 설계가 잘 잡혀 있어야, 유지보수와 변경이 쉬운 코드를 만들 수 있습니다.
- 이 장에서는 데이터 클래스를 예로 악마 퇴치의 기본이 되는 클래스 설계 방법을 설명합니다. 데이터 클래스 속에 숨어있는 악마들을 하나하나 퇴치해서 우아하고 성숙한 클래스를 만드는 방법을 살펴봅시다.

## 3.1 클래스 단위로 잘 동작하도록 설계하기  
- 클래스는 단독으로도 안전하게 작동할 수 있도록 설계해야 한다.
- 외부에서 복잡한 초기 설정 없이 사용할 수 있어야 하며, 내부 상태가 쉽게 망가지지 않도록 제한된 조작만 허용해야 한다.
#### 3.1.1 클래스 구성 요소  
좋은 클래스의 구성
- 인스턴스 변수
- 해당 변수를 안전하게 조작하는 메서드    

**데이터 클래스의 문제점**
- 인스턴스 변수만 존재하고, 로직은 다른 클래스에 분산됨  
    → 관련성 파악 어려움, 코드 중복, 초기화 누락 등 발생
- 초기화와 유효성 검사까지 외부 클래스에 의존  
    → 잘못된 값 유입 가능, 자기 방어 능력이 없음
    
**핵심 원칙**
- 클래스는 자신의 상태를 스스로 보호할 수 있어야 하며, 유효하지 않은 상태를 방지하는 책임을 가져야 한다.
#### 3.1.2 모든 클래스가 갖추어야 하는 자기 방어 임무  
- 클래스, 메서드, 모듈 등은 각각이 독립적으로 신뢰할 수 있는 품질을 갖춰야 한다.
- 외부 도움 없이는 사용할 수 없는 클래스는 미성숙한 설계다.
- 모든 클래스는 초기화, 유효성 검사, 상태 보호 기능을 스스로 갖춰야 한다.


---
title: "Java : 메모리 구조"
excerpt: 
categories:
  - Java
tags: 
permalink: /categories/language/java/grammers/Java-Memory-Structure
toc: true
toc_sticky: true
date: 2025-07-24
last_modified_at: 2025-07-24
---
# Reference
- https://www.youtube.com/watch?v=zta7kVTVkuk
	- 해당 링크를 보고 정리한 글

# JVM이란 ?
- JVM 이란 "Java Virtual Machine"의 줄임말임
- 자바 애플리케이션을 어느 CPU나 OS에서도 실행할 수 있게 지원하는 역할
- 자바 코드를 컴파일하여 바이트 코드로 변환하여 해당 운영체제가 이해할 수 있게 기계어로 실행
- JVM의 구성은 크게 4가지로 구분됨
	- Class Loader
	- Execution Engine
	- Garbage Collector
	- Runtime Data Area

## Execution Engine
- Runtime Data Area에 할당된 바이트 코드를 실행 시키는 주체
- 코드를 실행하는 방식은 크게 2가지 방식이 존재
#### Interpreter
- 바이트 코드를 해석하여 실행하는 역할을 수행
- 다만 같은 메서드라도 여러번 호출될 때 매번 새로 수행해야 함

#### JIT(Just In Time) Compiler
- Interpreter의 단점을 해소
- 반복되는 코드를 발견하여 전체 바이트 코드를 컴파일하고 그것을  Native Code로 변경하여 사용
	- *Native Code*
		- 자바에서 부모가 되는 C, C++, 어셈블리어를 의미

#### Garbage Collector
- 더 이상 참조되지 않는 메모리 객체를 모아 제거하는 역할을 수행
- 일반적으로 자동으로 실행되지만, 수동으로 실행하기 위해 "System.gc()"를 사용할 수 있음 (다만, 실행이 보장되지는 않음)
- 앞으로 사용되지 않는 객체의 메모리를 Garbage 라고 부름
	- 이런 Garbage를 정해진 스케줄에 의해 정리해주는 것을 GC(Garbage Collection)라 부름
	
##### Stop The World
- GC를 수행하기 위해 JVM이 멈추는 현상을 의미
- GC가 작동하는 동안 GC 관련 Thread를 제외한 모든 Thread는 멈춤
	- 일반적으로 "튜닝"이라는 것은 이 시간을 최소화하는 것을 의미함

##### GC의 종류
- Serial GC
- Parallel GC
	- Java 8 (default)
- CMS GC
- G1 GC
	- Java 10(default)
- Z GC
	- Java 11에서 설정가능

자기 애플리케이션 및 서비스 특성에 맞는 GC를 골라서 사용해야함


## Class Loader
JVM으로 바이트 코드(.class)를 로드하고, 링크를 통해 배치하는 작업을 수행하는 모듈

로드된 바이트 모듈을 엮어서 JVM의 메모리 영역인 Runtime Data Area에 배치함

클래스를 메모리에 올리는 로딩 기능은 한번에 메모리에 올리지 않고, 어플리케이션에서 필요한 경우 동적으로 메모리에 적재하게 됨

클래스 파일의 로딩은 3단계로 구성
- Loading -> Linking -> Initialization

## Runtime Data Area
어플리케이션이 동작하기 위해 OS에서 할당받은 메모리 공간을 의미

크게 5가지
- Method Area
	- static으로 선언된 변수, Class 레벨의 모든 데이터가 이곳에 저장
	- JVM 마다 단 하나의 Method Area
	- Runtime Constant Pool이라는 별도의 영역 존재
	- 저장되는 정보의 종류
		- Field Info : 멤버 변수의 이름, Data Type, Modifier
		- Method Info : 메소드 이름, Return Type, Paramter, Modifier
		- Type Info : class, interface, Type, Super Class
	- Heap과 마찬가지로 GC 관리 대상
- Heap Area
- Stack Area
- PC Register
- Native Method Stack

(정리중...)
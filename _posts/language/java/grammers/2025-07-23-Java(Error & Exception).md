---
title: "Java : 예외처리"
excerpt: Error & Exception
categories:
  - Java
tags:
  - Java
permalink: /categories/language/java/grammers/error-n-exception
toc: true
toc_sticky: true
date: 2025-07-23
last_modified_at: 2025-07-23
---
# Java의 Exception 계층
![Image](https://media.licdn.com/dms/image/v2/D4D12AQF0yLjQGK2C2w/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1697864284432?e=1758758400&v=beta&t=YadgREURLigT2P8n5omjTmCVEf6J5USZ_p9-gR7pXGk)
- Error & Exception 은 "Throwable" 클래스를 상속받아 생성됨

# Error, 오류
- 오류는 시스템 레벨에서 프로그램에 심각한 문제를 야기하여 실행중인 프로그램을 종료함
- 개발자가 미리 예측하여 처리할 수 없는 것이 대부분
- 오류에 대한 처리는 불가함

## Error Type
1. `Compile Error, 컴파일 에러`
	- 문법적인 오류나 문맥이 맞지 않는 코드를 작성하여 컴파일 단계에서 발생하는 에러
	- 프로그램이 실행되지 못하고 종료되는 현상이 발생
2. `Runtime Error, 런타임 에러`
	- 프로그램이 작동하면서 예기치 않은 상황에 의해 발생하는 에러
	- 프로그램이 오작동하거나 종료되는 현상이 발생

# Exception, 예외
- 예외는 오류와 같이 실행중인 프로그램을 비정상적으로 종료 시킴
- 일반적으로 개발자가 구현한 로직에서 발생
- 개발자가 예외가 발생할 수 있는 상황을 예측하여 조치할 수 있음

## Exception Type

### 1. Checked Exception
- 반드시 예외 처리가 필요하며, Compile 단계에서 확인됨
- 예외 발생 시 "롤백하지" 않음
- Example
	- IOException
	- SQLException

### 2. Unchecked Exception
- 명시적 처리 강제하지 않음, Runtime 단계에서 확인됨
- 예외 발생 시 : 롤백함
- Example
	- NullPointerException
	- IllegalArgumentException
	- IndexOutofBoundException
	- SystemException



# How to ?

## 1. Try ~ Catch ~ finally
 예외 처리 메소드를 직접 처리하기 위해서는 try, catch, finally 키워드를 이용
```java
try { // 예외가 발생할 것으로 예상되는 코드}
catch (// 예외 클래스 e1) {}
catch (// 예외 클래스 e1 | 예외 클래스 e2 ) {}
finally { //try, catch 구문 종료 후 실행되는 코드}
```

## 2. throws, throw

`throws`
- 예외 처리 방식의 또 다른 방법으로 발생된 예외 상황을 호출한 지점으로 리턴하는 방식
- 이런 예외 처리 방식은 한 메소드에서 예외 처리하기 위해 사용됨
- 예외 타입이 여러개 발생할 것으로 예상될 경우 콤마를 사용하여 복수 입력이 가능함

`throw`
- 예외 상황을 인위적으로 발생시키키기 위해 throw 키워드 사용
	- 개발자가 의도한 예외 상황


# Example

## 1. try ~ catch ~ finally

다음은 Exception이 발생하는 코드이다.
```java
public class ExceptionNotes {  
    public static void main(String[] args) {  
        String numbers = "abcd";  
        Integer number =  Integer.parseInt(numbers);  
  
        System.out.println(number);
    }  
}
```
```text
Exception in thread "main" java.lang.NumberFormatException: For input string: "abcd"
```
try ~ catch를 사용하면 다음과 같이 예외처리가 가능
```java
public static void main(String[] args) {  
    String numbers = "abcd";  
    try{  
        Integer number =  Integer.parseInt(numbers);  
        System.out.println(number);  
    } catch(NumberFormatException e1) {  
        System.out.println(e1);  
    } finally {  
        System.out.println("close");  
    }  
}
```

## 2. throws ~ throw
```java
public class ExceptionNotes {  
  
    public static void raiseException() throws Exception{  
        throw new RuntimeException();  
    }  
  
    public static void method() {  
        try {  
            raiseException();  
        } catch (Exception e) {  
            System.out.println("예외가 발생함");  
        }  
    }    
  
    public static void main(String[] args) {  
        ExceptionNotes.method();    
    }  
}
```
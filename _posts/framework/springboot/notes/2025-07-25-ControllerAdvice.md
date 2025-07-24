---
title: "[SpringBoot] 스프링 부트에서 API Exception은 어떻게 처리할까 ?"
excerpt: ControllerAdvice를 이용해 Exception 처리하기
categories:
  - SpringBoot
tags: 
permalink: /categories/framework/springboot/controller-advice
toc: true
toc_sticky: true
date: 2025-07-25
last_modified_at: 2025-07-25
---
# How to ?

Service 로직에서 의도한 Exception을 발생시켜 이 Exception을 API를 통해 결과를 알려줘야하는 경우엔 어떻게 할까 ?

# OverAll

`@ControllerAdvice`
 - `Spring 3.2`부터는 `@ControllerAdvice` 어노테이션을 제공한다. `@ControllerAdvice`를 사용하면 Controller 클래스들의 모든 예외에 대해서 공통으로 처리할 수 있다. (Global Exception Handling)

`@ExceptionHandler`
 - 개별 컨트롤러나 서비스 메서드 내에서 발생하는 특정 예외를 처리하는 방법으로 `@ExceptionHandler` 어노테이션을 사용할 수 있다. 
	- 이를 통해 해당 예외 유형에 대한 맞춤형 처리 로직을 정의할 수 있다. 



# Summary


## 1. 사용자 정의 Exception 생성하기
```java
public class MyException extends RuntimeException {  
  
    public MyException() {  
    }  
  
    public MyException(String message) {  
        super(message);  
    }  
}

```
- 위 코드는 "Service Layer"에서 사용할 수 있는 사용자 정의 Exception을 임의적으로 선언한 경우다. RuneTimeException을 상속받아 정의되었으며 UnCheckException 이다.

##  2. Service에서 사용자 정의 MyException 일으키기
```java
public void validAge(int age) {  
    if (age < 19) {  
        throw new MyException("소주를 구매할 수 없습니다.");  
    } else {  
        System.out.println("소주를 구매할 수 있습니다.");  
    }  
}
```
- 앞서 선언한 `MyException` 클래스를 Service Layer의 특정 메서드에서 사용할 경우 위와 같은 예시가 만들어진다. 

## 3. Exception Message Class 작성하기
```java
import lombok.Getter;  
import lombok.Setter;  
import java.util.Date;  
  
@Setter  
@Getter  
public class ApiErrorSpec {  
    private String message;  
    private int code;  
    private Date timeStamp;    
}
```
- 앞서 작성된 "MyException"을 발생시켜 최종적으로 "어떤 메시지"를 보여줄 것인가에 해당하는 클래스를 작성한다. 위의 결과 다음과 같은 형태의 Http Response 가 만들어진다.

```java
{
	"message" : "...",
	"code" : 00,
	"timeStampe" : "2025-12-02 12:00:00"
}
```

## 4. ApiExceptionHandler 만들기
이제 ControllerAdvice와 ExceptionHandler를 사용해 MyException을 응답으로 내보낼 ExceptionHandler 클래스를 만들자.
```java  
import org.springframework.http.HttpStatus;  
import org.springframework.http.ResponseEntity;  
import org.springframework.web.bind.annotation.ControllerAdvice;  
import org.springframework.web.bind.annotation.ExceptionHandler;  
  
import java.util.Date;  
  
@ControllerAdvice  
public class ApiExceptionHandler {  
  
    @ExceptionHandler(RuntimeException.class)  
    public ResponseEntity<ApiErrorSpec> handleException() {  
        ApiErrorSpec spec = new ApiErrorSpec();  
        spec.setCode(1000);  
        spec.setMessage("test");  
        spec.setTimeStamp(new Date());  
  
        return new ResponseEntity<>(spec, HttpStatus.BAD_REQUEST);  
    }  
  
}
```
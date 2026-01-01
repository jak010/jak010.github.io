---
title: OOM-Kill 시뮬레이션 및 Swap Memory 증설을 통한 해결 (Docker 환경)
excerpt: AWS EC2에서 발생했던 OOM-Kill 이슈를 Docker 환경에서 시뮬레이션하고, Swap Memory 증설을 통해 해결하는 과정을 다룹니다.
categories:
  - content
tags:
  - OOM
  - OutOfMemory
  - SwapMemory
  - Docker
  - AWS
  - EC2
  - Python
permalink: /categories/devlife/DevOps/
toc: true
toc_sticky: true
date: 2026-01-01
last_modified_at: 2026-01-01
---

# OOM-Kill 시뮬레이션 및 Swap Memory 증설을 통한 해결 (Docker 환경)

25년 5월, 재직 중이던 회사에서 있었던 일이다. 기억하기로는 내부 솔루션에서 광고 관련 데이터 처리를 위해 각 플랫폼에서 여러 데이터를 수집 및 취합 후 특정 처리를 하던 배치 프로세스에서 OOM이 일어나 서비스가 죽는 현상이 있었다.

해당 서비스는 AWS의 EC2(t3a.small)에서 가동 중이었으며 아무래도 다량의 데이터 처리 및 누적된 데이터들로 인해 특정 조건에서 OOM이 일어나 프로세스가 죽는 현상인 듯싶었다. 어찌 됐든 실 사용자가 있었던 상황이기에 서비스를 중단한 뒤 조치를 취하는 선택은 후순위에 있었다.

결론적으로는 해당 이슈는 가동 중인 EC2의 swap memory의 크기를 수동적으로 늘리는 방식으로 해결했는데 지금에 와서 보니 이를 시뮬레이션할 수 있으면 괜찮을 듯싶어 기록을 남기려 한다.

## 환경

앞서 언급했듯 그 당시 회사에는 AWS의 EC2(t3a.smll)에서 일어났는데 지금 이 글을 쓰는 시점에서는 AWS를 사용할만한 여건이 되지 않기에 Docker를 통해 이를 확인해보고자 한다. (LocalStack을 이용한 테스트 환경을 고려하기도 했으나, 배보다 배꼽이 더 크게 될 것 같다)

## 준비

### 스크립트

의도적으로 메모리를 많이 사용하는 조건을 준비하기 위해 다음과 같은 파이썬 스크립트를 준비했다.

    """
    의도적으로 메모리를 많이 사용하는 스크립트
    """

    print("Allocating large memory...")

    data = []
    try:
        MB = 1024 * 1024 * 500  # 500 mB
        for i in range(2):
            data.append(bytearray(MB))
    except Exception as e:
        raise e

    print("Allocation complete")

위 코드는 data라는 변수에 500mb를 두 번씩 총 1G를 넣는 동작이다.

### Dockerfile

swap 메모리 테스트를 위한 컨테이너 환경 준비를 위해 다음처럼 Dockerfile을 작성한다.

    FROM ubuntu:24.04

    ENV DEBIAN_FRONTEND=noninteractive

    RUN apt-get update \
        && apt-get install -y --no-install-recommends \
            python3 \
            python3-pip \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

    WORKDIR /app
    COPY memory_error.py .

    CMD ["bash"]

## 실행

Dockerfile을 빌드하자.

    $ docker build -t oom-test:latest .

Docker Container에 특정 옵션을 설정하지 않고 실행 시 호스트에 있는 Swap을 사용한다고 한다. 그러니 다음과 같은 명령을 이용해 Container를 띄우고 스크립트를 실행하면 OOM Kill이 일어나는 것을 확인할 수 있다. (해당 명령은 의도적으로 swap 크기를 제한한 것이다)

    $ docker run -it --privileged --memory=500m --memory-swap=500m [CONTAINER_ID]

이후 컨테이너 내부에서 스크립트를 실행하면 다음과 같은 결과를 얻는다.

    root@8a0e0454b7c7:/app# python3 memory_error.py 
    Allocating large memory...
    Killed

    root@8a0e0454b7c7:/app# dmesg
    ...
    [157927.587676] oom-kill:constraint=CONSTRAINT_MEMCG,nodemask=(null),cpuset=8a0e0454b7c7538643539fe65e472836613d4b57985f9df0e6f66012467b9deb,mems_allowed=0,oom_memcg=/docker/8a0e0454b7c7538643539fe65e472836613d4b57985f9df0e6f66012467b9deb,task_memcg=/docker/8a0e0454b7c7538643539fe65e472836613d4b57985f9df0e6f66012467b9deb,task=python3,pid=18856,uid=0

    [157927.587790] Memory cgroup out of memory: Killed process 18856 (python3) total-vm:526384kB, anon-rss:509560kB, file-rss:5632kB, shmem-rss:0kB, UID:0 pgtables:1064kB oom_score_adj:0
    root@8a0e0454b7c7:/app#

스크립트에는 1GB 정도의 메모리를 사용하는 코드가 들어있고 500MB로 제한된 환경에서 실행하니 OOM-KILL이 일어나는 것을 확인했다. 이제 Swap Memory를 늘려서 OOM-Kill이 나는 걸 해결해 보자.

    $ docker run -it --privileged --memory=500m --memory-swap=1g  [CONTAINER_ID]

    root@232e730aa55b:/app# python3 memory_error.py 
    Allocating large memory...
    Allocation complete

## Swap(스왑) 메모리?

스왑 메모리는 디스크 공간을 이용하여 부족한 메모리를 대체할 수 있는 공간을 의미한다. 실제 메모리(RAM)가 가득 찬 경우 더 많은 메모리가 필요할 때 사용할 수 있다. 실제 메모리가 아닌 디스크를 이용하는 것이기 때문에 메모리 속도는 떨어진다고 한다. 통상 메인 메모리의 2배 정도로 설정한다고 한다.

“개요”에서 언급했던 일화에서도 스왑 메모리를 사용하는 건 임시방편이었다. 그럼에도 불구하고 그 당시 스왑 메모리 증설을 택할 수 있었던 이유에는 회사의 경영악화로 인해 AWS 비용은 줄이고 있었기에 특정 자원을 늘리는 선택을 할 수 없다는 배경이 있었다.

이 처리를 하고 나서 관련 업무 회의를 가졌을 때 그 당시 실장님께서는 과거 HDD 같으면 성능이 많이 떨어지겠지만 요즘 같은 SSD에는 꽤 괜찮지 않을까라는 의견을 주시기도 했다.

## 기타

구글 검색 시 스왑 메모리를 늘릴 수 있도록 알려주는 명령어 셋은 다음과 같다.

    sudo fallocate -l 1G /swapfile
    sudo chmod 600 /swapfile
    sudo mkswap /swapfile
    sudo swapon /swapfile

그러나 내 환경에서는 위와 같은 명령어 셋이 먹히지 않았다. Docker 컨테이너 내부에서는 swap을 켤 수 없으며, Docker Container는 자체 커널이 없고 호스트 커널의 메모리 관리를 그대로 사용한다고 한다.

## 마치며

그 당시 환경을 똑같이 재연하기 위해 AWS를 이용하고자 했으나 현재는 AWS를 사용할 수 없다. 대안으로 AWS Mocking 도구인 LocalStack을 이용하려 했으나 어차피 Docker를 쓰는 건 둘 다 똑같은 게 아닐까 싶어서 Docker를 선택하게 되었다.

본문에서도 드러났지만 Swap 메모리를 늘리는 건 임시방편이어야 한다. 그렇다면 Swap 메모리를 늘리지 않고 해결할 수 있는 방법은 뭘까를 고민해 볼 수 있을 듯싶다. 이는 상황에 따라 다르겠지만 본문에서 제시한 스크립트에서는 변수 하나에 큰 크기를 담는 게 아닌 스트리밍 방식으로 데이터를 처리하는 방법도 고려해 볼 수 있을 듯싶다.

끝으로 본문에서 사용된 코드는 아래 repo에서 확인할 수 있다.

[https://github.com/jak010/study-oom-test](https://github.com/jak010/study-oom-test)
#!/usr/bin/env python
# coding: utf-8

# In[5]:


#87p 3-1 
def min_coins(N):
    coins = [500, 100, 50, 10]
    count = 0  # 거슬러 줄 동전 개수
    
    # 가장 큰 화폐 단위부터 사용하여 거슬러 주기
    for coin in coins:
        count += N // coin  # 해당 동전으로 거슬러 줄 수 있는 개수 추가
        N %= coin  # 거슬러 준 후 남은 금액 업데이트
    
    return count  # 최소 동전 개수 반환

# 예제 실행
N = int(input("거슬러 줄 금액 (10의 배수): "))
print("최소 동전 개수:", min_coins(N))


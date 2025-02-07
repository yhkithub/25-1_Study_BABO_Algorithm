# solution 함수 정의
def solution (food_items,k):
    # 음식을 다 먹을때까지 시간 정의
    clear=0
    for i in range(len(food_items)):
        clear+=food_items[i]

    # 먹장을 진행한 시간 정의
    time=0
    # 인덱스를 가리키는 포인터 정의
    pointer=0

    # 먹방을 진행한 시간이 k보다 작을떄까지 반복
    while(time<k):
        # pointer가 가리키는 인덱스의 원소가 0이 아닐때
        if (food_items[pointer]!=0):
            #음식 섭취
            food_items[pointer]-=1
            #먹방시간 1초 증가
            time+=1
            # 음식을 다 먹었다면 -1출력
            if (time==clear):
                print(-1)
                break

        # 원소가 0을 가리키거나, 음식을 섭취했다면 pointer를 오른쪽으로 이동
        pointer+=1

        # pointer가 마지막 마지막 인덱스를 넘겼다면 0으로 이동
        if (pointer==len(food_items)):
            pointer=0

    # 네트워크가 종료된 시점
    if (time==k):
        # 포인터가 가리키는 음식의 양이 0일동안 반복
        while(food_items[pointer]==0):
            pointer+=1
            if (pointer==len(food_items)):
                pointer=0

        # 포인터가 가리키는 음식의 양이 0이 아니라면
        # 해당 포인터 출력
        print(pointer+1)
        return 0

solution([3,2,2],5)

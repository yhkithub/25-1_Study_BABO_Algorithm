# 첫 줄에서 리스트 길이 받아오기
n=int(input())

# 두번째 줄에서 리스트에 들어갈 데이터 받기
data=list(map(int,input().split()))

#리스트 내림차순 정렬
data.sort(reverse=True)

group=0
max_pointer=0
ungrouped_nums=n

# 리스트 처음부터 끝까지 순회
while(max_pointer<n):
	# 남은 리스트의 원소 갯수가 현재 가장 큰 수 이상이라면
	if (ungrouped_nums>=data[max_pointer]):
		# 가장 큰 수만큼의 원소를 그룹에 넣기
		ungrouped_nums-=data[max_pointer]
		max_pointer+=data[max_pointer]
		
		group+=1
		continue
	# 남은 리스트의 원소 갯수가 현재 가장 큰 수 보다 작다면
	else:
		# 다음 가장 큰 수로 넘어가기
		max_pointer+=1
		ungrouped_nums-=1
	
# 결과 출력
print(group)
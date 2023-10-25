## 📚 Greedy Algorithm
![greedy-optimal](https://github.com/hufs71/code-study/assets/115367115/fb859a05-00bc-4be6-be9d-610f4aabffee)


* 현재 상황에서 지금 당장 좋은 것만 고르는 방법
* 키워드: `가장 큰 순서대로`, `가장 작은 순서대로`
* 정렬 알고리즘과 짝을 이뤄 자주 출제
* 그리디 알고리즘으로 문제의 해법을 찾았을 때는 그 해법이 정당한지 검토해야 함
---
### 해결 방법
1. 선택 절차(Selection Procedure): 현재 상태에서의 최적의 해답을 선택한다.
2. 적절성 검사(Feasibility Check): 선택된 해가 문제의 조건을 만족하는지 검사한다.
3. 해답 검사(Solution Check): 원래의 문제가 해결되었는지 검사하고, 해결되지 않았다면 선택 절차로 돌아가 위의 과정을 반복한다.

### 조건
1. 탐욕적 선택 속성(Greedy Choice Property) : 앞의 선택이 이후의 선택에 영향을 주지 않는다.
2. 최적 부분 구조(Optimal Substructure) : 문제에 대한 최종 해결 방법은 부분 문제에 대한 최적 문제 해결 방법으로 구성된다.

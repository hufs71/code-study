# ☁️ 정리
## 23-10-1주차
* 날짜 형식 ex. 2023-10-07 으로 표현하기
```sql
DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d')
```
## 23-10-2주차
* `%H`는 24시 기준 시간, `%h`는 12시 기준 시간.
* NULL 여부 확인할 때에는 '=' 연산자 쓰지 않고 is 로 확인한다.
```sql
-- (o)
WHERE joined.in IS NULL

-- (x)
WHERE joined.in = NULL
```

# ☁️ 정리
## 23-10
* 날짜 형식 ex. 2023-10-07 으로 표현하기
```sql
DATE_FORMAT(R.CREATED_DATE, '%Y-%m-%d')
```
---
* `%H`는 24시 기준 시간, `%h`는 12시 기준 시간.
* NULL 여부 확인할 때에는 '=' 연산자 쓰지 않고 is 로 확인한다.
```sql
-- (o)
WHERE joined.in IS NULL

-- (x)
WHERE joined.in = NULL
```
---
* 반올림: `ROUND(숫자,반올림할 자릿수)`, 숫자를 반올림할 자릿수 +1 자릿수에서 반올림
* 버림: `TRUNCATE(숫자,버릴 자릿수)`, 숫자를 버릴 자릿수 아래로 버림

## 23-11

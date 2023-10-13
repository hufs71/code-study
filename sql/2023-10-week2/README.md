# 정리
* `%H`는 24시 기준 시간, `%h`는 12시 기준 시간.
* NULL 여부 확인할 때에는 '=' 연산자 쓰지 않고 is 로 확인한다.
```sql
-- (o)
WHERE joined.in IS NULL

-- (x)
WHERE joined.in=NULL
```

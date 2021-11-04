-- 코드를 입력하세요
SELECT animal_type, COUNT(animal_id) As `count` from ANIMAL_INS group by animal_type order by animal_type ASC;
/* 
animal_type 컬럼, 그룹화된 animal_type 칼럼에서 animal_id 숫자를 카운트한 count 컬럼 
animal_type 기준 오름차순 정렬 
*/
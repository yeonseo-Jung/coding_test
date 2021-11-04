-- 코드를 입력하세요
SELECT animal_type, COUNT(animal_id) As `count` from ANIMAL_INS group by animal_type order by animal_type ASC;

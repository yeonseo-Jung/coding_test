set @hour := -1; /* 로컬변수 선언 */

select (@hour := @hour + 1) as `HOUR`, /* @hour 변수 1씩 증가시키기 */
(select count(animal_id) from animal_outs where hour(datetime) = @hour) as `count` /* datetime 컬럼에서 값의 시간이 @hour인 animal_id 개수 카운트 */
from animal_outs
where @hour < 23;

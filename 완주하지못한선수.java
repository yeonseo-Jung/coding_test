import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        LinkedHashMap<String, Integer> participantMap = new LinkedHashMap<>();
        LinkedHashMap<String, Integer> completionMap = new LinkedHashMap<>();

        // completion을 이름 / 갯수로 변환
        for(int i = 0; i < completion.length; i++) {
            if(!completionMap.containsKey(completion[i])) { // Key 없을 경우(처음 삽입)
                completionMap.put(completion[i], 1);
            } else { // Key 존재할 경우
                completionMap.put(completion[i], completionMap.get(completion[i]) + 1);
            }
        }

        // participant을 이름 / 갯수로 변환
        for(int i = 0; i < participant.length; i++) {
            if(!participantMap.containsKey(participant[i])) { // Key 없을 경우(처음 삽입)
                participantMap.put(participant[i], 1);
            } else { // Key 존재할 경우
                participantMap.put(participant[i], participantMap.get(participant[i]) + 1);
            }
        }

        for(String key : participantMap.keySet()) { // participantMap 전체 조회
            int temp = 0;
            if(completionMap.containsKey(key)) { // completion에 존재할 경우 값 가져오기 이외는 0
                temp = completionMap.get(key);
            }

            if(Objects.equals(participantMap.get(key) - temp, 1)) { // 두 배열 비교해서 1남는 값 찾기
                answer = key;
                break;
            }
        }

        return answer;   
    }
}
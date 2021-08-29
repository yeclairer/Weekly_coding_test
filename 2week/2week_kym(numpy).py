# Author @winston1214
## Numpy version
import numpy as np
def solution(scores):
    scores = np.array(scores)
    answer = ''
    for i in range(len(scores)):
        i_score = scores[:,i]
        cnt_arr = np.unique(i_score,return_counts=True)[-1]
        if len(cnt_arr) >= 2:
            if cnt_arr[0] == 1 or cnt_arr[-1] == 1:
                if np.argmax(i_score) == i:
                    i_score = np.delete(i_score,np.argmax(i_score))
                elif np.argmin(i_score) == i:
                    i_score = np.delete(i_score,np.argmin(i_score))
        avg = np.mean(i_score)
        bins = np.array([50,70,80,90])
        dic = {0:'F',1:'D',2:'C',3:'B',4:'A'}
        answer += dic[np.digitize(avg,bins)]
    return answer
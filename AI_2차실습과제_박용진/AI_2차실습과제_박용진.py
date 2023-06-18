from sklearn import datasets
from sklearn import svm, tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, train_test_split
import numpy as np

digit=datasets.load_digits()

# 40%를 테스트 집합으로 함
x_train,x_test,y_train,y_test=train_test_split(digit.data,digit.target,train_size=0.6) 

s=svm.SVC(gamma=0.001)
# 2-1. 아래 [코드작성] 부분에 5-겹 교차검증 코드를 작성하시요
[코드 작성]
print("\nSVM의 정확률: ", accuracies)
print("정확률(평균)=%0.3f, 표준편차 =%0.3f"%(accuracies.mean()*100,accuracies.std()))

t=tree.DecisionTreeClassifier()
# 2-2. 아래 [코드작성] 부분에 5-겹 교차검증 코드를 작성하시요
[코드 작성]
print("\n결정트리의 정확률: ", accuracies)
print("정확률(평균)=%0.3f, 표준편차 =%0.3f"%(accuracies.mean()*100,accuracies.std()))

r=RandomForestClassifier()
# 2-3. 아래 [코드작성] 부분에 5-겹 교차검증 코드를 작성하시요
[코드 작성]
print("\n랜덤포리스트의 정확률: ", accuracies)
print("정확률(평균)=%0.3f, 표준편차 =%0.3f"%(accuracies.mean()*100,accuracies.std()))

# 정확률을 비교한 결과 SVM이 가장 우수하므로 SVM에 대해 테스트 집합의 정확률을 측정함
# 60%의 훈련 집합으로 SVM을 학습함
s.fit(x_train,y_train) 

# 40%의 테스트 집합으로 성능 측정
print('\n테스트 집합에 대한 정확률=%0.3f'%s.score(x_test,y_test)) 



#[실행결과]
#SVM의 정확률:  [0.99074074 0.99074074 0.98611111 0.99069767 0.99069767]
#정확률(평균)=98.980, 표준편차 =0.002

#결정트리의 정확률:  [0.82407407 0.81481481 0.85185185 0.78604651 0.82790698]
#정확률(평균)=82.094, 표준편차 =0.021

#랜덤포리스트의 정확률:  [0.96296296 0.97222222 0.97685185 0.9627907  0.95813953]
#정확률(평균)=96.659, 표준편차 =0.007

#테스트 집합에 대한 정확률=0.986


from sklearn.model_selection import train_test_split

X = [[1],[2],[3],[4],[5],[6]]
y = [2,4,6,8,10,12]

X_train,X_test,y_train,y_test = train_test_split(
    X,y,test_size=0.2,random_state=42)

print("Training:",X_train)
print("Testing:",X_test)
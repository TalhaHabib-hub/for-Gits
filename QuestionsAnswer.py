listsOfQuestions = [["Which of the following is a scalar quantity?", "Density","Displacement","Torque","Weight",1],["Which of the following is a the only vector quantity?", "Temperature","Energy","Power","Momentum",4],["Which of the following lists of physical quantities consists only of vectors?", "Timpe,Temperature,Velocity","Force,Volume,Momentum","Velocity,acceleration,mass","Force,Acceleartion,Velocity",4],["The angle between rectangular components along x-axis is?", "0'","60'","90;","120'",3],["A force of 10N is acting along y-axis. its component along x-axis is?", "10N","20N","100N","Zero N",4],["The vector product of two non zero vectors is zero, when?", "They are parallel to each other","They are perpendicular to each other","They are equal vectors","They are inclined at angle of 60'",1],["Identify the vector quantity?", "Heat","Angular momentum","Time","work",2],["Which of the following is a scalar quantity?", "Magnetic momentum","Acceleration due to gravity","Electric field","Electrostatic potential",4],["The resultant of two equal forces is double of either of the force. The angle between them is?", "0'","60'","90","120",1],["The resultant of two equal forces is double of either of the force. The angle between them is?", "0'","60'","90","120",1]]

markstore = 0
reward = [10,20,30,40,50,60,70,80,90,100]
treward = 0
for i in range(0,len(listsOfQuestions)):
    print(f"Q.{i+1}")
    print(listsOfQuestions[i][0])
    print(f"1.{listsOfQuestions[i][1]}")
    print(f"2.{listsOfQuestions[i][2]}")
    print(f"3.{listsOfQuestions[i][3]}")
    print(f"4.{listsOfQuestions[i][4]}")
    ans = int(input("choose (1-4)"))
    if ans ==listsOfQuestions[i][-1]:
        print("Correct")
        markstore = markstore + 10
        print("Your points",markstore,"/",(i+1)*10) 
    else:
        
        
        print("Wrong!---------> correct:",end=""),print(listsOfQuestions[i][listsOfQuestions[i][-1]]),print("Your points",markstore,"/",(i+1)*10)
    print("")

print("you got",markstore,"/",100)
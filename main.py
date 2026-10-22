import pandas as pd 
Students=pd.read_csv("Students Data.csv")
#print(Students)#Here all columns wont be displayed because of terminal screen width
#print(Students.to_string())#This is used when we want all columns to be displayed

# To calculate Total Marks 
Students["TotalMarks"]=(
    Students["PythonGrade"]+
    Students["DBMSGrade"]+
    Students["JavaGrade"]+
    Students["OSGrade"]+
    Students["ComputerNetworksGrade"]
)
print(Students.to_string())
#Grade_points=Students[Subjects].map(calculate_SGPA) 
#print(Grade_points)


#def calculate_SGPA(marks):
Subjects=[
        "PythonGrade",
        "DBMSGrade",
        "JavaGrade",
        "OSGrade",
        "ComputerNetworksGrade"]
#Grade_points=Students[Subjects].map(calculate_SGPA) 
#print(Grade_points) 
def calculate_SGPA(marks):
    if marks=="Ab":
        return Absent
    elif  marks>=90:
        return 10
    elif marks>=80:
        return 9
    elif marks>=70:
        return 8
    elif marks>=60:
        return 7
    elif marks>=50:
        return 6
    else:
        return 0
        print(Students.columns.tolist())
Grade_points=Students[Subjects].map(lambda marks:calculate_SGPA(marks*10)) 
print(Grade_points) 
Students["TotalGrades"]=Grade_points.sum(axis=1)
Students["SGPA"]=Grade_points.mean(axis=1)
print(Students[["StudentName","TotalGrades","SGPA"]])
def calculate_result(row):
    for subject in Subjects:
        mark = pd.to_numeric(row[subject], errors="coerce")

        if pd.isna(mark):
            return "Absent"

        if mark < 4:
            return "Fail"

    return "Pass"
Students["Result"] = Students.apply(calculate_result, axis=1)
Students["Average Marks"] = Students[Subjects].apply(
    pd.to_numeric, errors="coerce"
).mean(axis=1)
print("\nCLASS STATISTICS")

print("Total Students:", len(Students))

print("Students Passed:",
      (Students["Result"] == "Pass").sum())

print("Students Failed:",
      (Students["Result"] == "Fail").sum())

print("Students Absent:",
      (Students["Result"] == "Absent").sum())

print("Class Average Marks:",
      round(Students["Average Marks"].mean(), 2))

print("Highest TotalGrades:",Students["TotalGrades"].max())

print("Lowest TotalGrades:",
      Students["TotalGrades"].min())
print("\n========== SUBJECT-WISE ANALYSIS ==========")

Subject_Averages = Students[Subjects].apply(
    pd.to_numeric, errors="coerce"
).mean()

print("Average Marks in Each Subject:")
print(Subject_Averages.round(2))

print("\nBest Performing Subject:")
print(Subject_Averages.idxmax())

print("\nLowest Performing Subject:")
print(Subject_Averages.idxmin())
print("\n========== TOP 5 STUDENTS ==========")

Top_Students = Students.sort_values(
    by="SGPA", ascending=False
).head(5)

print(Top_Students[
    ["StudentName", "TotalGrades", "SGPA", "Result"]
].to_string(index=False))
print("\n========== FINAL STUDENT REPORT ==========")
print(Students.to_string(index=False))
Students.to_csv("student_performance_report.csv", index=False)
print("\nReport saved as student_performance_report.csv")



export default function updateStudentGradeByCity(listOfStudents, city, newGrades) {
  const result = listOfStudents
    .filter((student) => student.location === city)
    .map((student) => {
      const matchingGrade = newGrades.find((grade) => grade.studentId === student.id);
      if (matchingGrade) {
        return { ...student, grade: matchingGrade.grade };
      }
      return { ...student, grade: 'N/A' };
    });

  return result;
}

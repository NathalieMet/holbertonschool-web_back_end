export default function getStudentIdsSum(listOfStudents) {
  const ids = listOfStudents.map((student) => student.id);
  const sum = ids.reduce((total, num) => total + num, 0);
  return sum;
}

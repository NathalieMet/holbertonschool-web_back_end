export default function getStudentsByLocation(listOfStudents, city) {
  const result = listOfStudents.filter((student) => student.location === city);
  return result;
}

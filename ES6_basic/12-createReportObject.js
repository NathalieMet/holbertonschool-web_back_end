export default function createReportObject(employeesList) {
  const allEmployees = {};

  Object.entries(employeesList).forEach(([department, employees]) => {
    allEmployees[department] = [...employees];
  });

  return {
    allEmployees,
    getNumberOfDepartments() {
      return Object.keys(allEmployees).length;
    },
  };
}

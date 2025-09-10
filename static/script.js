function validateStudentId(studentId) {
  const pattern = /^BWU\/BTA\/\d{2}\/\d+$/;
  return pattern.test(studentId);
}

document.addEventListener('DOMContentLoaded', function() {
  const fetchButton = document.querySelector('#student-login button');
  const studentIdInput = document.getElementById('student-id');
  
  fetchButton.addEventListener('click', function() {
    const studentId = studentIdInput.value.trim();
    
    if (!validateStudentId(studentId)) {
      alert('Invalid Student ID format. Please use: BWU/BTA/YY/XXX (e.g., BWU/BTA/24/616)');
      studentIdInput.focus();
      return;
    }
    
    // Proceed with fetching materials
    console.log('Valid Student ID:', studentId);
  });
});
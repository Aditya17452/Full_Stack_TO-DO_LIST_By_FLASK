// Auto-hide Flask messages after 3 seconds
document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll(".alert");
  alerts.forEach(alert => {
    setTimeout(() => {
      alert.classList.add("fade");
      setTimeout(() => alert.remove(), 500);
    }, 3000);
  });
});

// Confirm before clearing all tasks
const clearForm = document.querySelector('form[action*="clear_tasks"]');
if (clearForm) {
  clearForm.addEventListener("submit", (e) => {
    if (!confirm("Are you sure you want to clear all tasks?")) {
      e.preventDefault();
    }
  });
}
